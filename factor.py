class Factor:
    def __init__(self, variable:str=None, degree:int=1):
        (self.variable, self.degree) = (variable, degree)
        if degree == 0 or variable == None:
            self.isconstant = True
