%Include data
:- consult('students.pl').
:- consult('subjects.pl').

%Rules
count_status(ST, LENGH):- %Cuenta los estudiantes con estado 0 o 1
    findall(_,student(_,_,_,_,ST),LIST),length(LIST,LENGH).

career_enrollment(LB, N):- %Alumnos con respecto a la carrera, retorna matricula
    findall(M,student(M,_,_,N,_),LA),
    atomics_to_string(LA, ', ', LB).

career_student_name(LB, N):- %Alumnos con respecto a la carrera, retorna nombre
    findall(M,student(_,M,_,N,_),LA),
    atomics_to_string(LA, ', ', LB).

semester_enrollment(LB, N):- %Alumnos con respecto al semestre, retorna matricula
    findall(M,student(M,_,N,_,_),LA),
    atomics_to_string(LA, ', ', LB).

semester_student_name(LB, N):- %Alumnos con respecto al semestre, retorna nombre
    findall(M,student(_,M,N,_,_),LA),
    atomics_to_string(LA, ', ', LB).

career_maxminsum_credits(MAX, MIN, SUM, CAREER):- %Maximo, minimo & suma de todos los creditos de las materias por carrera
    findall(D, subject(_,_,_,CAREER,D), LIST),
    max_member(MAX, LIST),
    min_member(MIN, LIST),
    sum_list(LIST, SUM).