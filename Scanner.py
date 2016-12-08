import sys
import re

"""
Copyright Flanders Lorton 2016
https://github.com/florton/Turing-Machine-Compiler
"""

def Scan(file):
    try:
        turingMachine = open(file, 'r')
    except:
        raise RuntimeError("Please specify a valid turing language file")
        
    stateRegex = re.compile("(\w+)={(start)?,?(accept|reject)?,?(\S*)}")
    edgeRegex = re.compile(",?\((.)->(.),(R|S|L),(\w+)\)")
    inputRegex = re.compile("Input\((.*)\)")
    outputRegex = re.compile("Output\(((\d+|),?(\d+|))\)")
    failRegex = re.compile("MissingEdgeReject\(\)")
    commentRegex = re.compile("//.*")
    
    input = ""
    states = {}
    output = None
    reject = False
    for line in turingMachine:
        line = line.replace(" ", "")
        if line == '\n':
            continue
        reMatch = re.match(commentRegex,line)
        if reMatch is not None:
            continue
        reMatch = re.match(stateRegex,line)
        if reMatch is not None:
            parsedEdges = {}
            stateName = reMatch.group(1)
            start = True if reMatch.group(2)=='start' else False
            modifier = reMatch.group(3)
            line = reMatch.group(4)
            edges = re.findall(edgeRegex,line)
            for edge in edges:
                readChar = edge[0]
                writeChar = edge[1]
                nextMove = edge[2]
                nextState = edge[3]
                parsedEdges[readChar] = (writeChar,nextMove,nextState)
            states[stateName] = {'name': stateName,'start':start, 'modifier':modifier,'edges':parsedEdges}
            continue
        reMatch = re.match(inputRegex,line)
        if reMatch is not None:
            input = reMatch.group(1)
            continue
        reMatch = re.match(outputRegex,line)
        if reMatch is not None:
            output = [reMatch.group(2),reMatch.group(3)]
            continue
        reMatch = re.match(failRegex,line)
        if reMatch is not None:
            reject = True
            continue
        error = "Error Parsing Line: " + line
        raise RuntimeError(error)
    if input == '' and len(sys.argv) >2:
        input = str(sys.argv[2])
    return (input,output,states,reject)
        
if __name__ == "__main__":
    output = Scan(sys.argv[1])
    print output[0]
    print output[1]
    for state in output[2]:
        print state
        for edge in output[2][state]:
            print str(edge) +':' + str(output[2][state][edge])
