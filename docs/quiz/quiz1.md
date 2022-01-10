# Quiz 1: String Matching

## Task

* Create a python file called [`quiz1.py`](../../src/quiz/quiz1.py) under the [`quiz`](../../src/quiz/) package and copy the code.
* Update the `normalize()` function such that it takes a string and returns a string where all cardinals are normalized into digitals:
  * I met **twelve** people &rarr; I met **12** people
  * I have **one** brother and **two** sisters &rarr; I have **1** brother and **2** sisters
  * A year has **three hundred sixty five** days &rarr; A year has **365** days
  * I made **a million** dollars &rarr; I made **1000000** dollars
* Run `quiz1.py` to see if your function returns correct output.
* Your function will be evaluated with a more thorough set of examples.

## Notes

* Your program should handle:
  * Both uppercase and lowercase letters.
  * Hyphenated words (e.g., `thirty-five` &rarr; `35`).
  * Preceding and succeeding symbols (e.g., `one, "two", three!?` &rarr; `1, "2", 3!?`).
* Your program should not convert:
  * Indefinite articles except for the case when they are followed by numbers such as `hundred`, `thousand`, etc.
  * Ordinals (e.g., `first`, `fifth`).
  * Decimals (e.g., `five point two`).
  * Fractions (e.g., `a half`, `two third`).
* Other than the converted cardinals, all the other parts of the string should stay as the original forms including consecutive spaces and symbols.
* The converted cardinals should not include comma. For example, `one thousand one` should be converted to `1001`, not `1,001`.
* More conversion examples:
  * `Three hundred` and `Sixty Five` &rarr; `300` and `65`
  * `Twenty three hundred` &rarr; `2300`


## Submission

* Commit and push `quiz1.py` to your GitHub repository.
* Check if `quiz1.py` is placed under the `quiz` directory in your repository.

## Extra Credit

* Update `normalize_extra()` to handle the case of indefinite articles (e.g., `a`, `an`) being used to indicate quantities.
In the example below, `a boy` should not be converted into `1 boy` whereas `a sister` should because it indicates the quantity:
  * I know a boy who has **a** sister &rarr; I know a boy who has **1** sister
* The `normalize_extra()` function should convert only indefinite articles, nothing else.
* Write a report `quiz1.pdf` that explains how you handle this special case and submit: https://canvas.emory.edu/courses/96729/assignments/554949
* Give out a (linguistically) sounding explanation rather than a list out examples. For instance, instead of stating that your program converts all indefinite articles preceding a certain list of words, explain what types (or categories) of words following indefinite articles are considered.
