# Quiz 2: Ontology and Taxonomy

## Tasks

* Create a python file called [`quiz2.py`](../../src/quiz/quiz2.py) under the [`quiz`](../../src/quiz/) package and copy the code.
* Complete the `antonyms()` method that takes a sense ID, and returns a set of `Synset` representing the union of all antonyms of the sense as well as its synonyms.
  ```
  antonyms('purchase.v.01')
  -> {Synset('sell.v.01')}
  
  antonym('end.v.02')
  -> {Synset('begin.v.03'), Synset('get_down.v.07')}

  print(antonyms('nonspecific.a.01'))
  -> {Synset('specific.a.01'), Synset('specific.a.04')}
   ```
* Complete the `paths()` method that takes two distinct sense IDs and returns a list of `Synset` list where each `Synset` list shows the path from the first sense to the second sense with respect to the corresponding lowest common hypernym:
  ```
  paths('dog.n.01', 'cat.n.01')
  -> [
       [Synset('dog.n.01'), Synset('canine.n.02'), Synset('carnivore.n.01'), Synset('feline.n.01'), Synset('cat.n.01')]
     ]
  
  paths('body.n.09', 'sidereal_day.n.01')
  -> [
       [Synset('body.n.09'), Synset('mass.n.01'), Synset('physical_property.n.01'), Synset('property.n.02'), Synset('attribute.n.02'), Synset('time.n.05'), Synset('cosmic_time.n.01'), Synset('sidereal_time.n.01'), Synset('sidereal_day.n.01')],
       [Synset('body.n.09'), Synset('mass.n.01'), Synset('fundamental_quantity.n.01'), Synset('measure.n.02'), Synset('time_unit.n.01'), Synset('sidereal_day.n.01')]
     ]

  paths('boy.n.01', 'girl.n.01')
  -> [
       [Synset('male_child.n.01'), Synset('male.n.02'), Synset('person.n.01'), Synset('adult.n.01'), Synset('woman.n.01'), Synset('girl.n.01')]
       [Synset('male_child.n.01'), Synset('male.n.02'), Synset('person.n.01'), Synset('female.n.02'), Synset('woman.n.01'), Synset('girl.n.01')]
     ]
  ```
* Your functions will be evaluated with a more thorough set of examples.

## Notes

* The `antonyms()` function returns an empty set if no antonym is found.
* For the `path()` function:
  * For `dog.n.01` and `cat.n.01`, although `dog.n.01` has two hypernym paths, there is only one lowest common hypernym between the two senses, `carnivore.n.01`, such that the returned list should include only one inner-list. 
  * For `body.n.09` and `sidereal_day.n.01`, there are two lowest common hypernyms, `attribute.n.02` and `measure.n.02`, and only one path exist from each sense to every LCH such that the returned list should contain two inner lists.
  * For `boy.n.01` and `girl.n.01`, there are two hypernym paths of `boy.n.01`:
    ```
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('causal_agent.n.01'), Synset('person.n.01'), Synset('male.n.02'), Synset('male_child.n.01')]
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('object.n.01'), Synset('whole.n.02'), Synset('living_thing.n.01'), Synset('organism.n.01'), Synset('person.n.01'), Synset('male.n.02'), Synset('male_child.n.01')]
    ```
    , four hypernym paths of `girl.n.01`:
    ```
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('causal_agent.n.01'), Synset('person.n.01'), Synset('adult.n.01'), Synset('woman.n.01'), Synset('girl.n.01')]
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('object.n.01'), Synset('whole.n.02'), Synset('living_thing.n.01'), Synset('organism.n.01'), Synset('person.n.01'), Synset('adult.n.01'), Synset('woman.n.01'), Synset('girl.n.01')]
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('causal_agent.n.01'), Synset('person.n.01'), Synset('female.n.02'), Synset('woman.n.01'), Synset('girl.n.01')]
    [Synset('entity.n.01'), Synset('physical_entity.n.01'), Synset('object.n.01'), Synset('whole.n.02'), Synset('living_thing.n.01'), Synset('organism.n.01'), Synset('person.n.01'), Synset('female.n.02'), Synset('woman.n.01'), Synset('girl.n.01')]
    ```
    , and one lowest common hypernym, `Synset('person.n.01')`. Once you truncate all paths by the LCS, only one path gets retained for `boy.n.01`:
    ```
    [Synset('person.n.01'), Synset('male.n.02'), Synset('male_child.n.01')]
    ```
    and two paths get retained for `girl.n.01`:
    ```
    [Synset('person.n.01'), Synset('adult.n.01'), Synset('woman.n.01'), Synset('girl.n.01')]
    [Synset('person.n.01'), Synset('female.n.02'), Synset('woman.n.01'), Synset('girl.n.01')]
    ```
    Thus, the returned list should include two inner lists. 

## Submission

* Commit and push `quiz2.py` to your GitHub repository.
* Check if `quiz2.py` is placed under the `quiz` directory in your repository.