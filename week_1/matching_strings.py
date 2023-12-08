def matching_strings():
    result = []
    strings_dict = {i: 0 for i in set(strings)}
    for i in strings:
        strings_dict[i] += 1
    for i in queries:
        if i in strings_dict:
            result.append(strings_dict[i])
        else:
            result.append(0)
    return result


strings = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj',
           'asdjf']
queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
expected = [1, 3, 4, 3, 2]

print(matching_strings())
