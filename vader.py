from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VaderSentimentIntensityAnalyzer
from LeIA.leia import SentimentIntensityAnalyzer as LeiaSentimentIntensityAnalyzer
import re
import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt

vader = []
leia = []
ours = []

with open("harryEN.txt") as f:
    book = f.read()
    chapters = re.split(r"\"HP 1 - Harry Potter and the\nSorcerer's Stone\n\n\"CHAPTER\s\w+\n",book)

del chapters[0]

vader = []

analyzer = VaderSentimentIntensityAnalyzer()
for chapter in chapters:
    vs = analyzer.polarity_scores(chapter)
    vader.append(vs['compound'])
    
print("vader")


with open("harryPT.txt") as f:
    livro = f.read()
    capitulos = re.split(r"\#\s[IVXLCDM]+\n",livro)

del capitulos[0]

analyzer = LeiaSentimentIntensityAnalyzer()
for capitulo in capitulos:
    vs = analyzer.polarity_scores(capitulo)
    leia.append(vs['compound'])

print("leia")


for capitulo in capitulos:
    process = subprocess.Popen(["sentAnalize","-a"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
    process.stdin.write(capitulo)
    process.stdin.flush()
    
    stdout,stderr = process.communicate()
    
    ours.append(float(stdout))
    
    process.wait()
    
vader,leia,ours = np.array(vader),np.array(leia),np.array(ours)

min_val = np.min(ours)
max_val = np.max(ours)

ours = -1 + (2* (ours-min_val)/(max_val - min_val))


X = [ str(1+x) for x in range(17)]
X_axis = np.arange(len(X))

plt.bar(X_axis-0.1,vader,0.1,label='vader')
plt.bar(X_axis,leia,0.1,label='leia')
plt.bar(X_axis+0.1,ours,0.1,label='ours')

plt.xticks(X_axis,X)
plt.xlabel("Capitulos")
plt.ylabel("Value")
plt.title("Comparation")
plt.legend()
plt.show()