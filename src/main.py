from pyswip import Prolog
prolog = Prolog()
import os

def welcome():
    prolog.consult("src/welcome.pl")
    welcome = list(prolog.query("header()."))
    print(welcome)


def ALL():
    prolog.consult("src/subjects.pl")
    print("#### MATERIAS ####")
    for sb in prolog.query("subject(A, B, C, D, E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Carrera: ", sb["D"], " Creditos: ", sb["E"])
    return 0


def SEMESTER():
    prolog.consult("src/subjects.pl")
    print("#### FILTRAR POR SEMESTRE ####")
    sm = input("Numero de semestre: ")
    for sb in prolog.query("subject(A, B, " + sm + ", D, E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"],
              " Carrera: ", sb["D"], " Creditos: ", sb["E"])


def CAREER():
    prolog.consult("src/subjects.pl")
    print("#### FILTRAR POR CARRERA ####")
    crr = input("Numero de carrera: ")
    for sb in prolog.query("subject(A, B, C, " + crr + ", E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Creditos: ", sb["E"])


def CREDITS():
    prolog.consult("src/subjects.pl")
    print("#### FILTRAR POR CREDITOS ####")
    cr = input("Cantidad de creditos: ")
    for sb in prolog.query("subject(A, B, C, D, " + cr + ")."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Carrera: ", sb["D"])


def STATUS(status):
    prolog.consult("src/calculations.pl")
    welcome = prolog.query("count_status(" + status + ", LENGH)")
    print(list(welcome))


def alumnos(case):
    if(case == 1):
        STATUS("1")
    if(case == 2):
        STATUS("0")


def default():
    return "Opcion Invalida"

def menustart():
    welcome()
    os.system('cls') # NOTA para windows tienes que cambiar clear por cls
    print("----------- MENU INICIAL -----------")
    print("1. TOTAL DE MATERIAS")
    print("2. FILTRAR SEMESTRE")
    print("3. FILTRAR CARRERA")
    print("4. FILTRAR CREDITOS")
    print("5. ALUMNOS")
    print("-----------------------------------")


while True:
    # Mostramos el menu
    menustart()
    case = int(input("Seleccione una opcion: "))
    if(case == 1):
        ALL()
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    elif(case == 2):
        SEMESTER()
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif(case == 3):
        CAREER()
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif(case == 4):
        CREDITS()
        input("Has pulsado la opción 4...\npulsa una tecla para continuar")
    elif(case == 5):
        menustudent()
        input("Has pulsado la opción ...\npulsa una tecla para continuar")


def menustudent():
    print("----------- MENU ALUMNOS -----------")
    print("1. TOTAL DE APROBADOS")
    print("2. TOTAL DE REPROBADOS")
    print("-----------------------------------")
    case = int(input("Seleccione una opcion: "))
    alumnos(case)
