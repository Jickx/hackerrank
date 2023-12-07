from unittest import TestCase


def time_conversion(time):
    h = int(time[:2])
    if 'AM' in time:
        if h == 12:
            h = 00
    elif 'PM' in time:
        if h != 12:
            h += 12
    hour = str(h).zfill(2)
    return f'{hour}{time[2:-2]}'


class TestTimeConversion(TestCase):
    def test_time_conversion(self):
        self.assertEqual(time_conversion('07:05:45PM'), '19:05:45')
        self.assertEqual(time_conversion('12:00:00AM'), '00:00:00')
        self.assertEqual(time_conversion('12:10:15PM'), '12:10:15')
        self.assertEqual(time_conversion('11:00:00PM'), '23:00:00')
