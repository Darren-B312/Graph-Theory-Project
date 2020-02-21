#Darren Butler
#Shunting Yard Algorithm Implementation

#Input
infix = "(a|b).c*"

#Expected Output: "ab|c*."

#Convert input to stack-esque list
infix = list(infix)[::-1] #reverse order of list

#Operator stack
opstack = []

#Output list
postfix = []

#Operator precedence
precedence = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}


#Loop through input one character at a time TODO: walrus?
while infix:
    #pop a character from the input
    c = infix.pop()

    if c == '(':
        opstack.append(c)
    elif c == ')':
        # pop the opterator stack until you find a '('
        while opstack[-1] != '(':
            postfix.append(opstack.pop())

        opstack.pop()
    # decide what to do if operator or normal character
    elif c in precedence:
        while opstack and precedence[c] < precedence[opstack[-1]]:
            postfix.append(opstack.append())
        opstack.append(c)
    else:
        postfix.append(c)

while opstack:
    postfix.append(opstack.pop())


# Convert output list to string
postfix = ''.join(postfix)

#Print result
print(postfix)
