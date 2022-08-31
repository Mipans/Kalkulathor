# This is the main file

from term import Term
from polynomial import Polynomial

a = Term(1, 2)
f = Term(21, 2)

b = Term(8, 1)
d = Term(24, 1)
e = Term(9, 1)

c = Term(16, 0)
g = Term(24, 0)
h = Term(51, 0)

p = Polynomial([a, d, c, h])
p2 = Polynomial([f, b, e, g])

def main():
    print("\nfirst poly               : ",p.str())
    print(  "             second poly : ",p2.str())
    print(  "           - second poly : ",p2.negative().str())
    print("\nfirst poly + second poly : ",p.addition(p2).str())
    print("\nfirst poly - second poly : ",p.subtraction(p2).str())
    print("\nfirst poly * second poly : ",p.multiplication(p2).str())

if __name__ == '__main__':
    main()
