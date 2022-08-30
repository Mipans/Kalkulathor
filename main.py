from factor import Factor
from term import Term
from equation import Equation

x  = Factor("x")
x2 = Factor("x", 2)
y  = Factor("y")
y2 = Factor("y", 2)
z  = Factor("z")
z2 = Factor("z", 2)

term11 = Term(1, x2)
term12 = Term(4, x, y)
term13 = Term(4, y2)
equation1 = [term11, term12, term13]

term21 = Term(1, x2)
term22 = Term(4, y2)
term23 = Term(9, z2)
term24 = Term(2, x, y)
term25 = Term(3, x, z)
term26 = Term(6, y, z)
equation2 = [term21, term22, term23, term24, term25, term26]

def s_equation(equation:list):
    text = ""
    for term in equation:
        text += " + " + str(term.coefficient)
        t = ""
        for factor in term.factors:
            t += factor.variable + "^" + str(factor.degree)
        text += t
    return text

print(s_equation(equation1))
print(s_equation(equation2))
