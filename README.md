# mathfunctionize [![PyPI Downloads](https://static.pepy.tech/personalized-badge/mathfunctionize?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/mathfunctionize)
An extensive Python library for math functions in advanced fields of math. Visit [upcoming.md](upcoming.md) for future functions to be added.

## Getting Started
---
Run ```pip install mathfunctionize``` to get started

Import the library into python file: ```from mathfunctionize import mathfunctionize```

Functions are able to be used by stating ```mathfunctionize.intendedFunction()``` and replacing ```intendedFunction()``` with one of the available functions listed below.

## Constants
---
```pi``` - the ratio of a circle's circumference to its diameter, approximately 3.14159

```e``` - Euler's number, the base of the natural logarithm, approximately 2.71828

## Arithmetic
---
```addition(arr)``` - takes a list of numbers and returns the sum of all elements, e.g. ```addition([1, 2, 3])``` returns ```6```

```subtraction(arr)``` - takes a list of numbers and subtracts each subsequent element from the first, e.g. ```subtraction([10, 3, 2])``` returns ```5```

```multiplication(arr)``` - takes a list of numbers and returns the product of all elements, e.g. ```multiplication([2, 3, 4])``` returns ```24```

```division(arr)``` - takes a list of numbers and divides the first element by each subsequent element, e.g. ```division([100, 5, 2])``` returns ```10```

```power(arr)``` - takes a list of numbers and exponentiates left-to-right, e.g. ```power([2, 3])``` returns ```8```

```modulo(arr)``` - takes a list of numbers and applies the modulo operator left-to-right, e.g. ```modulo([10, 3])``` returns ```1```

```flatDivision(arr)``` - takes a list of numbers and performs floor division left-to-right, e.g. ```flatDivision([10, 3])``` returns ```3```

## Algebra
---
```gamma(x)``` - computes the gamma function of x, a generalization of the factorial to real and complex numbers where gamma(n) = (n-1)! for positive integers

```factorial(x)``` - returns the factorial of a non-negative integer x, i.e. x! = x * (x-1) * ... * 1

```absolute(x)``` - returns the absolute value of x

```squareRoot(x)``` - returns the square root of x

```cubeRoot(x)``` - returns the cube root of x

```nthRoot(x, n)``` - returns the nth root of x

```round(x, place)``` - rounds x to the nearest specified place value (e.g. 1, 10, 100)

## Counting
---
```combinations(n, r)``` - returns the number of ways to choose r items from n items without regard to order, i.e. n! / (r! * (n-r)!)

```permutations(n, r)``` - returns the number of ways to arrange r items from n items where order matters, i.e. n! / (n-r)!

```circularPermutations(n)``` - returns the number of ways to arrange n items in a circle, i.e. (n-1)!

```derangements(n)``` - returns the number of permutations of n elements where no element appears in its original position

## Probability
---
```bayes_theorem(priorA, priorB, likelihoodA, likelihoodB)``` - computes the posterior probability using Bayes' theorem given prior probabilities and likelihoods for two hypotheses

```uniformPDF(a, b)``` - returns the probability density for a continuous uniform distribution over the interval [a, b]

```uniformCDF(X, a, b)``` - returns the cumulative distribution function value for a uniform distribution, giving the probability that a random variable is less than or equal to X

```normalPDF(X, mean, stdDev)``` - returns the probability density of the normal (Gaussian) distribution at point X given a mean and standard deviation

```normalCDF(x, mean, stdDev)``` - returns the cumulative distribution function value for the normal distribution, approximating the probability that a random variable is less than or equal to x

```gammaPDF(x, a, b)``` - returns the probability density of the gamma distribution at point x with shape parameter a and rate parameter b

## Complex Numbers
---
```complex_addition(a, b)``` - adds two complex numbers represented as strings (e.g. ```"3+4i"```, ```"2-1i"```) and returns the result as a string

```complex_subtraction(a, b)``` - subtracts two complex numbers represented as strings and returns the result as a string

## Trigonometry
---
```sin(x)``` / ```sine(x)``` - returns the sine of x (in radians) using a Taylor series approximation

```cos(x)``` / ```cosine(x)``` - returns the cosine of x (in radians) using a Taylor series approximation

```tan(x)``` / ```tangent(x)``` - returns the tangent of x (in radians), computed as sine(x) / cosine(x)

```csc(x)``` / ```cosecant(x)``` - returns the cosecant of x (in radians), computed as 1 / sine(x)

```sec(x)``` / ```secant(x)``` - returns the secant of x (in radians), computed as 1 / cosine(x)

```cot(x)``` / ```cotangent(x)``` - returns the cotangent of x (in radians), computed as cosine(x) / sine(x)

```arcsine(x)``` - returns the inverse sine of x (where -1 <= x <= 1) using a Taylor series approximation

```arccosine(x)``` - returns the inverse cosine of x (where -1 <= x <= 1) using a Taylor series approximation

```arctangent(x)``` - returns the inverse tangent of x (where -1 <= x <= 1) using a Taylor series approximation

```arccotangent(x)``` - returns the inverse cotangent of x (x cannot be 0)

```arcsecant(x)``` - returns the inverse secant of x (where |x| >= 1)

```arccosecant(x)``` - returns the inverse cosecant of x (where |x| >= 1)

```degreeToRadian(degree)``` - converts an angle from degrees to radians, normalizing to the range [0, 2*pi]

```radianToDegree(radian)``` - converts an angle from radians (in the range [0, 2*pi]) to degrees

## Quantitative Analysis
---
```localMinimum(arr)``` - finds all local minima in an array and returns a list containing the count and their positions

```localMaximum(arr)``` - finds all local maxima in an array and returns a list containing the count and their positions

```globalMinimum(arr)``` - finds the smallest value in an array and returns a list containing the value and all positions where it occurs

```globalMaximum(arr)``` - finds the largest value in an array and returns a list containing the value and all positions where it occurs

## Statistics
---
```mean(arr)``` - returns the arithmetic mean (average) of a list of numbers

```median(arr)``` - returns the median (middle value) of a sorted list of numbers, averaging the two middle values for even-length lists

```standardDevation(arr)``` - returns the population standard deviation of a list of numbers, measuring the spread of data around the mean

```mode(arr)``` - returns the most frequently occurring value in a list of numbers

```variance(arr)``` - returns the population variance of a list of numbers, measuring how far each value is from the mean

## Linear Algebra
---
```additionMatrix(arr1, arr2)``` - adds two matrices of the same dimensions element-wise and returns the resulting matrix

```subtractionMatrix(arr1, arr2)``` - subtracts two matrices of the same dimensions element-wise and returns the resulting matrix

```multiplicationMatrix(arr1, arr2)``` - performs matrix multiplication on two matrices where the number of columns in arr1 equals the number of rows in arr2

```determinant(arr)``` - computes the determinant of a square matrix using cofactor expansion

```transpose(arr)``` - returns the transpose of a matrix, swapping rows and columns
