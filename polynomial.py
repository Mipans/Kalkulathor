from term import Term
class Polynomial:
    def __init__(self, *term:Term):
        self.terms = term

        self.degree = 0
        self.constant = 0
        for term in self.terms:
            d = 0
            for factor in term.factors:
                d += factor.degree
            if d >= self.degree:
                self.degree = d
            if term.isconstant:
                self.constant += term.coefficient
    
    def string(self):
        text = ""
        for term in self.terms:
            text += " + " + str(term.coefficient)
            t = ""
            for factor in term.factors:
                t += factor.variable + "^" + str(factor.degree)
            text += t
        return text.replace(" + ", "", 1)