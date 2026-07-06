# mathfunctionize research and implementation roadmap
---

This roadmap expands the original list of upcoming functions into a practical
research plan for growing `mathfunctionize`. The goal is to deepen the topics
already present in the library before adding too many new domains, while still
preserving the long-term direction toward advanced fields of mathematics.

## Roadmap principles

- Keep the library pure Python and dependency-free unless a future change makes
  a dependency clearly necessary.
- Prefer small, understandable functions that match the current public API.
- Add tests alongside each new function group, especially for numeric edge cases.
- Fix correctness issues in existing functions before building more behavior on
  top of them.
- Document expected input formats clearly, especially for complex numbers,
  matrices, sets, and callable functions.

## Priority tiers

### Tier 1: deepen existing shipped areas

These topics already exist in the README and should be made more complete first.

1. Statistics: fix `variance`, ship quartiles and interquartile range, add
   sample statistics.
2. Number theory: expand beyond `isPrime`.
3. Complex numbers: support multiplication, division, modulus, argument, and
   polar form.
4. Probability: test the existing functions and review `gammaPDF`.
5. Linear algebra: add matrix inverse, rank, trace, and systems of equations.

### Tier 2: make the original future topics concrete

These were listed in the original `upcoming.md` but need detailed function
plans.

1. Real analysis
2. Type theory
3. Homotopy theory
4. Knot theory

### Tier 3: add new research areas

These domains fit the current mission of an advanced math function library.

1. Abstract algebra
2. Graph theory and discrete math
3. Numerical analysis
4. Ordinary differential equations
5. Multivariable and vector calculus
6. Combinatorics
7. Geometry
8. Mathematical logic
9. Optimization
10. Information theory
11. Category theory
12. Game theory
13. Fourier analysis
14. Dynamical systems

---

# Existing topic expansion plan

## Constants

Current coverage:

- `pi`
- `e`

Missing depth:

- More named constants that are common across algebra, analysis, geometry, and
  number theory.
- Helper functions for comparing floating point values.

Candidate additions:

- `tau`: `2 * pi`
- `phi`: golden ratio
- `sqrt2`: square root of 2
- `ln2`: natural logarithm of 2 approximation
- `eulerMascheroni`: Euler-Mascheroni constant approximation
- `approxEqual(a, b, tolerance=1e-9)`: compare numerical results safely

Test notes:

- Verify approximate constants with tolerance-based assertions.
- Keep constant names stable and document precision.

## Arithmetic

Current coverage:

- `addition`, `subtraction`, `multiplication`, `division`
- `power`, `modulo`, `flatDivision`

Missing depth:

- Identity behavior for empty arrays is not defined.
- Division by zero behavior is not documented.
- Common helpers such as sign, reciprocal, and absolute differences are absent.

Candidate additions:

- `summation(arr)`: alias or clearer equivalent for `addition`
- `product(arr)`: alias or clearer equivalent for `multiplication`
- `reciprocal(x)`: return `1 / x`
- `sign(x)`: return `-1`, `0`, or `1`
- `averageRateOfChange(f, a, b)`: useful bridge into calculus
- `clamp(x, lower, upper)`: bound a value to an interval

Test notes:

- Add zero-division tests.
- Add negative number and decimal tests.
- Decide whether aliases should be documented as first-class functions.

## Algebra

Current coverage:

- `gamma`, `factorial`, `absolute`
- `squareRoot`, `cubeRoot`, `nthRoot`
- `round`

Missing depth:

- `gamma` handles only a narrow recursive subset.
- Roots do not define behavior for negative inputs and even roots.
- There are no logarithm, exponential, polynomial helper, or equation-solving
  utilities here.

Candidate additions:

- `log(x, base=e)`: logarithm with configurable base
- `ln(x)`: natural logarithm
- `exp(x)`: exponential function
- `quadraticFormula(a, b, c)`: solve quadratic equations
- `linearEquation(a, b)`: solve `ax + b = 0`
- `isPerfectSquare(n)`: useful in algebra and number theory
- `simplifyRadical(n)`: return outside and inside radical factors
- `fallingFactorial(x, n)` and `risingFactorial(x, n)`

Test notes:

- Test integer, fractional, and invalid inputs.
- Compare logarithm and exponential approximations with known values.

## Counting

Current coverage:

- `combinations`
- `permutations`
- `circularPermutations`
- `derangements`

Missing depth:

- Counting lacks combinations with repetition and partition-style functions.
- No direct support for binomial coefficients as a named function.

Candidate additions:

- `binomialCoefficient(n, k)`
- `multisetCombinations(n, k)`: combinations with repetition
- `stirlingSecondKind(n, k)`
- `bellNumber(n)`
- `integerPartitions(n)`
- `inclusionExclusion(sizes, intersections)`: simplified helper
- `catalanNumber(n)`

Test notes:

- Add boundary tests for `n = 0`, `k = 0`, and `k > n`.
- Verify identities such as symmetry of binomial coefficients.

## Probability

Current coverage:

- `bayes_theorem`
- `uniformPDF`, `uniformCDF`
- `normalPDF`, `normalCDF`
- `gammaPDF`

Missing depth:

- Distribution functions are not tested.
- `gammaPDF` should be reviewed for formula correctness.
- Discrete distributions are absent.
- Expected value and variance helpers for distributions are absent.

Candidate additions:

- `bernoulliPMF(x, p)`
- `binomialPMF(k, n, p)` and `binomialCDF(k, n, p)`
- `poissonPMF(k, lam)` and `poissonCDF(k, lam)`
- `exponentialPDF(x, lam)` and `exponentialCDF(x, lam)`
- `gammaCDF(x, a, b)` using a numerical approximation
- `expectedValue(values, probabilities)`
- `conditionalProbability(pAB, pB)`
- `independent(pA, pB, pAB, tolerance=1e-9)`

Test notes:

- Add probability mass sums for discrete distributions.
- Test CDF monotonicity.
- Validate parameter errors, such as negative standard deviation or invalid
  probabilities.

## Complex Numbers

Current coverage:

- `complex_addition`
- `complex_subtraction`

Missing depth:

- Complex numbers are represented as strings but parsing is repeated inside each
  function.
- Multiplication and division are absent.
- Polar form is absent.

Candidate additions:

- `parseComplex(z)`: convert strings like `"3+4i"` into real and imaginary
  parts.
- `formatComplex(real, imaginary)`: standardize string output.
- `complex_multiplication(a, b)`
- `complex_division(a, b)`
- `complex_modulus(z)`
- `complex_argument(z)`
- `complex_conjugate(z)`: alias or shared implementation with `conjugate`
- `rectangularToPolar(z)`
- `polarToRectangular(r, theta)`
- `complex_power(z, n)`

Test notes:

- Test `a+bi`, `a-bi`, pure real, and pure imaginary inputs.
- Test division by zero.
- Keep output formatting consistent.

## Trigonometry

Current coverage:

- `sin` / `sine`, `cos` / `cosine`, `tan` / `tangent`
- `csc` / `cosecant`, `sec` / `secant`, `cot` / `cotangent`
- Inverse trigonometric functions
- Degree/radian conversion

Missing depth:

- No dedicated trigonometry tests.
- Hyperbolic functions are absent.
- Angle normalization behavior should be documented.

Candidate additions:

- `sinh(x)`, `cosh(x)`, `tanh(x)`
- `arsinh(x)`, `arcosh(x)`, `artanh(x)`
- `normalizeRadians(x)`
- `normalizeDegrees(x)`
- `lawOfSines(a=None, A=None, b=None, B=None)`
- `lawOfCosines(a=None, b=None, c=None, C=None)`
- `degreesMinutesSeconds(degree)`

Test notes:

- Test key angles: `0`, `pi / 6`, `pi / 4`, `pi / 2`, `pi`.
- Test reciprocal identities where defined.
- Test inverse function domain errors.

## Quantitative Analysis

Current coverage:

- `localMinimum`, `localMaximum`
- `globalMinimum`, `globalMaximum`

Missing depth:

- Current functions operate on arrays only.
- There are no optimization helpers for callable functions.
- Plateaus and repeated extrema need clear behavior.

Candidate additions:

- `argMin(arr)` and `argMax(arr)`
- `rangeOfData(arr)`
- `criticalPoints(f, a, b, step=0.01)`
- `monotonicIntervals(arr)`
- `isIncreasing(arr)` and `isDecreasing(arr)`
- `movingAverage(arr, window)`

Test notes:

- Add plateau cases such as `[1, 2, 2, 1]`.
- Add repeated global extrema tests.

## Statistics

Current coverage:

- `mean`, `median`, `standardDevation`
- `mode`, `variance`

Missing depth:

- `variance` currently returns inside the loop and should be fixed.
- `standardDevation` has a spelling issue in the public API.
- `quartiles` and `interquartileRange` exist in comments but are not shipped.
- No sample variance or sample standard deviation.

Candidate additions:

- `standardDeviation(arr)`: correctly spelled alias
- `sampleVariance(arr)`
- `sampleStandardDeviation(arr)`
- `quartiles(arr)`
- `interquartileRange(arr)`
- `percentile(arr, p)`
- `zScore(x, mean, stdDev)`
- `covariance(xValues, yValues)`
- `correlation(xValues, yValues)`
- `linearRegression(xValues, yValues)`

Test notes:

- Add tests for population versus sample formulas.
- Add empty-list and single-value behavior.
- Preserve `standardDevation` for backward compatibility if adding the corrected
  spelling.

## Naive Set Theory

Current coverage:

- Basic set operations such as union, intersection, difference, complement,
  power set, subset checks, cardinality, and Cartesian product.

Missing depth:

- Set representation is list-based, so order and duplicates need clear rules.
- Relations and functions between sets are absent.
- Partitions and equivalence relations are absent.

Candidate additions:

- `setDifference(set1, set2)`: clearer alias for `difference`
- `cartesianPower(set, n)`
- `relationDomain(relation)` and `relationRange(relation)`
- `isRelation(relation, set1, set2)`
- `isFunctionRelation(relation, domain, codomain)`
- `isInjective(mapping)`, `isSurjective(mapping, codomain)`, `isBijective(mapping, codomain)`
- `partition(set, blocks)`
- `isEquivalenceRelation(relation, set)`

Test notes:

- Use list-based pairs consistently.
- Test duplicate inputs and output order.

## ZFC Axiomatic Set Theory

Current coverage:

- Extensionality, empty set, pairing, union, separation, replacement, infinity,
  regularity, and choice.

Missing depth:

- These functions demonstrate axioms but do not model formal set-theoretic
  foundations deeply.
- Ordinal and cardinal helpers would make this section more educational.

Candidate additions:

- `successorOrdinal(n)`
- `vonNeumannOrdinal(n)`
- `ordinalLessThan(a, b)`
- `finiteCardinalEquivalent(set1, set2)`
- `powerSetAxiom(set)`
- `orderedPair(a, b)`: Kuratowski-style ordered pair
- `cartesianProductAxiom(set1, set2)`
- `transitiveSet(set)`

Test notes:

- Keep representations simple and document limitations.
- Test small ordinals only because nested lists grow quickly.

## Linear Algebra

Current coverage:

- Matrix addition, subtraction, multiplication
- Determinant
- Transpose

Missing depth:

- No matrix inverse, rank, identity matrix, trace, vector operations, or linear
  system solving.
- Determinant uses cofactor expansion, which is simple but slow for large
  matrices.

Candidate additions:

- `identityMatrix(n)`
- `trace(matrix)`
- `matrixMinor(matrix, row, col)`
- `cofactorMatrix(matrix)`
- `inverseMatrix(matrix)`
- `rank(matrix)`
- `rowEchelon(matrix)`
- `reducedRowEchelon(matrix)`
- `solveLinearSystem(A, b)`
- `dotProduct(v, w)`, `crossProduct(v, w)`, `vectorNorm(v)`
- `eigenvalues2x2(matrix)`

Test notes:

- Test dimension mismatch errors.
- Test singular matrices.
- Compare `A * inverse(A)` with identity for small matrices.

## Metric Spaces

Current coverage:

- `dist`
- `isMetricSpace`

Missing depth:

- Only three named metrics are supported.
- Open balls, closed balls, boundedness, and convergence are absent.
- Metric-space topology could connect this section to real analysis and
  topology.

Candidate additions:

- `openBall(center, radius, points, metric="euclidean")`
- `closedBall(center, radius, points, metric="euclidean")`
- `isBounded(points, metric="euclidean")`
- `diameter(points, metric="euclidean")`
- `nearestNeighbor(point, points, metric="euclidean")`
- `sequenceConverges(sequence, target, tolerance=1e-9)`
- `discreteMetric(x, y)`
- `minkowskiDistance(x, y, p)`

Test notes:

- Test invalid metrics and dimension mismatches.
- Test metric axiom failures with intentionally bad distance functions.

## Calculus

Current coverage:

- `limit`, `derivative`, `concavity`, `integral`, `continuity`

Missing depth:

- Numerical methods use fixed tolerances and step sizes.
- One-sided limits and higher derivatives are not public.
- There is no symbolic calculus; the section should document that it is
  numerical.

Candidate additions:

- `leftLimit(f, a)` and `rightLimit(f, a)`
- `nthDerivative(f, x, n)`
- `secondDerivative(f, x)`
- `partialDerivative(f, point, variableIndex)`
- `gradient(f, point)`
- `riemannSum(f, a, b, n, method="midpoint")`
- `trapezoidalIntegral(f, a, b, n=1000)`
- `newtonMethod(f, derivativeFunction, initialGuess)`
- `criticalPointType(f, x)`

Test notes:

- Use functions with known derivatives and integrals.
- Add discontinuity tests.
- Add tolerance-based numeric assertions.

## Complex Analysis

Current coverage:

- `conjugate`
- `rootsOfUnity`

Missing depth:

- Complex arithmetic needs to be stronger before complex analysis can deepen.
- No complex derivative, analytic checks, contour tools, or transformations.

Candidate additions:

- `complexDerivative(f, z, h=1e-5)`
- `cauchyRiemann(u, v, x, y, tolerance=1e-5)`
- `isAnalytic(u, v, x, y, tolerance=1e-5)`
- `mobiusTransform(z, a, b, c, d)`
- `complexExponential(z)`
- `complexLog(z)`
- `contourIntegral(f, pathPoints)`
- `residueSimplePole(numerator, denominator, pole)`

Test notes:

- Build on shared complex parsing and formatting helpers.
- Start with simple functions such as `f(z) = z^2`.

## Number Theory

Current coverage:

- `isPrime`

Missing depth:

- This is one of the thinnest existing sections.
- Divisibility, factorization, modular arithmetic, and arithmetic functions are
  absent.

Candidate additions:

- `gcd(a, b)` and `lcm(a, b)`
- `extendedGcd(a, b)`
- `modularExponent(base, exponent, modulus)`
- `modInverse(a, modulus)`
- `primeFactors(n)`
- `sieve(limit)`
- `eulerTotient(n)`
- `isCoprime(a, b)`
- `chineseRemainder(remainders, moduli)`
- `divisors(n)`
- `isPerfectNumber(n)`
- `mobiusFunction(n)`

Test notes:

- Test negative inputs and zero behavior.
- Verify number-theory identities, such as `gcd(a, b) * lcm(a, b) == abs(a*b)`
  for nonzero integers.

## Topology

Current coverage:

- `smooth`

Missing depth:

- `smooth` is closer to numerical calculus than point-set topology.
- Open sets are represented in naive set theory, but topology-specific helpers
  are missing.

Candidate additions:

- `isTopology(collection, universalSet)`
- `interior(set, topology)`
- `closure(set, topology, universalSet)`
- `boundary(set, topology, universalSet)`
- `isClosedSet(set, topology, universalSet)`
- `isContinuousMap(f, domainTopology, codomainTopology)`
- `isHomeomorphism(f, inverse, domainTopology, codomainTopology)`
- `connectedComponents(points, adjacency)`
- `isConnected(points, adjacency)`
- `isCompactFinite(set, topology)`

Test notes:

- Start with finite topological spaces.
- Document that these are finite/discrete models, not full general topology.

## Polynomials

Current coverage:

- `polyEval`
- `divide`
- `zeros`
- `factor`

Missing depth:

- Arithmetic between polynomials is absent.
- Derivatives and integrals of polynomial coefficient lists are absent.
- Root finding is limited.

Candidate additions:

- `polyAdd(p, q)` and `polySubtract(p, q)`
- `polyMultiply(p, q)`
- `polyDerivative(coefficients)`
- `polyIntegral(coefficients, constant=0)`
- `polyDegree(coefficients)`
- `polyLeadingCoefficient(coefficients)`
- `polyNormalize(coefficients)`
- `syntheticDivision(coefficients, root)`
- `rationalRootCandidates(coefficients)`
- `polyGcd(p, q)`

Test notes:

- Test leading zero handling.
- Test division identity: `dividend = divisor * quotient + remainder`.

---

# Original future topics

## Real Analysis

Purpose:

- Build a formal analysis layer that complements the current numerical calculus
  functions.

Candidate additions:

- `sequenceLimit(sequence, tolerance=1e-9)`
- `isConvergentSequence(sequence, tolerance=1e-9)`
- `isCauchySequence(sequence, tolerance=1e-9)`
- `seriesPartialSums(terms, n)`
- `isConvergentSeries(terms, tolerance=1e-9)`
- `ratioTest(terms, n)`
- `rootTest(terms, n)`
- `epsilonDeltaLimit(f, a, L, epsilonValues)`
- `uniformContinuity(f, domainPoints, tolerance=1e-9)`
- `supremum(values)` and `infimum(values)`
- `boundedAbove(values)` and `boundedBelow(values)`

Implementation notes:

- Keep the first version finite and numerical.
- Clearly document that functions approximate analysis concepts on sampled data.

## Knot Theory

Purpose:

- Add an approachable finite representation for knots and links.

Candidate additions:

- `knotCrossingNumber(diagram)`
- `writhe(diagram)`
- `mirrorKnot(diagram)`
- `reverseKnot(diagram)`
- `isAlternating(diagram)`
- `linkingNumber(linkDiagram)`
- `reidemeisterMoveOne(diagram, index)`
- `reidemeisterMoveTwo(diagram, index)`
- `reidemeisterMoveThree(diagram, index)`
- `alexanderPolynomialSimple(diagram)`

Implementation notes:

- Start with a simple diagram encoding before adding invariants.
- Document every representation choice with examples.

## Type Theory

Purpose:

- Provide educational helpers for typed expressions and small lambda-calculus
  examples.

Candidate additions:

- `variable(name, typeName)`
- `functionType(inputType, outputType)`
- `isType(expression)`
- `lambdaExpression(variable, body)`
- `freeVariables(expression)`
- `substitute(expression, variable, replacement)`
- `betaReduce(expression)`
- `churchNumeral(n)`
- `inferSimpleType(expression, context)`
- `typeCheck(expression, expectedType, context)`

Implementation notes:

- Begin with simply typed lambda calculus.
- Avoid dependent types until the expression representation is stable.

## Homotopy Theory

Purpose:

- Add finite and computational models that connect topology, graph theory, and
  algebraic structures.

Candidate additions:

- `path(points)`
- `composePaths(path1, path2)`
- `reversePath(path)`
- `pathHomotopic(path1, path2, adjacency)`
- `fundamentalGroupFinite(space, basePoint)`
- `homotopyEquivalent(space1, space2)`
- `contractible(space)`
- `coveringMap(domain, codomain, mapping)`
- `simplicialComplex(faces)`
- `eulerCharacteristic(complex)`

Implementation notes:

- Start with graph-like spaces and finite simplicial complexes.
- Add examples because these concepts are abstract without representation docs.

---

# Tier 3 new research areas

## Abstract Algebra

Why it fits:

- It naturally follows set theory, counting, and number theory.

Candidate additions:

- `isGroup(elements, operation)`
- `isAbelianGroup(elements, operation)`
- `identityElement(elements, operation)`
- `inverseElement(element, elements, operation)`
- `elementOrder(element, elements, operation)`
- `isSubgroup(subset, group, operation)`
- `cyclicGroup(n)`
- `permutationCompose(p, q)`
- `permutationInverse(p)`
- `isRing(elements, additionOperation, multiplicationOperation)`
- `isField(elements, additionOperation, multiplicationOperation)`

## Graph Theory and Discrete Math

Why it fits:

- It pairs with counting, set theory, topology, and optimization.

Candidate additions:

- `vertices(graph)` and `edges(graph)`
- `degree(graph, vertex)`
- `adjacencyMatrix(graph)`
- `isConnectedGraph(graph)`
- `breadthFirstSearch(graph, start)`
- `depthFirstSearch(graph, start)`
- `shortestPath(graph, start, end)`
- `hasCycle(graph)`
- `isTree(graph)`
- `minimumSpanningTree(graph)`
- `graphColoringGreedy(graph)`

## Numerical Analysis

Why it fits:

- The current calculus and trigonometry functions are already numerical.

Candidate additions:

- `bisectionMethod(f, a, b, tolerance=1e-9)`
- `secantMethod(f, x0, x1, tolerance=1e-9)`
- `fixedPointIteration(g, x0, tolerance=1e-9)`
- `newtonRaphson(f, df, x0, tolerance=1e-9)`
- `lagrangeInterpolation(points, x)`
- `linearInterpolation(points, x)`
- `simpsonRule(f, a, b, n)`
- `trapezoidalRule(f, a, b, n)`
- `eulerMethod(f, x0, y0, h, steps)`
- `rungeKutta4(f, x0, y0, h, steps)`

## Ordinary Differential Equations

Why it fits:

- ODE solvers extend calculus and numerical analysis.

Candidate additions:

- `eulerODE(f, x0, y0, h, steps)`
- `improvedEulerODE(f, x0, y0, h, steps)`
- `rungeKuttaODE(f, x0, y0, h, steps)`
- `slopeField(f, xValues, yValues)`
- `isEquilibriumPoint(f, y)`
- `linearFirstOrderSolution(p, q, x0, y0)`
- `separableStep(f, x, y, h)`

## Multivariable and Vector Calculus

Why it fits:

- It bridges calculus, linear algebra, and physics-style applications.

Candidate additions:

- `partialDerivative(f, point, variableIndex)`
- `gradient(f, point)`
- `directionalDerivative(f, point, direction)`
- `jacobian(functions, point)`
- `hessian(f, point)`
- `divergence(vectorField, point)`
- `curl(vectorField, point)`
- `lineIntegral(vectorField, pathPoints)`

## Combinatorics

Why it fits:

- Counting already exists; this makes the area more complete.

Candidate additions:

- `pascalRow(n)`
- `stirlingFirstKind(n, k)`
- `stirlingSecondKind(n, k)`
- `bellNumber(n)`
- `catalanNumber(n)`
- `integerPartitions(n)`
- `compositions(n)`
- `generatingFunctionCoefficients(sequence, n)`

## Geometry

Why it fits:

- Geometry provides concrete use cases for trigonometry, algebra, and metric
  spaces.

Candidate additions:

- `distance2D(p1, p2)`
- `midpoint(p1, p2)`
- `slope(p1, p2)`
- `triangleArea(a, b, c)`
- `polygonArea(points)`
- `circleArea(radius)`
- `circleCircumference(radius)`
- `lineIntersection(line1, line2)`
- `isCollinear(points)`
- `angleBetweenVectors(v, w)`

## Mathematical Logic

Why it fits:

- Logic complements type theory, set theory, and proof-style functions.

Candidate additions:

- `truthTable(expression, variables)`
- `logicalAnd(a, b)`, `logicalOr(a, b)`, `logicalNot(a)`
- `implies(a, b)` and `iff(a, b)`
- `isTautology(expression, variables)`
- `isContradiction(expression, variables)`
- `isSatisfiable(expression, variables)`
- `deMorgansLawCheck(a, b)`
- `modusPonens(p, impliesPQ)`

## Optimization

Why it fits:

- It extends quantitative analysis and calculus.

Candidate additions:

- `gradientDescent(f, gradientFunction, start, learningRate, steps)`
- `goldenSectionSearch(f, a, b, tolerance=1e-9)`
- `coordinateDescent(f, start, step, iterations)`
- `convexOnSamples(values)`
- `projectToInterval(x, lower, upper)`
- `argMinFunction(f, candidates)`
- `argMaxFunction(f, candidates)`

## Information Theory

Why it fits:

- It connects probability, statistics, and discrete math.

Candidate additions:

- `entropy(probabilities)`
- `crossEntropy(p, q)`
- `klDivergence(p, q)`
- `mutualInformation(jointDistribution)`
- `informationContent(probability)`
- `giniImpurity(probabilities)`

## Category Theory

Why it fits:

- It is a long-term bridge between abstract algebra, type theory, and topology.

Candidate additions:

- `isCategory(objects, morphisms, compose, identity)`
- `isFunctor(sourceCategory, targetCategory, objectMap, morphismMap)`
- `naturalTransformation(functorF, functorG, components)`
- `oppositeCategory(category)`
- `productCategory(categoryA, categoryB)`

## Game Theory

Why it fits:

- It adds applied mathematical decision-making and pairs well with optimization.

Candidate additions:

- `payoff(matrix, rowStrategy, columnStrategy)`
- `dominantStrategy(payoffMatrix, player)`
- `nashEquilibria2x2(playerA, playerB)`
- `zeroSumValue(matrix)`
- `minimax(matrix)`
- `mixedStrategyExpectedPayoff(matrix, rowProbabilities, columnProbabilities)`

## Fourier Analysis

Why it fits:

- It extends trigonometry, complex numbers, and numerical analysis.

Candidate additions:

- `discreteFourierTransform(values)`
- `inverseDiscreteFourierTransform(values)`
- `fourierSeriesCoefficient(f, n, a, b)`
- `sineSeriesCoefficient(f, n, a, b)`
- `cosineSeriesCoefficient(f, n, a, b)`
- `convolution(sequenceA, sequenceB)`

## Dynamical Systems

Why it fits:

- It connects calculus, ODEs, numerical analysis, and topology.

Candidate additions:

- `iterateFunction(f, x0, steps)`
- `fixedPoints(f, candidates, tolerance=1e-9)`
- `logisticMap(r, x0, steps)`
- `orbit(f, x0, steps)`
- `isPeriodicOrbit(values, period, tolerance=1e-9)`
- `cobwebData(f, x0, steps)`
- `lyapunovExponentLogistic(r, x0, steps)`

---

# Professional-level expansion requirements

The sections above name useful next functions. A professional roadmap should
also define the engineering and mathematical standards that each area must meet
before it is considered mature.

## Cross-cutting library standards

Every area should eventually include:

- Clear input contracts: valid domains, shapes, types, and edge-case behavior.
- Deterministic output formats: especially for matrices, graphs, sets, complex
  numbers, symbolic expressions, and probability distributions.
- Tolerance controls for numerical functions, with documented defaults.
- Exact alternatives where practical, such as rational arithmetic for small
  combinatorics, integer number theory, and finite algebra.
- Helpful exceptions for invalid mathematical input instead of silent failures.
- Examples in the README for the most common use cases.
- Unit tests for normal cases, boundary cases, invalid inputs, and identities.
- Property-style tests where identities are central, such as group axioms,
  metric axioms, distribution normalization, and matrix inverse identities.
- Internal helper functions for parsing and validation so public functions do
  not repeat fragile logic.
- Versioned deprecation notes when misspelled or weak APIs are replaced.

## Existing-area maturity targets

### Numerical foundations

The numerical parts of arithmetic, algebra, trigonometry, calculus, statistics,
probability, linear algebra, and optimization should share these capabilities:

- `isFiniteNumber(x)`: reject `nan`, infinities, and unsupported values.
- `validateTolerance(tolerance)`: enforce positive numeric tolerances.
- `relativeError(actual, expected)` and `absoluteError(actual, expected)`.
- `approximatelyEqual(a, b, absTol=1e-9, relTol=1e-9)`.
- Centralized finite-difference helpers for derivatives.
- Centralized summation helpers for numerical integration and series.
- Consistent behavior for empty arrays, singleton arrays, and zero-length
  intervals.

### Data-structure foundations

The structural areas of set theory, topology, graph theory, algebra, type
theory, category theory, and homotopy theory should share these capabilities:

- Canonical representations for ordered pairs, relations, graphs, paths,
  functions, morphisms, and finite spaces.
- Validators such as `isMatrix`, `isSquareMatrix`, `isGraph`, `isRelation`,
  `isTopology`, and `isOperationClosed`.
- Conversion helpers between equivalent representations, such as edge lists,
  adjacency dictionaries, and adjacency matrices.
- Small finite models first, with explicit notes when a function is a finite
  approximation of a general mathematical definition.

### Documentation foundations

Each mature topic should include:

- One paragraph explaining the mathematical object being represented.
- A compact table of functions.
- At least one basic example and one edge-case example.
- A "Limitations" note for numerical approximations or finite models.
- A "Related topics" note so users can move between areas naturally.

---

# Fifty additional professional research areas

The following areas extend the roadmap beyond the current README topics and the
initial Tier 3 list. Each section includes scope, useful objects, candidate
APIs, and implementation or testing notes.

## 1. Measure Theory

Purpose:

- Provide finite and numerical models for measurable spaces, measures, and
  integration, creating a rigorous bridge between real analysis and probability.

Core objects:

- Sigma-algebras on finite sets
- Measures and probability measures
- Measurable functions
- Simple functions

Candidate additions:

- `isSigmaAlgebra(collection, universalSet)`
- `generatedSigmaAlgebra(subsets, universalSet)`
- `isMeasure(measure, sigmaAlgebra)`
- `measureOfSet(measure, subset)`
- `isMeasurableFunction(f, domainSigma, codomainSigma)`
- `simpleFunctionIntegral(values, measures)`
- `outerMeasure(set, coverings, measure)`
- `probabilitySpace(universalSet, sigmaAlgebra, measure)`

Test notes:

- Verify closure under complement and countable union in finite models.
- Test measure axioms: non-negativity, empty set measure, and finite additivity
  for disjoint sets.

## 2. Functional Analysis

Purpose:

- Represent normed spaces, Banach-space-style checks on finite samples, and
  linear functionals.

Core objects:

- Normed vector spaces
- Linear functionals
- Bounded operators
- Inner product spaces

Candidate additions:

- `isNorm(norm, vectors)`
- `lpNorm(vector, p)`
- `supNorm(values)`
- `innerProduct(v, w)`
- `isInnerProduct(inner, vectors)`
- `operatorNorm(matrix, p=2)`
- `isLinearFunctional(functional, vectors)`
- `isContraction(operator, vectors, norm)`

Test notes:

- Test norm axioms and Cauchy-Schwarz on known finite vectors.
- Document that completeness checks are finite approximations.

## 3. Operator Theory

Purpose:

- Study transformations between vector spaces, especially matrix-backed linear
  operators.

Core objects:

- Linear operators
- Adjoint operators
- Projections
- Spectral radius

Candidate additions:

- `applyOperator(matrix, vector)`
- `operatorCompose(A, B)`
- `adjointOperator(matrix)`
- `isSelfAdjoint(matrix)`
- `isProjection(matrix)`
- `spectralRadius(matrix)`
- `commutator(A, B)`
- `isNormalOperator(matrix)`

Test notes:

- Use small matrices with known eigenvalues.
- Test identities such as `P * P == P` for projections.

## 4. Harmonic Analysis

Purpose:

- Expand Fourier analysis into broader transform, convolution, and frequency
  decomposition tools.

Core objects:

- Signals
- Kernels
- Fourier coefficients
- Convolution operators

Candidate additions:

- `normalizeSignal(values)`
- `circularConvolution(a, b)`
- `correlationSignal(a, b)`
- `fourierMagnitude(values)`
- `fourierPhase(values)`
- `lowPassFilter(values, cutoff)`
- `highPassFilter(values, cutoff)`
- `dirichletKernel(n, x)`

Test notes:

- Test convolution length and identity kernels.
- Verify Parseval-style identities on small finite sequences where practical.

## 5. Partial Differential Equations

Purpose:

- Add finite-difference approximations for basic PDE models.

Core objects:

- Grids
- Boundary conditions
- Difference stencils
- Heat, wave, and Laplace equations

Candidate additions:

- `finiteDifferenceGrid(xPoints, tPoints)`
- `laplacian2D(grid, i, j, h)`
- `heatEquationStep(grid, alpha, dt, dx)`
- `waveEquationStep(previous, current, c, dt, dx)`
- `dirichletBoundary(grid, value)`
- `neumannBoundary(grid, derivative)`
- `solveLaplace2D(boundaryGrid, iterations)`
- `stabilityHeatEquation(alpha, dt, dx)`

Test notes:

- Test grid shape validation.
- Add conservation or monotonicity checks for simple cases.

## 6. Stochastic Processes

Purpose:

- Model random processes over discrete time and finite state spaces.

Core objects:

- Random walks
- Markov chains
- Transition matrices
- Stationary distributions

Candidate additions:

- `randomWalkPath(start, steps, increments)`
- `isTransitionMatrix(matrix)`
- `markovStep(distribution, transitionMatrix)`
- `markovChainDistribution(initial, transitionMatrix, steps)`
- `stationaryDistribution(transitionMatrix)`
- `absorbingStates(transitionMatrix)`
- `hittingProbability(transitionMatrix, start, target)`
- `expectedReturnTime(transitionMatrix, state)`

Test notes:

- Verify transition rows sum to one.
- Test known two-state chains and absorbing chains.

## 7. Stochastic Calculus

Purpose:

- Provide educational discrete approximations of stochastic calculus concepts.

Core objects:

- Brownian paths
- Quadratic variation
- Ito sums
- Stochastic differential equation steps

Candidate additions:

- `brownianPath(increments, start=0)`
- `quadraticVariation(path)`
- `itoIntegralApprox(integrandValues, brownianIncrements)`
- `stratonovichIntegralApprox(integrandValues, brownianIncrements)`
- `geometricBrownianMotionPath(mu, sigma, increments, start)`
- `eulerMaruyamaStep(x, drift, diffusion, dt, dW)`
- `blackScholesCallPrice(S, K, r, sigma, T)`
- `blackScholesPutPrice(S, K, r, sigma, T)`

Test notes:

- Keep randomness injectable through provided increments.
- Test deterministic increment paths for reproducibility.

## 8. Time Series Analysis

Purpose:

- Add sequence analysis tools for data indexed by time.

Core objects:

- Lagged series
- Autocorrelation
- Moving averages
- Trend and seasonality

Candidate additions:

- `lag(values, k)`
- `differenceSeries(values, order=1)`
- `autocovariance(values, lag)`
- `autocorrelation(values, lag)`
- `movingAverage(values, window)`
- `exponentialSmoothing(values, alpha)`
- `detectTrend(values)`
- `seasonalIndices(values, period)`

Test notes:

- Validate window and lag sizes.
- Test constant, linear, and periodic sequences.

## 9. Bayesian Statistics

Purpose:

- Extend probability into prior-posterior updates and conjugate models.

Core objects:

- Priors
- Likelihoods
- Posteriors
- Credible intervals

Candidate additions:

- `bayesianUpdateDiscrete(prior, likelihood)`
- `normalizeProbabilities(weights)`
- `betaPosterior(alpha, beta, successes, failures)`
- `betaMean(alpha, beta)`
- `betaVariance(alpha, beta)`
- `credibleIntervalDiscrete(distribution, confidence)`
- `maximumAPosteriori(distribution)`
- `posteriorPredictiveDiscrete(posterior, likelihoods)`

Test notes:

- Verify posterior probabilities sum to one.
- Test conjugate beta-binomial examples with known means.

## 10. Statistical Inference

Purpose:

- Add confidence intervals, hypothesis tests, and estimators.

Core objects:

- Estimators
- Confidence intervals
- Test statistics
- P-values

Candidate additions:

- `confidenceIntervalMean(values, confidence=0.95)`
- `zTestMean(sampleMean, populationMean, stdDev, n)`
- `tStatisticMean(values, hypothesizedMean)`
- `chiSquareStatistic(observed, expected)`
- `proportionConfidenceInterval(successes, trials, confidence=0.95)`
- `meanSquaredError(estimates, actual)`
- `bias(estimates, actual)`
- `bootstrapMeans(values, resamples)`

Test notes:

- Test against hand-computed small examples.
- Document approximation assumptions.

## 11. Experimental Design

Purpose:

- Provide helpers for controlled experiments and simple statistical planning.

Core objects:

- Treatments
- Blocks
- Random assignments
- Factorial designs

Candidate additions:

- `completeRandomAssignment(subjects, treatments)`
- `blockedRandomAssignment(blocks, treatments)`
- `factorialDesign(factors)`
- `latinSquare(n)`
- `treatmentMeans(data, treatmentLabels)`
- `anovaOneWay(groups)`
- `effectSizeDifference(meanA, meanB, pooledStdDev)`
- `minimumDetectableEffect(stdDev, n, alpha, power)`

Test notes:

- Make randomized functions accept deterministic seeds or orderings.
- Test balanced-design counts.

## 12. Computational Geometry

Purpose:

- Add algorithmic geometry on points, segments, polygons, and hulls.

Core objects:

- Points
- Line segments
- Polygons
- Convex hulls

Candidate additions:

- `orientation(p, q, r)`
- `segmentsIntersect(a, b, c, d)`
- `pointInPolygon(point, polygon)`
- `convexHull(points)`
- `closestPair(points)`
- `boundingBox(points)`
- `polygonCentroid(points)`
- `triangulateConvexPolygon(points)`

Test notes:

- Test collinear and duplicate points.
- Validate clockwise and counterclockwise polygon order.

## 13. Differential Geometry

Purpose:

- Represent curves and surfaces with numerical geometric invariants.

Core objects:

- Parametric curves
- Parametric surfaces
- Curvature
- Torsion

Candidate additions:

- `curveDerivative(curve, t)`
- `arcLength(curve, a, b)`
- `curvature2D(curve, t)`
- `curvature3D(curve, t)`
- `torsion(curve, t)`
- `surfaceNormal(surface, u, v)`
- `firstFundamentalForm(surface, u, v)`
- `geodesicStep(surface, point, direction, step)`

Test notes:

- Use circles and lines as baseline cases.
- Add tolerance-based tests for numerical derivatives.

## 14. Riemannian Geometry

Purpose:

- Add metric tensors and finite-dimensional geometric computations.

Core objects:

- Metric tensors
- Christoffel symbols
- Geodesics
- Curvature tensors

Candidate additions:

- `metricTensorEuclidean(n)`
- `innerProductMetric(metric, v, w)`
- `christoffelSymbols(metricFunctions, point)`
- `geodesicEquationStep(metricFunctions, state, step)`
- `sectionalCurvature(metricFunctions, point, plane)`
- `scalarCurvature(metricFunctions, point)`
- `raiseIndex(metricInverse, covector)`
- `lowerIndex(metric, vector)`

Test notes:

- Start with Euclidean and sphere-like examples.
- Clearly label advanced functions as numerical approximations.

## 15. Algebraic Geometry

Purpose:

- Study polynomial solution sets and ideal-like computations in a lightweight
  way.

Core objects:

- Affine varieties
- Polynomial systems
- Ideals
- Groebner-style reductions

Candidate additions:

- `evaluatePolynomialMultivariate(terms, point)`
- `zeroSet(polynomials, candidatePoints)`
- `isPolynomialInIdeal(polynomial, generators, candidates)`
- `monomialOrder(monomials, order="lex")`
- `leadingTerm(polynomial, order="lex")`
- `sPolynomial(f, g)`
- `buchbergerStep(generators)`
- `affineVarietyDimensionEstimate(points)`

Test notes:

- Begin with finite candidate sets.
- Test small bivariate polynomial systems.

## 16. Arithmetic Geometry

Purpose:

- Connect number theory and algebraic geometry through curves over finite
  fields and rational points.

Core objects:

- Finite-field points
- Elliptic curves
- Rational points
- Modular reductions

Candidate additions:

- `pointsOnCurveModP(polynomial, p)`
- `ellipticCurveDiscriminant(a, b)`
- `isPointOnEllipticCurve(point, a, b, modulus=None)`
- `ellipticCurveAdd(P, Q, a, modulus=None)`
- `ellipticCurveScalarMultiply(P, n, a, modulus=None)`
- `countPointsEllipticCurveModP(a, b, p)`
- `hasGoodReduction(a, b, p)`
- `rationalPointHeight(point)`

Test notes:

- Test point addition identity and inverse cases.
- Validate finite-field arithmetic through existing number theory helpers.

## 17. Algebraic Topology

Purpose:

- Add computable invariants for finite topological and simplicial structures.

Core objects:

- Simplicial complexes
- Chains
- Boundary maps
- Homology groups

Candidate additions:

- `facesOfComplex(complex)`
- `boundaryOfSimplex(simplex)`
- `boundaryMatrix(complex, dimension)`
- `chainGroupRank(complex, dimension)`
- `bettiNumber(complex, dimension)`
- `eulerCharacteristicFromBetti(bettiNumbers)`
- `simplicialHomologyRanks(complex)`
- `isCycle(chain, boundaryMatrix)`

Test notes:

- Test intervals, triangles, circles, and filled triangles.
- Keep early outputs as ranks before modeling full abelian groups.

## 18. Geometric Topology

Purpose:

- Study manifolds and embeddings using finite/combinatorial models.

Core objects:

- Triangulations
- Surfaces
- Manifold checks
- Handles and genus

Candidate additions:

- `isTriangulatedSurface(complex)`
- `vertexLink(complex, vertex)`
- `isCombinatorialManifold(complex)`
- `surfaceEulerCharacteristic(vertices, edges, faces)`
- `orientableSurfaceGenus(vertices, edges, faces)`
- `connectedSumInvariant(surfaceA, surfaceB)`
- `boundaryComponents(complex)`
- `isOrientableSurface(complex)`

Test notes:

- Test sphere, torus-style examples, and disks once representations exist.
- Document combinatorial assumptions.

## 19. Differential Topology

Purpose:

- Connect calculus and topology through smooth maps and local structure.

Core objects:

- Smooth maps
- Jacobians
- Regular values
- Transversality-style finite checks

Candidate additions:

- `jacobianRank(f, point)`
- `isImmersion(f, point)`
- `isSubmersion(f, point)`
- `isRegularValue(f, value, candidatePreimages)`
- `criticalValues(f, domainPoints)`
- `degreeMapCircle(mapSamples)`
- `localDiffeomorphism(f, point)`
- `sardSampleCheck(f, domainPoints)`

Test notes:

- Use low-dimensional numerical examples.
- Be explicit that global theorems are sampled approximations.

## 20. Lie Theory

Purpose:

- Add matrix Lie groups and Lie algebras for advanced algebra and geometry.

Core objects:

- Matrix groups
- Lie algebras
- Brackets
- Exponential maps

Candidate additions:

- `matrixCommutator(A, B)`
- `isSkewSymmetric(matrix)`
- `lieBracket(A, B)`
- `matrixExponential(matrix, terms=20)`
- `specialOrthogonal2(theta)`
- `isLieAlgebra(elements, bracket)`
- `adjointRepresentation(element, algebra)`
- `bakerCampbellHausdorff(A, B, terms=3)`

Test notes:

- Test bracket bilinearity and antisymmetry on matrices.
- Start with 2x2 examples.

## 21. Representation Theory

Purpose:

- Study algebraic structures through linear transformations.

Core objects:

- Group actions
- Characters
- Representations
- Irreducibility checks

Candidate additions:

- `groupAction(group, setValues, action)`
- `orbitOfElement(group, element, action)`
- `stabilizer(group, element, action)`
- `representationMatrices(group, mapping)`
- `characterOfRepresentation(matrices)`
- `regularRepresentation(group)`
- `isInvariantSubspace(subspace, matrices)`
- `burnsideLemma(group, setValues, action)`

Test notes:

- Test small cyclic groups and permutation actions.
- Verify orbit-stabilizer identity for finite groups.

## 22. Galois Theory

Purpose:

- Connect field extensions, polynomial roots, and symmetry.

Core objects:

- Polynomial fields
- Splitting fields in simple cases
- Automorphisms
- Galois groups

Candidate additions:

- `rationalRootTest(coefficients)`
- `isIrreduciblePolynomial(coefficients, field="Q")`
- `polynomialDiscriminantQuadratic(a, b, c)`
- `polynomialDiscriminantCubic(a, b, c, d)`
- `quadraticGaloisGroup(a, b, c)`
- `fieldExtensionDegree(minimalPolynomial)`
- `conjugateRootsQuadratic(a, b, c)`
- `isSeparablePolynomial(coefficients, characteristic=0)`

Test notes:

- Start with quadratic and cubic cases.
- Reuse polynomial and number theory utilities.

## 23. Commutative Algebra

Purpose:

- Support rings, ideals, modules, and algebraic computations that feed algebraic
  geometry.

Core objects:

- Rings
- Ideals
- Modules
- Quotient rings

Candidate additions:

- `idealGeneratedBy(generators, ringElements, operations)`
- `isIdeal(subset, ringElements, add, multiply)`
- `idealSum(I, J)`
- `idealProduct(I, J, multiply)`
- `radicalIdealApprox(ideal, candidates, powerLimit)`
- `quotientRingClasses(ringElements, ideal)`
- `isMaximalIdeal(ideal, ringElements, operations)`
- `isPrimeIdeal(ideal, ringElements, operations)`

Test notes:

- Use finite rings such as integers modulo n.
- Test ideal closure properties.

## 24. Homological Algebra

Purpose:

- Add chain complexes and exactness checks, supporting topology and algebra.

Core objects:

- Chain complexes
- Boundary maps
- Kernels
- Images
- Exact sequences

Candidate additions:

- `isChainComplex(boundaryMatrices)`
- `kernelDimension(matrix)`
- `imageDimension(matrix)`
- `homologyDimension(boundaryN, boundaryNext)`
- `isExactAt(mapA, mapB)`
- `chainMap(complexA, complexB, maps)`
- `mappingCone(chainMap)`
- `longExactSequenceRanks(data)`

Test notes:

- Use matrix ranks over small fields or rationals.
- Verify `d_n * d_(n+1) == 0`.

## 25. Noncommutative Algebra

Purpose:

- Represent algebraic structures where multiplication order matters.

Core objects:

- Noncommutative rings
- Algebras
- Commutators
- Centers

Candidate additions:

- `isAssociativeOperation(elements, operation)`
- `isCommutativeOperation(elements, operation)`
- `centerOfAlgebra(elements, multiply)`
- `commutatorElement(a, b, multiply, subtract)`
- `leftIdealGeneratedBy(generators, elements, add, multiply)`
- `rightIdealGeneratedBy(generators, elements, add, multiply)`
- `matrixAlgebraBasis(n)`
- `quaternionMultiply(q1, q2)`

Test notes:

- Use matrices and quaternions as concrete examples.
- Test associativity separately from commutativity.

## 26. Universal Algebra

Purpose:

- Generalize algebraic structures by operations and identities.

Core objects:

- Signatures
- Algebras
- Homomorphisms
- Congruences

Candidate additions:

- `signature(operations)`
- `isAlgebraForSignature(elements, operations, signature)`
- `satisfiesIdentity(elements, operations, lhs, rhs)`
- `isHomomorphism(domain, codomain, mapping, operations)`
- `subalgebraGeneratedBy(generators, elements, operations)`
- `congruenceRelation(elements, relation, operations)`
- `quotientAlgebra(elements, congruence, operations)`
- `productAlgebra(algebraA, algebraB)`

Test notes:

- Start with semigroups, monoids, and lattices.
- Test preservation of operations under homomorphisms.

## 27. Lattice Theory

Purpose:

- Study ordered structures with meets and joins.

Core objects:

- Posets
- Lattices
- Meets
- Joins
- Bounds

Candidate additions:

- `meet(a, b, orderRelation, elements)`
- `join(a, b, orderRelation, elements)`
- `isLattice(elements, orderRelation)`
- `isDistributiveLattice(elements, meetOperation, joinOperation)`
- `isCompleteLattice(elements, orderRelation)`
- `leastElement(elements, orderRelation)`
- `greatestElement(elements, orderRelation)`
- `hasseDiagram(elements, orderRelation)`

Test notes:

- Test subset lattices and divisor lattices.
- Verify absorption and distributive laws.

## 28. Order Theory

Purpose:

- Provide general tools for partial orders, total orders, and fixed points.

Core objects:

- Preorders
- Partial orders
- Total orders
- Chains and antichains

Candidate additions:

- `isReflexiveRelation(relation, elements)`
- `isAntisymmetricRelation(relation, elements)`
- `isTransitiveRelation(relation, elements)`
- `isPartialOrder(relation, elements)`
- `isTotalOrder(relation, elements)`
- `minimalElements(elements, orderRelation)`
- `maximalElements(elements, orderRelation)`
- `topologicalSort(poset)`

Test notes:

- Test relation properties independently.
- Reuse graph helpers for topological sorting.

## 29. Model Theory

Purpose:

- Evaluate structures against first-order-style signatures and formulas.

Core objects:

- Languages
- Structures
- Assignments
- Formulas

Candidate additions:

- `structure(domain, functions, relations, constants)`
- `evaluateTerm(term, structure, assignment)`
- `satisfiesAtomicFormula(formula, structure, assignment)`
- `satisfiesFormula(formula, structure, assignment)`
- `elementaryEquivalentFinite(structureA, structureB, formulas)`
- `theoryModels(theory, candidateStructures)`
- `isIsomorphicStructure(structureA, structureB, mapping)`
- `automorphismsFiniteStructure(structure)`

Test notes:

- Keep formula representation simple and documented.
- Test with finite graphs and finite orders.

## 30. Proof Theory

Purpose:

- Add proof checking and derivation helpers for logical systems.

Core objects:

- Propositions
- Inference rules
- Proof trees
- Sequents

Candidate additions:

- `sequent(assumptions, conclusion)`
- `applyModusPonens(rule, premises)`
- `isValidInference(rule, premises, conclusion)`
- `proofTree(conclusion, premises)`
- `checkProof(steps, rules)`
- `normalFormProof(proof)`
- `deductionTheoremTransform(proof)`
- `cutEliminationStep(proof)`

Test notes:

- Begin with propositional logic.
- Test invalid proof steps explicitly.

## 31. Descriptive Set Theory

Purpose:

- Provide finite analogues and educational helpers for definable sets and
  hierarchies.

Core objects:

- Borel-like generated collections
- Trees
- Cantor-space finite prefixes
- Equivalence relations

Candidate additions:

- `cylinderSet(prefix, alphabet)`
- `cantorPrefixTree(depth)`
- `borelGeneratedFinite(generators, universalSet)`
- `isBorelFinite(setValue, generatedCollection)`
- `treeBodyPrefixes(tree, depth)`
- `equivalenceClasses(relation, elements)`
- `smoothEquivalenceRelationFinite(relation, elements)`
- `reductionBetweenRelations(relationA, relationB, mapping)`

Test notes:

- Clearly state finite approximation limits.
- Test generated collections from small bases.

## 32. Computability Theory

Purpose:

- Model algorithms, decidability, and computable functions in an educational
  form.

Core objects:

- Turing-machine-like states
- Partial functions
- Deciders
- Enumerators

Candidate additions:

- `simulateDFA(automaton, inputString)`
- `simulateTuringMachine(machine, tape, maxSteps)`
- `haltsWithin(machine, tape, maxSteps)`
- `isTotalOnSamples(function, samples)`
- `enumerateLanguage(generator, steps)`
- `characteristicFunction(setValues, universalSet)`
- `composePartialFunctions(f, g)`
- `primitiveRecursiveAdd(a, b)`

Test notes:

- Use explicit step limits to avoid nontermination.
- Test simple accept/reject machines.

## 33. Automata and Formal Languages

Purpose:

- Add tools for regular languages, grammars, and parsing.

Core objects:

- DFAs
- NFAs
- Regular expressions
- Context-free grammars

Candidate additions:

- `dfaAccepts(dfa, inputString)`
- `nfaAccepts(nfa, inputString)`
- `nfaToDfa(nfa)`
- `minimizeDfa(dfa)`
- `regularLanguageUnion(dfaA, dfaB)`
- `regularLanguageIntersection(dfaA, dfaB)`
- `cykParse(grammar, inputString)`
- `grammarDerives(grammar, inputString, maxDepth)`

Test notes:

- Test automata with empty strings and dead states.
- Validate transition completeness.

## 34. Coding Theory

Purpose:

- Support error-detecting and error-correcting codes.

Core objects:

- Codewords
- Hamming distance
- Linear codes
- Generator and parity-check matrices

Candidate additions:

- `hammingDistance(a, b)`
- `minimumDistance(codewords)`
- `encodeLinearCode(message, generatorMatrix, modulus=2)`
- `syndrome(received, parityCheckMatrix, modulus=2)`
- `detectError(received, parityCheckMatrix)`
- `correctSingleBitError(received, parityCheckMatrix)`
- `hammingCode74Encode(message)`
- `hammingCode74Decode(codeword)`

Test notes:

- Test all one-bit errors for small Hamming codes.
- Verify matrix dimensions over finite fields.

## 35. Cryptography

Purpose:

- Provide educational number-theoretic cryptography primitives.

Core objects:

- Modular arithmetic
- Keys
- Ciphers
- Hash-style toy functions

Candidate additions:

- `caesarCipher(text, shift)`
- `affineCipherEncrypt(text, a, b)`
- `affineCipherDecrypt(text, a, b)`
- `rsaKeyCheck(p, q, e)`
- `rsaEncryptNumber(message, e, n)`
- `rsaDecryptNumber(ciphertext, d, n)`
- `diffieHellmanPublic(g, private, p)`
- `diffieHellmanShared(public, private, p)`

Test notes:

- Mark these as educational, not production-security utilities.
- Test small textbook examples only.

## 36. Finite Fields

Purpose:

- Support arithmetic over fields with finitely many elements.

Core objects:

- Prime fields
- Polynomial quotient fields
- Field elements
- Multiplicative groups

Candidate additions:

- `fieldAdd(a, b, p)`
- `fieldSubtract(a, b, p)`
- `fieldMultiply(a, b, p)`
- `fieldInverse(a, p)`
- `fieldDivide(a, b, p)`
- `fieldPower(a, n, p)`
- `isPrimitiveRoot(g, p)`
- `multiplicativeOrderMod(a, p)`

Test notes:

- Test field axioms for small primes.
- Reuse modular inverse from number theory.

## 37. Analytic Number Theory

Purpose:

- Add functions that study integers through analytic approximations.

Core objects:

- Prime-counting functions
- Arithmetic sums
- Zeta-like approximations
- Chebyshev functions

Candidate additions:

- `primeCountingFunction(n)`
- `logIntegralApprox(x)`
- `riemannZetaPartial(s, terms)`
- `mobiusSummatory(n)`
- `mertensFunction(n)`
- `chebyshevTheta(n)`
- `chebyshevPsi(n)`
- `divisorSummatory(n)`

Test notes:

- Compare small values to exact hand-computed results.
- Document approximation limits for large analytic functions.

## 38. Algebraic Number Theory

Purpose:

- Study algebraic integers, norms, traces, and quadratic fields.

Core objects:

- Number fields
- Rings of integers in simple cases
- Norms and traces
- Ideals in quadratic rings

Candidate additions:

- `quadraticFieldElement(a, b, d)`
- `quadraticFieldAdd(x, y, d)`
- `quadraticFieldMultiply(x, y, d)`
- `quadraticFieldConjugate(x, d)`
- `quadraticFieldNorm(x, d)`
- `quadraticFieldTrace(x, d)`
- `isAlgebraicIntegerQuadratic(x, d)`
- `classNumberEstimateQuadratic(d)`

Test notes:

- Start with square-free `d`.
- Test norm multiplicativity.

## 39. Diophantine Approximation

Purpose:

- Approximate real numbers by rationals and analyze integer solutions.

Core objects:

- Continued fractions
- Rational approximations
- Pell equations
- Approximation errors

Candidate additions:

- `continuedFraction(x, terms)`
- `continuedFractionConvergents(coefficients)`
- `bestRationalApproximation(x, maxDenominator)`
- `approximationError(x, numerator, denominator)`
- `solvePell(D, limit)`
- `fareySequence(n)`
- `mediant(fracA, fracB)`
- `isDiophantineSolution(equation, values)`

Test notes:

- Test sqrt(2) convergents.
- Validate exact integer equations.

## 40. Ergodic Theory

Purpose:

- Study long-term averages of transformations on finite or sampled spaces.

Core objects:

- Measure-preserving maps
- Orbits
- Time averages
- Invariant sets

Candidate additions:

- `timeAverage(f, transform, x0, steps)`
- `spaceAverage(values, measure)`
- `isMeasurePreserving(transform, space, measure)`
- `invariantSet(transform, subset)`
- `ergodicSampleCheck(transform, space, measure)`
- `poincareReturnTimes(transform, x0, targetSet, steps)`
- `birkhoffAverage(values)`
- `mixingSampleCheck(transform, sets, steps)`

Test notes:

- Use finite rotations and permutations.
- Keep claims as sample-based checks.

## 41. Chaos Theory

Purpose:

- Deepen dynamical systems with sensitivity, bifurcations, and chaotic maps.

Core objects:

- Iterated maps
- Orbits
- Lyapunov exponents
- Bifurcation samples

Candidate additions:

- `sensitivityToInitialConditions(f, x0, delta, steps)`
- `bifurcationDataLogistic(rValues, x0, burnIn, samples)`
- `lyapunovExponentMap(f, derivative, x0, steps)`
- `tentMap(mu, x)`
- `henonMap(a, b, point)`
- `lorenzStep(point, sigma, rho, beta, dt)`
- `poincareSection(points, coordinateIndex, value)`
- `chaosGame(vertices, ratios, choices, start)`

Test notes:

- Use deterministic choice lists for chaos-game examples.
- Test known fixed and periodic regimes.

## 42. Control Theory

Purpose:

- Add linear-system and feedback-control computations.

Core objects:

- State-space systems
- Transfer functions
- Controllability
- Observability

Candidate additions:

- `stateStep(A, B, x, u)`
- `simulateLinearSystem(A, B, x0, inputs)`
- `controllabilityMatrix(A, B)`
- `observabilityMatrix(A, C)`
- `isControllable(A, B)`
- `isObservable(A, C)`
- `feedbackGainStep(A, B, K)`
- `pidStep(error, previousError, integral, kp, ki, kd, dt)`

Test notes:

- Reuse matrix rank from linear algebra.
- Test small systems with known controllability.

## 43. Convex Analysis

Purpose:

- Support convex sets, convex functions, and subgradient-style tools.

Core objects:

- Convex combinations
- Convex sets
- Convex functions
- Supporting hyperplanes

Candidate additions:

- `convexCombination(points, weights)`
- `isConvexSet(points, membershipFunction, samples)`
- `isConvexFunctionOnSamples(values)`
- `subgradientAbsoluteValue(x)`
- `supportFunction(points, direction)`
- `projectionOntoInterval(x, lower, upper)`
- `projectionOntoSimplex(vector)`
- `jensensInequalityCheck(f, points, weights)`

Test notes:

- Test weight normalization and nonnegative weights.
- Use simple intervals and quadratic functions.

## 44. Calculus of Variations

Purpose:

- Study functionals and extremizing curves through numerical approximations.

Core objects:

- Functionals
- Paths
- Euler-Lagrange equations
- Variations

Candidate additions:

- `functionalPathIntegral(lagrangian, path, tValues)`
- `variationPath(path, perturbation, epsilon)`
- `firstVariation(functional, path, perturbation)`
- `eulerLagrangeResidual(lagrangian, path, tValues)`
- `shortestPathFunctional(path)`
- `energyFunctional(path)`
- `gradientDescentPath(functional, path, step, iterations)`
- `brachistochroneResidual(path)`

Test notes:

- Use straight-line paths for shortest-path examples.
- Make discretization explicit.

## 45. Optimal Transport

Purpose:

- Compare distributions through transport costs.

Core objects:

- Discrete measures
- Cost matrices
- Couplings
- Wasserstein distance

Candidate additions:

- `isCoupling(coupling, source, target)`
- `transportCost(coupling, costMatrix)`
- `greedyTransport(source, target, costMatrix)`
- `wasserstein1D(sourceValues, targetValues, weightsA=None, weightsB=None)`
- `earthMoversDistance1D(source, target)`
- `normalizeMeasure(weights)`
- `costMatrix(pointsA, pointsB, metric="euclidean")`
- `barycenterDiscrete(distributions, weights)`

Test notes:

- Test mass conservation.
- Start with one-dimensional exact examples.

## 46. Numerical Linear Algebra

Purpose:

- Add stable computational methods for matrices beyond symbolic-style formulas.

Core objects:

- Matrix decompositions
- Iterative solvers
- Conditioning
- Orthogonality

Candidate additions:

- `luDecomposition(matrix)`
- `qrDecomposition(matrix)`
- `choleskyDecomposition(matrix)`
- `powerIteration(matrix, iterations)`
- `conditionNumber(matrix)`
- `jacobiSolve(A, b, iterations)`
- `gaussSeidelSolve(A, b, iterations)`
- `gramSchmidt(vectors)`

Test notes:

- Test reconstruction identities such as `A == L * U`.
- Use tolerance-based comparisons.

## 47. Approximation Theory

Purpose:

- Approximate functions with polynomials, splines, and basis expansions.

Core objects:

- Polynomial approximants
- Interpolation nodes
- Approximation error
- Orthogonal polynomials

Candidate additions:

- `leastSquaresPolynomial(points, degree)`
- `chebyshevNodes(a, b, n)`
- `chebyshevPolynomial(n, x)`
- `legendrePolynomial(n, x)`
- `approximationErrorSamples(f, g, points)`
- `minimaxApproximationStep(f, degree, points)`
- `bernsteinPolynomial(fValues, n, x)`
- `piecewiseLinearApproximation(points, x)`

Test notes:

- Test interpolation exactness at nodes.
- Compare low-degree known polynomials.

## 48. Wavelet Theory

Purpose:

- Add multiresolution analysis for finite signals.

Core objects:

- Scaling functions
- Wavelets
- Filter banks
- Multilevel decompositions

Candidate additions:

- `haarTransform(values)`
- `inverseHaarTransform(coefficients)`
- `haarApproximation(values, level)`
- `waveletEnergy(coefficients)`
- `thresholdCoefficients(coefficients, threshold)`
- `multiLevelHaar(values, levels)`
- `reconstructMultiLevelHaar(data)`
- `detailCoefficients(values)`

Test notes:

- Test round-trip transform and inverse.
- Validate power-of-two length requirements.

## 49. Splines and Computer-Aided Geometric Design

Purpose:

- Support piecewise polynomial curves and geometric modeling.

Core objects:

- Bezier curves
- B-splines
- Control points
- Knot vectors

Candidate additions:

- `bezierPoint(controlPoints, t)`
- `deCasteljau(controlPoints, t)`
- `bezierDerivative(controlPoints, t)`
- `bernsteinBasis(n, i, t)`
- `bsplineBasis(i, degree, knots, t)`
- `bsplinePoint(controlPoints, degree, knots, t)`
- `catmullRomPoint(points, t)`
- `curveSubdivision(controlPoints)`

Test notes:

- Test endpoint interpolation for Bezier curves.
- Validate knot vector lengths.

## 50. Matroid Theory

Purpose:

- Generalize independence from linear algebra and graph theory.

Core objects:

- Ground sets
- Independent sets
- Circuits
- Bases
- Rank functions

Candidate additions:

- `isMatroid(groundSet, independentSets)`
- `matroidRank(subset, independentSets)`
- `matroidBases(groundSet, independentSets)`
- `matroidCircuits(groundSet, independentSets)`
- `isIndependentMatroid(subset, independentSets)`
- `dualMatroidBases(groundSet, bases)`
- `graphicMatroid(graph)`
- `greedyMatroidOptimization(groundSet, independentSets, weights)`

Test notes:

- Verify hereditary and exchange axioms.
- Test uniform and graphic matroids.

---

# Suggested implementation order

1. Fix statistics correctness and ship commented-out statistics helpers.
2. Add missing tests for trigonometry, probability, complex numbers, roots,
   conversions, and variance.
3. Build shared complex parsing and formatting helpers, then expand complex
   arithmetic.
4. Expand number theory with `gcd`, `lcm`, factorization, modular arithmetic,
   and totient.
5. Add core linear algebra utilities such as identity matrices, trace, inverse,
   rank, and solving linear systems.
6. Add graph theory basics to support future topology and homotopy examples.
7. Implement numerical analysis root-finding and interpolation helpers.
8. Start Real Analysis with finite/numerical sequence and series helpers.
9. Add Type Theory using a simple expression representation.
10. Add Homotopy Theory and Knot Theory after their representations are
    documented with examples.
11. Add the cross-cutting validators and numerical tolerance helpers before
    implementing large advanced areas.
12. Build finite algebra, finite topology, graph, matrix, and probability
    foundations that can be reused by the 50 additional research areas.
