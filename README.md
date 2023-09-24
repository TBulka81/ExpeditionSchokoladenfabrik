# ExpeditionSchokoladenfabrik

## Getting the Baseline Source Code

### Installing Git

The baseline source code is provided as a _git repository_. In order to get it, git needs to be installed. It can be downloaded from the following web site: [https://git-scm.com/](https://git-scm.com/). The download section on the right side of the screen should show the correct download for your operating system (assuming your are either using Windows or Mac). 

Install the downloaded software according to the usual mechanism of your operating system of choice. Linux users should resort to their native package manager instead. If in doubt, accept the standard configuration during the installation process.

### Downloading the Source Code

The source code can be cloned from git in the following way:

1. Windows users have to open the App `Git Bash` - Mac and Linux users have to open their terminal of choice.
2. Within the terminal window, navigate to your installation folder of choice with the help of the `cd` command.
3. Within the folder of choice, execute the following command: `git clone https://github.com/TBulka81/ExpeditionSchokoladenfabrik.git`

A closer inspection should now show, that a new folder named `ExpeditionSchokoladenfabrik` exists, which contains:

1. This file (`README.md`)
2. A file named `requirements.txt`
3. A folder named `src/`
4. A folder named `model/`

## Installing the Python Programming Language

Working on the case requires you to have the Python programming language installed. It can be downloaded from [https://www.python.org/](https://www.python.org/). The download section should offer the most up-to-date Python version for your platform (Python 3.11.5 at the time of writing). You can use your operating system's native way to install new applications and - if in doubt - accept the default installation parameters.

__NB.__ The baseline code has only been tested with Python versions >= 3.11. It is strongly discouraged to rely on an older version which might come along with your operating system. Installing a more up-to-date version as described before is usually the way to go.

After Python has been installed, depending on your operating system, you should see something like the following after starting one of the commands `py`, `python` or `python3.11` from the command line:

```
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You now can quit the REPL with the following command: `quit()`.

## Installing the Development Environment

We need some means to edit source code, but do not propose any specific means to do so. If you do have a preferred source code editor or IDE for the Python language, feel free to use it.

For those, who do not (yet) have an editor/IDE of choice, we recommend the Visual Studio Code text editor and some additional PlugIns:

* Visual Studio Code can be downloaded from the following web site: [https://code.visualstudio.com/](https://code.visualstudio.com/). The installation is self explanatory for Windows and Mac systems.
* Once the editor has been installed, start the Visual Studio Code app.
* Install the Python extension as described on this page: [Link](https://learn.microsoft.com/en-us/training/modules/python-install-vscode/5-exercise-install-python-extension?pivots=windows).
* Close Visual Studio Code.

## Creating a Virtual Environment

In order to minimize the potential of conflicting libraries we want to create a so called _virtual environment_ to keep our newly installed programming set-up apart. To do so, we do the following:

1. In the terminal of your choice navigate to the `ExpeditionSchokoladenfabrik` folder by means of the `cd` command.
2. Use the python command you just used before to create the virtual environment by executing the command `python -m venv venv`.
3. Start Visual Studio Code with the following command: `code .` (don't forget the dot!).

## Installing the Required Libraries

A number of libraries are necessary to run the baseline code. These are provided in the file `requirements.txt`. These can be installed in one go by following the following steps:

1. Within Visual Studio Code hit `Ctrl-Shift-P` and select `Python: Create Terminal` from the dropdown menu.
2. Convince yourself, that you are in the `ExpeditionSchokoladenfabrik` folder (you can used the command `pwd` to do so).
3. Execute the following command: `pip install streamlit tensorflow pandas Pillow`.

You should see, that the Python package manager `pip` installs some packages. If no error occured, the programming environment for the excursion is set up.

## Test the Baseline Code

Finally, we want to check, whether the baseline code can be run successfully. To do so, please execute the following steps:

1. Make sure, that you are still in the terminal within Visual Studio Code after you installed the packages.
2. Execute the following command: `cd src`.
3. Execute the following command: `streamlit run schoko_control_center.py`

In your standard browser a new tab with a bare-bones application which allows evaluation of the model should appear.
