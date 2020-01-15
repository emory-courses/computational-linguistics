# Getting Started

## Python

* Install [Python 3.6.x](https://www.python.org/downloads/) or above (the current version is `3.8.x`).
* Note that lower versions of Python will not be compatible to this course.


## Git Repository

* Login to [Github](https://github.com) (create an account if you do not have one). 
* Create a new repository called `cs329` and make it PRIVATE.
* From the `[Settings]` menu, add the TAs as collaborators of this repository.
  * Sarah Fillwock: `sfillwo`.
  * Liyan Xu: `lxucs`.


## PyCharm

* Install [PyCharm](https://www.jetbrains.com/pycharm/download/) on your local machine.
  * The following instructions assume that you have "PyCharm 2019.3 Professional Edition".
  * You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Add your Github account:
  * Go to `[Preferences] - [Version Control] - [Github]`.
  * Click the `+` button, and enter your Github ID and password.
  * If you are using two-factor authentication, click `[Use Token]` and login with your [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).
* Create a new project:
  * Click `[Get from Version Control]` and choose `[GitHub]` on the left menu.
  * Select the `cs329` repository and clone it.  Make sure the directory name is `cs329`.
* Setup the interpreter:
  * Go to `[Preferences] - [Project: cs329] - [Project Interpreter]`.
  * Click the gear button on the righthand side and select `Add`.
  * In the prompted window, select `[Virtualenv Environment]` and choose `Python 3.6.x` as the base interpreter.
* Install a package:
  * Go to `[Preferences] - [Project: cs329] - [Project Interpreter]`.
  * Click the `+` button at the bottom.
  * Search and install for the `numpy` package.
* Create a new package:
  * At any step, if it prompts you to add a new file/package to git, click `Add`.
  * Create a python package called [`src/quiz/`](../src/quiz/).
  * Create a python file called [`quiz0.py`](../src/quiz/quiz0.py) under the `quiz` package and copy the code.
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


## Submission

* From PyCharm, add the followings to git by right clicking on those files and choosing `[Git] - [Add]`:
  * `quiz/quiz0.ipynb`
  * `quiz/quiz0.py`
* Once the files are added to git, they should turn into green. If not, restart PyCharm and add the files again.
* Create a file called [`.gitignore`](../.gitignore) under the `cs329` directory and copy the followings:
  ```
  .idea/
  venv/
  **/.ipynb_checkpoints/
  ```
* Commit and push your changes to Github:
  * Right click on `cs329`, choose `[Git] - [Commit Directory]`, enter a commit message (e.g., "Submit quiz 0."), and click the `[Commit and Push]` button.
  * Make sure ones in `.gitignore` are not getting pushed to Github.
* Check if the above files are properly pushed to your Github respoistory.
* Submit the address of your `cs329` repository (e.g., https://github.com/your_id/cs329.git) to https://canvas.emory.edu/courses/71182/assignments/294068
