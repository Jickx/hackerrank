def grading_students(seq):
    result = []
    for num in seq:
        if num < 38 or num == 100:
            result.append(num)
            continue
        int1 = int(str(num)[0])
        int2 = int(str(num)[1])
        if 8 <= int2 <= 9:
            int1 += 1
            int2 = 0
        elif 3 <= int2 <= 4:
            int2 = 5
        else:
            result.append(num)
            continue
        result.append(int1 * 10 + int2)
    return result


seq = [73, 67, 38, 33]
expected = [75, 67, 40, 33]

print(grading_students(seq))

