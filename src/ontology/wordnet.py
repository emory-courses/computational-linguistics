import nltk
from nltk.corpus import wordnet as wn

nltk.download()
print wn.synsets('dog')