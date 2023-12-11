from unittest import TestCase


def breaking_records(scores):
    result = [0, 0]
    maxim = minim = scores[0]
    for i in scores:
        if i > maxim:
            result[0] += 1
            maxim = i
        elif i < minim:
            result[1] += 1
            minim = i
    return result


class TestBreakingRecords(TestCase):
    def test_breaking_records(self):
        self.assertEqual(breaking_records(
            [10, 5, 20, 20, 4, 5, 2, 25, 1]), [2, 4]
        )
        self.assertEqual(breaking_records(
            [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), [4, 0]
        )
