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
import json
from typing import Dict


def cosine(x1: Dict[str, float], x21: Dict[str, float]) -> float:
    # TODO: to be updated
    return 0


def normalize_extra(text):
    # TODO: to be updated
    return text


if __name__ == '__main__':
    fables = json.load(open('res/aesopfables.json'))
    fables_alt = json.load(open('res/aesopfables.json'))
