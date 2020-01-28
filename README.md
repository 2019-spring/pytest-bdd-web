# Installation of packages

## Create Virtual environments: venv - virtual environment 
venv comes with python package.
Navigate to the project directory, using GitBash type the following:

    cd myproject/
    python3 -m venv .myvenv (or py -3 -m venv .venv)
    source .myvenv/bin/activate (for mac)
    source .myvenv/Scripts/activate (for windows)

When you are done working on our project, we can exit the environment with
    >>> deactivate (this will return to regular prompt)

Install packages on your environment

    pip install pytest
    pip install pytest-bdd
    pip install selenium
    pip install numpy=1.15.3
    pip list
    pip uninstall packagename

Creating the copy of environment to share after installing everything create a requirements.txt file

    pip freeze > requirements.txt

Note: virtual environment needs to be ignored before shared in github  

Cloning the environment dependencies
clone the repository, then create a vir. environment under project and install requirements.txt

    python3 -m venv .projvenv/
    pip install -r requirements.txt

Note: if any problems with environment you can remove (rm -r .projvenv), then repeat the process to recreate.


## Project structure

BDD project structure:

    - tests - package
        - page - package
            - base - package (directory needs to have __init__.py emty file)
        - feature - package
        - step_definitions - package
        
    - utitilities - packages
    - configfiles - packages
    - screenshots
    - reports 

## How to pull the project

Clone the repository :

```
git clone https://github.com/2019-spring/pytest-bdd-web.git
```
Do not create virtual environment if you want to install the dependencies from requirements file.

Run following command to create a virtual environment after cloning the project to non-git directory.
```
pip install -r requirements.txt
```
Create a new branch and start working on the project. 

NOTE: You will not have access to push the changes. You might be able to push the branch.

* PROJECT IS NOT RUNNABLE AT THIS MOMENT

    You can check github account for the new commits and you can easily pull to your master branch.
