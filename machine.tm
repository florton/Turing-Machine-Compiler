//This machine adds a 1 to the number then prints the new number
//The input must start with '$' and be followed by a binary number
// $1101 , $111, $110100011, $001
//The '$' will be overwritten if the 1 is carried out.
// e.g $111 -> 1000

Input()
q1 = {start, (1->1,R,q1), (0->0,R,q1), ($->$,R,q1), (#->#,L,q2)}
q2 = {(1->0,L,q2), (0->1,S,q3), ($->1,S,q3)}
q3 = {accept}
Output() 