import unittest
from main import sample_mul_func


class Another_Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiple_default(self):
        assert sample_mul_func() == 0

    def test_multiple_a5b7(self):
        assert sample_mul_func(a=5, b=7) == 35


if __name__ == '__main__':
    unittest.main()
