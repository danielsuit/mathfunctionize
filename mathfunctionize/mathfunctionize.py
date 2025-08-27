#arithmetics
pi = 3.141592653589793
e = 2.718281828459045
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def power(a, b):
    return a ** b
def modulo(a, b):
    return a % b
def flatDivision(a, b):
    return a // b
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
    if (place > 0 and modulo(place, 10) == 0) or (place == 1):
        if modulo(x, place) < (multiplication(0.5, place)):
            return flatDivision(x, place)
    return flatDivision(x, place) + place
# counting
def permutations(n, r):
    return division(factorial(n), factorial(n - r))

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

def combinations(n, r):
    return division(permutations(n, r), factorial(r))

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
#statistics
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
# trigonometrics
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