from pyswip import Prolog
prolog = Prolog()


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


def materias(case):
    if(case == 1):
        ALL()
    if(case == 2):
        SEMESTER()
    if(case == 3):
        CAREER()
    if(case == 4):
        CREDITS()
    if(case == 5):
        menustudent()


def menustudent():
    print("----------- MENU ALUMNOS -----------")
    print("1. TOTAL DE APROBADOS")
    print("2. TOTAL DE REPROBADOS")
    print("-----------------------------------")
    case = int(input("Seleccione una opcion: "))
    alumnos(case)


def menustart():
    welcome()
    print("----------- MENU INICIAL -----------")
    print("1. TOTAL DE MATERIAS")
    print("2. FILTRAR SEMESTRE")
    print("3. FILTRAR CARRERA")
    print("4. FILTRAR CREDITOS")
    print("5. ALUMNOS")
    print("-----------------------------------")


menustart()
