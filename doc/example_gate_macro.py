from emora_stdm import DialogueFlow, NatexNLU, NatexNLG, Macro, KnowledgeBase
import os

kb_dict= {
    "ontology": {
        "person": ["male", "female", "friend"],
        "female": ["wife", "daughter", "sister", "aunt", "grandmother", "niece", "girlfriend", "mother"],
        "male": ["husband", "son", "brother", "uncle", "grandfather", "nephew", "boyfriend", "father"],
        "related_person": ["partner", "roommate", "sibling", "friend", "child", "parent", "relative"],
        "partner": ["spouse", "romantic_partner", "boyfriend", "girlfriend"],
        "spouse": ["husband", "wife"],
        "parent": ["mother", "father"],
        "family": ["parent", "uncle", "aunt", "cousin", "niece", "nephew", "grandparent", "child"],
        "child": ["son", "daughter"],
        "sibling": ["brother", "sister"],
        "relative": ["aunt", "uncle", "grandfather", "grandmother", "niece", "nephew", "cousin"]
    },
    "expressions": {
        "negation": ["no", "not", "don't", "dont", "won't", "wont", "shouldn't", "shouldnt",
                     "can't", "cant", "isn't", "isnt"],
        "positive_sentiment": ["good", "great", "fantastic", "lovely", "awesome", "wonderful", "spectacular",
                                "superb", "excellent", "nice", "sweet", "cute", "adorable", "fun", "perfect",
                                "super"],
        "negative_sentiment": ["bad", "stupid", "horrible", "awful", "dumb", "sad", "terrible"],

        "someone": ["someone", "somebody", "some body", "some one"],
        "anyone":  ["any one", "anyone", "any body", "anybody"],

        "boyfriend": ["boyfriend","boy friend"],
        "girlfriend": ["girlfriend","girl friend"],
        "romantic_partner": ["lover", "significant other"],
        "roommate": ["roommate","roomate","room mate"],
        "mother": ["mother", "mom", "ma", "mama", "mommy"],
        "father": ["father", "dad", "pa", "papa", "daddy"],
        "child": ["kid", "kiddo", "offspring", "child"],
        "son": ["son","boy"],
        "daughter": ["daughter","girl"],
        "grandfather": ["grandpa"],
        "grandmother": ["grandma"],

        "smart": ["smart","intelligent", "bright", "capable", "sharp"],
        "funny": ["funny","humorous", "clever", "witty", "hilarious", "joker", "jokester"],
        "outgoing": ["outgoing", "extraverted", "sociable", "social", "friendly", "warm"],
        "shy": ["shy", "intraverted", "guarded", "loner"],
        "polite": ["polite", "manners", "decent"],
        "conceited": ["conceited", "overconfident", "arrogant", "full of", "narcissistic", "egotistic", "egotistical", "selfish"],
        "beautiful": ["gorgeous", "pretty", "hot", "sexy"]
      }
}

kb = KnowledgeBase()
kb.load_json(kb_dict)
df = DialogueFlow(initial_state="root", kb=kb)

root = 'root'
end = 'end'
df.add_state(root, error_successor=root, memory=0)
df.add_state(end, error_successor=end)
df.add_system_transition(root, end, 'I have no nonrepetitive options', score=0)

# S: Who do you live with?
root = 'root'
df.add_state('opening live with', error_successor=root)
df.add_system_transition(root, 'opening live with', '[!#GATE() "So, who do you live with?"]')

df.add_user_transition('opening live with', root, '[!#NOT(#EXP(negation)) [{$related_type={#ONT(person),#EXP(roommate),family},people, someone, anyone, guys, girls}]]')

df.add_user_transition('opening live with', 'live alone', '{[no one], [alone], [none], [myself], [#EXP(negation), {#EXP(roommate), people, someone, anyone}]}')
df.add_state('live alone response', error_successor=root)
df.add_system_transition('live alone', 'live alone response', '"Sometimes it is nice to live by yourself."')

# S: Who are you close to?
root = 'root'
df.add_state('opening close to', system_multi_hop=True)
df.add_system_transition('opening close to', root, '')
df.add_system_transition(root, 'opening close to', '[!#GATE() "So tell me, who are you closest to in your life?"]')

# U: my $related_type
root = 'root'
df.add_state('related', root, user_multi_hop=True)
df.add_user_transition(root, 'related', '[my $related_type=#ONTE(related_person)]', score=0.5)

# S: What is $related_type like?
root = 'root'
df.add_state('personality', error_successor='default personality', user_multi_hop=True)
df.add_system_transition(root, 'personality', '[!#GATE(related_type:mother) "So, what is your" $related_type "like?"]')

df.add_system_transition('default personality', root, '"It sounds like your" $related_type "is even more interesting than you\'re letting on"')

df.add_system_transition(end, end, "I have no nonrepetitive options.")

if __name__ == '__main__':
    df.run(debugging=False)
