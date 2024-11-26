% food(X); lunch(X); dinner(X). %
food(burger).
food(sandwich).
food(pizza).
lunch(sandwich).
dinner(pizza).

meal(X) :- food(X).
%food(X); lunch(X); dinner(X).%
