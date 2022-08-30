from factor import Factor
from term import Term
from polynomial import Polynomial

x  = Factor("x")
x2 = Factor("x", 2)
y  = Factor("y")
y2 = Factor("y", 2)
z  = Factor("z")
z2 = Factor("z", 2)

term11 = Term(1, x2)
term12 = Term(4, x, y)
term13 = Term(4, y2)
polynomial1 = Polynomial(term11, term12, term13, Term(15), Term(-92))

term21 = Term(1, x2)
term22 = Term(4, y2)
term23 = Term(9, z2)
term24 = Term(2, x, y)
term25 = Term(3, x, z)
term26 = Term(6, y, z)
polynomial2 = Polynomial(term21, term22, term23, term24, term25, term26, Term(2), Term(3/8))


print(polynomial1.string())
print(polynomial2.string())

print("polinom 1'in derecesi : " + str(polynomial1.degree))
print("polinom 2'in derecesi : " + str(polynomial2.degree))
print("polinom 1'in sabit terimi : " + str(polynomial1.constant))
print("polinom 2'in sabit terimi : " + str(polynomial2.constant))