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

FM = {
    'antgrass2.ram': 'TheAntsandtheGrasshopper',
    'TheAssandhisPurchaser2': 'TheAssandHisPurchaser',
    'TheAssandtheLapdog2': 'TheAssandtheLapdog',
    'TheAssintheLionSkin': 'TheAssintheLionsSkin',
    'TheBellyandtheMembers2': 'TheBellyandtheMembers',
    'TheBuffoonandtheCountryman': 'TheBuffoonandtheCountryman2',
    'TheCrowandthePitcher2': 'crowpitc2.ram',
    'TheDogintheManger2': 'TheDogintheManger',
    'TheDogandtheShadow2': 'TheDogandtheShadow',
    'TheEagleandtheArrow2': 'TheEagleandtheArrow',
    'TheFoxandtheCrow2': 'TheFoxandtheCrow',
    'TheFoxandtheGoat2': 'TheFoxandtheGoat',
    'TheFoxandtheGrapes2': 'TheFoxandtheGrapes',
    'TheFoxandtheLion': 'TheFoxandtheLion2',
    'TheFoxandtheMask': 'foxmask2.ram',
    'haretort2.ram': 'TheHareandtheTortoise',
    'harefrog2.ram': 'TheHaresandtheFrogs',
    'TheHorseandtheAss2': 'TheHorseandtheAss',
    'TheLionandtheMouse2': 'lionmouse',
    'TheLioninLove2': 'TheLioninLove',
    'TheManandtheSatyr2': 'TheManandtheSatyr',
    'MercuryandtheWoodman': 'MercuryandtheWorkmen',
    'milkpail2.ram': 'milkmaidjug.jpg',
    'TheOldManandDeath2': 'TheOldManandDeath',
    'TheOldWomanandtheWine-Jar': 'womanjar2.ram',
    'TheOne-EyedDoe': 'TheOneEyedDoe',
    'ThePeacockandJuno': 'ThePeacockandJuno2',
    'TheRoseandtheAmaranth': 'TheRoseandtheAmaranth2',
    'TheSerpentandtheEagle': 'TheSerpentandtheEagle2',
    'shepherd2.ram': 'shepwolf2.ram',
    'TheSickLion2': 'TheSickLion',
    'TheTownMouseandtheCountryMouse': 'TheTownMouseandtheCountryMouse2',
    'TheTrumpeterTakenPrisoner2': 'TheTrumpeterTakenPrisoner',
    'TheTwoPots2': 'twopots2.ram',
    'TheVainJackdaw': 'TheVainJackdaw2',
    'TheWolfandtheCrane2': 'TheWolfandtheCrane',
    'TheWolfandtheLamb2': 'TheWolfandtheLamb',
    'TheWolfinSheepsClothing2': 'TheWolfinSheepsClothing'
}


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
