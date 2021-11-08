# Getting Started

## Python

* Install [Python 3.10.x](https://www.python.org/downloads/).
* Lower versions of Python may not be compatible to this course.

## Git Repository

* Login to [Github](https://github.com) (create an account if you do not have one). 
* Create a new repository called `cs329` and make it **private**.
* From the `[Settings]` menu, add the instructors as collaborators of this repository.
  * Jinho Choi: `jdchoi77`

## PyCharm

* Install [PyCharm](https://www.jetbrains.com/pycharm/download/) on your local machine.
  * The following instructions assume that you have "PyCharm 2021.3.x Professional Edition".
  * You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Add your Github account:
  * Go to `[Preferences] - [Version Control] - [Github]`.
  * Click the `+` button to log in via Github.
  * If you are using two-factor authentication, click `[Use Token]` and login with your [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).
* Create a new project:
  * Click the `[Get from VCS]` button on the `Welcome` prompt.
  * Choose `[GitHub]` on the left menu, select the `cs329` repository, and click the `[Clone]` button.  Make sure the directory name is `cs329`.
* Setup the interpreter:
  * Go to `[Preferences] - [Project: cs329] - [Project Interpreter]`.
  * Click the gear button on the righthand side and select `Add`.
  * In the prompted window, choose `[Virtualenv Environment]` on the left menu and select `Python 3.9.x` as the base interpreter.
* Install a package:
  * Go to `[Preferences] - [Project: cs329] - [Project Interpreter]`.
  * Click the `+` button at the bottom.
  * Search and install for the `numpy` package.
* Create a new package:
  * At any step, if it prompts you to add a new file/package to git, click `Add`.
  * Create a python package called [`src/quiz/`](../src/quiz/).
  * Create a python file called [`quiz0.py`](../src/quiz/quiz0.py) under the `quiz` package and copy the code.
    ```python
    import numpy as np

    a = np.array([1,2,3])
    b = np.array([4,5,6])
    print((a + b) * 2)
    ```
  * Run `quiz0` by clicking `[Run] - [Run]`.
  * If it prompts `[10 14 18]`, your program runs successfully.

## Jupyter Notebook

* Open a terminal in PyCharm.
* Install [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html) by entering the following command (this is another way of installing a package):
  ```
  pip install jupyter
  ```
* Enter the following command to launch Jupyter Notebook:
  ```
  (venv) $ jupyter notebook
  ```
* On the web-browser where it is launched, choose the [`src/quiz/`](../src/quiz/) directory.
* Create a new notebook called [`quiz0.ipynb`](../src/quiz/quiz0.ipynb) and run the code in [`quiz0.py`](../src/quiz/quiz0.py).
* If it prompts `[10 14 18]`, your notebook runs successfully.
