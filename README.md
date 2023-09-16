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

## Installing the Programming Environment
### Installing the Python Programming Language
Working on the case requires you to have the Python programming language installed. It can be downloaded from [https://www.python.org/](https://www.python.org/). The download section should offer the most up-to-date Python version for your platform (Python 3.11.5 at the time of writing). You can use your operating system's native way to install new applications and - if in doubt - accept the default installation parameters.

__NB.__ The baseline code has only been tested with Python versions >= 3.11. It is strongly discouraged to rely on an older version which might come along with your operating system. Installing a more up-to-date version as described before is usually the way to go.

After Python has been installed, depending on your operating system, you should see something like the following after starting one of the commands `py`, `python` or `python3.11` from the command line:

```
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You now can quit the REPL with the following command: `quit()`.

### Installing the Required Libraries
A number of libraries are necessary to run the baseline code. These are provided in the file `requirements.txt`. These can be installed in one go by following the following steps:

1. Start the terminal app of your choice (e.g. PowerShell on Windows or Terminal on Mac).
2. Navigate to the folder `ExpeditionSchokoladenfabrik` you cloned before from github by means of the `cd` command.
3. Execute the following command: `pip install -r requirements.txt`

You should see, that the Python package manager `pip` installs some packages. If no error occured, the programming environment for the excursion is set up.

## Installing the Development Environment
We need some means to edit source code, but do not propose any specific means to do so. If you do have a preferred source code editor or IDE for the Python language, feel free to use it.

For those, who do not (yet) have an editor/IDE of choice, we recommend the Visual Studio Code text editor and some additional PlugIns:

* Visual Studio Code can be downloaded from the following web site: [https://code.visualstudio.com/](https://code.visualstudio.com/). The installation is self explanatory for Windows and Mac systems.
* Once the editor has been installed, start the Visual Studio Code app.
* Install the Python extension as described on this page: [Link](https://learn.microsoft.com/en-us/training/modules/python-install-vscode/5-exercise-install-python-extension?pivots=windows)
* Close Visual Studio Code

## Test the Baseline Code
Finally, we want to check, whether the baseline code can be run successfully. To do so, please execute the following steps:

1. Navigate to the folder `ExpeditionSchokoladenfabrik` via the command line as before.
2. Start Visual Studio Code with the command `code .` (don't forget the dot!).
3. Visual Studio Code should show the folder tree on the left side of the screen.
4. Start a terminal by hitting `Ctrl-Shift-P` and then selecting `Python: Create Terminal` from the dropdown menu
5. In the terminal which shows up execute the following command: `cd src`.
6. Execute the following command: `streamlit run schoko_control_center.py`

In your standard browser a new tab with a bare-bones application which allows evaluation of the model should appear.
