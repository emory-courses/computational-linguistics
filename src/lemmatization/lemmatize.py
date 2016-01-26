def readBaseSet(fin):
    s = set()
    for line in fin:
        s.add(line.strip())
    return s

def readExceptionDictionary(fin):
    d = dict()
    for line in fin:
        l = line.split()
        d[l[0]] = l[1]
    return d

def _lemmatize(word, baseset, excdict, rulelist):
    word = word.lower()

    if word in baseset:
        return word

    if word in excdict:
        return excdict[word]

    for rule in rulelist:
        if word.endswith(rule[0]):
            idx = len(rule[0])
            if len(rule) > 2 and rule[2]: idx += 1
            lemma = word[:-idx] + rule[1]
            if lemma in baseset: return lemma

    return None

def lemmatize(word, pos='*'):
    if pos is 'v': return _lemmatize(word, VERB[0], VERB[1], VERB[2])
    if pos is 'n': return _lemmatize(word, NOUN[0], NOUN[1], NOUN[2])
    if pos is 'j': return _lemmatize(word, ADJT[0], ADJT[1], ADJT[2])
    if pos is 'r': return _lemmatize(word, ADRB[0], ADRB[1], ADRB[2])

    for pos in ['v','n','j','r']:
        lemma = lemmatize(word, pos)
        if lemma: return lemma

    return word.lower()

VERB_BASE_SET      = readBaseSet(open('verb.base'))
NOUN_BASE_SET      = readBaseSet(open('noun.base'))
ADJECTIVE_BASE_SET = readBaseSet(open('adjective.base'))
ADVERB_BASE_SET    = readBaseSet(open('adverb.base'))

VERB_EXC_DICT      = readExceptionDictionary(open('verb.exc'))
NOUN_EXC_DICT      = readExceptionDictionary(open('noun.exc'))
ADJECTIVE_EXC_DICT = readExceptionDictionary(open('adjective.exc'))
ADVERB_EXC_DICT    = readExceptionDictionary(open('adverb.exc'))

VERB_RULES         = [('ies','y'),('ied','y'),('es',''),('ed',''),('s',''),('d',''),('ying','ie'),('ing',''),('ing','e'),('n',''),('ung','ing'),('ing','',True),('ing','e',True),('ed','',True)]
NOUN_RULES         = [('ies','y'),('es',''),('s',''),('men','man'),('ae','a'),('i','us')]
ADJECTIVE_RULES    = [('ier','y'),('iest','y'),('er',''),('est',''),('er','e'),('est','e'),('er','',True),('est','',True)]
ADVERB_RULES       = [('ier','y'),('iest','y'),('er',''),('est',''),('er','e'),('est','e'),('er','',True),('est','',True)]

VERB = (VERB_BASE_SET, VERB_EXC_DICT, VERB_RULES)
NOUN = (NOUN_BASE_SET, NOUN_EXC_DICT, NOUN_RULES)
ADJT = (ADJECTIVE_BASE_SET, ADJECTIVE_EXC_DICT, ADJECTIVE_RULES)
ADRB = (ADVERB_BASE_SET, ADVERB_EXC_DICT, ADVERB_RULES)


print '######### VERBS ########'
word = 'study'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'studies'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'studied'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'studying'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'push'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'pushes'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'take'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'takes'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'taking'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'lie'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'lying'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'run'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'running'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'enter'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'entered'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'hear'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'heard'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'draw'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'drawn'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

word = 'cling'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'clung'
print '%10s -> %10s' % (word, lemmatize(word,'v'))

print '######### NOUNS ########'
word = 'study'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'studies'
print '%10s -> %10s' % (word, lemmatize(word,'n'))

word = 'cross'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'crosses'
print '%10s -> %10s' % (word, lemmatize(word,'n'))

word = 'area'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'areas'
print '%10s -> %10s' % (word, lemmatize(word,'n'))

word = 'woman'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'women'
print '%10s -> %10s' % (word, lemmatize(word,'n'))

word = 'vertebra'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'vertebrae'
print '%10s -> %10s' % (word, lemmatize(word,'n'))

word = 'focus'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'foci'
print '%10s -> %10s' % (word, lemmatize(word,'n'))


print '###### ADJECTIVES ######'
word = 'easy'
print '%10s -> %10s' % (word, lemmatize(word,'j'))
word = 'easier'
print '%10s -> %10s' % (word, lemmatize(word,'j'))
word = 'easiest'
print '%10s -> %10s' % (word, lemmatize(word,'j'))

word = 'small'
print '%10s -> %10s' % (word, lemmatize(word,'j'))
word = 'smaller'
print '%10s -> %10s' % (word, lemmatize(word,'j'))
word = 'smallest'
print '%10s -> %10s' % (word, lemmatize(word,'j'))

word = 'big'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'bigger'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'biggest'
print '%10s -> %10s' % (word, lemmatize(word,'r'))


print '######## ADVERBS #######'
word = 'early'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'earlier'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'earliest'
print '%10s -> %10s' % (word, lemmatize(word,'r'))

word = 'soon'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'sooner'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'soonest'
print '%10s -> %10s' % (word, lemmatize(word,'r'))

word = 'large'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'larger'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'largest'
print '%10s -> %10s' % (word, lemmatize(word,'r'))


print '######## UNKNOWN #######'
word = 'studied'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'studying'
print '%10s -> %10s' % (word, lemmatize(word,'v'))
word = 'crosses'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'women'
print '%10s -> %10s' % (word, lemmatize(word,'n'))
word = 'easier'
print '%10s -> %10s' % (word, lemmatize(word,'j'))
word = 'easiest'
print '%10s -> %10s' % (word, lemmatize(word,'j'))
word = 'larger'
print '%10s -> %10s' % (word, lemmatize(word,'r'))
word = 'largest'
print '%10s -> %10s' % (word, lemmatize(word,'r'))

word = 'running'
print '%10s -> %10s' % (word, lemmatize(word))
word = 'zipped'
print '%10s -> %10s' % (word, lemmatize(word))
word = 'bigger'
print '%10s -> %10s' % (word, lemmatize(word))
word = 'biggest'
print '%10s -> %10s' % (word, lemmatize(word))
