# This is the polynomial class

from term import Term
from functions import termify, sort_list_of_terms

class Polynomial:
    def __init__(self, terms:list=[Term(0)]):
        self._terms = []
    
        # Clean the polynomial by collecting the similar terms
        new_terms = dict()
        for term in terms:
            factors = ""
            for factor in term.get_factors():
                factors += factor[0] + str(factor[1])
            coefficient = term.get_coefficient()

            if factors not in new_terms:
                new_terms[factors] = coefficient
            else:
                new_terms[factors] += coefficient

        for fac, coe in new_terms.items():
            if fac != '':
                factors = termify(fac)
            else:
                factors = []
            self._terms.append(Term(coe, factors))
        self._terms = sort_list_of_terms(self._terms).copy()

    # Get values
    def get_terms(self):
        return self._terms

    def get_degree(self):
        d = int(0)
        for t in self.get_terms():
            if t.get_degree() < d:
                d = t.get_degree()
        return d

    def __len__(self):
        return len(self._terms)


    def addition(self, other): # Add two polynomials
        newTerms = dict()
        newList = []
        for term in self.get_terms():
            coefficient = term.get_coefficient()
            factors = ""
            for factor in term.get_factors():
                factors += factor[0] + str(factor[1])

            newTerms[factors] = coefficient

        for term in other.get_terms():
            coefficient = term.get_coefficient()
            factors = ""
            for factor in term.get_factors():
                factors += factor[0] + str(factor[1])

            if factors not in newTerms:
                newTerms[factors] = coefficient
            else:
                newTerms[factors] += coefficient

        for fac, coe in newTerms.items():
            if fac != '':
                factors = termify(fac)
            else:
                factors = []
            newList.append(Term(coe, factors))
        return Polynomial(sort_list_of_terms(newList))


    def multiplication(self, other): # Multiply two polynomials
        newList = []
        for first in range(len(self)):
            firstTerm = self._terms[first]

            for second in range(len(other)):
                secondTerm = other._terms[second]
                
                newList.append(secondTerm.multiplication(firstTerm))
            
        newTerms = dict()
        for term in newList:
            factors = ""
            for factor in term.get_factors():
                factors += factor[0] + str(factor[1])
            coefficient = term.get_coefficient()

            if factors not in newTerms:
                newTerms[factors] = coefficient
            else:
                newTerms[factors] += coefficient

        newList.clear()
        for fac, coe in newTerms.items():
            if fac != '':
                factors = termify(fac)
            else:
                factors = []
            newList.append(Term(coe, factors))
        return Polynomial(sort_list_of_terms(newList))


    def negative(self): # Multiply a polynomial with -1
        n = Polynomial([Term(-1)])
        return self.multiplication(n)


    def subtraction(self, other): # Subtract two polynomials
        return self.addition(other.negative())


    def str(self): # Turn the object to a string
        text = ""
        for i in range(len(self)):
            term = self.get_terms()[i]
            if term.get_coefficient() < 0:
                text += " - " + term.str().replace("-", "")
            else:
                text += " + " + term.str()
                if i == 0 and term.get_coefficient() > 0:
                    text.replace(" + ", "")
        return text
