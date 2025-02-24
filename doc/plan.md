# pseudocode

```
import sys.argv and random

if only one argument 
	print message about how you need to provide the things like 'assault' or 'any'
else
	if 'any' in sys.argv
		call any function
	else if 'assault' in sys.argv
		call assault function
	else if 'skirmisher' in sys.argv
		call skirmisher function
	else if 'recon' in sys.argv
		call skirmisher function
	else if 'support' in sys.argv
		call support function
	else if 'defense' in sys.argv
		call defense function

def any
	characters = [list of all characters in the game]
	pick random index between 0 and length of characters list using random.randint and return whoever is at that index

def other functions
	same as above, just shorter character lists. 
	repeating names is fine this is a short program
```
