from pyswip import Prolog
prolog = Prolog()
prolog.consult("src/subjects.pl")

for sb in prolog.query("subject(A, B, C, D, E)"):
    print("Clave: ", sb["A"], " Nombre: ", sb["B"], " Semestre: ",
          sb["C"], " Carrera: ", sb["D"], " Creditos: ", sb["E"])
