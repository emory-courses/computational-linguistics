from emora_stdm import DialogueFlow
from enum import Enum, auto

####################################################################################
# Demonstrates how to use the NER and POS macros in Natex Expressions.
#
# You MUST be using v1.29 of emora_stdm.
# To upgrade to latest version:
#     pip install --upgrade emora_stdm
#
# If that doesn't work, try
#     pip uninstall emora_stdm
#     pip install emora_stdm==1.29
#
# You use these macros similar to the ONT macro, except you do
# not need to build the dictionary of information.
#
# ----------
# NER
# ----------
# The NER macro uses the SpaCy package to identify named
# entities in a piece of text. Named entities are things like
# people, companies, locations, and so on.
#
# A list of possible categories of named entities that can be recognized
# can be found at https://spacy.io/api/annotation#named-entities
#
# ----------
# POS
# ----------
# The POS macro uses the SpaCy package to identify words
# in a piece of text based on its part of speech (noun, verb, adjective, etc.)
#
# A list of possible types of parts of speech that can be recognized can
# be found at https://spacy.io/api/annotation#pos-universal
#
# ----------
# Sample Conversation:
# ----------
#     S: Who is your favorite celebrity?
#     U: Loading wordnet.json...  done in 6.014761924743652schris evans
#     S: I really like chris evans too! Where do you think they live?
#     U: hawaii
#     S: I seem to not know that location. What activities do you think they like to do?
#     U: reading
#     S: Ok,  reading , interesting. How would you describe that activity or your opinion on it?
#     U: it is fun
#     S: Yeah for sure. It is  fun . So, what other celebrity do you like?
#     U: miley cyrus
#     S: I really like miley cyrus too! Where do you think they live?
#     U: hollywood
#     S: Yes, their home is likely to be hollywood . What activities do you think they like to do?
#     U: running or walking on the beach
#     S: Ok,  running , interesting. How would you describe that activity or your opinion on it?
#     U: it is difficult
#     S: Yeah for sure. It is  difficult . So, what other celebrity do you like?

####################################################################################

class State(Enum):
    START = auto()
    ASK_CELEB = auto()
    REC_CELEB_ANS = auto()
    COMMENT_CELEB = auto()
    UNKNOWN_CELEB = auto()
    UNKNOWN_LOC = auto()
    CELEB_LOCATION = auto()
    ACK = auto()
    ACT = auto()
    REC_ACT= auto()
    UNKNOWN_ACT= auto()
    DESC= auto()
    REC_DESC= auto()
    UNKNOWN_DESC= auto()

df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM)

df.add_system_transition(State.START, State.ASK_CELEB, '"Who is your favorite celebrity?"')

# NER to find people names that are mentioned
df.add_user_transition(State.ASK_CELEB, State.REC_CELEB_ANS, '[$fave_celeb=#NER(person)]')

df.set_error_successor(State.ASK_CELEB, State.UNKNOWN_CELEB)

df.add_system_transition(State.REC_CELEB_ANS, State.CELEB_LOCATION, '[!"I really like" $fave_celeb "too! Where do you think they live?"]')

df.add_system_transition(State.UNKNOWN_CELEB, State.CELEB_LOCATION, '"Hmm... I do not know them. Where do you think they live?"')

# NER to find locations that are mentioned
df.add_user_transition(State.CELEB_LOCATION, State.ACK, '[$loc=#NER(gpe)]')

df.set_error_successor(State.CELEB_LOCATION, State.UNKNOWN_LOC)

df.add_system_transition(State.ACK, State.ACT, '[!"Yes, their home is likely to be" $loc ". What activities do you think they like to do?"]')

df.add_system_transition(State.UNKNOWN_LOC, State.ACT, '"I seem to not know that location. What activities do you think they like to do?"')

# POS to find nouns or verbs
df.add_user_transition(State.ACT, State.REC_ACT, '[$activity=#POS(noun,verb)]')

df.set_error_successor(State.ACT, State.UNKNOWN_ACT)

df.add_system_transition(State.REC_ACT, State.DESC, '[!"Ok, " $activity ", interesting. How would you describe that activity or your opinion on it?"]')

df.add_system_transition(State.UNKNOWN_ACT, State.DESC, '"I have never done that activity before. How would you describe that activity or your opinion on it?"')

# POS to find adjectives
df.add_user_transition(State.DESC, State.REC_DESC, '[$description=#POS(adj)]')

df.set_error_successor(State.DESC, State.UNKNOWN_DESC)

df.add_system_transition(State.REC_DESC, State.ASK_CELEB, '[!"Yeah for sure. It is " $description ". So, what other celebrity do you like?"]')

df.add_system_transition(State.UNKNOWN_DESC, State.ASK_CELEB, '"You have very interesting ideas about that. So, what other celebrity do you like?"')

if __name__ == "__main__":
    df.run(debugging=False)