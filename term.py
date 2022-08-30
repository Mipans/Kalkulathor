from factor import Factor
class Term:
    def __init__(self, coefficient:int=1, *args:Factor):
        self.coefficient = coefficient
        self.factors = args
