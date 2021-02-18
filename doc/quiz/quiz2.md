# Quiz 2: Ontology and Taxonomy

## Task

* Create a python file called [`quiz2.py`](../../src/quiz/quiz2.py) under the [`quiz`](../../src/quiz/) package and copy the code.
* 

Modify each of the user transitions from `State.PROMPT` (including any you added for Tasks 1 and 2) such that the transition matches as long as the user says at least one of the specified words.

In other words, if the user says more than just the specified words, the transition should still match. (This isn't currently true, test and see for yourself!)

Here is an example:
```
(System) Enter an animal:
(User) what about frog
(System) frog is a reptile, enter another animal: 
(User) hmm cat i guess
(System) cat is a mammal, enter another animal:
(User) a parrot
(System) parrot is a bird, enter another animal:
...
``` 