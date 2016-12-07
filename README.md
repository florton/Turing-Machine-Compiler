#Turing Machine Language Python Interpreter
### © Flanders Lorton 2016

####I wrote this language and interpreter from scratch to generate turing machines and run them in Python.


##Example machine: Add 1 to a binary number
The input starts with '$'. The '$' will be overwritten if the 1 is carried out.

###machine.tm
```
Input($1011)
q1 = {start, (1->1,R,q1), (0->0,R,q1), ($->$,R,q1), (#->#,L,q2)} 
q2 = {(1->0,L,q2), (0->1,S,q3), ($->1,S,q3)}
q3 = {accept}
Output()
```
###output for machine.tm
```
$1100
True
```

##Turing Machine Language Syntax:

The machine returns True if it hits an accept state

The machine returns False if it hits a reject state

There is so guarantee the machine will ever stop if it never hits an accept or reject

###Input
Input can only be called once

it can be passed zero or more non-whitespace characters.

Input will be empty if not called
```
Input()
Input(Hello)
Input(2312jsndjn32n:"]\-!!2~k3n4n5)
```
###Output
Output can only be called once

If it is left blank the machine will print the whole tape

Output takes one or two ints (x,y) or (x)

The machine will print the tape from x inclusive to y non-inclusive

if the index of y is beyond the length of the tape, the machine will print the whole tape with a '#' at the end
```
Output()
Output(1,5)
Output(3)
```

###States
**states** must be written in the following format

`name = {modifier, edges }`or `name = { edges }` 

or `name = {modifier}` if it is an accept or reject state

**name** must consist of one or more non-whitespace characters.

names must be unique for each state

**modifier** must be:

`start`  only one start state per machine or

`accept` or `reject`these states should not have edges

**edges**

edges must we written in the following format

seperate multiple edges with commas

`(readChar -> writeChar , moveTape, nextState)`

**readChar**

readChar can be any non-whitespace character that will be read from the tape in the current position

or a `#` to reference the end of the tape

**writeChar**

writeChar can be any non-whitespace character that will be written to the tape in the current position

or a `#` to reference the end of the tape

**moveTape**

moveTape must be `R` `L` or `S`

these correspond to a move of Right Left or Stay from the current position

**nextState**

nextState must be a declared state name


####Examples
````

q1 = {start, (1->1,R,q1), (0->0,R,q1), ($->$,R,q1), (#->#,L,q2)}
stateX = {(5->1,S,q1)}
q2 = {(1->0,L,q2), (0->1,S,q3), ($->1,S,q3)}
q3 = {accept}
q4 = {accept}
state17 = {reject, (1->z,R,stateX)}
````

###Comments

All text after each line will be ignored
Do not put text before code
````
q2 = {(1->0,L,q2), (0->1,S,q3), ($->1,S,q3)}   This is a comment
q3 = {accept}                                  #this too
Output()                                       //me three
```

###Bugs&Errors

This interpreter is new and is not extensively tested.

Report bugs to florton@lion.lmu.edu