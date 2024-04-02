from .utils import parser,getDatasetFolder
import os

def lex(destinationFolder):
    def aux(line):
        d = line.split('\t')
        word = d[0]
        label = d[1]
        return (word,-1 if label == 'NEGATIVE' else 1)
    parser(os.path.join(getDatasetFolder(),"LinguaKit"),'lex.txt',aux,destinationFolder)
    
def train(destinationFolder):
    def aux(line):
        d = line.split('\t')
        word = d[0]
        label = d[1]
        return (word,-1 if label == 'NEGATIVE' else 1)
    parser(os.path.join(getDatasetFolder(),"LinguaKit"),'train.txt',aux,destinationFolder)

def parseLinguaKit(destinationFolder):
    lex(destinationFolder)
    train(destinationFolder)


if __name__ == '__main__':
    parseLinguaKit('parsedDatasets')