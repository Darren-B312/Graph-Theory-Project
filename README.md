# Graph Theory Project - Python RegEx Engine

## Project Brief
Write a program in the Python programming language that can build a non-deterministic finite automaton (NFA) from a regular expression and can use the NFA to check if the regular expression matches any given string of text.  

## Usage
To use this RegEx engine you can clone and import regex.py into your python script then call the match(regex, text) function. This script can also be run directly from the command line:  

```sh
$ python regex.py <RegEx> <text>
Match: True/False
```

E.g.
```sh
$ python regex.py "a(bc+|d*)" abccccc
Match: True
```
note: it is important that your RegEx is between double quotes (E.g. "myRegEx") when using the command line. This is because some operators used in regular expressions like '|' have conflicts with the command line. It is not necessary to surround your text in quotes unless it has spaces.

This implementation supports the following RegEx operators:
- '*' Kleene star: The preceding item will be matched zero or more times.
- '+' The preceding item will be matched one or more times.
- '.' Concatenation: This operator does not need to be included to form a valid RegEx (E.g. "a.b.c", should be input as "abc").
- '|' Alternation: Either the item before or after this operator will be matched.
- '(' & ')' Grouping: Parentheses can be used to apply precedence to parts of a RegEx.

## RegEx Formatting
Your regular expression should be in infix format with no concatenation operators. This program contains two functions, shunt() and concat() which will convert your RegEx to a format usable by the compile_nfa() function.

The following examples should illustrate the modifications made to an input RegEx before it is compiled into a NFA.

>abc >>> concat() >>> a.b.c >>> shunt() >>> abc. . 

>ab*c|(a+bc) >>> concat() >>> a.b*.c|(a+.b.c) >>> shunt() >>> ab*c. .a+bc. .|

>(ab)+ >>> concat() >>> (a.b)+ >>> shunt() >>> ab.+

>a(bc|d*) >>> concat() >>> a.(b.c|d*) >>> shunt() >>> abc.d*|.

## Code Breakdown
### Classes
- State: This class represents a NFA state. Every state has a label, and 0, 1 or 2 edges from it. The label can be ε.
- Fragment: Represents a part of a NFA. Each fragment has a start and accept state.

### Functions
- shunt(): This function is an implementation of Edsger Dijkstra's  [Shunting Yard Algorithm.](http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/) It takes a RegEx string in infix notation and returns the expression in postfix. Converting the RegEx into postfix means characters and operators can be popped off a stack for processing and have their precedence preserved.
- compile_nfa(): This function pops characters off the postfix RegEx stack and constructs NFA fragments with the given operators. Each of the operators has different rules for how their fragments’ [states and edges](https://miro.medium.com/max/1216/1*DY9OhfFJzJC_ocyZPTqmeQ.png) should be connected up. In [this](https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079) Blogpost, the implementation of regular expressions in the Go language is detailed extensively. All the NFA fragments are appended onto each other as the function executes. The function then returns a NFA comprised of all the fragments.   
-  follow_e(): This function uses recursion to follow all 'ε' (empty string) edges until a non-null state is found. Once the function completes execution you are left with a set containing all non-empty states.
-  match(): This function is an implementation of Ken [Thompson's Construction](https://en.wikipedia.org/wiki/Thompson%27s_construction). It iterates through each character in the given text and compares it with the label of the states in the NFA to determine if a pattern that leads to an accept state can be found.
- concat(): This function is my own (probably naive) attempt to automatically insert '.' concatenation characters where necessary to a given RegEx (E.g. a(bc|d*) >>> a.(b.c|d*)). It works by popping characters off the string and based on a few rules, either append the character to the new string, or preface it with a '.' and then append. To devise the logic for whether to append with or without concatenating, I used Excel to draw up a sort of 'truth table' spreadsheet where, based on the character being currently read, and the character that was previously read, determines what the outcome should be. For example, if the string "ab*c" is to be processed, 'a' will be popped off the stack, and because it is the first character read, it will be appended to the new string on its own. When 'b' is read, the if statement logic will see that both the current and previously read characters are both non-special characters, and therefore preface 'b' with a concatenation operator before appending it to the new string (I.e. 'a.b'). Next the * character is read, in this case, regardless of the previous character, the * operator is appended without concatenation (I.e. 'a .b * '). Finally, when the 'c' is read, because the previous character was a * and the current character is non-special, it will be concatenated. This results in the final string 'a.b *. c'. I have provided a [link](https://docs.google.com/spreadsheets/d/1f7rVm_3zULyT2payz8z5QDAsHX-VyFitZLPphWPj8Wc/edit#gid=0) to the spreadsheet on google sheets. I hope it will help in illustrating how I arrived at the code in my function. Please contact me by email if there is any problem accessing the sheet.

## Resources
### Links
Throughout the README I have included links to the resources used in developing this program. The following were also used: 
- [Regex under the hood: Implementing a simple regex compiler in Go](https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079)
- [Regular expression metacharacters](https://linux.die.net/Bash-Beginners-Guide/sect_04_01.html)
- [Common Operators](http://web.mit.edu/gnu/doc/html/regex_3.html)
- [Ctrl+A, Ctrl+C in vim](https://stackoverflow.com/a/25365189)

### Videos
Besides the resources link to above, I found the Computerphile YouTube channel has great videos discussing regular expressions which are both informative and entertaining. Specifically, they have a great video* interview with Brian Kernighan, formerly of Bell Labs and a contemporary of Ken Thompson, in which he describes how the Unix 'grep' command came to be.
- [Regular Expressions - Computerphile](https://www.youtube.com/watch?v=528Jc3q86F8)
- [Using Regular Expressions - Computerphile](https://www.youtube.com/watch?v=6gddK-cOxYc)
- [RegEx Roman Numerals - Computerphile](https://www.youtube.com/watch?v=M3x5Z3iIoSU)
- [Where GREP Came From - Computerphile](https://www.youtube.com/watch?v=NTfOnGZUZDk)*

    
    
    
    
    
    
    
    
 
    
    

