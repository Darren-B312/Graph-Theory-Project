# GMIT Graph Theory Project 

## Project Brief
Write a program in the Python programming language [2] that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.  

## Usage
To use this RegEx engine you can clone and import regex.py into your python script then call the match(regex, text) function. This script can also be run directly from the command line:  

```sh
$ python regex.py <RegEx> <text>
Match: True/False
```

E.g:
```sh
$ python regex.py "a(bc+|d*)" abccccc
Match: True
```
note: it is important that your RegEx is between double quotes (E.g: "myRegEx") when using the command line. This is because some operators used in regular expressions like '|' have conflicts with the command line. It is not necessary to surround your text in quotes.

This implementation supports the following RegEx operators:
- '*' Kleene star: The preceding item will be matched zero or more times.
- '+' The preceding item will be matched one or more times.
- '.' Concatonation: This operator does not need to be included to form a valid RegEx (E.g: "a.b.c", should be input as "abc").
- '|' Alternation: Either the item before or after this operator will be matched.
- '(' & ')' Grouping: Parentheses can be used to apply precedence to parts of a RegEx.

## RegEx Formatting
Your regular expression should be in infix format with no concatonation operators. This program contains two functions, shunt() and concat() which will convert your RegEx to a format usable by the compile_nfa() function.

The following exmaples should illustrate the modifications made to an input RegEx before it is compiled into a NFA.

>abc >>> concat() >>> a.b.c >>> shunt() >>> abc. . 

>ab*c|(a+bc) >>> concat() >>> a.b*.c|(a+.b.c) >>> concat >>> ab*c. .a+bc. .|

>(ab)+ >>> concat() >>> (a.b)+ >>> shunt() >>> ab.+

>a(bc|d*) >>> concat() >>> a.(b.c|d*) >>> shunt() >>> abc.d*|.# Graph-Theory-Project
