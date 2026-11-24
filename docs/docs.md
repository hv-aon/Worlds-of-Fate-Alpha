# Documentation for Worlds of Fate

This markdown file contains every command used in the file Worlds of Fate.py with descriptions explaining each of them. It's primarily meant for modders, but anyone else can have a look at what's going on behind-the-scenes!

## Imports

```python
import random
import time
import sys
import shelve```

The `import` function is used to import different modules used throughout the code. Here, I've imported random, time, sys, and shelve; random is a module to generate (pseudo-)random numbers, utilized primarily for determining spawnpoints, time is a module used to provide space between each line, sys is used to close the game, and shelve is used to generate save files that I have not yet completed adding to the game.

### Use(s) of Random (DEPRECATED AS OF 0.1)

```python
spawn = random.randint(1, 12)
```

The above code (pseudo-)randomly applies a number from 1 through 12 to variable spawn to determine the player's starting point.

##Use(s) of Secrets

```python
spawn = secrets.choice((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
```

The above code randomly generates and applies a number from 1 through 12 to variable spawn to determine the player's starting point.


### Use(s) of Time

```python
time.sleep(1)
time.sleep(2)
time.sleep(3)
time.sleep(5)
time.sleep(30)
```

The above code provides spaces of time between lines of text. Makes it much easier to stop and read the text for players.

### Use(s) of Sys

```python
sys.exit
```

The above code simply closes the game.

### Use(s) of Shelve

```python
inventory = set()
shelfFile = shelve.open('SaveFile.txt', writeback=True)
shelfFile['nameVariable'] = name
shelfFile['placementVariable'] = placement
shelfFile['inventoryVariable'] = inventory
inventory.add()
shelfFile.close
```

The above code does the following:
- States that variable inventory is the same as set();
- Opens the save file, creates one if not already created, and allows the game to write to it;
- Defines save-file variables as being the same value as game variables;
- Adds an object to inventoryVariable through inventory being tied with set();
- And closes the save file.

## Prints and Inputs

The following is an example of a print command:

```python
print("hello")
```

It prints a specified line of text (typically formatted as ("Line of text")) in the environment in which the file is running.

There is another variant of print() used in this game's code:

```python
print(f"hello {name}")
```

In a statement such as `print(f"{a}")`, the f implies that "{a}" (or another used variable) should be replaced with the value of variable "a". It is used only with two variables (name, name_ingame) in this entire game.

Now for the two different types of uses of input:

```python
name = input()
answer = input().lower()
```

`name = input()` makes the next line an answer prompt that determines the value of 'name'; 'name' is stored as-is without modifications.

`answer = input().lower()` makes the next line an answer prompt that determines the value of 'answer' (see: If/Elif Statements); once the player enters the answer, it converts it to lowercase, and then processes it.

## If/Elif Statements

If/elif statements in this game are used primarily in the following ways:

```python
if (spawnpoint == 1, 2, 3, 4, 5, 6):
elif (spawnpoint == 7, 8, 9, 10, 11, 12):

if answer == "answer":
elif answer == "answer two":
elif answer == "answer three (optional)":
```

The first use, with variable spawnpoint, is used to determine the spawnpoint of the player; if the output matches any of the numbers in the list, it places them there. The second use, with variable answer, is typically used with yes/no (determines game choices) or with specialized word prompts (also determines game choices).

## More Variable Uses

Here are some uses of variables not yet spoken of:

```python
name = None
placement = [0, 1]
placement.append()
attribute = 1
```

Here are each of the functions for this code:

- `name = None` states that variable name has zero value;
- `placement = [0, 1]` states that variable placement is a list (used for saving);
- `placement.append()` is used with a number inside of () that adds said number to the list tied to placement;
- And `attribute = 1` is a backup for saving that is not properly implemented ('keyattribute', 'panattribute', 'gameattribute', and 'keysecretattribute' are all uses of this).

===================================================

Thank you for reading this game's documentation! 
If it helped you with modding, then you're welcome.

(WRITTEN BY WOILEF
VER. 0.1, 11/23/2026)
