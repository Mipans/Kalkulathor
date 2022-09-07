# This is the factor class

class Factor:
    def __init__(self, variable:str, degree:float=0):
        self._variable = variable
        self._degree = degree


    # Get values
    def get_degree(self):
        return self._degree

    def get_variable(self):
        return self._variable

    def is_constant(self):
        if self._degree == 0:
            return True
        else:
            return False


    # Turning the object to a string
    def str(self):
        text = ""
        if self.get_degree() == 0:
            return text
        elif self.get_degree() == 1:
            text += self.get_variable()
            return text
        else:
            text += f"{self.get_variable()}^{self.get_degree()}"
            return text
