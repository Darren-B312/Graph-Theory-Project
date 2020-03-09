# Darren Butler
# Classes used in Thompson's construction


class State:
    # Every state has 0, 1 or 2 edges from it
    edges = []

    # Label for the arrows,none means epsilon (empty set)
    label = None

    # Constructor
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label


class Fragment:
    start = None
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


myInstance = State(label='a', edges=[])
myOtherInstance = State(edges=[myInstance])

myFragment = Fragment(myInstance, myOtherInstance)

print(myInstance.label)
print(myOtherInstance.edges[0])
print(myFragment)

