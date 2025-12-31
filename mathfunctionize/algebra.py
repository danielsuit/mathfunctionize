import arithmetic
def algebraGamma(x):
    if x == 0 or (x < 0 and x % 1 == 0):
        raise Exception("Invalid input")
    if x == 1:
        return 1
    if x == 0.5:
        return algebraSquareRoot(3.141592653589793)
    return (x - 1) * algebraGamma(x - 1)
def algebraFactorial(x):
    if x == 0:
        return 1
    else:
        return x * algebraFactorial(x-1)
def algebraAbsolute(x):
    if x < 0:
        return -x
    else:
        return x
def algebraSquareRoot(x):
    return x ** (1/2)
def algebraCubeRoot(x):
    return x ** (1/3)
def algebraNthRoot(x, n):
    return x ** (1/n)
def algebraRound(x, place):
    if (place > 0 and arithmetic.arithmeticModulo(place, 10) == 0) or (place == 1):
        if arithmetic.arithmeticModulo(x, place) < (arithmetic.arithmeticMultiplication(0.5, place)):
            return arithmetic.arithmeticFlatDivision(x, place)
    return arithmetic.arithmeticFlatDivision(x, place) + place