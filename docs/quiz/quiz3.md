# Quiz 3: Part-of-Speech Tagging

## Tasks

Your task is to develop an accurate part-of-speech tagging model:

* Create a python file called [`quiz3.py`](../../src/quiz/quiz3.py) under the [`quiz`](../../src/quiz/) package and copy the code.
* Complete the `train()` method that takes training and the development sets and returns the best set of arguments necessary to run your model.
* Complete the `predict()` method that takes a list of tokens and the arguments from `train()` and returns corresponding predicted part-of-speech tags.
* Generate the `quiz3.pkl` file under the `quiz` package that saves your best set of arguments.
* Write a report describing how you improve the model accuracy and saves it as `quiz3.pdf`.

## Notes

* Feel free to use any code provided by this course.
* Use backoff and/or interpolation to estimate the final scores from multiple probability distributions.
* The weights for probabilities can be any floats including negative values.
* The baseline approach that uses all 4 dictionaries from the course is already provided: : [`quiz3_base.py`](../../src/quiz/quiz3_base.py).   
* Your job is to develop a model that performs more accurately than the baseline model. You may want to consider more advanced probabilities such as (not limited to):
  * P(p<sub>i</sub>|w<sub>i</sub>, w<sub>i-1</sub>)
  * P(p<sub>i</sub>|w<sub>i</sub>, w<sub>i+1</sub>)
  * P(p<sub>i</sub>|w<sub>i</sub>, p<sub>i-1</sub>)
* Your model will be evaluated on an evaluation set that is not provided to you.

## Submission

* Commit and push `quiz3.py` and `quiz3.pkl` to your GitHub repository.
* Submit `quiz3.pdf` to: https://canvas.emory.edu/courses/83264/assignments/461923
