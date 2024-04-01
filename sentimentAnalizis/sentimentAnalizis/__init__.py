#!/usr/bin/env python3

'''
Name 
    sentAnalize - 

SYNOPSIS
    -f <file> - Use file instead of stdin
    -n - Use normalization (only affects negative polarities)
    -c - Print word counts
    -a - Calculate Average polarity
    -d - Individual averages for negative and positive polarities
    -i <+|-> - Show only positive or negative polarity values
    -s <dec|inc|alp> - Sort the polarities in increasing, decreasing or alphabetical orders, respectively (decreasing is default)
    -l <limit> - Limit how many polarities are shown
    --help - Show this help message


DESCRIPTIONS

FILES:

'''

__version__ = "0.0.1"

from .datasetParsers.parse import parseDatasets
from .parser import analize,calibrate as calibrateFunc, normalize
from .utils import collect
import sys
from jjcli import *
from .datasetParsers.utils import getDatasetFolder
from os.path import join as pathJoin

def init():
    parseDatasets(pathJoin(getDatasetFolder(),'parsedDatasets'),getDatasetFolder())

def calibrate():
    if len(sys.argv)!=2 or sys.argv[1]=='--help':
        print("usage: sentAnalize-calibrate -h for this guide")
        print("usage: sentAnalize-calibrate <file> calibrate the program so the inputed file equivalate 0")
    else:
        with open(sys.argv[1],'r') as f:
            bases,_ = analize(f.read())
            calibrateFunc(bases)

cl = clfilter("dcf:awl:i:s:n", doc=__doc__) ## Option values in cl.opt dictionary

def print_stat(value, occurences, label="", trimDecimals=False):
    prefix = f"{label} : " if label else ""
    ans = f"{value:.2f}" if trimDecimals else f"{value:.12f}"
    suffix = f" (x{occurences})" if "-c" in cl.opt else ""

    print(f"{prefix}{ans}{suffix}")

def handle_bases(bases, wordCount):
    #Calcualte average
    if "-a" in cl.opt:
        total = sum(b.value() for b in bases)
        print_stat(total/wordCount, wordCount)      #TODO: divide by zero

    #Or treat the words individually
    else:
        out=[]
        for w,bs in collect(bases).items():
            avg = sum([b.value() for b in bs])/len(bs)
            out.append((w,avg,bs))
        
        #Sort the output
        reverse = cl.opt.get("-s") == "dec" or cl.opt.get("-s") == None
        key = (lambda x: x[0]) if cl.opt.get("-s") == "alp" else (lambda x: x[1])
        out.sort(key=key, reverse=reverse)
    
        #Limit the output
        if "-l" in cl.opt:
            out = out[:int(cl.opt.get("-l"))]

        for word, value, bs in out:
            print_stat(value, len(bs), word, True)


def main():
    if "-i" in cl.opt and "-d" in cl.opt:
        print("Incompatible options: -i and -d")
        return

    if "-a" in cl.opt and "-l" in cl.opt:
        print("Incompatible options: -a and -l")
        return

    if "-a" in cl.opt and "-s" in cl.opt:
        print("Incompatible options: -a and -s")
        return

    #TODO: check values of -s -i -l

    #Get the input
    in_data = "" 
    if "-f" in cl.opt:
        f = open(cl.opt.get("-f"))
        in_data = f.read()
        f.close()
    else:
        in_data = sys.stdin.read()

    #Analize the input
    bases, wordCount = analize(in_data)

    #Optionally normalize
    if "-n" in cl.opt:
        normalize(bases)

    #Filter only one polarity
    if "-i" in cl.opt:
        pol = cl.opt.get("-i")
        filt = (lambda v: v.value() > 0) if pol == "+" else (lambda v: v.value() < 0)
        handle_bases(list(filter(filt,bases)), wordCount)
    #Output two results, one for each polarity
    elif "-d" in cl.opt:
        print("POSITIVOS")
        handle_bases([b for b in bases if b.value() > 0], wordCount)
        print("\nNEGATIVOS")
        handle_bases([b for b in bases if b.value() < 0], wordCount)
    else:
        handle_bases(bases, wordCount)