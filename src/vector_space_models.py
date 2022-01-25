# ========================================================================
# Copyright 2022 Emory University
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

import json
from collections import Counter
from typing import Dict, Tuple

import math
import requests


def download(remote_addr: str, local_addr: str):
    r = requests.get(remote_addr)
    fin = open(local_addr, 'wb')
    fin.write(r.content)


def term_frequencies(fables) -> Dict[str, Counter]:
    def key(t): return t[t.rfind('&') + 1:]

    return {key(fable['source']): Counter(fable['tokens'].split()) for fable in fables}


def document_frequencies(fables) -> Dict[str, int]:
    dfs = Counter()
    for fable in fables:
        dfs.update(set(fable['tokens'].split()))
    return dfs


def tf_idfs(fables) -> Dict[str, Dict[str, int]]:
    tfs = term_frequencies(fables)
    dfs = document_frequencies(fables)
    out = dict()
    D = len(tfs)

    for dkey, term_counts in tfs.items():
        out[dkey] = {t: tf * math.log(D / dfs[t]) for t, tf in term_counts.items()}

    return out


if __name__ == '__main__':
    # download aesop's fables
    aesop_link = 'https://raw.githubusercontent.com/emory-courses/computational-linguistics/master/docs/res/aesopfables.json'
    aesop_file = 'res/aesopfables.json'
    # download(aesop_link, aesop_file)

    # read json
    fables = json.load(open(aesop_file))
    print(len(fables))
    for fable in fables[:10]: print(fable['title'])

    # retrieve term frequencies
    tfs = term_frequencies(fables)
    print(tfs['Androcles'])

    # retrieve document frequencies
    dfs = document_frequencies(fables)
    print(dfs['Lion'], dfs['lion'])
    for term, count in sorted(dfs.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(term, count)

    # retrieve TF-IDFs
    tfidfs = tf_idfs(fables)
    print(tfidfs['Androcles']['Lion'])

    for t, tf in sorted(tfs['Androcles'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(t, tf, math.log(len(tfs) / dfs[t]))

    for t, tfidf in sorted(tfidfs['Androcles'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(t, tfidf, dfs[t])

