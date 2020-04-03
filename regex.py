# Darren Butler
# Classes used in Thompson's construction
import sys


class State:
    """A state with one or two edges, all edges have a label."""
    def __init__(self, label=None, edges=None):
        # every state has 0, 1 or 2 edges from it
        if edges is None:
            edges = []
        self.edges = edges if edges else []
        self.label = label  # label for the arrows (null = epsilon)


class Fragment:
    """An NFA fragment with a start & accept state."""
    def __init__(self, start, accept):
        self.start = start  # start state of NFA fragment
        self.accept = accept  # accept state of NFA fragment


def shunt(infix):
    """Return the infix regular expression in postfix."""
    # Convert input to stack-like list
    infix = list(infix)[::-1]  # reverse order of list

    operators = []  # Operator stack
    postfix = []  # Postfix regular expression

    # Operator precedence
    precedence = {'*': 100, '+': 90, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through input one character at a time
    while infix:
        c = infix.pop()  # pop a character from the input
        if c == '(':
            operators.append(c)
        elif c == ')':
            # pop the operator stack until you find a '('
            while operators[-1] != '(':
                postfix.append(operators.pop())

            operators.pop()
        # decide what to do if operator or normal character
        elif c in precedence:
            while operators and precedence[c] < precedence[operators[-1]]:
                postfix.append(operators.pop())
            operators.append(c)
        else:
            postfix.append(c)

    while operators:
        postfix.append(operators.pop())

    # Convert output list to string
    return ''.join(postfix)


def compile_nfa(infix):
    """Return an NFA fragment representing the infix regular expression."""
    print("DEBUG - infix: " + infix)
    postfix = shunt(infix)  # convert infix to postfix#
    print("DEBUG - postfix: " + postfix)
    postfix = list(postfix)[::-1]  # convert postfix to stack of characters
    nfa_stack = []  # stack for NFA fragments

    while postfix:
        c = postfix.pop()  # pop a char from postfix
        if c == '.':
            frag1 = nfa_stack.pop()  # pop 2 fragments off the stack
            frag2 = nfa_stack.pop()
            # point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            start = frag2.start
            accept = frag1.accept
        elif c == '|':
            frag1 = nfa_stack.pop()  # pop 2 fragments off the stack
            frag2 = nfa_stack.pop()
            accept = State()  # create new start & accept states
            start = State(edges=[frag2.start, frag1.start])
            frag2.accept.edges.append(
                accept)  # point the old accept states at the new one
            frag1.accept.edges.append(accept)
        elif c == '*':
            frag = nfa_stack.pop()  # pop a single fragment off the stack
            accept = State()  # create new start and accept states
            start = State(edges=[frag.start, accept])
            frag.accept.edges = [frag.start, accept]  # point the arrows
        elif c == '+':
            frag = nfa_stack.pop()
            accept = State()
            start = frag.start
            frag.accept.edges = ([frag.start, accept])
        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # create a new fragment to represent the new NFA
        new_fragment = Fragment(start, accept)
        nfa_stack.append(new_fragment)  # push the new NFA to the NFA stack

    # the NFA stack should have exactly one NFA on it
    return nfa_stack.pop()


def follow_e(state, current):
    """Recursively follow all empty string edges
        until a non null state is found"""
    if state not in current:  # only when state has not already been seen
        # add a state to a set and follow all f the e arrows
        current.add(state)
        if state.label is None:  # if state is labelled by empty string
            # loop through the states pointed to by this state
            for x in state.edges:
                follow_e(x, current)  # RECURSION - follow all of their e's too


def match(regex, s):
    """This function will return true if and only if
        the regular regex (fully) matches the string s"""
    regex = concat(regex)
    nfa = compile_nfa(regex)  # compile the regular expression into NFA

    # two sets of states, current and previous
    current = set()
    follow_e(nfa.start, current)
    previous = set()

    for c in s:
        previous = current  # keep track of where we were
        current = set()  # empty set for states we're about to be in
        for state in previous:
            if state.label is not None:  # only follow arrows not labeled by e
                # if the label of the state is equal to the character read
                if state.label == c:
                    # add the state(s) at the end of the arrow to current
                    follow_e(state.edges[0],
                             current)

    return nfa.accept in current  # does NFA match the string s


def concat(s):
    # TODO: include reference to documentation which explains this function
    """This function takes a more user friendly regex (E.g: 'abc'), and
     inserts '.' concat operators where appropriate. (E.g: 'a.b.c')"""
    my_list = list(s)[::-1]  # convert regex string to a reverse ordered list
    # characters with special rules
    special_characters = ['*', '|', '(', ')', '+']
    output = []  # the compiler friendly regular expression (E.g: 'a.b.c')

    while my_list:  # iterate over the user friendly regex
        c = my_list.pop()

        if len(output) == 0:  # always append the first character from the list
            output.append(c)
        elif c not in special_characters:  # if c is a normal character
            # if the previous character is non-special, *, or +
            if output[-1] not in special_characters or output[-1] == '*' \
                    or output[-1] == '+':
                output.append('.')  # preface c with a . operator
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


if __name__ == "__main__":
    print("Match: " + str(match(sys.argv[1], sys.argv[2])))
