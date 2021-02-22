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


def antonyms(word: str, pos: Optional[str] = None) -> Set[Synset]:
    # TODO: to be updated
    pass


def path(sense_0: str, sense_1: str) -> List[Synset]:
    # TODO: to be updated
    pass


if __name__ == '__main__':
    print(antonyms('purchase', pos='v'))
    print([s.name() for s in path('dog.n.01', 'cat.n.01')])
