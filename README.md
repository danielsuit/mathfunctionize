# mathfunctionize [![PyPI Downloads](https://static.pepy.tech/personalized-badge/mathfunctionize?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/mathfunctionize)
An extensive Python library for math functions in advanced fields of math. Visit [upcoming.md](upcoming.md) for the research roadmap and future functions to be added.
[Website](https://mathfunctionize.web.app/)
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

## Naive Set Theory
---
```set(arr)``` - removes all duplicate elements from a list and returns a new list containing only unique values in their original order

```union(set1, set2)``` - returns the union of two sets, containing all unique elements that are in either set1 or set2

```intersection(set1, set2)``` - returns the intersection of two sets, containing only the elements present in both set1 and set2

```difference(set1, set2)``` - returns the difference of two sets, containing elements that are in set1 but not in set2

```symmetricDifference(set1, set2)``` - returns the symmetric difference of two sets, containing elements that are in either set but not in both

```powerSet(set)``` - returns the power set of a given set, which is the list of all possible subsets including the empty set

```isOpenSet(set, topology)``` - determines whether a given set is an open set within a specified topology by checking if every element of the set belongs to the topology

```cartesianProduct(set1, set2)``` - returns the Cartesian product of two sets, producing a list of all ordered pairs [a, b] where a is from set1 and b is from set2

```isMemberOfSet(x, set)``` - returns True if element x is a member of the given set, False otherwise

```isSubset(set1, set2)``` - returns True if every element of set1 is also in set2, False otherwise

```setEquality(set1, set2)``` - returns True if both sets contain exactly the same elements, regardless of order

```complement(set, universal)``` - returns the complement of a set with respect to a universal set, containing all elements in the universal set that are not in the given set

```cardinality(set)``` - returns the number of elements in a set

```isProperSubset(set1, set2)``` - returns True if set1 is a subset of set2 but the two sets are not equal

```isSuperset(set1, set2)``` - returns True if every element of set2 is also in set1

```isProperSuperset(set1, set2)``` - returns True if set1 is a superset of set2 but the two sets are not equal

```isDisjoint(set1, set2)``` - returns True if the two sets share no elements in common

```isEmpty(set)``` - returns True if the set contains no elements

## ZFC Axiomatic Set Theory
---
```extensionality(set1, set2)``` - verifies the Axiom of Extensionality by checking whether two sets are equal iff they contain exactly the same elements

```emptySet()``` - returns the empty set, affirming the Axiom of Empty Set

```pairing(a, b)``` - returns a set containing exactly two elements a and b, applying the Axiom of Pairing

```axiomOfUnion(collection)``` - takes a list of sets and returns the union of all their elements, applying the Axiom of Union

```separation(set, predicate)``` - returns the subset of elements from a set that satisfy a given predicate function, applying the Axiom of Separation (Specification)

```replacement(set, func)``` - maps a function over a set and returns the set of all outputs with duplicates removed, applying the Axiom of Replacement

```infinitySet(n)``` - returns the first n elements of the von Neumann ordinal construction of the natural numbers, where 0 = [], 1 = [[]], 2 = [[], [[]]], etc., demonstrating the Axiom of Infinity

```regularity(set)``` - verifies the Axiom of Regularity (Foundation) by checking that no element of the set is equal to the set itself, returns True if the axiom holds

```axiomOfChoice(collection)``` - given a collection of non-empty sets, selects one element from each set and returns them as a list, applying the Axiom of Choice

## Linear Algebra
---
```additionMatrix(arr1, arr2)``` - adds two matrices of the same dimensions element-wise and returns the resulting matrix

```subtractionMatrix(arr1, arr2)``` - subtracts two matrices of the same dimensions element-wise and returns the resulting matrix

```multiplicationMatrix(arr1, arr2)``` - performs matrix multiplication on two matrices where the number of columns in arr1 equals the number of rows in arr2

```determinant(arr)``` - computes the determinant of a square matrix using cofactor expansion

```transpose(arr)``` - returns the transpose of a matrix, swapping rows and columns

## Metric Spaces
---
```dist(x, y, metric)``` - computes the distance between two points x and y in n-dimensional space under a specified metric. Supports "euclidean" (default), "manhattan", and "chebyshev"

```isMetricSpace(d, S)``` - determines whether a distance function d satisfies the three metric space axioms (non-negativity with identity of indiscernibles, symmetry, and the triangle inequality) over a set S

## Calculus
---
```limit(f, x, a)``` - evaluates the limit of a function f as x approaches a value a using numerical approximation from both sides. Returns None if the two-sided limit does not exist

```derivative(f, x)``` - computes the numerical derivative of a function f at a point x using the central difference method

```concavity(f, x)``` - determines the concavity of a function f at a point x by computing the second derivative. Returns "concave up", "concave down", or "inflection point"

```integral(f, a, b)``` - computes the definite integral of a function f over the interval [a, b] using Simpson's rule

```continuity(f, x)``` - tests whether a function f is continuous at a point x by checking that the left-hand limit, right-hand limit, and function value are all equal. Returns a boolean

## Complex Analysis
---
```conjugate(z)``` - returns the complex conjugate of a complex number z represented as a string. For z = "a+bi", returns "a-bi"

```rootsOfUnity(n)``` - computes all n-th roots of unity, returning them as a list of complex number strings evenly spaced on the unit circle

## Number Theory
---
```isPrime(x)``` - determines whether a positive integer x is a prime number. Returns a boolean

## Topology
---
```smooth(f, x)``` - tests whether a function f appears to be infinitely differentiable (smooth) at a point x by computing successive numerical derivatives and checking for convergence. Returns a boolean

## Polynomials
---
```polyEval(coefficients, x)``` - evaluates a polynomial at a given value x, where coefficients are ordered from highest degree to lowest

```divide(dividend, divisor)``` - performs polynomial long division on two polynomials represented by their coefficient lists. Returns [quotient, remainder]

```zeros(coefficients)``` - finds the real roots of a polynomial given its coefficients. Supports linear, quadratic, and higher-degree polynomials via rational root search

```factor(coefficients)``` - factors a polynomial given its coefficients into irreducible factors. Returns a list of [factor, multiplicity] pairs
