from factor import F
class T:
    def __init__(self, coefficient:int=1, *factor:F):
        self.coefficient = coefficient
        self.factors = set(factor)

        self.isconstant = True
        for factor in self.factors:
            if not factor.isconstant:
                self.isconstant = False
    
    def addition(self, other):
        if self.factors == other.factors:
            self.coefficient += other.coefficient
            return self
        else:
            return None

    def string(self):
        t = ""
        if self.coefficient != 1:
            t = str(self.coefficient)
        for factor in self.factors:
            t += factor.string()
        return t
