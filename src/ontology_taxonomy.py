# ========================================================================
# Copyright 2020 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
from typing import Optional, Set, List

from nltk.corpus import wordnet as wn
from nltk.corpus.reader import Synset


def synonyms(word: str, pos: Optional[str] = None, count: Optional[int] = 0) -> Set[str]:
    """
    :param word: the word to retrieve synonyms for.
    :param pos: the part-of-speech tag of the word; if None, retrieve synonyms across all part-of-speeches.
    :param count: the minimum frequency of the synonym to be retrieved.
    :return: the lemma set of all synonyms of the specific word.
    """
    syns = set()

    for synset in wn.synsets(word, pos):
        for lemma in synset.lemmas():
            if lemma.count() >= count:
                syns.add(lemma.name())

    return syns


def lch_paths(sense_0: str, sense_1: str) -> List[List[Synset]]:
    """
    :param sense_0: the ID of the first sense.
    :param sense_1: the ID of the second sense.
    :return: the list of LCH paths where each LCH path shows the path from the LCD to its root.
    """
    synset_0 = wn.synset(sense_0)
    synset_1 = wn.synset(sense_1)
    hypernym_paths_0 = synset_0.hypernym_paths()
    lch = synset_0.lowest_common_hypernyms(synset_1)
    paths = []

    for hypernym in lch:
        for syn_list in hypernym_paths_0:
            i = next((i for i, syn in enumerate(syn_list) if syn == hypernym), -1)
            if i >= 0: paths.append(syn_list[:i+1])

    return paths


if __name__ == '__main__':
    print(synonyms('dog', pos='n'))
    print(synonyms('dog', pos='n'))

    paths = lch_paths('dog.n.01', 'cat.n.01')
    for path in paths: print(' -> '.join([syn.name() for syn in path]))
