def hcf(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    lccm_1 = (x * y) // hcf(x, y)
    return lccm_1


print(hcf(24, 54))
print(lcm(24, 54))
