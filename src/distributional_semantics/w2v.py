#!/usr/bin/python
import sys
import numpy as np

def readVocab(fin):
    return ([word.strip() for word in fin])

def readWordVectors(fin, vocab):
    word_vectors = {}
    header = fin.readline()
    vocab_size, vector_size = map(int, header.split())
    binary_len = np.dtype('float32').itemsize * vector_size
    print 'All vocab size: ', vocab_size
    print 'Our vocab size: ', len(vocab)
    print 'Vector size   : ', vector_size

    for line in xrange(vocab_size):
        word = []
        while True:
            ch = fin.read(1)
            if ch == b' ':
                word = ''.join(word)
                break
            if ch != b'\n':
                word.append(ch)

        if word in vocab: word_vectors[word] = np.fromstring(fin.read(binary_len), dtype='float32')
        else: fin.read(binary_len)

    return word_vectors

def getCosineSimilarity(v1, v2):
    num  = np.dot(v1, v2)
    den1 = np.sqrt(np.dot(v1, v1))
    den2 = np.sqrt(np.dot(v2, v2))
    return num / (den1 * den2)

def getSimilarities(wv, v1):
    l = [(getCosineSimilarity(v1, v2), w2) for (w2, v2) in wv.items()]
    return sorted(l, reverse=True)

VOCAB_FILE = sys.argv[1]
W2V_FILE = sys.argv[2]
K = 10

vocab = readVocab(open(VOCAB_FILE))
wv = readWordVectors(open(W2V_FILE), vocab)

print 'king:'
l = getSimilarities(wv, wv['king'])
for (v, w) in l[:K]: print '  ', w, v

print 'king - male + female:'
l = getSimilarities(wv, wv['king'] - wv['male'] + wv['female'])
for (v, w) in l[:K]: print '  ', w, v

