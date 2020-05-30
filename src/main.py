from pyswip import Prolog
prolog = Prolog()

prolog.consult("src/welcome.pl")
welcome = list(prolog.query("header()."))
print(welcome)

prolog.consult("src/subjects.pl")

print("#### MATERIAS ####")
for sb in prolog.query("subject(A, B, C, D, E)."):
    print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
          sb["C"], " Carrera: ", sb["D"], " Creditos: ", sb["E"])

print("#### FILTRAR POR SEMESTRE ####")
sm = input("Numero de semestre: ")
for sb in prolog.query("subject(A, B, " + sm + ", D, E)."):
    print("Clave: ", sb["A"], " Nombre: ", sb["B"],
          " Carrera: ", sb["D"], " Creditos: ", sb["E"])

print("#### FILTRAR POR CARRERA ####")
crr = input("Numero de carrera: ")
for sb in prolog.query("subject(A, B, C, " + crr + ", E)."):
    print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
          sb["C"], " Creditos: ", sb["E"])

print("#### FILTRAR POR CREDITOS ####")
cr = input("Cantidad de creditos: ")
for sb in prolog.query("subject(A, B, C, D, " + cr + ")."):
    print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
          sb["C"], " Carrera: ", sb["D"])
