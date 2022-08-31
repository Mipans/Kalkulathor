from factor import F
from term import T
from polynomial import P

polynomial1 = P(T(1, F("x", 2)), T(4, F("x")), T(4))

polynomial2 = P(T(1, F("x", 2)), T(4), T(2, F("x")), T(3, F("x")), T(6))


def main():
    print(f"""
                polinom 1 : {polynomial1.string()}
    polinom 1'in derecesi : {str(polynomial1.degree)}
polinom 1'in sabit terimi : {str(polynomial1.constant)}
                polinom 2 : {polynomial2.string()}
    polinom 2'in derecesi : {str(polynomial2.degree)}
polinom 2'in sabit terimi : {str(polynomial2.constant)}
""")

if __name__ == '__main__':
    main()