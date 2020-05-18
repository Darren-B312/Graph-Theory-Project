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

## Test <a name="test"/>

## Algorithms <a name="algorithms"/>

## References <a name="references"/>
