import unittest
import poker


class MyTestCase(unittest.TestCase):
    def test_throwing(self):
        manager = poker.Manager()
        self.assertEqual({1, 2, 3, 4, 5, 6}, set(manager.throw()))

        res = set(manager.re_throw(3))
        self.assertTrue(res.issubset({1, 2, 3, 4, 5, 6}))

    def test_combinations(self):
        manager = poker.Manager()
        res = manager.throw()
        combs = manager.get_combinations([3, 3, 4, 5, 5])
        self.assertEqual({'1': -3, '2': -3, '3': -1, '4': -2, '5': -1, '6': -3,
                          'pair': 20, 'two pair': 32, 'triange': 0, 'small street': 0, 'big street': 0}, combs)

        res = manager.re_throw(3)
        combs = manager.get_combinations([3, 3, 4, 5, 5])
        self.assertEqual({'1': -3, '2': -3, '3': -1, '4': -2, '5': -1, '6': -3,
                          'pair': 10, 'two pair': 16, 'triange': 0, 'small street': 0, 'big street': 0}, combs)

        combs = manager.get_combinations([1, 2, 3, 4, 5])
        self.assertEqual({'1': -2, '2': -2, '3': -2, '4': -2, '5': -2, '6': -3,
                          'pair': 0, 'two pair': 0, 'triange': 0, 'small street': 14, 'big street': 15}, combs)


if __name__ == '__main__':
    unittest.main()
