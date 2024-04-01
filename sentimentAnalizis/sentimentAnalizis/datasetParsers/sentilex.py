from .utils import parser,average_parser,getDatasetFolder
import os

def sentilex(destinationFolder):
    def aux(line):
        s = line.split(';')
        if len(s)==5:
            word,flex,tg,pol,anot = s
            word,lemma = word.split(',')
            pol=float(pol[7:])
            return (word,pol)
        return None
    parser(os.path.join(getDatasetFolder(),"sentilex"),'sentilex.txt',aux,destinationFolder)
    
def sentilexlemmas(destinationFolder):
    def aux(line):
        s = line.split(';')
        if len(s)==5:
            word,flex,tg,pol,anot = s
            word,lemma = word.split(',')
            lemma,pos = lemma.split('.')
            pol=float(pol[7:])
            return (lemma,pol)
        return None
    average_parser(os.path.join(getDatasetFolder(),"sentilex"),'sentilex.txt',aux,destinationFolder,'sentilexLemmas.json')
    
def parseSentilex(destinationFolder):
    sentilex(destinationFolder)
    sentilexlemmas(destinationFolder)

if __name__ == "__main__":
    parseSentilex('parsedDatasets')