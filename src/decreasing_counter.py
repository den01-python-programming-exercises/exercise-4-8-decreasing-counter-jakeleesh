class DecreasingCounter:

    def __init__(self,initial_value):
        self.value = initial_value

    def print_value(self):
        print("value: " + str(self.value))

    def decrement(self):
        # write the method implementation here
        # the aim is to decrement the value of the counter by one
        if (self.value > 0):
            self.value -= 1

    # and the other methods go here
    def reset(self):
        self.value = 0
