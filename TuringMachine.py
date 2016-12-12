import sys
from Scanner import Scan

"""
Copyright Flanders Lorton 2016
https://github.com/florton/Turing-Machine-Compiler
"""

try:
    machine = Scan(sys.argv[1])
except:
    raise RuntimeError("Please specify a valid turing language file")
    
input = machine[0]
output = machine[1]
states = machine[2]
functions = machine[3]
tape = []

def Run():

    #Process Input
    for char in input:
        tape.append(char)
    tape.append('#')

    #Load start, accept & reject states
    start = None
    accept = []
    reject = []
    for name, state in states.iteritems():
        if state['start']:
            start = state
        if state['modifier'] == 'accept':
            accept.append(state)
        if state['modifier'] == 'reject':
            reject.append(state)    

    #Run Through States
    currentState = start
    tapePosition = 0
    while(True):      
        if functions['debug']:
            Debug(tapePosition,currentState,functions['debug'])             
        if tape[-1] != '#' or tapePosition == len(tape)-1:
            tape.append('#')    
        if currentState in accept:
            return Return(True)
        if currentState in reject:
            return Return(False)
            
        #Run deterministic edge
        try:
            currentEdge = currentState['edges'][str(tape[tapePosition])]
        except:
            if functions['rejectEdges']:
                return Return(False)
            error = "Could not find an edge for char: '" + str(tape[tapePosition]) + "' from state: " + str(currentState['name'])
            print "Current position: " + str(tapePosition)
            print tape
            raise RuntimeError(error)
        tape[tapePosition] = currentEdge[0]
        if currentEdge[1] == 'R':
            tapePosition = tapePosition +1
        elif currentEdge[1] == 'L':
            tapePosition = tapePosition-1 if tapePosition!=0 else 0
        currentState = states[currentEdge[2]]

def Return(bool):
    final = Output()
    if bool == False:
        return 'X'
    if(functions['pipe']):
        return final
    if(final != None):
        print final
    return bool
        
def Output():
    #Print Output (Tape Subsection)
    if output is not None:
        final = ''
        start = 0
        end = tape.index('#')
        if output[0] != '':
            start = int(output[0])
        if output[1] != '':    
            end = int(output[1])    
        for char in tape[start:end]:
                final = final + char
        return final

def Debug(tapePosition,currentState,flags):
    print "Current State: " + currentState['name']
    print tape
    print ''.rjust(5*tapePosition)+'  ^'
    if flags == 'slow':
        raw_input()
    
        
if __name__ == "__main__":
    print Run()