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

from pathlib import Path
from typing import List, Tuple, Dict

import requests


def download_data(path):
    def download(remote_addr: str, local_addr: str):
        r = requests.get(remote_addr)
        with open(local_addr, 'wb') as fin:
            fin.write(r.content)

    url = 'https://raw.githubusercontent.com/emory-courses/cs329/master/dat/pos/wsj-pos.{}.gold.tsv'

    remote = url.format('trn')
    download(remote, path / Path(remote).name)

    remote = url.format('dev')
    download(remote, path / Path(remote).name)


def read_data(filename: str):
    data, sentence = [], []
    fin = open(filename)

    for line in fin:
        l = line.split()
        if l:
            sentence.append((l[0], l[1]))
        else:
            data.append(sentence)
            sentence = []

    return data


def word_count(data: List[List[Tuple[str, str]]]) -> int:
    """
    :param data: a list of tuple list where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: the total number of words in the data
    """
    return sum([len(sentence) for sentence in data])


def create_uni_pos_dict(data: List[List[Tuple[str, str]]]) -> Dict[str, List[Tuple[str, float]]]:
    """
    :param data: a list of tuple list where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a dictionary where the key is a word and the value is the list of possible POS tags with probabilities in descending order.
    """
    model = dict()
    # To be updated
    return model

import nltk
def postag(text):
    tokens = nltk.word_tokenize("And now for something completely different")


if __name__ == '__main__':
    # create a directory to download pos data
    path = Path.cwd()

    while path.name != 'cs329':
        path = path.parent

    path /= 'dat/pos'
    path.mkdir(parents=True, exist_ok=True)

    # download data
    download_data(path)

    # read data
    trn_data = read_data(path / 'wsj-pos.trn.gold.tsv')
    print(len(trn_data))
    print(trn_data[0])

    # word count
    print(word_count(trn_data))