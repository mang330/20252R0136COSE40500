def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)

if __name__ == "__main__":
    print(gcd(24, 18))
    print(lcm(24, 18))
