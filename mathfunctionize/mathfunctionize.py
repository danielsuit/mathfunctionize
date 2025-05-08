#arithmetics
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
def round(x, place):
    if (place > 0 and modulo(place, 10) == 0) or (place == 1):
        if modulo(x, place) < (multiplication(0.5, place)):
            return flatDivision(x, place)
    return flatDivision(x, place) + place
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
        return (arr[int((len(arr)/2))] + arr[int((len(arr)/2))+1]) / 2
    return arr(int(len(arr)/2))
def standardDevation(arr):
    mean = mean(arr)
    total = 0
    for i in arr:
        total += ((i - mean)**2)**(0.5)
    return total / len(arr)
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
# matrix
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
    