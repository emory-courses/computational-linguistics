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

from typing import Dict, List, Tuple, Set


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
        for j in range(1, len(tokens)+1):
            key = ' '.join(tokens[i:j])
            val = gazetteer.get(key, None)
            if val: entities.append((i, j, key, val))
    return entities


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