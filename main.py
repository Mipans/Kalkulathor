# This is the main file

from term import *
from polynomial import Polynomial


a = Term(-2, [("y",2), ("x",3)])
b = Term(1,  [("x",2)])
c = Term(0,  [("x",1), ("y",3)])
d = Term(1,  [("y",1), ("x",1), ("x",3)])
e = Term(2,  [("x",3)])
f = Term(-3, [])

myList = [a, b, d, e, f]
numbers = [-5, 2, 1, -26, 9, -2]

poly1 = Polynomial([a, d, f, Term(16)])
poly2 = Polynomial([b, c, e, Term(-5)])

def main():
    print("poly1 : " + poly1.str())
    print("poly2 : " + poly2.str())
    print("\npoly1 + poly2 = " + poly1.addition(poly2).str())
    print("\npoly1 * poly2 = " + poly1.multiplication(poly2).str())

if __name__ == '__main__':
    main()
