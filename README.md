# Mu0
A simple cpu model designed by University of Manchester， implemented using python


Implement a hardware using software can be challenging, although try not to use software features as much as i can, some part of the design just could not be implemented without using software features(such as 'if' 'for'), list some issues below:

1. implement d flip flop using 'if' 'else', and store the 'voltage' as a bit;
2. for simplicity, using 'for' to compress all bits in 16bits register to a integer, may not be a violation of rules, just laziness;
3. using variables to store signals sometimes, again, just laziness;
4. don't know how to simulate 'synchronous transmission of singals', just use sequence expression instead;
5. too lazy to write other issues;


Usage:
     python Timer.py
