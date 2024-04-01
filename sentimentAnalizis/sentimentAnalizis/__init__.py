#!/usr/bin/env python3

'''
Name 
    sentAnalize - 

SYNOPSIS
    -f <file> - Use file instead of stdin
    -c - Word Counted for averages
    -a - Calculate Average polarity
    -d - Individual averages for negative and positive polarities
    -w - Calculate polarity for each word instead of sentence in the case of being averages
    -i <+|-> - Show only positive or negative polarity values
    -s <inc|dec> - Sort the polarities by biggest or smallest respectivly
    -l - limit how many polarities are shown


DESCRIPTIONS

FILES:

'''

__version__ = "0.0.1"

from .datasetParsers.parse import parseDatasets
from .parser import analize,calibrate as calibrateFunc, totalPolaritySentence, totalPolarityWord,separateSignals,toTuples,tuples2Dict
import sys
from jjcli import *
from .datasetParsers.utils import getDatasetFolder
from os.path import join as pathJoin

def init():
    
    parseDatasets(pathJoin(getDatasetFolder(),'parsedDatasets'),getDatasetFolder())

def calibrate():
    if len(sys.argv)!=2 or sys.argv[1]=='-h':
        print("usage: sentAnalize-calibrate -h for this guide")
        print("usage: sentAnalize-calibrate <file> calibrate the program so the inputed file equivalate 0")
    else:
        with open(sys.argv[1],'r') as f:
            calibrateFunc(analize(f.read()))







def main():
    cl = clfilter("dcf:awl:i:s:", doc=__doc__) ## Option values in cl.opt dictionary
    
    in_data = "" 
    if "-f" in cl.opt:
        f = open(cl.opt.get("-f"))
        in_data = f.read()
        f.close()
    else:
        in_data = sys.stdin.read()
    sentiment = analize(in_data)
    
    if "-a" in cl.opt:
        if "-w" in cl.opt:
            value,wordCount = totalPolaritySentence(sentiment)
        else:
            value,wordCount = totalPolarityWord(sentiment)
        if '-c' in cl.opt:
            value = f"{value} out of {wordCount} words" 
    elif "-d" in cl.opt:
        pos,neg = separateSignals(sentiment)
        if "-w" in cl.opt:
            posValue,posWordCount = totalPolaritySentence(pos)
            negValue,negWordCount = totalPolaritySentence(neg)
        else:
            posValue,posWordCount = totalPolarityWord(pos)
            negValue,negWordCount = totalPolarityWord(neg)
        if '-c' in cl.opt:
            value = f"Positive:{posValue} out of {posWordCount} words\nNegative:{negValue} out of {negWordCount} words"
        else:
            value = f"Positive:{posValue}\nNegative:{negValue}"
    else:
        if "-i" in cl.opt:
            positive,negative = separateSignals(sentiment)
            pos,neg = [],[]
            for p in positive:
                for i in p:
                    pos.append(i)
            for n in negative:
                for i in n:
                    neg.append(i)
            if cl.opt.get("-i")=='+':
                value = toTuples(pos)
            elif cl.opt.get("-i")=='-':
                value = toTuples(neg)
            else:
                print("invalid option for flag i")
                exit()
        else:
            value=[]
            for words in sentiment:
                for w in words:
                    value.append((w.text,w.value()))
        value = list(tuples2Dict(value).items())
        if "-s" in cl.opt:
            if cl.opt.get("-s")=='inc':
                value.sort(key=lambda x:x[1])
            elif cl.opt.get("-s")=='dec':
                value.sort(reverse=True,key=lambda x:x[1])
        else:
            value.sort(key=lambda x:x[0])
        if "-l" in cl.opt:
            value = value[:int(cl.opt.get("-l"))]
        value = '\n'.join(map(lambda x: f"{x[0]} : {x[1]}",value))
    print(value)
        
            
        
        
    
            
            
        
        
    