import json
import sys
from .Trie import Trie

def load_dataset(dataset):
    with open(f'datasets/{dataset}.json') as f:
        return json.load(f)


#ignore emojis for now...
words = load_dataset("words")
lemmas = load_dataset("lemmas")
boosters = load_dataset("boosters")
negate = load_dataset("negate")



bases = Trie(defaultValue = 0,starters = [words,lemmas])        #The base values. additive in nature
modifiers = Trie(defaultValue = 1,starters = [boosters,negate])     #Modify the surrounding base values (multiplicative)
modify_mask = ([0.2, 0.5, 0.8], [1, 0.9, 0.7, 0.5, 0.2])



#TODO: in this fase, latin characters and emojis are replaced and the input
#is divided into sentences, which are themselves lists of words
def process(input):
    return input



#Takes a list of words and returns a list of tokens
#Each token is either a base value, or a modifier
def tokenize(sentence):
    #TODO: consult tries
    ...


#The modifier tokens act on the base values around them according to the modify_mask
#Then the modified values are added together
def evaluate(tokens):
    ...

def analize():
    input = sys.stdin.read()
    print(bases.search(input.strip().split(' ')))
    sentences = process(input)
    sentiment = sum(evaluate(tokenize(s)) for s in sentences)
    print(sentiment)
