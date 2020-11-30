
riga(1..5).
colonna(1..5).
valore(1..5).

maggiore(1, 4, 1, 5).
maggiore(1, 3, 2, 3).
maggiore(2, 4, 2, 3).
maggiore(3, 2, 2, 2).
maggiore(2, 3, 3, 3).
maggiore(3, 4, 2, 4).
maggiore(4, 1, 4, 2).
maggiore(4, 5, 4, 4).
maggiore(5, 2, 5, 3).
maggiore(4, 4, 5, 4).
maggiore(5, 3, 4, 3).
InrigColVal(2,5,2).

%genera celle
cella(X,Y):-riga(X), colonna(Y).

in(X,Y,N) | out(X,Y,N):- cella(X,Y), valore(N).

%stessa cella con valore diverso
:-#count{V:in(X,Y,V)}





valoriFinali(X,Y,V):- InrigColVal(X,Y,V).



