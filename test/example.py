from pyswip import Prolog
prolog = Prolog()

prolog.consult("test/example.pl")
#status = input("Estado{Aprobado=1, NoAprobado=0}: ")
welcome = prolog.query("career_maxminsum_credits(MAX,MIN,SUM,2)")
print(list(welcome))


# prolog.assertz("father(michael,john)")
# prolog.assertz("father(michael,gina)")
# list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
# for soln in prolog.query("father(X,Y)"):
#    print(soln["X"], "is the father of", soln["Y"])

# for children in prolog.query("father(michael, Y)"):
#    print("Hijos de Michael: ", children["Y"])

# michael is the father of john
# michael is the father of gina
