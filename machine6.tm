//M accepts {x element of {0,1}* | There are an equal number of 0's and 1's}

q0 = {start, (y->y,R,q0),(#->#,S,qaccept),(1->x,R,q2),(0->x,R,q1)}
q1 = {(y->y,R,q1),(x->x,R,q1),(0->0,R,q1),(1->y,L,q3)}
q2 = {(y->y,R,q2),(x->x,R,q2),(1->1,R,q2),(0->y,L,q3)}
q3 = {(0->0,L,q3),(1->1,L,q3),(y->y,L,q3),(x->x,R,q0)}
qaccept = {accept}

RejectMissingEdges()
//Debug(slow)