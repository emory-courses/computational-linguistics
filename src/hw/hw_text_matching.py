from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum


# TODO: Update the State enum as needed
class State(Enum):
    START = 0
    PROMPT = 1
    ERR = 2


# TODO: create the ontology as needed
ontology = {
    "ontology": {

        }
}


knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Hi, what do you want to talk about?"')
df.set_error_successor(State.PROMPT, State.ERR)
# TODO: create your own dialogue manager


df.run(debugging=False)