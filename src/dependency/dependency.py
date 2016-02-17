import re
import bisect

RE_TAB = re.compile('\t')
ROOT_TAG = "@#r$%"
BLANK_FIELD = '_'

class TSVReader:
    def __init__(self, form=-1, lemma=-1, pos=-1, feats=-1, dhead=-1, deprel=-1):
        self.form   = form
        self.lemma  = lemma
        self.pos    = pos
        self.feats  = feats
        self.dhead  = dhead
        self.deprel = deprel

    def __iter__(self):
        return self

    def open(self, fin):
        self.fin = fin

    def close(self):
        if self.fin: self.fin.close()

    def next(self):
        list = []

        for line in self.fin:
            line = line.strip()

            if not line:
                if not list: continue
                break

            list.append(RE_TAB.split(line))

        if list: return self.toNodeList(list)
        else: raise StopIteration

    def toNodeList(self, list):
        nodes = [NLPNode()]
        for i,values in enumerate(list): nodes.append(self.create(i+1, values))

        if self.dhead >= 0:
            for i,values in enumerate(list): self.initDependencyHead(i+1, values, nodes)

        return nodes

    def create(self, id, values):
        f = l = p = t = None
        if self.form  >= 0: f = values[self.form]
        if self.lemma >= 0: l = values[self.lemma]
        if self.pos   >= 0: p = values[self.pos]
        if self.feats >= 0: t = values[self.feats]
        return NLPNode(id, f, l, p, t)

    def initDependencyHead(self, id, values, nodes):
        headID = int(values[self.dhead])
        nodes[id].setDependencyHead(nodes[headID], values[self.deprel])

class NLPNode:
    def __init__(self, id=0, form=ROOT_TAG, lemma=ROOT_TAG, pos=ROOT_TAG, feats=BLANK_FIELD, dhead=None, deprel=None):
        self.id                 = id
        self.word_form          = form
        self.lemma              = lemma
        self.part_of_speech_tag = pos
        self.feats              = feats
        self.dependency_head    = dhead
        self.dependency_label   = deprel
        self.dependent_list     = []

    def __gt__(self, other):
        return self.id > other.id

    def __str__(self):
        l = [str(self.id), self.word_form, self.lemma, self.part_of_speech_tag, str(self.feats)]

        if self.dependency_head:
            l.append(str(self.dependency_head.id))
            l.append(self.dependency_label)

        return '\t'.join(l)

#   ==================== GETTERS ====================

    def getWordForm(self):
        return self.word_form

    def getLemma(self):
        return self.lemma

    def getPartOfSpeechTag(self):
        return self.part_of_speech_tag

    def getDependencyHead(self):
        return self.dependency_head

    def getDependencyLabel(self):
        return self.dependency_head

    def getDependentList(self):
        return self.dependent_list

    def getSubNodeList(self):
        list = []
        self.getSubNodeListAux(self, list)
        list.sort()
        return list

    def getSubNodeListAux(self, node, list):
        list.append(node)

        for child in node.getDependentList():
            self.getSubNodeListAux(child, list)

#   ==================== SETTERS ====================

    def setWordForm(self, form):
        self.word_form = form

    def getLemma(self, lemma):
        self.lemma = lemma

    def getPartOfSpeechTag(self, tag):
        self.part_of_speech_tag = tag

    def setDependencyHead(self, node, label=None):
        if self.dependency_head != None:
            self.dependency_head.dependent_list.remove(self)

        if node != None:
            bisect.insort(node.dependent_list, self)

        self.dependency_head = node
        self.setDependencyLabel(label)

    def setDependencyLabel(self, label):
        self.dependency_label = label


filename = '/Users/jdchoi/Documents/EmoryNLP/emorynlp/src/main/resources/dat/emorynlp.txt.nlp'
reader = TSVReader(1,2,3,4,5,6)
reader.open(open(filename))

for nodes in reader:
    print '\n'.join(map(str,nodes)[1:])+'\n'

    for node in nodes[1:]:
        print node.id, node.getDependencyHead().id, map(lambda n: n.id, node.getDependentList())

    exit(1)
