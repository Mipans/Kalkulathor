# This is the main file

from term import Term
from polynomial import Polynomial


a = Term(-2, [("y",2), ("x",3)])
b = Term(1,  [("x",2)])
c = Term(0,  [("x",1), ("y",3)])
d = Term(1,  [("y",1), ("x",1), ("x",3)])
e = Term(2,  [("x",3)])
f = Term(-3, [])

myList = [a, b, d, e, f]

poly1 = Polynomial([a, d, f, Term(16)])
poly2 = Polynomial([b, c, e, Term(-5)])

def main():
    print("\npoly1 : " + str(poly1))
    print("poly2 : " + str(poly2))
    print("\npoly1 + poly2 = " + str(poly1.addition(poly2)))
    print("\npoly1 * poly2 = " + str(poly1.multiplication(poly2)) + "\n")
    print("derivative of poly1 based on x = " + str(poly1.derivative("x")))
    print("derivative of poly1 based on y = " + str(poly1.derivative("y")))
    print("derivative of poly2 based on x = " + str(poly2.derivative("x")))
    print("derivative of poly2 based on y = " + str(poly2.derivative("y")))
    while True:
        continue


if __name__ == '__main__':
    main()
