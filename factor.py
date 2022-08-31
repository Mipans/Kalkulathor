class F:
    def __init__(self, variable:str=None, degree:int=1):
        (self.variable, self.degree) = (variable, degree)
        self.isconstant = False
        if degree == 0 or variable == None:
            self.isconstant = True

    def string(self):
        if self.degree == 0:
            text = ""
        elif self.degree == 1:
            text = self.variable
        else:
            text = self.variable + "^" + str(self.degree)
        return text
