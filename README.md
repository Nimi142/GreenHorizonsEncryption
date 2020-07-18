# GreenHorizonsEncryption
A little tool I made to encrypt hebrew sentances.

## HowTo:
- Have a file (filename.txt) with the wanted sentance to encode (NOTE: the program overwrites the file, so if there is anything important there please back it up).
- boot up the main.py file (only it is required) and follow the instructions.
- check the file.

## Algorithm:
The algorithm works by taking one line of hebrew (with symbols) text, and it's output is two lines of hebrew text.
for every hebrew letter it does the following:
1. takes it's location in the alphabet (For example, for "ד" the number is 4 and for "כ" it is 11)
2. it finds two numbers, that when adding their location in the alphabet, the result is like the letter in the sentence.
3. If a number is bigger than 21, the software subtracts 22 from the number (for example: "ב" = 2 = 24-22 ,24 = 21 + 3 = "ש + "ג").
4. it adds one of the letters to the first line of the output and the other to the second line.

## !USE AT YOUR OWN RISK! I TAKE NO RESPONSIBILITY FOR THE ACTIONS OF THIS SOFTWARE.
