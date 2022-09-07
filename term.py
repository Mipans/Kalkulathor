# This is the term class

from functions import sort_list_of_strings


class Term:
    def __init__(self, coefficient:float=0, factors:list=[]):
        self._coefficient = coefficient
        self._factors = list()

        if self.get_coefficient() == 0:
            self._factors.clear()
        else:
        # Cleaning the term by collecting the similar factors
            _newFactors = dict()
            for factor in factors:
                var = factor[0]
                deg = factor[1]

                if var not in _newFactors:
                    _newFactors[var] = deg
                else:
                    _newFactors[var] += deg

            for v, d in _newFactors.items():
                if d != 0:
                    self._factors.append((v, d))
            self._factors = sort_list_of_strings(self._factors).copy()



    # Get values
    def get_factors(self): # Returns a list of factors as tuples
        return self._factors

    def get_coefficient(self): # Returns the coefficient as a float
        return self._coefficient

    def __len__(self): # Returns the amount of factors as an integer
        return len(self.get_factors())

    def get_degree(self): # Returns the sum of the degrees of all factors
        d = 0
        for factor in self.get_factors():
            for degree in factor[1]:
                d += degree
        return d

    def is_constant(self): # Returns True if the term has no factors, else returns False
        if len(self) == 0:
            return True
        else:
            return False


    # Returns the multiplication of the term with another term
    def multiplication(self, multiplier):
        oldFactors = dict()
        newFactors = list()
        if isinstance(multiplier, Term):
            coe = (self.get_coefficient(), multiplier.get_coefficient())
            for v, d in self.get_factors():
                oldFactors[v] = d

            for factor in multiplier.get_factors():
                var = factor[0]
                deg = factor[1]

                if var not in oldFactors:
                    oldFactors[var] = deg
                else:
                    oldFactors[var] += deg

            for v, d in oldFactors.items():
                newFactors.append((v, d))
            return Term(coe[0]*coe[1], sort_list_of_strings(newFactors))

        elif isinstance(multiplier, (float, int)):
            return Term(self.get_coefficient()*multiplier, self.get_factors())

    def negative(self):
        return Term(self.get_coefficient()*(-1), self.get_factors())


    # Turning the object to a string
    def str(self):
        if self.get_coefficient() == 0:
            return "0"
        elif self.get_coefficient() == 1:
            if len(self) != 0:
                text = ""
            else:
                text = "1"
        elif self.get_coefficient() == -1:
            if len(self) != 0:
                text = "-"
            else:
                text = "-1"
        else:
            text = str(self.get_coefficient())
        for var, deg in self.get_factors():
            if deg == 0:
                text += ""
            elif deg == 1:
                text += var
            else:
                newDeg, subScripts = "", ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
                for d in str(deg):
                    newDeg += subScripts[int(d)]
                text += var + newDeg
        return text

one = Term(1)
