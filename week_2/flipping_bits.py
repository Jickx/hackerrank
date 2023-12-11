def flipping_bits(seq):
    result = []
    for num in seq:
        bin_num = str(bin(num)[2:].zfill(32))
        invert_num = ''.join(['0' if i == '1' else '1' for i in bin_num])
        result.append(int(invert_num, 2))
    return result


seq = [2147483647, 1, 0]
expected = [2147483648, 4294967294, 4294967295]

assert (flipping_bits(seq)) == expected
