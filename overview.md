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
To use my code, you will need python and git installed on your machine. To do this will need to use the sudo (superuser do) command and the apt (Advanced Package Tool). Type the following commands into the terminal:

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
---help will print a list of the commands that this program supports to the screen, as well as give a brief explanation of it's use and also outline examples.


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
In this section I will explain each of the core classes and functions used by the program. Most of the algorithms used in the code have been separated out into their own functions. This was done to adhere to the “separation of concerns” design principle [2]. This design pattern not only promotes code reusability, but also makes for much more readable code as each function has one and only one job. Python code is generally quite like pseudocode anyway, and can often be read by those unfamiliar with the language. As such I will show full code snippets of the functions and classes as they appear in code and give more detailed descriptions of how they work.

<hr>

Class: State

    class State:    
	  def __init__(self, label=None, edges=None):  
		  if edges is None:  
	            edges = []  
	        self.edges = edges if edges else []  
	        self.label = label  # label for the arrows (null = epsilon)

This class is used to represent a node in a graph. Sometimes referred to as a vertex, it is “a fundamental unit of which graphs are formed” [3]. Each state has a label, this can be a normal character like ‘a’ or it can be None. In python “None” is the equivalent of “null” in other programming languages. A state with a None label represents ‘ε’, epsilon, the empty string. Each state also has a list of edges, this list is essentially a list of other states that are pointed to by this instance of the state class. If a state has no edges I.e. it has no arrows coming from it, it is an accept state.

<hr>

Class: Fragment

	class Fragment:  
	    def __init__(self, start, accept):  
	        self.start = start  
			self.accept = accept

This class is used to represent NFA fragments, smaller NFAs that are eventually combined to build one NFA. A fragment is essentially a combination of states. An instance of this class has a reference to two states, a start and an accept state. The graph is navigable by following the edges of the start state until you eventually come to the accept state. The simplest fragment will have two states, a start and an accept. More complex fragments will have many states between their start and accept state, though a reference to these middle states will not be directly held by the fragment instance.

<hr>

Function: match

    def match(regex, s):
	    regex = concat(regex)
	    nfa = compile_nfa(regex)

	    current = set()
	    follow_e(nfa.start, current)
	    previous = set()

	    for c in s:
	        previous = current
	        current = set()
	        for state in previous:
	            if state.label is not None:
	                if state.label == c:
	                    follow_e(state.edges[0],
	                             current)

	    return nfa.accept in current  

This function is the first function called when checking a regex against a string. It takes two string arguments, the regular expression “regex” and a query string “s”. This function encompasses all the function calls needed to convert the input regex to an NFA and then return true or false whether the query string matches the pattern described by the regex.

The first step is to call the concat() function and pass it the initially input regular expression. This function returns the same regular expression, but with ‘.’ concatenation characters inserted where necessary. The next step is to construct a NFA with the regex using the compile_nfa() function. This function returns an NFA which is stored in the “nfa” variable.

The set “current” is initialized, this set will be used to keep track of which states are currently being visited. This is important because in an NFA, we can be in 0, 1 or many states simultaneously. 

Next the follow_e function is called so that we immediately follow any empty string labels until we reach a non empty string state.

Now we initialize an empty set to keep track of all the states that we have visited before called "previous".

The function then enters a nested loop which does the following:

    loop through the string one character at a time
	    set our current states to be our previous states
	    reset current to be an empty set
	    loop through each state in previous
		    if the state's label is not null 
		    and 
		    if the state's label is equal to the current character
			    add the state at the end of the arrow to current
	    
Return true or false whether the nfa accept state is in the set of currently visited states after iterating over the whole string, there is only one accept state in our nfa, and if that state is one we have visited, then the NFA accepts the string.

<hr>

Function: concat

    def concat(s):
	    my_list = list(s)[::-1]
	    special_characters = ['*', '|', '(', ')', '+']
	    output = []  

	    while my_list:  
	        c = my_list.pop()

	        if len(output) == 0:  
	            output.append(c)
	        elif c not in special_characters:  
	            if output[-1] not in special_characters or output[-1] == '*' \
	                    or output[-1] == '+':
	                output.append('.')
	                output.append(c)
	            else:
	                output.append(c)
	        elif c == '*' or c == '|' or c == '+':
	            output.append(c)
	        elif c == '(':
	            if output[-1] != '|' and output[-1] != '(' and output[-1] != '.':
	                output.append('.')
	                output.append(c)
	            else:
	                output.append(c)
	        else:
	            output.append(c)

	    return ''.join(output)

This function takes the regex input by the user and inserts concatenation ‘.’ characters where necessary (E.g. abc would be converted to a.b.c). It works by popping characters off the regular expression. Using an admittedly cumbersome  if/elif/else statement, check the rules for the current and previous character, and decide whether to append the character to the output expression on it’s own, or by first appending a concatenation character. I built a spreadsheet with all the possible combinations that the current and previous character could be and what the outcome should be, you can see it [here](https://docs.google.com/spreadsheets/d/1f7rVm_3zULyT2payz8z5QDAsHX-VyFitZLPphWPj8Wc/edit?usp=sharing). In pseudocode, the function works like this:

    convert the string to a reverse ordered list (my_list)
    define characters that have special rulse (* | ( ) + )
    initialize a new empty list (output)
	
	while my_list still has characters
		pop a character c from the list
		
		if output list is empty
			-> append c with no concatenation
		if c is non-special character
		and 
			if last character added to output list is not a special character, * or +
				-> append a concatenation character and then c to output
			else 
				append c with no concatenation
		if c is *, | or +
			-> append with no concatenation
		if c is (
			if previous character is not | and not ( and not .
				-> append a concatenation character and then c to output
			else
				-> append c with no concatentation
		else 
			-> append c with no concatentation
		
		return output as a string


<hr>

Function: compile_nfa

    def compile_nfa(infix):
	    postfix = shunt(infix)  
	    postfix = list(postfix)[::-1]  
	    nfa_stack = []  

	    while postfix:
	        c = postfix.pop()  
	        if c == '.':
	            frag1 = nfa_stack.pop()  
	            frag2 = nfa_stack.pop()
	            frag2.accept.edges.append(frag1.start)
	            start = frag2.start
	            accept = frag1.accept
	        elif c == '|':
	            frag1 = nfa_stack.pop()  
	            frag2 = nfa_stack.pop()
	            accept = State()  
	            start = State(edges=[frag2.start, frag1.start])
	            frag2.accept.edges.append(
	                accept)  
	            frag1.accept.edges.append(accept)
	        elif c == '*':
	            frag = nfa_stack.pop()  
	            accept = State()  
	            start = State(edges=[frag.start, accept])
	            frag.accept.edges = [frag.start, accept]  
	        elif c == '+':
	            frag = nfa_stack.pop()
	            accept = State()
	            start = frag.start
	            frag.accept.edges = ([frag.start, accept])
	        else:
	            accept = State()
	            start = State(label=c, edges=[accept])

	        new_fragment = Fragment(start, accept)
	        nfa_stack.append(new_fragment)  

	    return nfa_stack.pop()

This function takes a regular expression in infix notation and calls the shunt() function to convert it to postfix. It then iterates over the regex and constructs NFA fragments based on the rules of each special character. These fragments are eventually combined together to create one larger NFA which represents the overall regular expression. In pseudocode it looks something like this:

    while there are still characters in the regex
	    pop the next character off the regex
	    if the character is:
		    . // concatenation
				pop two fragments off the nfa stack
			    point the second fragments accept state to the start state of fragment 1
			    
		    | // alternation
			    pop two fragments off the nfa stack
			    create a new start and accept state
			    point the old accept states at the new accept state
			    have the new start state point to the old start states
			    
		    * // Kleene star
			    pop one fragment off the stack
			    create new start and accept states
			    have the old start state edges point to the new start state
			    change the old accept state edges so that they point at the new accept state and the old start state
			    
		    + // 1 or more operator
				pop one fragment off the stack
				create a new accept state
				set the new start state to the old start state
				set the old start state and the new accept state as the new accept state edges
				 
		else // a non-special character
			create a new accept state with a null label
			create a new start state with label c (the non-special character) and the edges of the accept state
			add an edge from the s start state to the accept state
			label the inital state with the character
			
		regardless of what character is read do the following: 
			create a new fragment with the start and accept state from above
			push the new fragment to the NFA stack
Finally, once we have popped every character off the postfix regular expression, we return the only NFA left on the nfa_stack, which is our overall NFA which represents the regular expression that was originally passed to the function.

I found the best way to learn how the different operators are converted into NFA fragments was to look at a visual representation like the one below and read through the code step by step to figure out how the states are being stitched together.

![# Regex under the hood: Implementing a simple regex compiler in Go](https://miro.medium.com/max/1216/1*DY9OhfFJzJC_ocyZPTqmeQ.png)

<hr>

Function: shunt

    def shunt(infix):
	    infix = list(infix)[::-1]  

	    operators = []  
	    postfix = []  

	    precedence = {'*': 100, '+': 90, '.': 80, '|': 60, ')': 40, '(': 20}

	    while infix:
	        c = infix.pop()  
	        if c == '(':
	            operators.append(c)
	        elif c == ')':
	            while operators[-1] != '(':
	                postfix.append(operators.pop())

	            operators.pop()
	        elif c in precedence:
	            while operators and precedence[c] < precedence[operators[-1]]:
	                postfix.append(operators.pop())
	            operators.append(c)
	        else:
	            postfix.append(c)

	    while operators:
	        postfix.append(operators.pop())

	    return ''.join(postfix)

This function takes a regular expression in infix notation and returns the same regular expression in postfix notation. Postfix notation is a much better way to format a regular expression so that a computer can process the characters and operators. It is however not the notation that most people are used to, infix is a much more natural way for us to read mathematical expressions. As such we need some way to allow a regex be input in a human readable form and be converted to a more computer readable form. This algorithm was invented by Edsger Dijkstra [4]. It is named after a shunting yard, which is used to efficiently move train carriages on an off the track so they can be reordered. The algorithm works like this: 

    convert the input string to a stack-like list, infix
    initialize a stack for operators and the postfix expression
    define special characters and give them a precedence
	
	while there are still characters left on infix
		pop a character c
		if c is (
			-> append c to operator stack
		if c is )
			-> pop characters off the operator stack and append them to postfix until you find a '('
			-> pop another character from the operator stack
		if c is in the precedence set
			while there are characters in the operator stack and the precedence of c is less than the precedence of the last character on the postfix stack
			-> append c
		else 
			-> append c
		
	while there are still operators left
		-> append them to postfix (all the special characters have been dealt with)
	
	return the postfix stack as a string

<hr>

Function: follow_e

    def follow_e(state, current):
	    if state not in current: 
	        current.add(state)
	        if state.label is None:  
	            for x in state.edges:
	                follow_e(x, current)  

This function is used to navigate through the graph over any states with an empty string label (ε). The function takes two arguments, a state and a set of states that are currently being visited. In pseudocode, the algorithm follows these steps:

    if state s is not in current ->  add s to current
	    if the s's label is null (empty string)
		    for each state pointed to by s
			    follow_e(s, current) // recursive

If the state is not already in the set, I.e. that state is not currently being visited, add it. If the state is labeled by the empty string ε I.e. it’s label is None (null) iterate over each state pointed to by the initial state and recursively follow all of those states empty labels.


## References <a name="references"/>
The following are resources I specifically referenced in this document:

 - [1] - [Regular Expression](https://en.wikipedia.org/wiki/Regular_expression)  - I am aware that wikipedia is not considered to be the most reliable academic resource, that said, for well understood topics, it often has succinct and eloquent ways to phrase or outline a concept.
 - [2] - [Separation of Concerns](https://medium.com/machine-words/separation-of-concerns-1d735b703a60) - This is a great piece that describes the usefulness of this design pattern in developing code that is modular, reusable and also easier to understand.
 - [3] - [Vertex (graph theory)](https://en.wikipedia.org/wiki/Vertex_%28graph_theory%29) - Like the previous wikipedia link, I used this to find concise phrases to describe states in graph theory, not as a foundation for my research.
 - [4] - [The Shunting Yard Algorithm](https://unnikked.ga/the-shunting-yard-algorithm-36191ea795d9) - This article breaks down the algorithm into a detailed step by step and includes useful diagrams for visual ease. It also details an implementation of the algorithm in Java.

These are the references I found useful in achieving the learning outcomes of this module: 

 - [Regex under the hood: Implementing a simple regex compiler in Go](https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079) - This article is an incredibly detailed description of regex under the hood. In particular the diagram that displays how NFA fragments are combined together based on the operator. This resource also has code snippets of a regex implementation using the Go language. It is worth noting that the Go language was designed in part by Ken Thompson, the same person who developed Thompson's construction, the algorithm on which all of regex was built.
 - [Programming Techniques: Regular expression search algorithm](https://dl.acm.org/doi/pdf/10.1145/363347.363387) -  Speaking of Ken Thompson, for curiosities sake, I had a glance through the 1968 publication of what would later be called Thomson's Construction. This is a fairly outdated piece that describes an implementation in IBM 7094 machine language. Still interesting to have a look through.
 - [Regex Common Operators](http://web.mit.edu/gnu/doc/html/regex_3.html) - This is a simple document that describes the most common regular expression operators in detail.
 - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) - I mostly adhered to the style guidelines set out in this document for my own python scripts.
 - [StackEdit](https://stackedit.io/) - Getting away from python and regular expressions, I used this online markdown file editor for both the readme and overview md files in this repository. It makes adding lists, links, images, code snippets very simple. It also allows you to edit the file and see the changes reflected in real time.
 - [Python 3.8.3 documentation](https://docs.python.org/3/) - I used the python documentation throughout development of this project. Specifically for things like unit testing, command line args, and for list/set manipulation.
 - Beyond the above resources, I also relied heavily on the lecture notes and video demonstrations. 

I outlined the following video resources in the readme file of this repository, but I will mention them here again. I found the Computerphile YouTube channel has great videos discussing regular expressions which are both informative and entertaining. Specifically, they have a great video interview with Brian Kernighan, formerly of Bell Labs and a contemporary of Ken Thompson, in which he describes how the Unix 'grep' command came to be (the 're' stands for regular expression).

 - [Regular Expressions - Computerphile](https://www.youtube.com/watch?v=528Jc3q86F8)
 - [Using Regular Expressions - Computerphile](https://www.youtube.com/watch?v=6gddK-cOxYc)
 - [RegEx Roman Numerals - Computerphile](https://www.youtube.com/watch?v=M3x5Z3iIoSU)
 - [Where GREP Came From - Computerphile](https://www.youtube.com/watch?v=NTfOnGZUZDk)
