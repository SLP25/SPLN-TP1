from .leIA import parseLeIA
from .linguaKit import parseLinguaKit
from .sentilex import parseSentilex
import os
import json
import shutil

def cleanup(src):
    shutil.rmtree(src)

def createTempFiles(src):
    if not os.path.isdir(src):
        if os.path.isfile(src):
            os.remove(src)
        os.mkdir(src)
    parseLeIA(src)
    parseLinguaKit(src)
    parseSentilex(src)

def createBoosters(src,dest):
    shutil.copy(os.path.join(src,'booster.json'),os.path.join(dest,'boosters.json'))

def createNegate(src,dest):
    shutil.copy(os.path.join(src,'negate.json'),os.path.join(dest,'negate.json'))

def createEmojis(src,dest):
    shutil.copy(os.path.join(src,'emojis.json'),os.path.join(dest,'emojis.json'))

def createLemmas(src,dest):
    shutil.copy(os.path.join(src,'sentilexLemmas.json'),os.path.join(dest,'lemmas.json'))

def createWords(src,dest):
    data={}
    files=['lex.json','sentilex.json','train.json','vader_lexicon.json']
    for file in files:
        with open(os.path.join(src,file)) as f:
            t=json.load(f)
            for k,v in t.items():
                data[k]=v
    with open(os.path.join(dest,'words.json'),'w') as f:
        json.dump(data,f,indent=4)
        

def parseDatasets(tempFolder,destFolder):
    createTempFiles(tempFolder)
    createBoosters(tempFolder,destFolder)
    createNegate(tempFolder,destFolder)
    createEmojis(tempFolder,destFolder)
    createLemmas(tempFolder,destFolder)
    createWords(tempFolder,destFolder)
    cleanup(tempFolder)
    
if __name__ == '__main__':
    parseDatasets('parsedDatasets','datasets')
