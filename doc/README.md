# purpose

sometimes while playing apex, someone has the idea of picking a random character out of the available ones. That is kind
of annoying to do, because you have to count out how many there are, go find a random number generator, and then count up
to that number across the characters - it's all a little tedious. I want a program that will simply spit out a random 
character when you hit a button. Simple!

I would also like it to be able to randomly pick a legend based on their class. Here are the classes in apex:
- assault
- skirmisher
- recon
- support
- defense

Examples of what I want output to look like for running this program:

```
src/picker.py
Error: must provide additional argument
Example of usage: src/picker.py any | assault | skirmisher | recon | support | defense

```
src/picker.py any
Fuse!
```
```
src/picker.py skirmisher
Octane!
```
```
src/picker.py defense
Caustic!
```

I don't know how crazy this program should be. I could really just examine the arguments provided and have a bunch of 
sloppy if-else statements and call it a day. I might just do that instead of building this to be expanded upon in the 
future. This is a smaller program and there isn't a need to go crazy with it.

