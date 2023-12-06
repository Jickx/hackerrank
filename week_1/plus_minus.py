#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plus_minus(arr):
    # Write your code here
    pos = len([i for i in arr if i > 0]) / len(arr)
    neg = len([i for i in arr if i < 0]) / len(arr)
    zero = len([i for i in arr if i == 0]) / len(arr)

    print(f'{pos:.5f}')
    print(f'{neg:.5f}')
    print(f'{zero:.5f}')


arr = [-4, 3, -9, 0, 4, 1]

plus_minus(arr)
