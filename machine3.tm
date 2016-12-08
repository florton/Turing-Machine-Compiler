// M recognizes L = {w$w | w is element of {0,1}*}
// Same as machine2.tm but uses RejectMissingEdges to save some edges

q1 = {start, (1->x,R,q3), ($->$,R,q8), (0->x,R,q2)}
q2 = {(0->0,R,q2),(1->1,R,q2),($->$,R,q4)}
q3 = {(0->0,R,q3),(1->1,R,q3),($->$,R,q5)}
q4 = {(x->x,R,q4),(0->x,L,q6)}
q5 = {(x->x,R,q5),(1->x,L,q6)}
q6 = {(0->0,L,q6),(1->1,L,q6),(x->x,L,q6),($->$,L,q7)}
q7 = {(0->0,L,q7),(1->1,L,q7),(x->x,R,q1)}
q8 = {(x->x,R,q8),(#->#,R,qaccept)}
qaccept = {accept}

RejectMissingEdges()