from enum import Enum, auto
from types import SimpleNamespace
from typing import Union, List, Set, Dict, Tuple

class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class Oridinal(AutoName):
    NORTH = auto()
    SOUTH = auto()







def add_state(states: Dict[int, SimpleNamespace], sid: int, nlu: Union[None, str, List[str]], nlg: Union[None, Set[str]]) -> SimpleNamespace:
    """
    :param states:
    :param sid:
    :param nlu:
    :param nlg:
    :return:
    """
    state = SimpleNamespace(sid=sid, nlu=nlu, nlg=nlg)
    states[sid] = state
    return state




def dialogue_smartphone() -> Tuple[Dict[int, SimpleNamespace], Dict[int, Set[int]]]:
    states: Dict[int, SimpleNamespace] = dict()
    transitions: Dict[int, Set[int]] = dict()

    sid = 0
    add_state(states, sid, None, {'Many of my friends are thinking to change their phones. Are you using a smartphone?'})
    sid += 1
    add_state(states, sid,
              '')




    return states, transitions



def fill(s: str) -> str:
    """

    :param s:
    :return:
    """

if __name__ == '__main__':
    # states, transition = dialogue_smartphone()
    print(list(Oridinal))

