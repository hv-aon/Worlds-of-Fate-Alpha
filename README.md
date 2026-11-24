# Worlds of Fate ALPHA 0.1

Worlds of Fate is a text-based CYOA game inspired by RPGs and visual novels, built entirely in Python 3.12.4 with exactly one file (the executable does have more, simply to package the file and run it, I believe!). It was compiled into an executable utilizing PyInstaller.

## Requirements

I am quite uneducated on PyInstaller, but from my research, there are no requirements for `Worlds of Fate.exe`. But if you are running from `Worlds of Fate.py`, you need to have Python (3.12.4 and/or higher) installed. There are a few ways to do this:

1. Download Python from Python's official website]
(https://python.org/downloads). This is the easiest and most effective way to get it.

2. If you're on Windows, open Terminal and run:

```powershell
winget install Python.Python.3.12
```

If you'd like to get a newer version, replace `3.12` with `3.13`, `3.14`, or `3.15`.

3. If you're on MacOS, install uv. You can get it from PyPi (https://pypi.org/project.uv), or run:

```bash
curl -LsSf https://astral.sh/uv/install.sh
```

(note: all newer MacOS versions have curl pre-installed; I do not know about older versions)
Linux typically has Python pre-installed, but if the distro you use for whatever reason does not have python, you can run the above command. If you don't have curl, run:

```bash
wget -q0- https://astral.sh/uv/install.sh
```

Once this is done, run:

```bash
uv python install
```

(This information comes from the uv documentation site (https://docs.astral.sh)!)

## How to Play

This game is, at its core, a text-based CYOA. It gives you prompts for specific actions, and you answer with a set of instructions. Listed are the types of questions:

1. Yes or No
A yes or no question is something like "{name} is your name?". You answer with a simple 'yes' or 'no.

2. Complex Question
A complex yes or no question is something along the lines of "Do you choose the red team or the blue team?". You answer this with the literal answers; remove "the", "a", and related words to answer with, in this case, a 'red team' or 'blue team'.

3. Non-Binary Complex Question
A complex question would be something like "Do you choose to enter the first, second, or third door?". They give you three answers; you do the same process as a Complex Question to answer with, in this case, 'first', 'second', or 'third'.

## Verification

This is a python-based game. Python files can hold viruses, so if you'd like to be extra-safe, verify the hash (if you downloaded the executable) or look at the code against the [documentation] (docs/docs.md) (if you downloaded the .py).

To verify the hash, run:
```powershell
Get-FileHash "C:\\path\to\Worlds of Fate.exe" SHA-256
```

Once you've obtained the it, compare it against the standard hash:

BCDE4C20945A5D86552AE42FD15A95F8C2E00B2445722B087BBB49E9C41BB4B9

If you see any differences, your file's been tampered with. Or it's just a different version, if you downloaded it from https://hv-aon.itch.io/worlds-of-fate slash https://hv-aon.itch.io/worlds-of-fate-pre-release or https://github.com/hv-aon/worlds-of-fate.

--HV AON IS NOT LIABLE FOR THIRD-PARTY DISTRIBUTIONS OR MODIFICATIONS OF WORLD OF FATE THAT HAVE VIRUSES!--

## Modding

As a Python game, Worlds of Fate supports modding. 

### Making a Mod

To make a mod of this game, you first need a Python IDE (editor). 

1. IDLE. I personally recommend IDLE, not only because it's Python's editor that comes packed with an installation of Python, but also because it makes it really simple to code. Installation: Python's official site (https://python.org/downloads).

2. VSCode. This is a free app created by Microsoft. It has many more features than IDLE, and has a much better debugger. The one problem I have with it is how much it pushes its AI. Installation: VSCode's official site (https://code.visualstudio.com/download), or if you're on Windows, Microsoft Store.

3. There are many others out there, so if you don't like the three listed, you can find others on Google.

Once you have an IDE, you can begin modding. `Worlds of Fate.py` already has explanations for most things, but they're unserious; for an extensive explanation, read the documentation (docs/docs.md).

### Compiling a Mod

To compile a mod, I reccomend using PyInstaller. You can install it a few ways:

1. If you're in Windows, open Terminal and run:
```powershell
pip install pyinstaller
```

2. On MacOS or Linux, I reccomend just releasing the .py file, because I could not find documentation on using uv to install PyInstaller.

Once you have PyInstaller, run the following commands in the terminal:

```powershell
cd path/to/your/mod
pyinstaller your_mod.py
```

If you want to compile it into one file:

```powershell
cd path/to/your/mod
pyinstaller --onefile your_mod.py
```

If you want to add a custom icon:

```powershell
cd path/to/your/mod
pyinstaller --icon="icon.ico" your_mod.py
```
(The icon must be a .ico, otherwise it'll throw an error.)

To mix `--onefile` and `--icon`, do `--onefile --icon="icon.ico"`.

If for whatever reason it's not working, but PyInstaller isn't recognized, run these commands in PowerShell:

```powershell
cd path/to/your/mod
python -m pyinstaller your_mod.py
```
(Everything else is the same after the `-m`.)

### Releasing a Mod

To release a mod:

1. As an executable: Release the mod on Itch.io (https://itch.io) or GitHub (https://github.com). Make sure to include a `README.md` (like this one!) and `LICENSE.txt`. You can find how to format these online, or just use mine as templates!

2. As a .py file: Release the mod on the two platforms listed above, nothing extra needed (though I'd still make the README and LICENSE just to be safe).

IF YOU'RE MODIFYING THIS README, REPLACE THE HASH IN THE VERIFY SECTION WITH THE HASH FOR YOUR EXECUTABLE!

## Are you suggesting coconuts migrate?

Not at all, they could be carried.

## Thanks and Acknowledgements (by Woilef)

- Thank you to not_proxywar, who suggested the name, two or three? openings, and multiple other aspects of this game. He was, and is, a big help to me while coding this game!

## License

GNU GPLv3 (https://choosealicense.com/licenses/gpl-3.0)
