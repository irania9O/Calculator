class Calculator:
    def __init__(self, value = 0):
        #Set value to sort in memory.
        self.value = value

    def __repr__(self):
        #To get alled when you print Calculator object.
        return repr(self.value)
    
    def checker(self, value):
        #Check if value is float or integer.
        if isinstance(value, (int, float)):
            return True
        else:
            raise ValueError(f"{value} is not integer or float.")
        
    def __iadd__(self, value):
        #To get called on addition with assignment e.g. a +=b.
        if self.checker(value):
            self.value += value
            return Calculator(self.value)
            
    def __isub__(self, value):
        #To get called on subtraction with assignment e.g. a -=b.
        if self.checker(value):
            self.value -= value
            return Calculator(self.value)
      
    def __imul__(self, value):
        #To get called on multiplication with assignment e.g. a *=b.
        if self.checker(value):
            self.value *= value
            return Calculator(self.value)
        
    def __itruediv__(self, value):
        #To get called on division with assignment e.g. a /=b.
        if self.checker(value):
            self.value /= value
            return Calculator(self.value)

        
