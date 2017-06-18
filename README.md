# php-compiler
Simple scanner and parser for some php syntax using ply library 
Implemented using python

# Requirements
PLY library to be able to use Lex and Yacc for scanner and parser
Tkinter library to be able to use GUI and build the text editor

# BNF
Found in bnf.txt, bnf describe how compiler will work and how syntax will take its sequence

# Main Code
Found in compiler.py
 
# Scanner
Have an array of tokens used in program
Each token have its regular expression
Handle error and identify error line number and the expected value

# Parser
Identify the right path, sequence or components for each syntax
Each function identify a path
Handle error and identify error line number and the expected value

# Editor
Have the functionality to 
1) Open file and compile it
2) Save file
3) Clear area
4) Add the php cover ("<?php ?>")


