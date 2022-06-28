def count_find_num(primesL, limit):
    base = eval('*'.join(map(str, primesL)))
    rst1 = [base]
    if base > limit:
        return []
    for each in primesL:
        for num in rst1:
            num = num * each
            while num not in rst1 and num <= limit:
                rst1 = rst1 + [num]
                num *= each
    return [len(rst1), max(rst1)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
