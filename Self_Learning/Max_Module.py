class Max :
    def __init__(self,numbers):
        self.numbers = numbers  
    def maxx(self) :
        max_number = self.numbers[0]
        for number in self.numbers :
            if number > max_number :
                max_number = number
        return max_number
