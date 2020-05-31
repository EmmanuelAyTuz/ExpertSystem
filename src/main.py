import os
import re
from pyswip import Prolog
prolog = Prolog()


def welcome():  # Mensaje de bienvenida
    prolog.consult("src/welcome.pl")
    welcome = list(prolog.query("header()."))
    print(welcome)


def listOfTuples(listA, listB):  # Combinar dos listas y retorna una nueva
    return list(map(lambda x, y: (x, y), listA, listB))


def fixOutput(query):  # Extrae los valores entre "'", separa por ",", retorna list
    prolog.consult("src/rules.pl")
    ntext = re.findall(
        r"'(.*?)'", str(list(prolog.query(query))))
    # print(ntext)
    return ntext[1].split(', ')


def ALLSUBJECT():  # Todas las materias
    prolog.consult("src/subjects.pl")
    print("#### MATERIAS ####")
    for sb in prolog.query("subject(A, B, C, D, E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Carrera: ", sb["D"], " Creditos: ", sb["E"])
    return 0


def SEMESTER():  # Filtro por semestre en las materias
    prolog.consult("src/subjects.pl")
    print("#### FILTRAR POR SEMESTRE ####")
    sm = input("Numero de semestre: ")
    for sb in prolog.query("subject(A, B, " + sm + ", D, E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"],
              " Carrera: ", sb["D"], " Creditos: ", sb["E"])


def CAREER():  # Filtro por carrera en las materias
    prolog.consult("src/subjects.pl")
    print("#### FILTRAR POR CARRERA ####")
    crr = input("Numero de carrera: ")
    for sb in prolog.query("subject(A, B, C, " + crr + ", E)."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Creditos: ", sb["E"])


def CREDITS():  # Filtro por creditos en las materias
    prolog.consult("src/subjects.pl")
    print("#### FILTRAR POR CREDITOS ####")
    cr = input("Cantidad de creditos: ")
    for sb in prolog.query("subject(A, B, C, D, " + cr + ")."):
        print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
              sb["C"], " Carrera: ", sb["D"])


def STATUS(status):  # Filtra por estado de los alumnos
    prolog.consult("src/rules.pl")
    welcome = prolog.query("count_status(" + status + ", LENGH)")
    print(list(welcome))


def STUDENTSBYCAREER():  # Consulta los alumnos por carrera imprime su matricula & nombre
    print("Indique(1 Sistemas, 2 Admon, 3 Ambiental, 4 Industrial, 5 Civil)")
    icareer = str(input("Carrera: "))
    print("Alumnos en la carrera:")
    query1 = "career_student_name(OUT," + icareer + ")"
    query2 = "career_enrollment(OUT," + icareer + ")"
    for x in listOfTuples(fixOutput(query1), fixOutput(query2)):
        print(x)
        print("\r")


def STUDENTSBYSEMESTER():  # Consulta los alumnos por semestre imprime su matricula & nombre
    print("Indique(1, 2, 3, 4, 5, 6, 7, 8, 9")
    isem = str(input("Semestre: "))
    print("Alumnos en el semestre:")
    query1 = "semester_student_name(OUT," + isem + ")"
    query2 = "semester_enrollment(OUT," + isem + ")"
    for x in listOfTuples(fixOutput(query1), fixOutput(query2)):
        print(x)
        print("\r")


def actionstudents(case):
    if(case == 1):
        STATUS("1")
    if(case == 2):
        STATUS("0")
    if(case == 3):
        STUDENTSBYSEMESTER()
    if(case == 4):
        STUDENTSBYCAREER()


def actionsubjects(case):
    if(case == 1):
        ALLSUBJECT()
    if(case == 2):
        SEMESTER()
    if(case == 3):
        CAREER()
    if(case == 4):
        CREDITS()


def default():
    return "Opcion Invalida"


def menustart():
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    welcome()
    print("----------- MENU INICIAL -----------")
    print("1. MATERIAS")
    print("2. ALUMNOS")
    print("3. SALIR")
    print("-----------------------------------")


def menusubject():
    print("----------- MENU MATERIAS -----------")
    print("1. TOTAL DE MATERIAS")
    print("2. FILTRAR SEMESTRE")
    print("3. FILTRAR CARRERA")
    print("4. FILTRAR CREDITOS")
    print("-----------------------------------")
    case = int(input("Seleccione una opcion: "))
    actionsubjects(case)


def menustudent():
    print("----------- MENU ALUMNOS -----------")
    print("1. TOTAL DE APROBADOS")
    print("2. TOTAL DE REPROBADOS")
    print("3. FILTRAR ALUMNOS POR SEMESTRE")
    print("4. FILTRAR ALUMNOS POR CARRERA")
    print("-----------------------------------")
    case = int(input("Seleccione una opcion: "))
    actionstudents(case)


while True:
    try:
        # Mostramos el menu
        menustart()
        case = int(input("Seleccione una opcion: "))
        if(case == 1):
            menusubject()
            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        elif(case == 2):
            menustudent()
            input("Has pulsado la opción ...\npulsa una tecla para continuar")
        elif(case == 3):
            break
        else:
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    except ValueError:
        input("DEBE INGRESAR NUMEROS")
    except:  # En caso de error:
        input("ERROR INTENTE DE NUEVO")
