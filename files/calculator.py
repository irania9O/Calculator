class Calculator:
    def __init__(self, value = 0):
        #set value to sort in memory
        self.value = value

    def __repr__(self):
        # called when you print Calculator object
        return repr(self.value)
