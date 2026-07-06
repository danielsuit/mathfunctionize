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
