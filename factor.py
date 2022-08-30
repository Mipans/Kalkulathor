class Factor:
    def __init__(self, variable:str=None, degree:int=1):
        (self.variable, self.degree) = (variable, degree)
        self.isconstant = False
        if degree == 0 or variable == None:
            self.isconstant = True
