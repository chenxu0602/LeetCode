
def computeGCD(x, y):

    while y:
        x, y = y, x % y

    return x

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
