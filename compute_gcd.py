
def computeGCD(x, y):

    while y:
        x, y = y, x % y

    return x

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)



if a % b == 0: gcd(a, b) = b
if a = bt + r for integers t and r, then gcd(a, b) = gcd(b, r)
