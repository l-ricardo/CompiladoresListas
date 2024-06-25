class NFA:
    def __init__(self):
        self.states = [[[-1] * MAX_STATES for _ in range(MAX_SYMBOLS)] for _ in range(MAX_STATES)]
        self.numStates = 0
        self.numSymbols = 0
        self.initialState = 0
        self.numFinalStates = 0
        self.finalStates = []

    def initializeNFA(self):
        for i in range(MAX_STATES):
            for j in range(MAX_SYMBOLS):
                for k in range(MAX_STATES):
                    self.states[i][j][k] = -1

    def addTransition(self, from_state, symbol, to_state):
        symbolIndex = ord(symbol) - ord('a')
        self.states[from_state][symbolIndex][to_state] = to_state

    def isFinalState(self, state):
        return state in self.finalStates

    def processInput(self, input):
        currentStates = [self.initialState]

        for symbol in input:
            symbolIndex = ord(symbol) - ord('a')
            nextStates = []

            for currentState in currentStates:
                for k in range(self.numStates):
                    if self.states[currentState][symbolIndex][k] != -1:
                        nextStates.append(self.states[currentState][symbolIndex][k])

            if not nextStates:
                return False

            currentStates = nextStates

        return any(self.isFinalState(state) for state in currentStates)


if __name__ == "__main__":
    MAX_STATES = 100
    MAX_SYMBOLS = 26

    nfa = NFA()
    nfa.initializeNFA()

    numStates = int(input())
    nfa.numStates = numStates

    numSymbols, *symbols = input().split()
    nfa.numSymbols = int(numSymbols)

    for _ in range(nfa.numStates * nfa.numSymbols):
        from_state, symbol, numDestinations = input().split()
        from_state, numDestinations = int(from_state), int(numDestinations)
        for _ in range(numDestinations):
            to_state = int(input())
            nfa.addTransition(from_state, symbol, to_state)

    nfa.initialState = int(input())

    nfa.numFinalStates = int(input())
    nfa.finalStates = list(map(int, input().split()))

    input_string = input()
    if nfa.processInput(input_string):
        print("Aceito")
    else:
        print("Rejeito")
