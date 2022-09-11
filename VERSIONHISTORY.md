# v0.3.4

* Intruduced derivative method to Polynomials
    - It takes in a string which represents the variable as input and returns the derivative of the polynomial for the given variable


# v0.3.3

* Intruduced version history (hey :D)

* Renamed ".str()" methods as ".\_\_str\_\_()" (why haven't i done this since v.0.1.1 ...)


# v0.3.2

* Intruduced "sort\_list\_of\_terms()"
    - It sorts a list of terms alphabethically according to the Terms variables

* Deleted Factors.
    - *Little sad violing starts playing*


# v0.3.1

* Renamed some variables in the Term class.


# v0.3.0

* Reintruduced Factors *(unused)*
    - Each Factor object has a variable and a degree.
    - ".get\_degree()" method returns the degree of the Factor
    - ".get\_variable()" method returns the variable of the Factor
    - ".is\_constant()" method retuns True if the degree is 0. False othervise
    - ".str()" method returns a string form of it's Term

* Added some functions in "functions.py" file
    - "numify(letter)" function takes in a string that is only one letter long and returns it's index on the alphabeth (that start's with x and ends with w).
    - "score(input)" function takes in a string and returns it's alphabethical score. The higher the score the latter it is.
    - "sort\_list\_of\_strings" function takes in a list and sorts it according to the score() value of it's items.
    - "termify(facc)" function takes in a string like "x4y7z93" and turns it into a list of tuples like [("x", 4), ("y", 7), ("z", 93)]

* Tweaked Terms
    - Now each Term has a coefficient and a list of tuples that represent it's factors. 
    - If two or factors with the same variable was passed in while initializing the Term it sums the degrees of them into one factor.
    - Intruduced ".get\_factors()" method which returns a list of factors represented in tuples.
    - Intruduced ".\_\_len\_\_()" method which returns the number of factors.
    - ".get\_degree()" method now retunrs the sum of all degrees of the Terms factors.
    - Intruduced ".multiplication()" method which takes in another Term as input and returns a Term with the coefficient and factors of multiplication of previous Terms.
    - Intruduced ".negative()" method which multiplies the Term with -1

* Tweaked Polynomials
    - Polynomials now support poly-variabled terms.


    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# v0.2.0

* Added special thanks

* Added proper commenting

* Removed poly-variabled terms
    - Now each Term object has a coefficient and a degree. Every term has the same variable (x).

* Polynomials now support addition, subtraction and multiplication
    - The addition method takes in another Polynomial as input and sums the coefficients of the Terms that has the same degree. If a Terms has unique degree then they get passed in without any modification.
    - The multiplication method takes in another Polynomial as input and multiplies each Terms of both Polynomials. If there are Terms with same degrees they get summed.
    - The negative method multiplies a Polynomial by -1.
    - The subtraction method takes in another Polynomial as input and adds the negative of the input Polynomial.

* Added "get" methods to Polynomials
    - ".\_\_len\_\_()" method retuns the number of Terms

* Added "get" methods to Terms
    - ".get\_degree()" method retuns the degree of the Term
    - ".get\_coefficient()" method retuns the constant of the Term
    - ".is\_constant()" method retuns True if the degree is 0. False othervise


    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# v0.1.2

* Added ".string()" method to Factors
    - The string method returns a string form of it's Factor

* Added ".string()" method to Terms

    - The string method returns a string form of it's Term
* Terms now support addition
    - The addition method takes in another Term as input and sums the coefficients if the factors are the same. 

* Tweaked logic of polynomials
    - The Polynomial will now sum the coefficients of Terms that has the same factors.


# v0.1.1

* Renamed "equations" to "polynomials"

* Polynomials now have some properties
    - Each Polynomial has a list of Terms.

* Added "string" method to polynomials
    - The string method returns a string form of it's Polynomial


# v0.1.0

* Intruduced factors
    - Each Factor object has a variable and a degree. For example x^4 or y^7 or z^93 are factors
    - If a Factor doesn't have a variable or has a degree of 0 then it is a constant

* Intruduced terms
    - Each Term object has a coefficient and a list of Factors. For example 4x^4 or -4/5y^7z^93 are Terms

* Intruduced equations (doesn't have any properties yet)
    - equations are just a list of Terms
