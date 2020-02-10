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
from typing import Set, Optional, List

from nltk.corpus.reader import Synset


def antonyms(word: str, pos: Optional[str] = None) -> Set[str]:
    # TODO: to be filled
    pass


def lch_paths(word_0: str, word_1: str) -> List[List[Synset]]:
    # TODO: to be filled
    pass


if __name__ == '__main__':
    print(antonyms('buy', pos='v'))
    for path in lch_paths('dog', 'cat'):
        print(path)
