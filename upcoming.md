# List of upcoming functions to be added
---

## Metric Spaces

`isMetricSpace(d, S)` - Determines whether a given distance function d satisfies the three metric space axioms (non-negativity with identity of indiscernibles, symmetry, and the triangle inequality) over a set S. Returns a boolean indicating whether (S, d) forms a valid metric space.

`dist(x, y, metric)` - Computes the distance between two points x and y under a specified metric. Supports common metrics such as Euclidean, Manhattan, and Chebyshev distance in n-dimensional space.

## Calculus

`limit(f, x, a)` - Evaluates the limit of a function f(x) as x approaches a value a, using numerical approximation from both the left and right sides. Detects one-sided limits and indicates when a two-sided limit does not exist.

`derivative(f, x)` - Computes the numerical derivative of a function f at a given point x using finite difference approximation. Returns the instantaneous rate of change of f at x.

`concavity(f, x)` - Determines the concavity of a function f at a point x by computing the second derivative. Returns whether the function is concave up (positive second derivative), concave down (negative second derivative), or at an inflection point.

`integral(f, a, b)` - Computes the definite integral of a function f over the interval [a, b] using numerical integration (e.g. Simpson's rule or the trapezoidal rule). Returns the signed area under the curve.

`continuity(f, x)` - Tests whether a function f is continuous at a point x by checking that the left-hand limit, right-hand limit, and function value at x all exist and are equal. Returns a boolean.

## Complex Analysis

`conjugate(z)` - Returns the complex conjugate of a complex number z. For z = a + bi, the conjugate is a - bi. Takes a string representation and returns a string.

`rootsOfUnity(n)` - Computes all n-th roots of unity, i.e. the n complex numbers z such that z^n = 1. Returns them as a list of complex number strings evenly spaced on the unit circle.

## Set Theory

`powerSet(S)` - Returns the power set of a given set S, which is the set of all possible subsets of S including the empty set and S itself. For a set of size n, the power set contains 2^n elements.

`union(A, B)` - Returns the union of two sets A and B, containing all elements that are in A, in B, or in both.

`intersection(A, B)` - Returns the intersection of two sets A and B, containing only the elements that are present in both A and B.

`isOpenSet(S, topology)` - Determines whether a given subset S is an open set within a specified topology. Returns a boolean based on whether S belongs to the collection of open sets defined by the topology.

## Real Analysis

## Number Theory

`isPrime(x)` - Determines whether a positive integer x is a prime number, i.e. a number greater than 1 whose only divisors are 1 and itself. Returns a boolean.

## Topology

`smooth(f, x)` - Tests whether a function f is infinitely differentiable (smooth) at a point x by computing successive numerical derivatives and checking for convergence. Returns a boolean or a smoothness classification.

## Polynomials

`factor(coefficients)` - Factors a polynomial given its coefficients into irreducible polynomial factors. Returns the factored form as a list of factor-multiplicity pairs.

`divide(dividend, divisor)` - Performs polynomial long division on two polynomials represented by their coefficient lists. Returns the quotient and remainder as separate coefficient lists.

`zeros(coefficients)` - Finds all real and complex roots (zeros) of a polynomial given its coefficients. Returns a list of values where the polynomial evaluates to zero.

## Knot Theory

## Type Theory

## Homotopy Theory
