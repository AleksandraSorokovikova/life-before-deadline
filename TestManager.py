import unittest
import poker


class MyTestCase(unittest.TestCase):
    def test_throwing(self):
        manager = poker.Manager()
        self.assertEqual({1, 2, 3, 4, 5, 6}, set(manager.throw()))

        res = set(manager.re_throw(3))
        self.assertTrue(res.issubset({1, 2, 3, 4, 5, 6}))


if __name__ == '__main__':
    unittest.main()
