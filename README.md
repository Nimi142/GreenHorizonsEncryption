# GreenHorizonsEncryption
A little tool I made to encrypt hebrew sentances.

## HowTo:
Have a file (filename.txt) with the wanted sentance to encode (NOTE: the program overwrites the file, so if there is anything important there please back it up).
boot up the main.py file (only it is required) and follow the instructions.
check the file.

## Algorithm:
The encryption algorith, works by going letter to letter, taking the letter's number in the alphabet and replacing it with two letters that when adding their place in the alphabet (with overflow) it equals the number of the previous letter.
