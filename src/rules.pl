%Include data
:- consult('students.pl').
:- consult('subjects.pl').

%Rules
count_status(ST, LENGH):-
    findall(_,student(_,_,_,_,ST),LIST),length(LIST,LENGH).
