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
from typing import Dict, Any, List

from src.vector_space_models import tf_idfs, most_similar


def cosine(x1: Dict[str, float], x21: Dict[str, float]) -> float:
    # TODO: to be updated
    return 0


def vectorize(documents: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
    # Feel free to update this function
    return tf_idfs(documents)


def similar_documents(X: Dict[str, Dict[str, float]], Y: Dict[str, Dict[str, float]]) -> Dict[str, str]:
    # Feel free to update this function
    return {k: most_similar(Y, x) for k, x in X.items()}


if __name__ == '__main__':
    fables = json.load(open('res/vsm/aesopfables.json'))
    fables_alt = json.load(open('res/vsm/aesopfables-alt.json'))

    v_fables = vectorize(fables)
    v_fables_alt = vectorize(fables_alt)

    for x, y in similar_documents(v_fables_alt, v_fables).items():
        print('{} -> {}'.format(x, y))
