# Quizzes

## Quiz 1

### Regular Expressions

* Create [`regular_expressions.py`](../src/regular_expressions.py) under the [`src/`](../src) directory and copy the contents.
* Complete the `turn_1b()` method such that it prompts to ask the kind of user's smartphone if it is not provided during `Turn 0`.
Once the information is retrieved, it should continue to `turn_1a()` as follows: 
  ```
  S: are you using a smartphone?
  U: yes
  S: what kind of smartphone do you have?
  U: samsung galaxy
  S: how long have you been using galaxy?
  ...
  ``` 
* Complete the `turn_3a()` method such that it properly estimates how old user's iPhone is given any version provided by the user.
Hint: use `res.d_iphone_v` defined in the main space.

### Submission

* Commit and push `src/regular_expression.py` to your GitHub repository.
* Submit `regular_expression.py` to https://canvas.emory.edu/courses/71182/assignments/294356


## Quiz 2

### Dialogue Management

reate [`state_machine.py`](../src/state_machine.py) under the [`src/`](../src) directory and copy the contents from the class source.

#### Task 1 

Set up the appropriate transitions such that the DialogueFlow can recognize `snake`, `lizard`, `turtle`, and `alligator` as `reptile`,
similar to how it recognizes `mammal` and `bird` already.
```
(System) Enter an animal:
(User) snake
(System) snake is a reptile, enter another animal: 
...
```

#### Task 2 

Set up the appropriate transitions using an ONTOLOGY reference such that the DialogueFlow can recognize `frog` and `salamander` as `amphibian`.

You must fill in the `ont_dict` variable with the `amphibian` ontology and use this ontology in the Natex expression you create for this case.
```
(System) Enter an animal:
(User) frog
(System) frog is an amphibian, enter another animal: 
...
```   

#### Task 3 

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

### Submission

* Commit and push `src/state_machine.py` to your GitHub repository.
* Submit `state_machine.py` to https://canvas.emory.edu/courses/71182/assignments/294365


## Quiz 3

### Ontology and Taxanomy

* Create [`quiz3.py`](../src/quiz/quiz3.py) under the [`src/quiz/`](../src/quiz) directory and copy the contents.
* Complete the `antonyms()` method that takes a word and an optional POS tag, and returns the list of antonyms of the word.
* Complete the `lch_paths()` method that takes two words (not sense IDs), and returns the list of Synset list where each Synset list shows the path from every lowest common hypernym of the two words to its root.


### Submission

* Commit and push `src/quiz/quiz3.py` to your GitHub repository.
* Submit `quiz3.py` to https://canvas.emory.edu/courses/71182/assignments/294364


## Quiz 4

### Letter of Intent

Create a PDF file called `loi.pdf` and write the following three contents:

* The title of your project.
* The name, discipline, and email address of each team member.
* An abstract describing your project in 400 words.

### Submission

* Submit `loi.pdf` to https://canvas.emory.edu/courses/71182/assignments/294160
* Only one submission is required per team.


## Quiz 5

### Structure Parsing

* Answer the three questions in [quiz_phrase_structures.pdf](quiz_phrase_structures.pdf).

### Submission

* Create a PDF file `quiz5.pdf` and include your answers.
* Submit `quiz5.pdf` to https://canvas.emory.edu/courses/71182/assignments/294369


## Quiz 6

### Proposal Ranking

* Select three proposals other than yours that you find most interesting. Proposals must be indicated by the project IDs and the titles.
* Give a brief explanation of why you choose those proposals.
* The explanation should be 50 - 100 words per proposal.

### Submission

* Submit your explanations to https://canvas.emory.edu/courses/71182/assignments/294380


## Quiz 7

### Vector Space Models

* TBA

### Submission

* https://canvas.emory.edu/courses/71182/assignments/294379


## Quiz 8

### Machine Learning

* TBA

### Submission

* https://canvas.emory.edu/courses/71182/assignments/294441


## Quiz 9

### Language Modeling

* TBA

### Submission

* https://canvas.emory.edu/courses/71182/assignments/294442


## Quiz 10

### Project Ranking

* Select three projects other than yours that you find most interesting. Projects must be indicated by the titles.
* Give a brief explanation of why you choose those projects.
* The explanation should be 50 - 100 words per project.

### Submission

* Submit your explanations to https://canvas.emory.edu/courses/71182/assignments/294380
