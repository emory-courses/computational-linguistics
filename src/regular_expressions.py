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
import re

RE_TOK = re.compile(r'([",.]|n\'t|\s+)')
RE_ABBR = re.compile(r'((?:Mr|Mrs|Ms|Dr)\.)|((?:[A-Z]\.){2,})')  # Mr. Dr. Mrs. U.S.A. USA.
RE_APOS = re.compile(r'\'(\d\ds?|cause)')
RE_CONC = re.compile(r'([A-Za-z]+)(n\'t)|(gon)(na)|(can)(not)')
RE_HYPE = re.compile(r'(https?:\/\/\S+)')
RE_NUMB = re.compile(r'(\d+\/\d+)|(\d{3}-\d{3}-\d{4})|(\d(?:,\d{3})+)')
RE_UNIT = re.compile(r'([$#])?(\d+)([km]g)?')


def tokenize_regex(text):
    prev_idx = 0
    tokens = []
    for m in RE_TOK.finditer(text):
        t = text[prev_idx:m.start()].strip()
        if t: tokens.append(t)
        t = m.group().strip()
        if t:
            if tokens and tokens[-1] in {'Mr', 'Ms'} and t == '.':
                tokens[-1] = tokens[-1] + t
            else:
                tokens.append(t)
        prev_idx = m.end()

    t = text[prev_idx:].strip()
    if t: tokens.append(t)
    return tokens


if __name__ == '__main__':
    text0 = 'Mr. Wayne isn\'t the hero we need, but "the one" we deserve.'
    text1 = 'Ms. Wayne is "Batgirl" but not "the one".'

    print(tokenize_regex(text0))
    print(tokenize_regex(text1))
