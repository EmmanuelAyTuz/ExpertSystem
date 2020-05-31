from pyswip import Prolog
prolog = Prolog()

prolog.consult("src/welcome.pl")
welcome = list(prolog.query("header()."))
print(welcome)

prolog.consult("src/subjects.pl")


def TOTAL():
    print("#### MATERIAS ####")
    for sb in prolog.query("subject(A, B, C, D, E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Carrera: ", sb["D"], " Creditos: ", sb["E"])
    return


def SEMESTRE():
    print("#### FILTRAR POR SEMESTRE ####")
    sm = input("Numero de semestre: ")
    for sb in prolog.query("subject(A, B, " + sm + ", D, E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"],
              " Carrera: ", sb["D"], " Creditos: ", sb["E"])
    return


def CARRERA():
    print("#### FILTRAR POR CARRERA ####")
    crr = input("Numero de carrera: ")
    for sb in prolog.query("subject(A, B, C, " + crr + ", E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Creditos: ", sb["E"])
    return


def CREDITOS():
    print("#### FILTRAR POR CREDITOS ####")
    cr = input("Cantidad de creditos: ")
    for sb in prolog.query("subject(A, B, C, D, " + cr + ")."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Carrera: ", sb["D"])
    return


def STATUS(status):
    prolog.consult("src/calculations.pl")
    welcome = prolog.query("count_status(" + status + ", LENGH)")
    print(list(welcome))
    return


def alumnos(case):
    sw = {
        1: STATUS(1),
        2: STATUS(0),
    }
    return sw.get(case, default())


def default():
    return "Opcion Invalida"


def materias(case):
    sw = {
        1: TOTAL(),
        2: SEMESTRE(),
        3: CARRERA(),
        4: CREDITOS(),
        5: menustudent(),
    }
    return sw.get(case, default())


def menustudent():
    print("----------- MENU ALUMNOS -----------")
    print("1. TOTAL DE APROBADOS")
    print("2. TOTAL DE REPROBADOS")
    print("-----------------------------------")
    case = int(input("Seleccione una opcion: "))
    alumnos(case)


def menuinicio():
    print("----------- MENU INICIAL -----------")
    print("1. TOTAL DE MATERIAS")
    print("2. FILTRAR SEMESTRE")
    print("3. FILTRAR CARRERA")
    print("4. FILTRAR CREDITOS")
    print("5. ALUMNOS")
    print("-----------------------------------")
    case = int(input("Seleccione una opcion: "))
    materias(case)


menuinicio()
