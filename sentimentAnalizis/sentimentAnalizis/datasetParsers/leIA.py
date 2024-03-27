from .utils import parser
            
def booster(destinationFolder):
    def aux(line):
        d = line.split(' ')
        label = d[-1]
        word = ' '.join(d[:-1])
        return (word,2 if label == 'INCR' else 0.5)
    parser("datasets/leIA",'booster.txt',aux,destinationFolder)

def emojis(destinationFolder):
    def aux(line):
        d = line.split('\t')
        k = d[0]
        v = ' '.join(d[1:])
        return (k,v)
    parser("datasets/leIA",'emojis.txt',aux,destinationFolder)

def negate(destinationFolder):
    def aux(line):
        return (line.strip(),-1)
    parser("datasets/leIA",'negate.txt',aux,destinationFolder)

def vader_legicon(destinationFolder):
    def aux(line):
        d = line.split('\t')
        k = d[0]
        v = d[1]
        return (k,float(v))
    parser("datasets/leIA",'vader_lexicon.txt',aux,destinationFolder)

def parseLeIA(destinationFolder):
    booster(destinationFolder)
    emojis(destinationFolder)
    negate(destinationFolder)
    vader_legicon(destinationFolder)

if __name__ == '__main__':
    parseLeIA('parsedDatasets')