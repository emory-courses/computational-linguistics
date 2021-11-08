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
from typing import List, Tuple, Dict, Any


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


def to_probs(model: Dict[Any, Counter]) -> Dict[str, List[Tuple[str, float]]]:
    for feature, counter in model.items():
        ts = counter.most_common()
        total = sum([count for _, count in ts])
        model[feature] = [(pos, count/total) for pos, count in ts]
    return model


def create_uni_pos_dict(data: List[List[Tuple[str, str]]]) -> Dict[str, List[Tuple[str, float]]]:
    """
    :param data: a list of tuple lists where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a dictionary where the key is a word and the value is the list of possible POS tags with probabilities in descending order.
    """
    model = dict()

    for sentence in data:
        for word, pos in sentence:
            model.setdefault(word, Counter()).update([pos])

    return to_probs(model)


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

    return to_probs(model)


def create_bi_wp_dict(data: List[List[Tuple[str, str]]]) -> Dict[str, List[Tuple[str, float]]]:
    """
    :param data: a list of tuple lists where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a dictionary where the key is the previous word and the value is the list of possible POS tags with probabilities in descending order.
    """
    model = dict()

    for sentence in data:
        for i, (_, curr_pos) in enumerate(sentence):
            prev_word = sentence[i-1][0] if i > 0 else PREV_DUMMY
            model.setdefault(prev_word, Counter()).update([curr_pos])

    return to_probs(model)


def create_bi_wn_dict(data: List[List[Tuple[str, str]]]) -> Dict[str, List[Tuple[str, float]]]:
    """
    :param data: a list of tuple lists where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a dictionary where the key is the previous word and the value is the list of possible POS tags with probabilities in descending order.
    """
    model = dict()

    for sentence in data:
        for i, (_, curr_pos) in enumerate(sentence):
            next_word = sentence[i+1][0] if i+1 < len(sentence) else PREV_DUMMY
            model.setdefault(next_word, Counter()).update([curr_pos])

    return to_probs(model)


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
            pos = bi_pos_dict.get(output[i-1][0] if i > 0 else PREV_DUMMY, None)
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


def predict_interporlation(
        uni_pos_dict: Dict[str, List[Tuple[str, float]]],
        bi_pos_dict: Dict[str, List[Tuple[str, float]]],
        bi_wp_dict: Dict[str, List[Tuple[str, float]]],
        bi_wn_dict: Dict[str, List[Tuple[str, float]]],
        uni_pos_weight: float,
        bi_pos_weight: float,
        bi_wp_weight: float,
        bi_wn_weight: float,
        tokens: List[str]) -> List[Tuple[str, float]]:
    output = []

    for i in range(len(tokens)):
        scores = dict()
        curr_word = tokens[i]
        prev_pos = output[i-1][0] if i > 0 else PREV_DUMMY
        prev_word = tokens[i-1] if i > 0 else PREV_DUMMY
        next_word = tokens[i+1] if i+1 < len(tokens) else PREV_DUMMY

        for pos, prob in uni_pos_dict.get(curr_word, dict()):
            scores[pos] = scores.get(pos, 0) + prob * uni_pos_weight

        for pos, prob in bi_pos_dict.get(prev_pos, dict()):
            scores[pos] = scores.get(pos, 0) + prob * bi_pos_weight

        for pos, prob in bi_wp_dict.get(prev_word, dict()):
            scores[pos] = scores.get(pos, 0) + prob * bi_wp_weight

        for pos, prob in bi_wn_dict.get(next_word, dict()):
            scores[pos] = scores.get(pos, 0) + prob * bi_wn_weight

        o = max(scores.items(), key=lambda k, v: v) if scores else ('XX', 0.0)
        output.append(o)

    return output


def evaluate_interpolation(
        uni_pos_dict: Dict[str, List[Tuple[str, float]]],
        bi_pos_dict: Dict[str, List[Tuple[str, float]]],
        bi_wp_dict: Dict[str, List[Tuple[str, float]]],
        bi_wn_dict: Dict[str, List[Tuple[str, float]]],
        uni_pos_weight: float,
        bi_pos_weight: float,
        bi_wp_weight: float,
        bi_wn_weight: float,
        data: List[List[Tuple[str, str]]],
        pprint=False):
    total, correct = 0, 0
    for sentence in data:
        tokens, gold = tuple(zip(*sentence))
        pred = [t[0] for t in predict_interporlation(uni_pos_dict, bi_pos_dict, bi_wp_dict, bi_wn_dict, uni_pos_weight, bi_pos_weight, bi_wp_weight, bi_wn_weight, tokens)]
        total += len(tokens)
        correct += len([1 for g, p in zip(gold, pred) if g == p])
    accuracy = 100.0 * correct / total
    print('{:5.2f}% ({}/{}) - uni_pos: {:3.1f}, bi_pos: {:3.1f}, bi_wp: {:3.1f}, bi_np: {:3.1f}'.format(accuracy, correct, total, uni_pos_weight, bi_pos_weight, bi_wp_weight, bi_wn_weight))
    return accuracy



def postag(text):
    tokens = nltk.word_tokenize("And now for something completely different")
    t = nltk.pos_tag(tokens)
    print(t)


if __name__ == '__main__':
    # create a directory to download pos data
    path = Path.cwd()

    while path.name != 'cs329':
        path = path.parent

    path /= 'res/pos'
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


