from math import log10, sqrt, pow, sin, exp, log, sin, cos, tan, factorial


class Calculator:
    def __init__(self, value=0):
        # Set value to sort in memory.
        self.value = value

    def __repr__(self):
        # To get alled when you print Calculator object.
        return repr(self.value)

    def checker(self, value):
        # Check if value is float or integer.
        if isinstance(value, (int, float)):
            return True
        else:
            raise ValueError(f"{value} is not integer or float.")

    def __iadd__(self, value):
        # To get called on addition with assignment e.g. a +=b.
        if self.checker(value):
            self.value += value
            return Calculator(self.value)

    def __isub__(self, value):
        # To get called on subtraction with assignment e.g. a -=b.
        if self.checker(value):
            self.value -= value
            return Calculator(self.value)

    def __imul__(self, value):
        # To get called on multiplication with assignment e.g. a *=b.
        if self.checker(value):
            self.value *= value
            return Calculator(self.value)

    def __itruediv__(self, value):
        # To get called on division with assignment e.g. a /=b.
        if self.checker(value):
            self.value /= value
            return Calculator(self.value)

    def __ipow__(self, value=2):
        # To get called on exponentswith assignment e.g. a **=b.
        if self.checker(value):
            self.value = pow(self.value, value)
            return Calculator(self.value)

    def log10(self):
        # Calculation of logarithm in base 10.
        self.value = log10(self.value)
        return Calculator(self.value)

    def sqrt_2(self):
        # Calculate the square root
        self.value = sqrt(self.value)
        return Calculator(self.value)

    def ten_pow(self):
        # Ten to the power of self.value
        self.value = pow(10, self.value)
        return Calculator(self.value)

    def sqrt_n(self, value):
        # Calculate the n root
        self.value = round(exp(log(self.value) / value), 10)
        return Calculator(self.value)

    def exp(self):
        # Calculate e raised to the power self.value
        self.value = exp(self.value)
        return Calculator(self.value)

    def sin(self):
        # Calculate the sine of self.value radians.
        self.value = sin(self.value)
        return Calculator(self.value)

    def cos(self):
        # Calculate the cosine of self.value radians.
        self.value = cos(self.value)
        return Calculator(self.value)

    def tan(self):
        # Calculate the tangent of self.value radians.
        self.value = tan(self.value)
        return Calculator(self.value)

    def negate(self):
        # negates
        self.value *= -1
        return Calculator(self.value)

    def factorial(self):
        # Calculate self.value factorial as an integer Raises ValueError if x is not integral or is negative.
        self.value = factorial(self.value)
        return Calculator(self.value)
