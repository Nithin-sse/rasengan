% add(5). %
add(N):-
    Sum is N*(N+1)/2,
    write(Sum).
