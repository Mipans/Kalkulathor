# This is the polynomial class

from term import Term
class Polynomial:
    def __init__(self, terms:list):
        self._terms = terms
        self._new_terms = dict()

        # Clean the polynomial by adding the similar terms
        for first in range(len(self)):
            firstTerm = self._terms[first]

            if firstTerm.get_degree() not in self._new_terms:
                self._new_terms[firstTerm.get_degree()] = firstTerm.get_coefficient()
            else:
                self._new_terms[firstTerm.get_degree()] += firstTerm.get_coefficient()

        self._terms.clear()
        for d, c in self._new_terms.items():
            self._terms.append(Term(c, d))
        self._new_terms.clear()


    def addition(self, other): # Add two polynomials
        newTerms = dict()
        newList = []
        for first in range(len(self)):
            firstTerm = self._terms[first]

            if firstTerm.get_degree() not in newTerms:
                newTerms[firstTerm.get_degree()] = firstTerm.get_coefficient()

        for second in range(len(other)):
            secondTerm = other._terms[second]
        
            if secondTerm.get_degree() not in newTerms:
                newTerms[secondTerm.get_degree()] = secondTerm.get_coefficient()
            else:
                newTerms[secondTerm.get_degree()] += secondTerm.get_coefficient()

        for d, c in newTerms.items():
            newList.append(Term(c, d))
        return Polynomial(newList)
    

    def multiplication(self, other): # Multiply two polynomials
        newTerms = dict()
        newList = []
        for first in range(len(self)):
            firstTerm = self._terms[first]

            for second in range(len(other)):
                secondTerm = other._terms[second]

                degree = firstTerm.get_degree() + secondTerm.get_degree()
                coefficient = firstTerm.get_coefficient() * secondTerm.get_coefficient()
                if degree not in newTerms:
                    newTerms[degree] = coefficient
                else:
                    newTerms[degree] += coefficient

        for d, c in newTerms.items():
            newList.append(Term(c, d))
        return Polynomial(newList)
    

    def negative(self): # Multiply a polynomial with -1
        n = Polynomial([Term(-1)])
        return self.multiplication(n)


    def subtraction(self, other): # Subtract two polynomials
        return self.addition(other.negative())


    def str(self): # Turn the polynominal to a string
        text = ""
        for term in self._terms:
            text += f" + {term.str()}"
        text = text.replace(" + ", "", 1)
        return text
    

    def get_terms(self): # Returns a list of Term objects
        return self._terms
    
    def get_degree(self):
        d = int(0)
        for t in self.get_terms():
            if t.get_degree() < d:
                d = t.get_degree()
        return d

    def __len__(self):
        return len(self._terms)
