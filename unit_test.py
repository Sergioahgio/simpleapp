from main import sample_sub_func, sample_sum_func
import unittest


class Sample_Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sum_noInput(self):
        result = sample_sum_func()
        assert result == 0

    def test_sum_withInput(self):
        result = sample_sum_func(a=1, b=3)
        assert result == 4

    def test_sub_noInput(self):
        result = sample_sub_func()
        assert result == 0

    def test_sub_withInput(self):
        result = sample_sub_func(a=4, b=2)
        assert result == 2


if __name__ == '__main__':
    unittest.main()
