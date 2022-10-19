import random
from multiset import *

class Manager:
    def __init__(self):
        self.res1 = [0 for _ in range(11)]
        self.res2 = [0 for _ in range(11)]
        self.cur_gamer = 0
        self.in_school = [True, True]
        self.is_first_try = None

    def throw(self):
        self.is_first_try = True
        return [random.randint(1, 6) for _ in range(5)]

    def re_throw(self, num):
        self.is_first_try = False
        return [random.randint(1, 6) for _ in range(num)]

    def get_combinations(self, nums):
        d = {'1': -3, '2': -3, '3': -3, '4': -3, '5': -3, '6': -3,
             'pair': 0, 'two pair': 0, 'triange': 0, 'small street': 0, 'big street': 0}

        for_multiset = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

        for n in nums:
            d[str(n)] += 1
            for_multiset[n] += 1

        nums = Multiset(nums)
        if Multiset({1: 2}).issubset(nums):
            d['pair'] = 2
        if Multiset({2: 2}).issubset(nums):
            if d['pair'] != 0:
                d['two pair'] = d['pair'] + 4
            d['pair'] = 4
        if Multiset({3: 2}).issubset(nums):
            if d['pair'] != 0:
                d['two pair'] = d['pair'] + 6
            d['pair'] = 6
        if Multiset({4: 2}).issubset(nums):
            if d['pair'] != 0:
                d['two pair'] = d['pair'] + 8
            d['pair'] = 8
        if Multiset({5: 2}).issubset(nums):
            if d['pair'] != 0:
                d['two pair'] = d['pair'] + 10
            d['pair'] = 10
        if Multiset({6: 2}).issubset(nums):
            if d['pair'] != 0:
                d['two pair'] = d['pair'] + 12
            d['pair'] = 12

        if Multiset({1: 3}).issubset(nums):
            d['triange'] = 3
        if Multiset({2: 3}).issubset(nums):
            d['triange'] = 6
        if Multiset({3: 3}).issubset(nums):
            d['triange'] = 9
        if Multiset({4: 3}).issubset(nums):
            d['triange'] = 12
        if Multiset({5: 3}).issubset(nums):
            d['triange'] = 15
        if Multiset({6: 3}).issubset(nums):
            d['triange'] = 18

        if Multiset({1: 1, 2: 1, 3: 1, 4: 1}).issubset(nums):
            d['small street'] = 10
        if Multiset({2: 1, 3: 1, 4: 1, 5: 1}).issubset(nums):
            d['small street'] = 14
        if Multiset({3: 1, 4: 1, 5: 1, 6: 1}).issubset(nums):
            d['small street'] = 18

        if Multiset({1: 1, 2: 1, 3: 1, 4: 1, 5: 1}).issubset(nums):
            d['big street'] = 15
        if Multiset({2: 1, 3: 1, 4: 1, 5: 1, 6: 1}).issubset(nums):
            d['big street'] = 20

        for key in d:
            if d[key] > 0 and self.is_first_try:
                d[key] *= 2

        return d
