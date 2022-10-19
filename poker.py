import random

class Manager:
    def __init__(self):
        self.res1 = [0 for _ in range(11)]
        self.res2 = [0 for _ in range(11)]
        self.curGamer = 0

    def throw(self):
        numbers = [1, 2, 3, 4, 5, 6]
        random.shuffle(numbers)
        return numbers