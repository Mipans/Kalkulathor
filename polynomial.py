from term import T
class P:
    def __init__(self, *term:T):
        self.terms = list(term)

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
                self.terms.remove(term)

        newTerms = []
        for i in range(len(self.terms)):
            if not self.terms[i].isconstant:
                firstTerm = self.terms[i]
                if i < len(self.terms):
                    for ii in range(i+1, len(self.terms)):
                        secondTerm = self.terms[ii]
                        if firstTerm.factors == secondTerm.factors:
                            firstTerm.coefficient += secondTerm.coefficient
                newTerms.append(firstTerm)
        self.terms = newTerms
        self.terms.append(T(self.constant))


    def string(self):
        text = ""
        for term in self.terms:
            text += " + " + term.string()
        return text.replace(" + ", "", 1)
