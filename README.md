# A script for calculating the intersection of strings

This script takes a number of text inputs, cleans them to accept only the 26 letters in the English alphabet, and then outputs the letters that are common to all inputs.

The easiest way to run it will be to copy the script into an online python interpreter [such as this one.](https://www.online-python.com/) Alternatively you can download the script and install python and then run it locally on your computer via the command line.

The no duplicates script is similar, but it ignores any letters that are in the overlap more than once, and only gives them once.

The combinations script is slightly different. This will compare three strings and provide either of the above results depending on how you set it. If you have clues that you're not sure what word they represent, you can put them into the arrays at the top and the script will produce an output line for each permutation of the possibilities. Combinations build up quickly, so watch out! This script has some limitations, for example if a word with multiple possibilities is in more than one circle then it will be matched with all of its own possibilities in the other circle.
