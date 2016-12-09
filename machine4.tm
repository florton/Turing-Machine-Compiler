// M accepts binary palindromes 
// 10101 , 101101, 1 ,010

q0 ={start, (1->x,R,q1),(0->x,R,q2),(x->x,S,qaccept)}
q1 ={(1->1,R,q1),(0->0,R,q1),(#->#,L,q3),(x->x,L,q3)}
q2 ={(1->1,R,q2),(0->0,R,q2),(#->#,L,q4),(x->x,L,q4)}
q3 ={(0->0,S,qreject), (1->x,L,q5),(x->x,S,qaccept)}
q4 ={(1->1,S,qreject), (0->x,L,q5),(x->x,S,qaccept)}
q5 ={(1->1,L,q5),(0->0,L,q5),(x->x,R,q0)}
qaccept = {accept}
qreject = {reject}

//Debug(slow)