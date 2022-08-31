# This is the term class

class Term:
    def __init__(self, coefficient:float, degree:float=0):
        self._coefficient = coefficient
        self._degree = degree

    # Turning the object to a string
    def str(self):
        text = ""
        if self._coefficient != 1:
            text = str(self._coefficient)
        if self._degree == 0:
            return text
        elif self._degree == 1:
            text += "x"
            return text
        else:
            text += f"x^{self._degree}"
            return text

    # Get values
    def get_degree(self):
        return self._degree

    def get_coefficient(self):
        return self._coefficient

    def is_constant(self):
        if self._degree == 0:
            return True
        else:
            return False
