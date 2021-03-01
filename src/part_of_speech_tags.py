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

import nltk
import requests
from pathlib import Path
from collections import Counter
from typing import List, Tuple, Dict


PREV_DUMMY = '!@#$'

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
    :param data: a list of tuple lists where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a dictionary where the key is a word and the value is the list of possible POS tags with probabilities in descending order.
    """
    model = dict()

    for sentence in data:
        for word, pos in sentence:
            model.setdefault(word, Counter()).update([pos])

    for word, counter in model.items():
        ts = counter.most_common()
        total = sum([count for _, count in ts])
        model[word] = [(pos, count/total) for pos, count in ts]

    return model


def create_bi_pos_dict(data: List[List[Tuple[str, str]]]) -> Dict[str, List[Tuple[str, float]]]:
    """
    :param data: a list of tuple lists where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a dictionary where the key is the previous POS tag and the value is the list of possible POS tags with probabilities in descending order.
    """
    model = dict()

    for sentence in data:
        for i, (_, curr_pos) in enumerate(sentence):
            prev_pos = sentence[i-1][1] if i > 0 else PREV_DUMMY
            model.setdefault(prev_pos, Counter()).update([curr_pos])

    for key, counter in model.items():
        ts = counter.most_common()
        total = sum([count for _, count in ts])
        model[key] = [(pos, count/total) for pos, count in ts]

    return model


def predict_uni_pos_dict(uni_pos_dict: Dict[str, List[Tuple[str, float]]], tokens: List[str], pprint=False) -> List[Tuple[str, float]]:
    def predict(token):
        t = uni_pos_dict.get(token, None)
        return t[0] if t else ('XX', 0.0)

    output = [predict(token) for token in tokens]
    if pprint:
        for token, t in zip(tokens, output):
            print('{:<15}{:<8}{:.2f}'.format(token, t[0], t[1]))

    return output


def predict_bi_pos_dict(uni_pos_dict: Dict[str, List[Tuple[str, float]]], bi_pos_dict: Dict[str, List[Tuple[str, float]]], tokens: List[str]) -> List[Tuple[str, float]]:
    output = []

    for i in range(len(tokens)):
        pos = uni_pos_dict.get(tokens[i], None)
        if pos is None:
            pos = bi_pos_dict.get(output[i-1], None)
        output.append(pos[0] if pos else ('XX', 0.0))

    return output


def evaluate_uni_pos(uni_pos_dict: Dict[str, List[Tuple[str, float]]], data: List[List[Tuple[str, str]]]):
    total, correct = 0, 0
    for sentence in data:
        tokens, gold = tuple(zip(*sentence))
        pred = [t[0] for t in predict_uni_pos_dict(uni_pos_dict, tokens)]
        total += len(tokens)
        correct += len([1 for g, p in zip(gold, pred) if g == p])
    print('{:5.2f}% ({}/{})'.format(100.0 * correct / total, correct, total))


def evaluate_bi_pos(uni_pos_dict: Dict[str, List[Tuple[str, float]]], bi_pos_dict: Dict[str, List[Tuple[str, float]]], data: List[List[Tuple[str, str]]]):
    total, correct = 0, 0
    for sentence in data:
        tokens, gold = tuple(zip(*sentence))
        pred = [t[0] for t in predict_bi_pos_dict(uni_pos_dict, bi_pos_dict, tokens)]
        total += len(tokens)
        correct += len([1 for g, p in zip(gold, pred) if g == p])
    print('{:5.2f}% ({}/{})'.format(100.0 * correct / total, correct, total))


def evaluate_nltk(data: List[List[Tuple[str, str]]]):
    total, correct = 0, 0
    for sentence in data:
        tokens, gold = tuple(zip(*sentence))
        pred = [pos for token, pos in nltk.pos_tag(tokens)]
        total += len(tokens)
        correct += len([1 for g, p in zip(gold, pred) if g == p])
    print('{:5.2f}% ({}/{})'.format(100.0 * correct / total, correct, total))


def postag(text):
    tokens = nltk.word_tokenize("And now for something completely different")
    t = nltk.pos_tag(tokens)
    print(t)


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

    # unigram model
    uni_pos_dict = create_uni_pos_dict(trn_data)

    tokens = "I bought a car yesterday that was blue".split()
    predict_uni_pos_dict(uni_pos_dict, tokens, True)

    tokens = "Dr. Choi has a good wifi connection from Emory".split()
    predict_uni_pos_dict(uni_pos_dict, tokens, True)

    dev_data = read_data(path / 'wsj-pos.dev.gold.tsv')
    evaluate_uni_pos(uni_pos_dict, dev_data)

    # bigram model
    bi_pos_dict = create_bi_pos_dict(trn_data)
    evaluate_bi_pos(uni_pos_dict, bi_pos_dict, dev_data)


