# constants
pi = 3.141592653589793
e = 2.718281828459045
# arithmetic
def addition(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result += arr[i]
    return result
def subtraction(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result -= arr[i]
    return result
def multiplication(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= arr[i]
    return result
def division(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result /= arr[i]
    return result
def power(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result **= arr[i]
    return result
def modulo(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result %= arr[i]
    return result
def flatDivision(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result //= arr[i]
    return result
# algebra
def gamma(x):
    if x == 0 or (x < 0 and x % 1 == 0):
        raise Exception("Invalid input")
    if x == 1:
        return 1
    if x == 0.5:
        return squareRoot(pi)
    return (x - 1) * gamma(x - 1)
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
def absolute(x):
    if x < 0:
        return -x
    else:
        return x
def squareRoot(x):
    return x ** (1/2)
def cubeRoot(x):
    return x ** (1/3)
def nthRoot(x, n):
    return x ** (1/n)
def round(x, place):
    if (place > 0 and modulo([place, 10]) == 0) or (place == 1):
        if modulo([x, place]) < (multiplication([0.5, place])):
            return flatDivision([x, place])
    return flatDivision([x, place]) + place
# counting
def combinations(n, r):
    return division([permutations(n, r), factorial(r)])
def permutations(n, r):
    return division([factorial(n), factorial(n - r)])
def circularPermutations(n):
    if n == 0:
        return 1
    return factorial(n - 1)
def derangements(n):
    res = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            res -= (1 / factorial(i))
            continue
        res += (1 / factorial(i))
    return int(factorial(n) * res)
# probability
def bayes_theorem(priorA, priorB, likelihoodA, likelihoodB):
    return (priorA * likelihoodA) / ((priorA * likelihoodA) + (priorB * likelihoodB))
def uniformPDF(a, b):
    return 1 / (b - a)
def uniformCDF(X, a, b):
    if X < a:
        return 0
    if X > b:
        return 1
    return (X - a) / (b - a)
def normalPDF(X, mean, stdDev):
    coeff = 1 / (stdDev * ((2 * pi) ** 0.5))
    exponent = -0.5 * (((X - mean) / stdDev) ** 2)
    return coeff * (e ** exponent)
def normalCDF(x, mean, stdDev):
    z = (x - mean) / stdDev
    t = 1 / (1 + 0.2316419 * absolute(z))
    d = 0.3989423 * e ** (-z * z / 2)
    prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))))
    if z > 0:
        prob = 1 - prob
    return prob
def gammaPDF(x, a, b):
    return (1/gamma(a))*power([b*x, a/x])*power([e, -b*x])
# complex numbers
def complex_addition(a, b):
    if a.find("+") != -1:
        a1 = float(a[0:a.find("+")])
        a2 = float(a[a.find("+")+1:a.find("i")])
    elif a.find("-", 1) != -1:
        a1 = float(a[0:a.find("-", 1)])
        a2 = float(a[a.find("-", 1):a.find("i")])
    elif a.find("i") != -1:
        a1 = 0
        a2 = float(a[0:a.find("i")])
    elif a.find("i") == -1:
        a1 = float(a)
        a2 = 0
    if b.find("+") != -1:
        b1 = float(b[0:b.find("+")])
        b2 = float(b[b.find("+")+1:b.find("i")])
    elif b.find("-", 1) != -1:
        b1 = float(b[0:b.find("-", 1)])
        b2 = float(b[b.find("-", 1):b.find("i")])
    elif b.find("i") != -1:
        b1 = 0
        b2 = float(b[0:b.find("i")])
    elif b.find("i") == -1:
        b1 = float(b)
        b2 = 0
    if a2 + b2 >= 0:
        return str(a1 + b1) + "+" + str(a2 + b2)+"i"
    return str(a1 + b1) + str(a2 + b2)+"i"
def complex_subtraction(a, b):
    if a.find("+") != -1:
        a1 = float(a[0:a.find("+")])
        a2 = float(a[a.find("+")+1:a.find("i")])
    elif a.find("-", 1) != -1:
        a1 = float(a[0:a.find("-", 1)])
        a2 = float(a[a.find("-", 1):a.find("i")])
    elif a.find("i") != -1:
        a1 = 0
        a2 = float(a[0:a.find("i")])
    elif a.find("i") == -1:
        a1 = float(a)
        a2 = 0
    if b.find("+") != -1:
        b1 = float(b[0:b.find("+")])
        b2 = float(b[b.find("+")+1:b.find("i")])
    elif b.find("-", 1) != -1:
        b1 = float(b[0:b.find("-", 1)])
        b2 = float(b[b.find("-", 1):b.find("i")])
    elif b.find("i") != -1:
        b1 = 0
        b2 = float(b[0:b.find("i")])
    elif b.find("i") == -1:
        b1 = float(b)
        b2 = 0
    if a2 - b2 >= 0:
        return str(a1 - b1) + "+" + str(a2 - b2)+"i"
    return str(a1 - b1) + str(a2 - b2)+"i"
# quantitative analysis
def localMinimum(arr):
    num = 0
    pos = []
    if len(arr) == 1:
        return [1 , [0]]
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return [1, [0]]
        if arr[0] > arr[1]:
            return [1, [1]]
        return [0, []]
    for i in range(1, len(arr)-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            num += 1
            pos.append(i)
    if(arr[0] < arr[1]):
        num += 1
        pos.append(0)
    if(arr[len(arr)-1] < arr[len(arr)-2]):
        num += 1
        pos.append(len(arr)-1)
    return [num, pos]
def localMaximum(arr):
    num = 0
    pos = []
    if len(arr) == 1:
        return [1 , [0]]
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [1, [0]]
        if arr[0] < arr[1]:
            return [1, [1]]
        return [0, []]
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            num += 1
            pos.append(i)
    if(arr[0] > arr[1]):
        num += 1
        pos.append(0)
    if(arr[len(arr)-1] > arr[len(arr)-2]):
        num += 1
        pos.append(len(arr)-1)
    return [num, pos]
def globalMinimum(arr):
    pos = []
    if len(arr) == 0:
        raise Exception("Invalid input")
    num = arr[0]
    for i in range(len(arr)):
        if arr[i] < num:
            num = arr[i]
            pos = [i]
        elif arr[i] == num:
            pos.append(i)
    return [num, pos]
def globalMaximum(arr):
    pos = []
    if len(arr) == 0:
        raise Exception("Invalid input")
    num = arr[0]
    for i in range(len(arr)):
        if arr[i] > num:
            num = arr[i]
            pos = [i]
        elif arr[i] == num:
            pos.append(i)
    return [num, pos]
# statistics
def mean(arr):
    total = 0
    for i in arr:
        total += i
    return total / len(arr)
def median(arr):
    arr.sort()
    if len(arr) == 0:
        return
    if len(arr)%2 == 0:
        return (arr[int((len(arr)/2) - 1)] + arr[int(len(arr)/2)]) / 2
    return arr[int(len(arr)/2)]
def standardDevation(arr):
    m = mean(arr)
    total = 0
    for i in arr:
        total += ((i - m)**2)
    return (total / len(arr))**0.5
def mode(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    num = arr[0]
    count = 1
    for i in range(len(arr)):
        if arr.count(arr[i]) > count:
            count = arr.count(arr[i])
            num = arr[i]
    return num
def variance(arr):
    m = mean(arr)
    total = 0
    for i in arr:
        total += ((i-m)**2)
        return total / len(arr)
# def quartiles(arr):
#     arr.sort()
#     if len(arr) == 0:
#         raise Exception("Invalid input")
#     Q2 = median(arr)
#     if len(arr) % 2 == 0:
#         Q1 = median(arr[0:int(len(arr)/2)])
#         Q3 = median(arr[int(len(arr)/2):len(arr)])
#     else:
#         Q1 = median(arr[0:int(len(arr)/2)])
#         Q3 = median(arr[int(len(arr)/2)+1:len(arr)])
#     return [Q1, Q2, Q3]
# def interquartileRange(arr):
#     Q1, Q2, Q3 = quartiles(arr)
#     return Q3 - Q1
# naive set theory
def set(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result
def union(set1, set2):
    return set(set1 + set2)
def intersection(set1, set2):
    result = []
    for i in set1:
        if i in set2:
            result.append(i)
    return result
def difference(set1, set2):
    result = []
    for i in set1:
        if i not in set2:
            result.append(i)
    return result
def symmetricDifference(set1, set2):
    return union(difference(set1, set2), difference(set2, set1))
def powerSet(set):
    result = [[]]
    for i in set:
        result += [j + [i] for j in result]
    return result
def isOpenSet(set, topology):
    for i in set:
        if i not in topology:
            return False
    return True
def cartesianProduct(set1, set2):
    result = []
    for i in set1:
        for j in set2:
            result.append([i, j])
    return result
def isMemberOfSet(x, set):
    return x in set
def isSubset(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True
def setEquality(set1, set2):
    return isSubset(set1, set2) and isSubset(set2, set1)
def complement(set, universal):
    return difference(universal, set)
def cardinality(set):
    return len(set)
def isProperSubset(set1, set2):
    return isSubset(set1, set2) and not setEquality(set1, set2)
def isSuperset(set1, set2):
    return isSubset(set2, set1)
def isProperSuperset(set1, set2):
    return isSuperset(set1, set2) and not setEquality(set1, set2)
def isDisjoint(set1, set2):
    return len(intersection(set1, set2)) == 0
def isEmpty(set):
    return len(set) == 0
# zfc axiomatic set theory
def extensionality(set1, set2):
    return setEquality(set1, set2)
def emptySet():
    return []
def pairing(a, b):
    return [a, b]
def axiomOfUnion(collection):
    result = []
    for s in collection:
        for i in s:
            if i not in result:
                result.append(i)
    return result
def separation(set, predicate):
    result = []
    for i in set:
        if predicate(i):
            result.append(i)
    return result
def replacement(set, func):
    result = []
    for i in set:
        val = func(i)
        if val not in result:
            result.append(val)
    return result
def infinitySet(n):
    result = []
    current = []
    for i in range(n):
        result.append(current)
        current = current + [current]
    return result
def regularity(set):
    for i in set:
        if i == set:
            return False
    return True
def axiomOfChoice(collection):
    result = []
    for s in collection:
        if len(s) == 0:
            raise Exception("Invalid input")
        result.append(s[0])
    return result
# trigonometry
def sin(x):
    return sine(x)
def cos(x):
    return cosine(x)
def tan(x):
    return tangent(x)
def csc(x):
    return cosecant(x)
def sec(x):
    return secant(x)
def cot(x):
    return cotangent(x)
def arcsine(x):
    if x < -1 or x > 1:
        raise Exception("Invalid input")
    return (x + (x**3)/6 + (3*x**5)/40 + (5*x**7)/112 + (35*x**9)/1152)
def arccosine(x):
    if x < -1 or x > 1:
        raise Exception("Invalid input")
    return (1 - (x**2)/2 + (x**4)/24 - (x**6)/720 + (x**8)/40320)
def arctangent(x):
    if x < -1 or x > 1:
        raise Exception("Invalid input")
    return (x - (x**3)/3 + (x**5)/5 - (x**7)/7 + (x**9)/9)
def arccotangent(x):
    if x == 0:
        raise Exception("Invalid input")
    return (1/x - (1/(3*x**3)) + (1/(5*x**5)) - (1/(7*x**7)) + (1/(9*x**9)))
def arcsecant(x):
    if x < 1 and x > -1:
        raise Exception("Invalid input")
    return (1/x + (1/(3*x**3)) + (1/(5*x**5)) + (1/(7*x**7)) + (1/(9*x**9)))
def arccosecant(x):
    if x < 1 and x > -1:
        raise Exception("Invalid input")
    return (1/x + (1/(3*x**3)) + (1/(5*x**5)) + (1/(7*x**7)) + (1/(9*x**9)))
def sine(x):
    return (x - (x**3)/6 + (x**5)/120 - (x**7)/5040 + (x**9)/362880)
def cosine(x):
    return (1 - (x**2)/2 + (x**4)/24 - (x**6)/720 + (x**8)/40320)
def tangent(x):
    if cosine(x) == 0:
        raise Exception("Invalid input")
    return sine(x) / cosine(x)
def cotangent(x):
    if sine(x) == 0:
        raise Exception("Invalid input")
    return cosine(x) / sine(x)
def cosecant(x):
    if sine(x) == 0:
        raise Exception("Invalid input")
    return 1 / sine(x)
def secant(x):
    if cosine(x) == 0:
        raise Exception("Invalid input")
    return 1 / cosine(x)
def degreeToRadian(degree):
    if degree < 0:
        x = degree // - 360
        return (degree + (x * 360)) * (pi / 180)
    if degree > 360:
        x = degree // 360
        return (degree - (x * 360)) * (pi / 180)
    return degree * (pi / 180)
def radianToDegree(radian):
    if radian < 0 or radian > (2 * pi):
        raise Exception("Invalid input")
    return radian * (180 / pi)
# linear algebra
def additionMatrix(arr1, arr2):
    if len(arr1) != len(arr2):
        raise Exception("Invalid input")
    if len(arr1[0]) != len(arr2[0]):
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr1)):
        temp.append([])
        for j in range(len(arr1[0])):
            temp[i].append(arr1[i][j] + arr2[i][j])
    return temp
def subtractionMatrix(arr1, arr2):
    if len(arr1) != len(arr2):
        raise Exception("Invalid input")
    if len(arr1[0]) != len(arr2[0]):
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr1)):
        temp.append([])
        for j in range(len(arr1[0])):
            temp[i].append(arr1[i][j] - arr2[i][j])
    return temp
def multiplicationMatrix(arr1, arr2):
    if len(arr1[0]) != len(arr2):
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr1)):
        temp.append([])
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]
            temp[i].append(total)
    return temp
def determinant(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    if len(arr) > 1 and len(arr[0]) != len(arr):
        raise Exception("Invalid input")
    if len(arr) == 1:
        return arr[0][0]
    if len(arr) > 1:
        total = 0
        for i in range(len(arr[0])):
            temp = []
            for j in range(1, len(arr)):
                temp.append(arr[j][0:i] + arr[j][i+1:len(arr)])
            if i % 2 == 0:
                total += arr[0][i] * determinant(temp)
            else:
                total += -1 * (arr[0][i] * determinant(temp))
        return total
def transpose(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    temp = []
    for i in range(len(arr[0])):
        temp.append([])
        for j in range(len(arr)):
            temp[i].append(arr[j][i])
    return temp
# metric spaces
def dist(x, y, metric="euclidean"):
    if len(x) != len(y):
        raise Exception("Invalid input")
    if metric == "euclidean":
        total = 0
        for i in range(len(x)):
            total += (x[i] - y[i]) ** 2
        return total ** 0.5
    elif metric == "manhattan":
        total = 0
        for i in range(len(x)):
            total += absolute(x[i] - y[i])
        return total
    elif metric == "chebyshev":
        maxVal = 0
        for i in range(len(x)):
            val = absolute(x[i] - y[i])
            if val > maxVal:
                maxVal = val
        return maxVal
    else:
        raise Exception("Invalid metric")
def isMetricSpace(d, S):
    for x in S:
        if d(x, x) != 0:
            return False
    for i in range(len(S)):
        for j in range(len(S)):
            if i != j:
                if d(S[i], S[j]) <= 0:
                    return False
                if absolute(d(S[i], S[j]) - d(S[j], S[i])) > 1e-10:
                    return False
    for i in range(len(S)):
        for j in range(len(S)):
            for k in range(len(S)):
                if d(S[i], S[k]) > d(S[i], S[j]) + d(S[j], S[k]) + 1e-10:
                    return False
    return True
# calculus
def limit(f, x, a):
    h = 1e-10
    left = f(a - h)
    right = f(a + h)
    if absolute(left - right) < 1e-6:
        return (left + right) / 2
    return None
def derivative(f, x):
    h = 1e-10
    return (f(x + h) - f(x - h)) / (2 * h)
def concavity(f, x):
    h = 1e-5
    secondDerivative = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
    if secondDerivative > 1e-6:
        return "concave up"
    elif secondDerivative < -1e-6:
        return "concave down"
    return "inflection point"
def integral(f, a, b):
    n = 1000
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            total += 2 * f(a + i * h)
        else:
            total += 4 * f(a + i * h)
    return total * h / 3
def continuity(f, x):
    h = 1e-10
    try:
        val = f(x)
        left = f(x - h)
        right = f(x + h)
    except:
        return False
    if absolute(left - val) < 1e-6 and absolute(right - val) < 1e-6:
        return True
    return False
# complex analysis
def conjugate(z):
    if z.find("+") != -1:
        real = z[0:z.find("+")]
        imag = z[z.find("+")+1:z.find("i")]
        return real + "-" + imag + "i"
    elif z.find("-", 1) != -1:
        real = z[0:z.find("-", 1)]
        imag = z[z.find("-", 1)+1:z.find("i")]
        return real + "+" + imag + "i"
    elif z.find("i") != -1:
        imag = float(z[0:z.find("i")])
        if imag >= 0:
            return "0.0-" + str(imag) + "i"
        return "0.0+" + str(absolute(imag)) + "i"
    return z
def rootsOfUnity(n):
    result = []
    for k in range(n):
        angle = 2 * pi * k / n
        real = cosine(angle)
        imag = sine(angle)
        if absolute(real) < 1e-10:
            real = 0.0
        if absolute(imag) < 1e-10:
            imag = 0.0
        if imag >= 0:
            result.append(str(real) + "+" + str(imag) + "i")
        else:
            result.append(str(real) + str(imag) + "i")
    return result
# number theory
def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True
# topology
def smooth(f, x):
    for n in range(1, 12):
        h = 0.1
        d1 = _nthDerivative(f, x, n, h)
        d2 = _nthDerivative(f, x, n, h / 2)
        if absolute(d1) > 1e12 or absolute(d2) > 1e12:
            return False
        if absolute(d1) > 1e-6 and absolute((d1 - d2) / d1) > 10:
            return False
    return True
def _nthDerivative(f, x, n, h):
    if n == 0:
        return f(x)
    return (_nthDerivative(f, x + h, n - 1, h) - _nthDerivative(f, x - h, n - 1, h)) / (2 * h)
# polynomials
def polyEval(coefficients, x):
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (x ** (len(coefficients) - 1 - i))
    return result
def divide(dividend, divisor):
    if len(divisor) == 0 or all(c == 0 for c in divisor):
        raise Exception("Invalid input")
    quotient = []
    remainder = list(dividend)
    while len(remainder) >= len(divisor):
        coeff = remainder[0] / divisor[0]
        quotient.append(coeff)
        for i in range(len(divisor)):
            remainder[i] -= coeff * divisor[i]
        remainder.pop(0)
    return [quotient, remainder]
def zeros(coefficients):
    if len(coefficients) == 0:
        raise Exception("Invalid input")
    if len(coefficients) == 1:
        return []
    if len(coefficients) == 2:
        return [-coefficients[1] / coefficients[0]]
    if len(coefficients) == 3:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        disc = b * b - 4 * a * c
        if disc > 0:
            return [(-b + squareRoot(disc)) / (2 * a), (-b - squareRoot(disc)) / (2 * a)]
        elif disc == 0:
            return [-b / (2 * a)]
        else:
            return []
    roots = []
    for candidate in range(-100, 101):
        if absolute(polyEval(coefficients, candidate)) < 1e-10:
            if candidate not in roots:
                roots.append(candidate)
    return roots
def factor(coefficients):
    roots = zeros(coefficients)
    if len(roots) == 0:
        return [[coefficients, 1]]
    result = []
    remaining = list(coefficients)
    for r in roots:
        count = 0
        while len(remaining) > 1:
            quot, rem = divide(remaining, [1, -r])
            if all(absolute(c) < 1e-10 for c in rem):
                count += 1
                remaining = quot
            else:
                break
        if count > 0:
            result.append([[1, -r], count])
    if len(remaining) > 1 or (len(remaining) == 1 and absolute(remaining[0] - 1) > 1e-10):
        result.append([remaining, 1])
    return result

from .upcoming import install_upcoming_functions as _install_upcoming_functions

_UPCOMING_FUNCTION_NAMES = _install_upcoming_functions(globals(), overwrite=False)
del _install_upcoming_functions