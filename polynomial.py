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

        if len(self.get_terms()) == 0:
            self._terms.append(Term(0))

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


    def derivative(self, variable:str): # Take the derivative of a Polynomial
        newTerms = []
        for term in self.get_terms():
            newCoefficient = term.get_coefficient()
            newFactors = []
            yes = False
            for factor in term.get_factors():
                if factor[0] != variable:
                    newFactors.append(factor)
                else:
                    yes = True
                    newCoefficient *= factor[1]
                    newFactors.append((factor[0], factor[1]-1))
            if yes:
                newTerms.append(Term(newCoefficient, newFactors))
        return Polynomial(newTerms)


    def __str__(self): # Turn the object to a string
        text = ""
        for i in range(len(self)):
            term = self.get_terms()[i]
            if term.get_coefficient() < 0:
                text += " - " + str(term).replace("-", "")
            else:
                if i > 0:
                    text += " + " + str(term)
                else:
                    text += str(term)
        return text
