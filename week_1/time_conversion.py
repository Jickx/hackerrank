from unittest import TestCase


def time_conversion(time):
    h, m, s = time.split(':')
    if s[2:] == 'AM':
        return f'00:{m}:{s[:-2]}' if h == '12' else f'{h}:{m}:{s[:-2]}'
    else:
        return f'{int(h)}:{m}:{s[:-2]}' if h == '12' else f'{int(h) + 12}:{m}:{s[:-2]}'


class TestTimeConversion(TestCase):
    def test_time_conversion(self):
        self.assertEqual(time_conversion('07:05:45PM'), '19:05:45')
        self.assertEqual(time_conversion('12:00:00AM'), '00:00:00')
        self.assertEqual(time_conversion('12:10:15PM'), '12:10:15')
        self.assertEqual(time_conversion('11:00:00PM'), '23:00:00')
