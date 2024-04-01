import re
import json
import os
import unidecode
from collections import defaultdict


def getDatasetFolder():
    datasetParsers,_ = os.path.split(__file__) 
    sentimentAnalisisSub = os.path.join(datasetParsers,'..')
    return os.path.join(sentimentAnalisisSub,'datasets')

with open(os.path.join(getDatasetFolder(),'emojis.txt')) as f:
    emojisList=f.readline()

def remove_accents(word):
    indexes=[]
    emojiList=[]
    for p,w in enumerate(word):
        if w in emojisList:
            indexes.append(p)
            emojiList.append(w)
    # Convert the word to ASCII characters without accents
    cleaned_word = unidecode.unidecode(word)
    # Remove the 'ç' character
    cleaned_word = cleaned_word.replace('ç', 'c')
    for p,i in enumerate(indexes):
       cleaned_word = cleaned_word[:i]+emojiList[p]+cleaned_word[i:]
    return cleaned_word.lower()


def parser(folder,file,func,outputFolder,output_file=None):
    input_path = os.path.join(folder,file)
    if output_file == None:
        output_file = '.'.join(file.split('.')[:-1]) + '.json'
    output_path = os.path.join(outputFolder,output_file)
    
    with open(input_path) as f:
        data={}
        for line in f:
            line=line.strip()
            r = func(line)
            if r is None: continue
            k,v = r
            if type(v)==str:
                data[remove_accents(k)]=remove_accents(v)
            else:
                data[remove_accents(k)]=v
        json_data = json.dumps(data, indent=4)
        with open(output_path,"w") as json_file:
            json_file.write(json_data)
            
def average_parser(folder,file,func,outputFolder,output_file=None):
    input_path = os.path.join(folder,file)
    if output_file == None:
        output_file = '.'.join(file.split('.')[:-1]) + '.json'
    output_path = os.path.join(outputFolder,output_file)
    
    with open(input_path) as f:
        data=defaultdict(list)
        for line in f:
            line=line.strip()
            r = func(line)
            if r is None: continue
            k,v = r
            data[remove_accents(k)].append(v)
        for k in data.keys():
            data[k]=sum(data[k])/len(data[k])
        json_data = json.dumps(data, indent=4)
        with open(output_path,"w") as json_file:
            json_file.write(json_data)