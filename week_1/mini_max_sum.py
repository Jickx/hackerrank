def mini_max_sum(arr):
    arr_sum = sum(arr)
    result = []
    for i in arr:
        result.append(arr_sum - i)

    print(min(result), max(result))


arr = [1, 2, 3, 4, 5]
print(mini_max_sum(arr))
