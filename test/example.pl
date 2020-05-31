%Include data
:- consult('src/students.pl').
:- consult('src/subjects.pl').

numb(1).
numb(2).
numb(3).
numb(4).
numb(5).
numb(6).
numb(7).

test(C):-
    A="Hola ",
    B="Mundo", 
    string_concat(A, B, C).