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
    if x < 0 or a <= 0 or b <= 0:
        raise Exception("Invalid input")
    return ((b ** a) / gamma(a)) * (x ** (a - 1)) * (e ** (-b * x))
def bernoulliPMF(x, p):
    if p < 0 or p > 1 or (x != 0 and x != 1):
        raise Exception("Invalid input")
    return (p ** x) * ((1 - p) ** (1 - x))
def binomialPMF(k, n, p):
    if k < 0 or n < 0 or k > n or p < 0 or p > 1:
        raise Exception("Invalid input")
    return combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))
def binomialCDF(k, n, p):
    if k < 0:
        return 0
    if k >= n:
        return 1
    total = 0
    for i in range(int(k) + 1):
        total += binomialPMF(i, n, p)
    return total
def poissonPMF(k, lam):
    if k < 0 or lam <= 0:
        raise Exception("Invalid input")
    return ((lam ** k) * (e ** (-lam))) / factorial(k)
def poissonCDF(k, lam):
    if k < 0:
        return 0
    total = 0
    for i in range(int(k) + 1):
        total += poissonPMF(i, lam)
    return total
def exponentialPDF(x, lam):
    if lam <= 0:
        raise Exception("Invalid input")
    if x < 0:
        return 0
    return lam * (e ** (-lam * x))
def exponentialCDF(x, lam):
    if lam <= 0:
        raise Exception("Invalid input")
    if x < 0:
        return 0
    return 1 - (e ** (-lam * x))
def expectedValue(values, probabilities):
    if len(values) != len(probabilities) or len(values) == 0:
        raise Exception("Invalid input")
    if absolute(addition(probabilities) - 1) > 1e-9:
        raise Exception("Invalid input")
    total = 0
    for i in range(len(values)):
        if probabilities[i] < 0:
            raise Exception("Invalid input")
        total += values[i] * probabilities[i]
    return total
def conditionalProbability(pAB, pB):
    if pAB < 0 or pB <= 0 or pAB > pB:
        raise Exception("Invalid input")
    return pAB / pB
def independent(pA, pB, pAB, tolerance=1e-9):
    return absolute((pA * pB) - pAB) <= tolerance
# complex numbers
def parseComplex(z):
    if isinstance(z, (int, float)):
        return [float(z), 0.0]
    if not isinstance(z, str):
        raise Exception("Invalid input")
    value = z.replace(" ", "")
    if len(value) == 0:
        raise Exception("Invalid input")
    if value.endswith("i"):
        without_i = value[:-1]
        split_at = -1
        for i in range(1, len(without_i)):
            if without_i[i] == "+" or without_i[i] == "-":
                split_at = i
        if split_at != -1:
            real = float(without_i[:split_at])
            imaginary_part = without_i[split_at:]
        else:
            real = 0.0
            imaginary_part = without_i
        if imaginary_part == "" or imaginary_part == "+":
            imag = 1.0
        elif imaginary_part == "-":
            imag = -1.0
        else:
            imag = float(imaginary_part)
        return [real, imag]
    return [float(value), 0.0]
def _formatComplexNumberPart(x):
    if absolute(x - int(x)) < 1e-10:
        return str(int(x))
    return str(x)
def formatComplex(real, imaginary):
    if absolute(real) < 1e-10:
        real = 0.0
    if absolute(imaginary) < 1e-10:
        imaginary = 0.0
    real_text = _formatComplexNumberPart(real)
    imag_text = _formatComplexNumberPart(absolute(imaginary))
    if imaginary < 0:
        return real_text + "-" + imag_text + "i"
    return real_text + "+" + imag_text + "i"
def complex_addition(a, b):
    a1, a2 = parseComplex(a)
    b1, b2 = parseComplex(b)
    return formatComplex(a1 + b1, a2 + b2)
def complex_subtraction(a, b):
    a1, a2 = parseComplex(a)
    b1, b2 = parseComplex(b)
    return formatComplex(a1 - b1, a2 - b2)
def complex_multiplication(a, b):
    a1, a2 = parseComplex(a)
    b1, b2 = parseComplex(b)
    return formatComplex((a1 * b1) - (a2 * b2), (a1 * b2) + (a2 * b1))
def complex_division(a, b):
    a1, a2 = parseComplex(a)
    b1, b2 = parseComplex(b)
    denominator = (b1 ** 2) + (b2 ** 2)
    if denominator == 0:
        raise Exception("Invalid input")
    real = ((a1 * b1) + (a2 * b2)) / denominator
    imaginary = ((a2 * b1) - (a1 * b2)) / denominator
    return formatComplex(real, imaginary)
def complex_modulus(z):
    real, imaginary = parseComplex(z)
    return ((real ** 2) + (imaginary ** 2)) ** 0.5
def complex_argument(z):
    import math
    real, imaginary = parseComplex(z)
    if real == 0 and imaginary == 0:
        raise Exception("Invalid input")
    return math.atan2(imaginary, real)
def rectangularToPolar(z):
    return [complex_modulus(z), complex_argument(z)]
def polarToRectangular(r, theta):
    import math
    if r < 0:
        raise Exception("Invalid input")
    return formatComplex(r * math.cos(theta), r * math.sin(theta))
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
    if len(arr) == 0:
        raise Exception("Invalid input")
    total = 0
    for i in arr:
        total += i
    return total / len(arr)
def median(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    sorted_arr = sorted(arr)
    if len(sorted_arr)%2 == 0:
        return (sorted_arr[int((len(sorted_arr)/2) - 1)] + sorted_arr[int(len(sorted_arr)/2)]) / 2
    return sorted_arr[int(len(sorted_arr)/2)]
def standardDevation(arr):
    m = mean(arr)
    total = 0
    for i in arr:
        total += ((i - m)**2)
    return (total / len(arr))**0.5
def standardDeviation(arr):
    return standardDevation(arr)
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
def sampleVariance(arr):
    if len(arr) < 2:
        raise Exception("Invalid input")
    m = mean(arr)
    total = 0
    for i in arr:
        total += ((i-m)**2)
    return total / (len(arr) - 1)
def sampleStandardDeviation(arr):
    return sampleVariance(arr)**0.5
def quartiles(arr):
    if len(arr) == 0:
        raise Exception("Invalid input")
    sorted_arr = sorted(arr)
    Q2 = median(sorted_arr)
    midpoint = int(len(sorted_arr)/2)
    if len(sorted_arr) % 2 == 0:
        lower = sorted_arr[0:midpoint]
        upper = sorted_arr[midpoint:len(sorted_arr)]
    else:
        lower = sorted_arr[0:midpoint]
        upper = sorted_arr[midpoint+1:len(sorted_arr)]
    Q1 = median(lower) if len(lower) > 0 else sorted_arr[0]
    Q3 = median(upper) if len(upper) > 0 else sorted_arr[-1]
    return [Q1, Q2, Q3]
def interquartileRange(arr):
    Q1, Q2, Q3 = quartiles(arr)
    return Q3 - Q1
def percentile(arr, p):
    if len(arr) == 0 or p < 0 or p > 100:
        raise Exception("Invalid input")
    sorted_arr = sorted(arr)
    if len(sorted_arr) == 1:
        return sorted_arr[0]
    position = (p / 100) * (len(sorted_arr) - 1)
    lower = int(position)
    upper = lower + 1
    if upper >= len(sorted_arr):
        return sorted_arr[lower]
    weight = position - lower
    return sorted_arr[lower] * (1 - weight) + sorted_arr[upper] * weight
def zScore(x, meanValue, stdDev):
    if stdDev == 0:
        raise Exception("Invalid input")
    return (x - meanValue) / stdDev
def covariance(xValues, yValues):
    if len(xValues) != len(yValues) or len(xValues) == 0:
        raise Exception("Invalid input")
    xMean = mean(xValues)
    yMean = mean(yValues)
    total = 0
    for i in range(len(xValues)):
        total += (xValues[i] - xMean) * (yValues[i] - yMean)
    return total / len(xValues)
def correlation(xValues, yValues):
    xStdDev = standardDevation(xValues)
    yStdDev = standardDevation(yValues)
    if xStdDev == 0 or yStdDev == 0:
        raise Exception("Invalid input")
    return covariance(xValues, yValues) / (xStdDev * yStdDev)
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
def identityMatrix(n):
    if n < 1:
        raise Exception("Invalid input")
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        result.append(row)
    return result
def trace(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise Exception("Invalid input")
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total
def matrixMinor(matrix, row, col):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise Exception("Invalid input")
    return [matrix[i][0:col] + matrix[i][col+1:len(matrix[i])] for i in range(len(matrix)) if i != row]
def cofactorMatrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise Exception("Invalid input")
    if len(matrix) == 1:
        return [[1]]
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix)):
            sign = 1 if (i + j) % 2 == 0 else -1
            result[i].append(sign * determinant(matrixMinor(matrix, i, j)))
    return result
def inverseMatrix(matrix):
    det = determinant(matrix)
    if det == 0:
        raise Exception("Invalid input")
    if len(matrix) == 1:
        return [[1 / det]]
    cofactors = cofactorMatrix(matrix)
    adjugate = transpose(cofactors)
    result = []
    for i in range(len(adjugate)):
        result.append([])
        for j in range(len(adjugate[i])):
            result[i].append(adjugate[i][j] / det)
    return result
def rowEchelon(matrix):
    if len(matrix) == 0:
        raise Exception("Invalid input")
    result = [row[:] for row in matrix]
    lead = 0
    rowCount = len(result)
    columnCount = len(result[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return result
        i = r
        while result[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if lead == columnCount:
                    return result
        result[i], result[r] = result[r], result[i]
        pivot = result[r][lead]
        result[r] = [value / pivot for value in result[r]]
        for i in range(r + 1, rowCount):
            factor = result[i][lead]
            result[i] = [result[i][j] - factor * result[r][j] for j in range(columnCount)]
        lead += 1
    return result
def rank(matrix):
    echelon = rowEchelon(matrix)
    count = 0
    for row in echelon:
        if any(absolute(value) > 1e-10 for value in row):
            count += 1
    return count
def dotProduct(v, w):
    if len(v) != len(w):
        raise Exception("Invalid input")
    total = 0
    for i in range(len(v)):
        total += v[i] * w[i]
    return total
def crossProduct(v, w):
    if len(v) != 3 or len(w) != 3:
        raise Exception("Invalid input")
    return [
        v[1] * w[2] - v[2] * w[1],
        v[2] * w[0] - v[0] * w[2],
        v[0] * w[1] - v[1] * w[0],
    ]
def vectorNorm(v):
    return (dotProduct(v, v)) ** 0.5
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
def gcd(a, b):
    a = int(a)
    b = int(b)
    while b != 0:
        a, b = b, a % b
    return absolute(a)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return absolute(int(a * b)) // gcd(a, b)
def extendedGcd(a, b):
    old_r = int(a)
    r = int(b)
    old_s = 1
    s = 0
    old_t = 0
    t = 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if old_r < 0:
        return [-old_r, -old_s, -old_t]
    return [old_r, old_s, old_t]
def modularExponent(base, exponent, modulus):
    if modulus == 0 or exponent < 0:
        raise Exception("Invalid input")
    result = 1
    base = base % modulus
    exponent = int(exponent)
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result
def modInverse(a, modulus):
    if modulus == 0:
        raise Exception("Invalid input")
    g, x, y = extendedGcd(a, modulus)
    if g != 1:
        raise Exception("Invalid input")
    return x % modulus
def primeFactors(n):
    n = int(n)
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    candidate = 3
    while candidate * candidate <= n:
        while n % candidate == 0:
            factors.append(candidate)
            n //= candidate
        candidate += 2
    if n > 1:
        factors.append(n)
    return factors
def sieve(limit):
    if limit < 2:
        return []
    primes = [True] * (limit + 1)
    primes[0] = False
    primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            multiple = p * p
            while multiple <= limit:
                primes[multiple] = False
                multiple += p
        p += 1
    return [i for i in range(limit + 1) if primes[i]]
def eulerTotient(n):
    n = int(n)
    if n < 1:
        raise Exception("Invalid input")
    result = n
    for p in set(primeFactors(n)):
        result -= result // p
    return result
def isCoprime(a, b):
    return gcd(a, b) == 1
def divisors(n):
    n = int(n)
    if n == 0:
        raise Exception("Invalid input")
    n = absolute(n)
    result = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
        i += 1
    return sorted(result)
def isPerfectNumber(n):
    if n < 2:
        return False
    properDivisors = divisors(n)
    properDivisors.remove(n)
    return addition(properDivisors) == n
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