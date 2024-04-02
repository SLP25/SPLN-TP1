from typing import Iterable
from unidecode import unidecode
import itertools
import json
import re
from bisect import bisect_left, bisect_right
from .Trie import Trie
from .Token import Base, Modifier
from .utils import enumerateWhen
from .datasetParsers.utils import getDatasetFolder
import os
from copy import deepcopy

DATASETFOLDER = getDatasetFolder()

def load_dataset(dataset):
    with open(os.path.join(DATASETFOLDER,f'{dataset}.json')) as f:
        return json.load(f)


words = load_dataset("words")
lemmas = load_dataset("lemmas")
boosters = load_dataset("boosters")
negate = load_dataset("negate")
emojis = load_dataset("emojis")

tokens = Trie(starter={**{k:Base(k,v) for k,v in {**lemmas,**words}.items()},**{k:Modifier(k,v) for k,v in {**boosters,**negate}.items()}})
modify_mask = ([0.2, 0.5, 0.8], [1, 0.9, 0.7, 0.5, 0.2])

#Takes a space-bounded string and transforms it into individual ascii words/single emojis
# "chapéu"      -> ["chapeu"]
# "slaaay💅💅"  -> ["slaaay", "💅", "💅"]
# "⽮"          -> []
def processWord(word: str) -> Iterable[str]:
    current = ""
    for c in word:
        if c in emojis:
            current = unidecode(current)
            if current:
                yield current
            yield c
            current = ""
        else:
            current += c

    current = unidecode(current)
    if current:
        yield current

#Replaces latin characters and emojis and the input
#is divided into sentences, which are themselves lists of words
def process(input: str) -> list[list[str]]:
    sentences = re.split(r"[.?!]", input)
    return [list(itertools.chain.from_iterable(processWord(w) for w in re.split(r"[\s,;:\"']", s) if w)) for s in sentences if s]


#Takes a list of words and returns a list of tokens
#Each token is either a base value, or a modifier
def tokenize(sentence: list[str]) -> Iterable[Base|Modifier]:
    while sentence != []:
        (consumed, token) = tokens.search(sentence)
        if token != None:
            yield deepcopy(token)
            sentence = sentence[consumed:]
        else:
            sentence = sentence[1:]




def applyModifiers(base: Base, index: int, modifiers: list[tuple[int,Modifier]]):
    (before, after) = modify_mask

    cutoff = bisect_left(modifiers, index, 0, None, key=lambda im: im[0])
    first = bisect_left(modifiers, index - len(after), 0, cutoff, key=lambda im: im[0])
    last = bisect_right(modifiers, index + len(before) - 1, cutoff, None, key=lambda im: im[0])

    for (i, m) in modifiers[first:cutoff]:
        base.apply(m, after[index-i-1])

    for (i, m) in modifiers[cutoff:last]:
        base.apply(m, before[len(before)+index-i-1])

#The modifier tokens act on the base values around them according to the modify_mask
#Then the modified values are added together
def evaluate(tokens: list[Base|Modifier]) -> list[Base]:
    enumerated = list(enumerateWhen(tokens, lambda t: not t.is_modifier()))
    bases = [(i,t) for i,t in enumerated if not t.is_modifier()]
    modifiers = [(i,t) for i,t in enumerated if t.is_modifier()]

    for i, b in bases:
        applyModifiers(b, i, modifiers)

    return [b for _,b in bases]


#We can now use the already calculated tokens to add the emojis into the tokens
for emoji,description in emojis.items():
    value = sum(b.value() for b in evaluate(tokenize(description.split())))
    tokens.insert([emoji], Base(emoji, value * 2))   #We give it an "emoji bonus" since emojis are usually emotionally charged

def analize(input: str) -> tuple[list[Base], int]:
    sentences = process(input)
    words = sum(len(s) for s in sentences)
    bases = list(itertools.chain.from_iterable(evaluate(tokenize(s)) for s in sentences))
    return bases, words



def calibrate(bases: list[Base]):
    totalpos = sum(x.value() for x in bases if x.value() > 0)
    totalneg = sum(x.value() for x in bases if x.value() < 0)
    
    mult = abs(totalpos/totalneg) #TODO: divide by zero
    with open(os.path.join(DATASETFOLDER,'multiplier.txt'),'w') as f:
        f.write(str(mult))


def normalize(bases):
    with open(os.path.join(DATASETFOLDER,'multiplier.txt')) as f:
        normalizerMultiplier = float(f.read())

    normalizer = Modifier("[NORMALIZER]", normalizerMultiplier)
    for b in bases:
        if b.value() < 0:
            b.apply(normalizer)

