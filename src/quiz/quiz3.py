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
from typing import List, Tuple


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


def train(data: List[List[Tuple[str, str]]]) -> Tuple[...]:
    """
    :param data: a list of tuple lists where each inner list represents a sentence and every tuple is a (word, pos) pair.
    :return: a tuple of a variable number of dictionaries
    """
    # To be updated
    # The returned tuple can be something like (uni_pos_dict, bi_pos_dict, bi_wp_dict, bi_wn_dict, uni_pos_weight, bi_pos_weight, bi_wp_weight, bi_wn_weight)
    return tuple()


def predict(tokens: List[str], *args) -> List[Tuple[str, float]]:
    """
    :param tokens: a list of tokens.
    :param args: a variable number of arguments
    :return: a list of tuple where each tuple represents a pair of (POS, score) of the corresponding token.
    """
    # TODO: to be updated
    return [('XX', 0) for _ in range(len(tokens))]


def experiment(trn_data: List[List[Tuple[str, str]]], dev_data: List[List[Tuple[str, str]]]):
    model = train(trn_data)
    total, correct = 0, 0
    for sentence in dev_data:
        tokens, gold = tuple(zip(*sentence))
        pred = [t[0] for t in predict(tokens, *model)]
        total += len(tokens)
        correct += len([1 for g, p in zip(gold, pred) if g == p])
    print('{:5.2f}% ({}/{})'.format(100.0 * correct / total, correct, total))


if __name__ == '__main__':
    path = 'cs329/dat/pos/'
    trn_data = read_data(path + 'wsj-pos.trn.gold.tsv')
    dev_data = read_data(path + 'wsj-pos.dev.gold.tsv')
    experiment(trn_data, dev_data)
