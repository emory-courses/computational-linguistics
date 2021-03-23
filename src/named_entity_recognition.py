# ========================================================================
# Copyright 2021 Emory University
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

__author__ = 'Jinho D. Choi'

from types import SimpleNamespace
from typing import Dict, List, Tuple, Set, Iterable, Any

import ahocorasick


def recognize_ngram(tokens: List[str], gazetteer: Dict[str, Set[str]]) -> List[Tuple[int, int, str, Set[str]]]:
    """
    :param tokens: a sequence of input tokens.
    :param gazetteer: a dictionary whose key is the text span of a named entity (e.g., "Emory University") and the value is the set of named entity tags for the entity.
    :return: a list of entities where each entity is represented by a tuple consisting of the following 4 items:
             - Index of the beginning token (inclusive)
             - Index of the ending token (exclusive)
             - Text span representing the entity (e.g., "Emory University")
             - Set of named entity tags for the entity
    """
    entities = []
    for i in range(len(tokens)):
        for j in range(i+1, len(tokens)+1):
            key = ' '.join(tokens[i:j])
            val = gazetteer.get(key, None)
            if val: entities.append((i, j, key, val))
    return entities


def create_ac(data: Iterable[Tuple[str, Any]]):
    """
    Creates the Aho-Corasick automation and adds all (span, value) pairs in the data and finalizes this matcher.
    :param data: a collection of (span, value) pairs.
    """
    AC = ahocorasick.Automaton(ahocorasick.STORE_ANY)

    for span, value in data:
        if span in AC:
            t = AC.get(span)
        else:
            t = SimpleNamespace(span=span, values=set())
            AC.add_word(span, t)
        t.values.add(value)

    AC.make_automaton()
    return AC


def match(AC, tokens: List[str]) -> List[Tuple[str, int, int, Set[str]]]:
    """
    :param AC: the finalized Aho-Corasick automation.
    :param tokens: the list of input tokens.
    :return: a list of tuples where each tuple consists of
             - span: str,
             - start token index (inclusive): int
             - end token index (exclusive): int
             - a set of values for the span: Set[Any]
    """
    smap, emap, idx = dict(), dict(), 0
    for i, token in enumerate(tokens):
        smap[idx] = i
        idx += len(token)
        emap[idx] = i
        idx += 1

    # find matches
    text = ' '.join(tokens)
    spans = []
    for eidx, t in AC.iter(text):
        eidx += 1
        sidx = eidx - len(t.span)
        sidx = smap.get(sidx, None)
        eidx = emap.get(eidx, None)
        if sidx is None or eidx is None: continue
        spans.append((t.span, sidx, eidx + 1, t.values))

    return spans


if __name__ == '__main__':
    GAZETTEER = {
        'Jinho': {'PER'},
        'Jinho Choi': {'PER'},
        'Emory': {'PER', 'ORG'},
        'Emory University': {'ORG'},
        'United States': {'GPE'},
        'United States of America': {'GPE'},
    }

    text = 'Jinho Choi is a professor at Emory University in the United States of America'
    tokens = text.split()

    entities = recognize_ngram(tokens, GAZETTEER)
    for entity in entities: print(entity)

    GAZETTEER = [
        ('Jinho', 'PER'),
        ('Jinho Choi', 'PER'),
        ('Emory', 'PER'),
        ('Emory', 'ORG'),
        ('Emory University', 'ORG'),
        ('United States', 'GPE'),
        ('United States of America', 'GPE'),
        ('Korean', 'LANG'),
        ('Korea', 'GPE'),
        ('South Korea', 'GPE'),
    ]

    AC = create_ac(GAZETTEER)

