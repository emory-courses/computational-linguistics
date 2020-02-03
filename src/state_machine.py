from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum

################################
# Modify State enum for any Quiz2 tasks as needed
################################

class State(Enum):
    START = 0
    PROMPT = 1
    MAMMAL = 2
    BIRD = 3
    ERR = 4

################################

################################
# Modify ont_dict for Quiz2 Task 3
################################

ont_dict = {
              "ontology": {

              }
           }

################################

knowledge = KnowledgeBase()
knowledge.load_json(ont_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Enter an animal"')
df.add_user_transition(State.PROMPT, State.MAMMAL, "$animal={cat,dog}")
df.add_user_transition(State.PROMPT, State.BIRD, "$animal={parrot,dove,crow}")
df.add_system_transition(State.MAMMAL, State.PROMPT, '[! $animal " is a mammal, enter another animal"]')
df.add_system_transition(State.BIRD, State.PROMPT, '[! $animal "is a bird, enter another animal"]')
df.add_system_transition(State.ERR, State.PROMPT, '"i dont know that one, enter another animal"')
df.set_error_successor(State.PROMPT, State.ERR)


################################
# Add Quiz2 Task 1 below
################################



################################
# Add Quiz2 Task 2 below
################################



################################
# Add Quiz2 Task 3 below
# (except do not move ont_dict from line 11)
################################



df.run(debugging=False)