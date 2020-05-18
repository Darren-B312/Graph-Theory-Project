# Graph Theory Project Overview
## Contents
 - [Introduction](#introduction)
 - [Run](#run)
 - [Test](#test)
 - [Algorithms](#algorithms)
 - [References](#references)

## Introduction <a name="introduction"/>
Welcome to my repository! I am a third-year software development student at GMIT. As part of a Graph Theory module, I was tasked with building a regular expression (regex) engine using python. Though my project is relatively primitive when compared with existing regex implementations, it was still a considerable challenge and involved a solid understanding of the underlying concepts to develop. In this overview I will attempt to explain and describe, in detail, the following:

 - How to setup and use my code to check if a string of characters matches a regex
 - My testing strategy for this project and how you can run those tests
 - The fundamental graph theory and computer science algorithms behind the code
 - Sources used during research and development of this project

A major requirement from the project brief is that this overview be pitched at second year computer science students. As such, I will assume that anyone reading this has a decent understanding of programming languages but not specifically python. I will attempt to be as “language agnostic” as possible when describing the algorithms used in this project.

This repository contains two python scripts, regex and test_regex. The first script, regex, contains all the classes and functions needed to take a regular expression, insert concatenation characters, convert from infix to postfix notation, compile a non-finite automaton (NFA) and finally, check if the NFA recognizes the query string.

This script can be imported to another python script and its functions used there, or it can also be used directly in the terminal. The second script, test_regex, uses a python unit test library and can be run to verify that regex engine is working as intended. This repository also has two markdown files, overview, which you are reading now and a readme, which contains a more condensed description of the repository. Lastly this repository has a few boilerplate files like a gitignore and a license, these can be ignored for the most part.

A regular expression, or regex for short, is an expression which describes a pattern of characters. The concept arose in the 1950s when the American mathematician Stephen Cole Kleene formalized the description of a regular language [1]. On first inspection, one might think this is not a particularly useful concept, however, think back to the last time you used “ctrl+f” in a web browser to quickly find a specific word or phrase in wall of text, or when you used the “find & replace” function of a word processing program to, in one fell swoop, fix your incorrect spelling of a word throughout the document. Beyond this, regular expressions are used in search engines and lexical analysis [1]. For a programmer, regular expressions are an incredibly useful idea when it comes to automating tasks, and overall timesaving.

## Run <a name="run"/>
To use my code, you will need python3 and git installed on your machine. To do this will need to use the sudo (superuser do) command and the apt (Advanced Package Tool). Type the following commands into the terminal:

    $ sudo apt-get install git
    $ sudo apt-get install python

![sudo apt-get](https://i.imgur.com/QMNaimI.png)

N.B. You may be prompted to give permission to install this software by entering y/n, yes or no. Git and Python are both reputable and widely used software products so you should have no reservations in giving them install privileges.


Assuming you have python and git installed on your machine, the following steps will detail how to download and run the code.

    $ git clone https://github.com/Darren-B312/Graph-Theory-Project.git

![git clone](https://imgur.com/iYAMoMW.png)

Next, use the cd command to navigate to the directory "Graph-Theory-Project" which we just cloned:

    $ cd Graph-Theory-Project

We can view all the files in the directory using the ls command:

    $ ls

![cd / ls](https://imgur.com/t5IdvtG.png)

We can view the code using the vim text editor like this: 

    $ vi regex.py

![vi](https://imgur.com/flA1o32.png)

N.B. To exit vim and return to the linux terminal, press the "esc" key to ensure you're not in insert mode, then type ":q!" to quit without saving, or ":wq" to save first, then press the enter key. 

To use the program in the terminal you will need to have python3 installed on your machine. You will need to format you command line input like this:

    $ python <script_file_name_here> <command_args_here>

Lets start by running the program with the help command:

    $ python regex.py --help

![--help](https://imgur.com/QS0fkYg.png)

We could then use the --ops command to see a list of regular expression operators supported by this engine:

    $ python regex.py --ops

![--ops](https://imgur.com/A1gWVa2.png)

To check if a query string of characters matches a regular expression, use the --match command with two additional arguments. The regular expression encased in double quotes and the string of characters we want to check against the regex:

    $ python regex.py --match "ab*c" abbbbbbbbbbbbc

![--match](https://imgur.com/Wc3CHRz.png)

We can use the match command in conjunction with the explain command to see a more detailed output of the process our regular expression undergoes. We will use a more complicated regular expression to demonstrate:

    $ python regex.py --match --explain "a(bc+|d*)" abccccc

![--match --explain](https://imgur.com/aJ6FdfK.png)


## Test <a name="test"/>
Testing this program was done using the python unit testing library, the documentation for this library can be found [here](https://docs.python.org/3/library/unittest.html). All of the testing code is in the test_regex file. To view this code in vim, as before, use the vi command:

    $ vi test_regex.py

![test_regex.py](https://imgur.com/CAtMeLn.png)

As you can see, each operator is individually tested in the match() function tests for strings the resulting NFA should and should not accept. The program was also tested with regular expressions that use a combination of operators. There are also tests for the concat() and shunt() functions.

The test script can be run from the terminal like any other python script:

    $ python test_regex.py

![test script running](https://imgur.com/4awdUYD.png)

If you were to add any new functionality or refactor the main regex script in any way, it would be very useful to rerun the test script to see if any of your changes had inadvertently broken the existing implementation.

## Algorithms <a name="algorithms"/>

## References <a name="references"/>
