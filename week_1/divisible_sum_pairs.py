from unittest import TestCase


def divisible_sum_pairs(k, ar):
    result = 0
    while len(ar) > 0:
        i = ar.pop()
        for j in ar:
            if (i + j) % k == 0:
                result += 1
    return result


class TestDivisibleSumPair(TestCase):
    def test_divisible_sum_pairs(self):
        self.assertEqual(divisible_sum_pairs(5, [1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(divisible_sum_pairs(3, [1, 3, 2, 6, 1, 2]), 5)
        self.assertEqual(divisible_sum_pairs(1, [1, 1]), 1)
