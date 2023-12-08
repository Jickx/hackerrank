def matching_strings():
    result = []
    for i in queries:
        ctr = 0
        for j in strings:
            if i == j:
                ctr += 1
        result.append(ctr)
    return result


strings= ['aba','baba','aba','xzxb']
queries = ['aba', 'xzxb', 'ab']
expected = [2, 1, 0]

print(matching_strings())