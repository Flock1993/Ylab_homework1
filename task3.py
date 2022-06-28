def zeros(n):
    total = 0
    i = 1
    while (n > 0) and (n/(5**i) >= 1):
        total += int(n/(5**i))
        i += 1
    return total


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
