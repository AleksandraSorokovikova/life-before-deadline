import random

class Manager:
    def __init__(self):
        self.res1 = [0 for _ in range(11)]
        self.res2 = [0 for _ in range(11)]
        self.cur_gamer = 0
        self.in_school = [True, True]

    def throw(self):
        numbers = [1, 2, 3, 4, 5, 6]
        random.shuffle(numbers)
        return numbers

    def re_throw(self, num):
        numbers = [1, 2, 3, 4, 5, 6]
        random.shuffle(numbers)
        return numbers[:num]

    # def get_combinations(self, nums):
    #     d = {'1': -3, '2': -3, '3': -3, '4': -3, '5': -3, '6': -3,
    #          'pair': 0, 'two pair': 0, 'triange': 0, }

