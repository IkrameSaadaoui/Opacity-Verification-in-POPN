# Problem Statement: 
# Let X = (Qx, ∑, δx, q0, Fx) be an NDFA which accepts the language L(X). 
# We have to design an equivalent DFA Y = (Qy, ∑, δy, q0, Fy) such that L(Y) = L(X). 
# The following procedure converts the NDFA to its equivalent DFA


import math
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])

def isValidInteger(a):
    isValid = True 
    try:
        a = int(a)
        if a <= 0:         
            isValid = False
            raise ValueError ("The number of states can not be negatif or zero  ")
    except TypeError:
        print ("The number of states must be a positive integer  ")
    return isValid

def automaton_definition():
    Q = [] ; E = [] ; F = [] ;

    nbStates = input("Enter the number of states in your automaton:  ")
    while not isValidInteger(nbStates):
        nbStates = input("Enter a valid number:  ")

    for i in range(1, int(nbStates) + 1):
        print("Enter the name of the ", ordinal(i),"state")
        q = input()
        Q.append(q)

    nbAlphabet = input("Enter the number of alphabetSet in your automaton:  ")
    while not isValidInteger(nbAlphabet):
        nbAlphabet = input("Enter a valid number:  ")
    for i in range(1, int(nbAlphabet) + 1):
        print("Enter name of the", ordinal(i),"event")
        e = input()
        E.append(e)
    intialState = input("Specify the initial state: ")

    nbFinalState = input("Enter the number of final states in your automaton:  ")
    while not isValidInteger(nbFinalState):
        nbFinalState = input("Enter a valid number:  ")
    for i in range(1, int(nbFinalState) + 1):
        print("Enter the name of the", ordinal(i),"final state")
        f = input()
        F.append(f)
    # Creates a list containing 5 lists, each of 8 items, all set to 0
    NFA_Matrix = [['empty' for x in range(int(nbAlphabet))] for y in range(int(nbStates))] 

    print ("Define the transitions in your automata"),
    
        # construct the NFA table
    for i in range(0,int(nbStates)):     # for each NFA state             
        for j in range(0,int(nbAlphabet)):    # for each input symbol 
            print(Q[i], '==',E[j],'==>', " ", end="")
            nextState = input()
            NFA_Matrix[i][j] = Q[i]
            NFA_Matrix[i][j] = E[j]
            NFA_Matrix[i][j] = nextState
        
    print('set of states', Q)  
    print('set of symbols', E)  
    print('set of final states', F)
    print('NFA matrix', NFA_Matrix)
    return Q, E, F, NFA_Matrix, nbStates, nbAlphabet, nbFinalState

StateSet, EventSet, FinalStates, Nfa, n_States, n_Sym, nbF = automaton_definition() 

def nfa_to_dfa():

    StateSet, EventSet, FinalStates, Nfa, n_States, n_Sym, nbF = automaton_definition() 
    statename[n_States][n_States]
    i = 0  # current index of DFA 
    n = 1  # number of DFA states 
 
    nextstate[n_States] 
    strcpy(statename[0], "0") # start state 
 
    for i in range(0,int(nbStates)):     # for each NFA state             
        for j in range(0,int(nbAlphabet)):    # for each input symbol  
            get_next_state(nextstate, statename[i], Nfa, n_States, j)
            dfa[i][j] = state_index(nextstate, statename, n)        
    return n;   # number of DFA states 
 
# Get next-state string for current-state string.
def get_next_state(nextstates, cur_states, nfa, n_nfa, symbol):
    temp[STATES]
    temp[0] = '\0'
    for i in range(strlen(cur_states)):
        string_merge(temp, nfa[cur_states[i]-'0'][symbol])
    strcpy(nextstates, temp)

 
def state_index(state,statename[][STATES], pn):
    if (!state): 
        return -1 # no next state 
    for i in  range(pn):
        if (!strcmp(state, statename[i])): 
            return i
    strcpy(statename[i], state);   # new state-name
    return pn+= 1

    