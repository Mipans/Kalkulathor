from factor import Factor
class Term:
    def __init__(self, coefficient:int=1, *factor:Factor):
        self.coefficient = coefficient
        self.factors = factor

        self.isconstant = True
        for factor in self.factors:
            if not factor.isconstant:
                self.isconstant = False
