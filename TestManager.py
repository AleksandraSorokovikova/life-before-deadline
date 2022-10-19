import unittest
import poker


class MyTestCase(unittest.TestCase):
    def test_something(self):
        manager = poker.Manager()
        self.assertEqual({1, 2, 3, 4, 5, 6}, set(manager.throw()))


if __name__ == '__main__':
    unittest.main()
