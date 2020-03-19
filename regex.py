# Darren Butler
# Classes used in Thompson's construction


class State:
    # Every state has 0, 1 or 2 edges from it
    edges = []

    # Label for the arrows, none means epsilon (empty set)
    label = None

    # Constructor
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label


class Fragment:
    start = None  # start state of NFA fragment
    accept = None  # accept state of NFA fragment

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


def shunt(infix):
    # Convert input to stack-esque list
    infix = list(infix)[::-1]  # reverse order of list

    # Operator stack
    opstack = []

    # Output list
    postfix = []

    # Operator precedence
    precedence = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through input one character at a time TODO: walrus?
    while infix:
        # pop a character from the input
        c = infix.pop()

        if c == '(':
            opstack.append(c)
        elif c == ')':
            # pop the operator stack until you find a '('
            while opstack[-1] != '(':
                postfix.append(opstack.pop())

            opstack.pop()
        # decide what to do if operator or normal character
        elif c in precedence:
            while opstack and precedence[c] < precedence[opstack[-1]]:
                postfix.append(opstack.pop())
            opstack.append(c)
        else:
            postfix.append(c)

    while opstack:
        postfix.append(opstack.pop())

    # Convert output list to string
    return ''.join(postfix)


def compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        # pop a char from postfix
        c = postfix.pop()
        if c == '.':
            frag1 = nfa_stack.pop()  # pop 2 fragments off the stack
            frag2 = nfa_stack.pop()
            frag2.accept.edges.append(frag1.start)  # point frag2's accept state at frag1's start state
            new_fragment = Fragment(frag2.start, frag1.accept)  # create new fragment to represent the combined NFA

        elif c == '|':
            frag1 = nfa_stack.pop()  # pop 2 fragments off the stack
            frag2 = nfa_stack.pop()

            accept = State()  # create new start & accept states
            start = State(edges=[frag2.start, frag1.start])

            frag2.accept.edges.append(accept)  # point the old accept states at the new one
            frag1.accept.edges.append(accept)
            new_fragment = Fragment(start, accept)

        elif c == '*':
            frag = nfa_stack.pop()  # pop a single fragment off the stack

            accept = State()  # create new start and accept states
            start = State(edges=[frag.start, accept])

            frag.accept.edges = [frag.start, accept]  # point the arrows

            new_fragment = Fragment(start, accept)  # create new fragment to represent the new combined NFA
        else:
            accept = State()
            start = State(label=c, edges=[accept])
            new_fragment = Fragment(start, accept)

        nfa_stack.append(new_fragment)

    # the NFA stack should have exactly one NFA on it
    return nfa_stack.pop()


def followes(state, current):
    if state not in current:  # only when state has not already been seen, no point in adding state to set twice
        # add a state to a set and follow all f the e arrows
        current.add(state)
        if state.label is None:  # if state is labelled by 
            for x in state.edges:  # loop through the states pointed to by this state
                followes(x, current)  # RECURSION - follow all of their epsilons too


def match(regex, s):
    # This function will return true if and only if the regular regex (fully) matches the string s

    nfa = compile(regex)  # compile the regular expression into NFA

    # two sets of states, current and previous
    current = set()
    followes(nfa.start, current)
    previous = set()

    for c in s:
        previous = current  # keep track of where we were
        current = set()  # create a new empty set for states we're about to be in
        for state in previous:
            if state.label is not None:  # only follow arrows not labeled by e(empty string)
                if state.label == c:  # if the label of the state is equal to the character read
                    followes(state.edges[0], current)  # add the state(s) at the end of the arrow to current

    return nfa.accept in current  # does NFA match the string s


print(match("a.b|b*", "bbbbbbbbbb"))
