import json
import sys

def load_dataset(dataset):
    with open(f'datasets/{dataset}.json') as f:
        return json.load(f)


#ignore emojis for now...
words = load_dataset("words")
lemmas = load_dataset("lemmas")
boosters = load_dataset("boosters")
negate = load_dataset("negate")

#TODO: create tries for bases and modifiers
bases = ...         #The base values. additive in nature
modifiers = ...     #Modify the surrounding base values (multiplicative)
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


while True:
    input = sys.stdin.read()
    sentences = process(input)
    sentiment = sum(evaluate(tokenize(s)) for s in sentences)
    print(sentiment)
