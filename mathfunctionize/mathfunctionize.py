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
    
