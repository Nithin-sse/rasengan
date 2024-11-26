parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, pat).
parent(pat, jim).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).
