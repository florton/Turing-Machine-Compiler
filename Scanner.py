import sys
import re

def Scan(file):
    try:
        turingMachine = open(file, 'r')
    except:
        raise RuntimeError("Please specify a valid turing language file")
        
    stateRegex = re.compile("(\w+)={(start|accept|reject)?,?(\S*)}")
    edgeRegex = re.compile(",?\((\S)->(\S),(R|S|L),(\w+)\)")
    inputRegex = re.compile("Input\((\S*)\)")
    outputRegex = re.compile("Output\(((\d+|),?(\d+|))\)")

    input = ""
    states = {}
    output = None
    for line in turingMachine:
        line = line.replace(" ", "")
        if line == '\n':
            continue
        reMatch = re.match(stateRegex,line)
        if reMatch is not None:
            parsedEdges = {}
            stateName = reMatch.group(1)
            modifier = reMatch.group(2)
            line = reMatch.group(3)
            edges = re.findall(edgeRegex,line)
            for edge in edges:
                readChar = edge[0]
                writeChar = edge[1]
                nextMove = edge[2]
                nextState = edge[3]
                parsedEdges[readChar] = (writeChar,nextMove,nextState)
            states[stateName] = {'name': stateName,'modifier':modifier,'edges':parsedEdges}
            continue
        reMatch = re.match(inputRegex,line)
        if reMatch is not None:
            input = reMatch.group(1)
            continue
        reMatch = re.match(outputRegex,line)
        if reMatch is not None:
            output = [reMatch.group(2),reMatch.group(3)]
            continue
        error = "Error Parsing Line: " + line
        raise RuntimeError(error)
    return (input,output,states)
        
if __name__ == "__main__":
    output = Scan(sys.argv[1])
    print output[0]
    print output[1]
    for state in output[2]:
        print state
        for edge in output[2][state]:
            print str(edge) +':' + str(output[2][state][edge])
