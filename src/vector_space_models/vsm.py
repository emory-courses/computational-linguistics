#!/usr/bin/python
import os
import sys
import glob
import math
from collections import Counter

def generateStopWords(tf, df, threshold):
    if threshold < 1: dc = len(tf)
    else: dc = 1
    return set([k for (k,v) in df.items() if float(v)/dc >= threshold])

def getTermFrequencies(fin):
    tf = Counter()
    for line in fin: tf.update(line.split())
    return tf

def getDocumentFrequencies(tf):
    df = Counter()
    for d in tf: df.update(d.keys())
    return df

def getTFIDF(tf, df, dc):
    return tf * math.log(float(dc) / df)

def getTFIDFs(tf, df, sw):
    dc = len(tf)
    tfidf = []

    for d1 in tf:
        d2 = {k:getTFIDF(v,df[k],dc) for (k,v) in d1.items() if k not in sw}
        tfidf.append(d2)

    return tfidf

def getEuclideanDistance(d1, d2):
    sum = 0

    for (k,v) in d1.items():
        if k in d2: sum += (v - d2[k])**2
        else: sum += v**2

    for (k,v) in d2.items():
        if k not in d1: sum += v**2

    return math.sqrt(sum)




IN_DIR = sys.argv[1]
filenames = glob.glob(os.path.join(IN_DIR,'*'))
tf = [getTermFrequencies(open(filename)) for filename in filenames]
df = getDocumentFrequencies(tf)
sw = generateStopWords(tf, df, 200)
sw = generateStopWords(tf, df, .8)
tfidf = getTFIDFs(tf, df, sw)
getEuclideanDistance(tfidf[0], tfidf[1])