from unittest import TestCase
import re


def parse_line(line):
    string = re.split(r'(?<=[a-z])(?=[A-Z])|\s', line.strip('()'))
    return [i.lower() for i in string]


def format_line(line_list, operation, type_of):
    if operation == 'S':
        return ' '.join(line_list)
    if type_of == 'C':
        return ''.join([i.capitalize() for i in line_list])
    line_str = ''.join([i.capitalize() for i in line_list])
    if type_of == 'M':
        return line_str[0].lower() + line_str[1:] + '()'
    elif type_of == 'V':
        return line_str[0].lower() + line_str[1:]


def camel_case(data):
    result = []
    data_list = data.split('\n')
    for line in data_list:
        if line == '':
            result.append('')
            continue
        operation, type_of, split_line = line.split(';')
        parsed_line = parse_line(split_line)
        formatted_line = format_line(parsed_line, operation, type_of)
        result.append(formatted_line)
    return '\n'.join(result)


data = """
C;V;can of coke
S;M;sweatTea()
S;V;epsonPrinter
C;M;santa claus
C;C;mirror
"""

expected = """
canOfCoke
sweat tea
epson printer
santaClaus()
Mirror
"""

print(camel_case(data))


class TestCamelCase(TestCase):
    def test_parse(self):
        self.assertEqual(parse_line('plasticCup()'),
                         ['plastic', 'cup'])
        self.assertEqual(parse_line('LargeSoftwareBook'),
                         ['large', 'software', 'book'])
        self.assertEqual(parse_line('mobile phone'),
                         ['mobile', 'phone'])
        self.assertEqual(parse_line('LargeSoftwareBook'),
                         ['large', 'software', 'book'])

    def test_format(self):
        self.assertEqual(format_line(['plastic', 'cup'],
                                     'S', 'M'), 'plastic cup')
        self.assertEqual(format_line(['coffee', 'machine'],
                                     'C', 'C'), 'CoffeeMachine')
        self.assertEqual(format_line(['large', 'software', 'book'],
                                     'S', 'C'), 'large software book')

    def test_camel_case(self):
        self.assertEqual(camel_case(data), expected)
