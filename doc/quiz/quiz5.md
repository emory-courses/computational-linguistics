# Quiz 5: Named Entity Recognition

## Tasks

Your task is to develop a named entity recognizer using gazetteers:

* Create a python file called [`quiz5.py`](../../src/quiz/quiz5.py) under the [`quiz`](../../src/quiz/) package and copy the code.
* Complete the `remove_overlaps()` method that takes a list of entities and returns another list of entities where there is no overlap between any entities.
  * Your function should remove the minimum number of entities. For example, if the gazetteer includes the following country names, `South Korea`, `Korea United`, `United States`, for the input text `South Korea United States`, it should return two entities, `South Korea` and `United States`, not `Korea United`.  
  * Your function should retain a longer entity over a short one when they overlap. For example, if the gazetter includes, `Atlantic City` and `City of Georgia`, for the input text `Atlantic City of Georgia`, it should return `City of Georgia` that consists of 3 tokens, not `Atlantic City` comprising 2 tokens. 
* Complete the 


## Submission

* Commit and push `quiz4.py`to your GitHub repository.
