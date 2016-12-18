//Machine recognizes { w$w | w is an element of {a,b}* }
// aaba$aaba -> True
// aaa$aab - > False

q0 = {start, (a->x,R,q1),(b->x,R,q3)}
q1 = {(a->a,R,q1),(b->b,R,q1),($->$,R,q2)}
q2 = {(x->x,R,q2),(a->x,L,q5)}
q3 = {(a->a,R,q3),(b->b,R,q3),($->$,R,q4)}
q4 = {(x->x,R,q4),(b->x,L,q5)}
q5 = {(a->a,L,q5),(b->b,L,q5),($->$,L,q6),(x->x,L,q5)}
q6 = {(x->x,S,q8),(a->a,L,q7),(b->b,L,q7)}
q7 = {(a->a,L,q7),(b->b,L,q7),(x->x,R,q0)}
q8 = {($->$,R,q8),(x->x,R,q8),(#->#,S,qaccept)}
qaccept = {accept}

RejectMissingEdges()

//Debug(slow)