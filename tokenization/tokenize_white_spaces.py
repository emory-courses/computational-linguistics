fin  = open('emory.txt')
fout = open('emory.txt.tokenized', 'w')

tokens = list()

for line in fin:
    l = line.split()
    tokens.extend(l)

for token in tokens:
    fout.write(token+'\n')

fin.close()
fout.close()