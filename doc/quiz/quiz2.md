# Quiz 2: Ontology and Taxonomy

## Tasks

* Create a python file called [`quiz2.py`](../../src/quiz/quiz2.py) under the [`quiz`](../../src/quiz/) package and copy the code.
* Complete the `antonyms()` method that takes a sense ID, and returns a set of `Synset` representing the union of all antonyms of the sense as well as its synonyms.
  ```
  antonyms('purchase.v.01')
  -> {wn.Synset('sell.v.01')}
   ```
* Complete the `paths()` method that takes two distinct sense IDs and returns a list of `Synset` list where each `Synset` list shows the path from the first sense to the second sense with respect to the corresponding lowest common hypernym:
  ```
  path('dog.n.01', 'cat.n.01')
  -> [
       [wn.synset('dog.n.01'), wn.synset('canine.n.01'), wn.synset('carnivore.n.01'), wn.synset('feline.n.01'), wn.synset('cat.n.01')]
     ]
  ```
* Your functions will be evaluated with a more thorough set of examples.

## Notes

* The `antonyms()` function returns an empty set if no antonym is found.

## Submission

* Commit and push `quiz2.py` to your GitHub repository.
* Check if `quiz2.py` is placed under the `quiz` directory in your repository.