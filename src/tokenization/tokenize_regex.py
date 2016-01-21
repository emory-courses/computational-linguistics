import string
import re

fin  = open('emory.txt')
fout = open('emory.txt.tokenized', 'w')

tokens = list()
acronym = re.compile('^([A-Z]\.)+$')
apostrophe = re.compile('(.*)(\'s)$')

for line in fin:
    l = line.split()

    for token in l:
        m = acronym.match(token)
        if m:
            tokens.append(token)
            continue

        m = apostrophe.match(token)
        if m:
            if m.group(1): tokens.append(m.group(1))
            tokens.append(m.group(2))
            continue

        beginIndex = 0

        for currIndex,c in enumerate(token):
            if c in string.punctuation:
                if beginIndex < currIndex:
                    tokens.append(token[beginIndex:currIndex])

                tokens.append(c)
                beginIndex = currIndex + 1

        if beginIndex < len(token):
            tokens.append(token[beginIndex:])

for token in tokens:
    fout.write(token+'\n')

fin.close()
fout.close()
