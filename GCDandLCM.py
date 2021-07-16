def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def take_lcm(a, b):
    return a * b // gcd(a, b)


def lcm(a, b):
    number_lcm = take_lcm(a[1], b[1])
    self_lcm = int(number_lcm / a[1])
    other_lcm = int(number_lcm / b[1])
    return (list(map(lambda x: x * self_lcm, a)),
            list(map(lambda x: x * other_lcm, b)))
