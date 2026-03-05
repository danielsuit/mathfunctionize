import unittest
import sys
import os
from mathfunctionize import mathfunctionize
class TestCounting(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual(mathfunctionize.permutations(5, 3), 60)

    def test_circularPermutations(self):
        self.assertEqual(mathfunctionize.circularPermutations(4), 6)

    def test_derangements(self):
        self.assertEqual(mathfunctionize.derangements(3), 2)
        self.assertEqual(mathfunctionize.derangements(4), 9)

    def test_combinations(self):
        self.assertEqual(mathfunctionize.combinations(5, 3), 10)
    def test_gamma(self):
        self.assertEqual(mathfunctionize.gamma(5), 24)
        self.assertAlmostEqual(mathfunctionize.gamma(5.5), 52.34277778455352, places=5)
        self.assertAlmostEqual(mathfunctionize.gamma(.5), 1.7724538509055159, places=5)
        self.assertAlmostEqual(mathfunctionize.gamma(1.5), 0.8862269254527579, places=5)
        self.assertAlmostEqual(mathfunctionize.gamma(2.5), 1.329340388179137, places=5)

class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(mathfunctionize.addition([1, 2]), 3)
        self.assertEqual(mathfunctionize.addition([1, 2, 3]), 6)

    def test_subtraction(self):
        self.assertEqual(mathfunctionize.subtraction([5, 3]), 2)
        self.assertEqual(mathfunctionize.subtraction([10, 3, 2]), 5)

    def test_multiplication(self):
        self.assertEqual(mathfunctionize.multiplication([3, 4]), 12)
        self.assertEqual(mathfunctionize.multiplication([2, 3, 4]), 24)

    def test_division(self):
        self.assertEqual(mathfunctionize.division([10, 2]), 5)
        self.assertEqual(mathfunctionize.division([100, 5, 2]), 10)

    def test_power(self):
        self.assertEqual(mathfunctionize.power([2, 3]), 8)

    def test_modulo(self):
        self.assertEqual(mathfunctionize.modulo([10, 3]), 1)

    def test_flatDivision(self):
        self.assertEqual(mathfunctionize.flatDivision([10, 3]), 3)

    def test_factorial(self):
        self.assertEqual(mathfunctionize.factorial(5), 120)

    def test_absolute(self):
        self.assertEqual(mathfunctionize.absolute(-5), 5)

    def test_rounding(self):
        self.assertEqual(mathfunctionize.round(94.2, 1), 94)

class TestArrayOperations(unittest.TestCase):
    def test_localMinimum(self):
        self.assertEqual(mathfunctionize.localMinimum([1,2,3,4,5,6,7,8,9,10]), [1, [0]])
        self.assertEqual(mathfunctionize.localMinimum([10,9,8,7,6,5,4,3,2,1]), [1, [9]])
        self.assertEqual(mathfunctionize.localMinimum([1,2,3,4,5,6,5,4,3,2,1]), [2, [0, 10]])
        self.assertEqual(mathfunctionize.localMinimum([1]), [1, [0]])

    def test_localMaximum(self):
        self.assertEqual(mathfunctionize.localMaximum([1,2,3,4,5,6,7,8,9,10]), [1, [9]])
        self.assertEqual(mathfunctionize.localMaximum([10,9,8,7,6,5,4,3,2,1]), [1, [0]])
        self.assertEqual(mathfunctionize.localMaximum([1,2,3,4,5,6,5,4,3,2,1]), [1, [5]])
        self.assertEqual(mathfunctionize.localMaximum([1]), [1, [0]])

    def test_globalMinimum(self):
        self.assertEqual(mathfunctionize.globalMinimum([1,2,3,4,5,6,7,8,9,10]), [1, [0]])
        self.assertEqual(mathfunctionize.globalMinimum([10,9,8,7,6,5,4,3,2,1]), [1, [9]])

    def test_globalMaximum(self):
        self.assertEqual(mathfunctionize.globalMaximum([1,2,3,4,5,6,7,8,9,10]), [10, [9]])

    def test_mode(self):
        self.assertEqual(mathfunctionize.mode([1,2,3,4,5,6,7,8,9,10]), 1)
        self.assertEqual(mathfunctionize.mode([1,2,3,4,5,6,7,8,9,10,1]), 1)
        self.assertEqual(mathfunctionize.mode([1,2,3,4,5,6,7,8,9,10,2]), 2)

class TestMatrixOperations(unittest.TestCase):
    def test_determinant(self):
        self.assertEqual(mathfunctionize.determinant([[1,2],[3,4]]), -2)
        self.assertEqual(mathfunctionize.determinant([[1,2,3],[4,5,6],[7,8,9]]), 0)

    def test_transpose(self):
        self.assertEqual(mathfunctionize.transpose([[1,2],[3,4]]), [[1,3],[2,4]])
        self.assertEqual(mathfunctionize.transpose([[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]])
        self.assertEqual(mathfunctionize.transpose([[1,2,3],[4,5,6],[7,8,9]]), [[1,4,7],[2,5,8],[3,6,9]])

    def test_additionMatrix(self):
        self.assertEqual(mathfunctionize.additionMatrix([[1,2],[3,4]], [[5,6],[7,8]]), [[6,8],[10,12]])

    def test_subtractionMatrix(self):
        self.assertEqual(mathfunctionize.subtractionMatrix([[1,2],[3,4]], [[5,6],[7,8]]), [[-4,-4],[-4,-4]])

    def test_multiplicationMatrix(self):
        self.assertEqual(mathfunctionize.multiplicationMatrix([[1,2],[3,4]], [[5,6],[7,8]]), [[19,22],[43,50]])

class TestStatistics(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mathfunctionize.mean([1,2,3,4,5]), 3)

    def test_median(self):
        self.assertEqual(mathfunctionize.median([1,2,3,4,5]), 3)
        self.assertEqual(mathfunctionize.median([1,2,3,4,5,6]), 3.5)

    def test_standardDeviation(self):
        self.assertAlmostEqual(mathfunctionize.standardDevation([1,2,3,4,5]), 1.41421356237, places=5)
        self.assertAlmostEqual(mathfunctionize.standardDevation([1,2,3,4,5,6]), 1.70782512766, places=5)

    def test_mode(self):
        self.assertEqual(mathfunctionize.mode([1,2,2,3,4]), 2)

class TestSetTheory(unittest.TestCase):
    def test_set(self):
        self.assertEqual(mathfunctionize.set([1,2,2,3,3,3]), [1,2,3])
        self.assertEqual(mathfunctionize.set([1,1,1,1]), [1])
        self.assertEqual(mathfunctionize.set([1,2,3]), [1,2,3])
        self.assertEqual(mathfunctionize.set([]), [])

    def test_union(self):
        self.assertEqual(mathfunctionize.union([1,2,3], [3,4,5]), [1,2,3,4,5])
        self.assertEqual(mathfunctionize.union([1,2], [3,4]), [1,2,3,4])
        self.assertEqual(mathfunctionize.union([], [1,2]), [1,2])
        self.assertEqual(mathfunctionize.union([1,2], []), [1,2])

    def test_intersection(self):
        self.assertEqual(mathfunctionize.intersection([1,2,3], [2,3,4]), [2,3])
        self.assertEqual(mathfunctionize.intersection([1,2], [3,4]), [])
        self.assertEqual(mathfunctionize.intersection([1,2,3], [1,2,3]), [1,2,3])

    def test_difference(self):
        self.assertEqual(mathfunctionize.difference([1,2,3,4], [2,4]), [1,3])
        self.assertEqual(mathfunctionize.difference([1,2,3], [4,5,6]), [1,2,3])
        self.assertEqual(mathfunctionize.difference([1,2,3], [1,2,3]), [])

    def test_symmetricDifference(self):
        self.assertEqual(mathfunctionize.symmetricDifference([1,2,3], [2,3,4]), [1,4])
        self.assertEqual(mathfunctionize.symmetricDifference([1,2], [3,4]), [1,2,3,4])
        self.assertEqual(mathfunctionize.symmetricDifference([1,2,3], [1,2,3]), [])

    def test_powerSet(self):
        self.assertEqual(mathfunctionize.powerSet([1,2]), [[], [1], [2], [1,2]])
        self.assertEqual(mathfunctionize.powerSet([]), [[]])

    def test_isOpenSet(self):
        self.assertEqual(mathfunctionize.isOpenSet([1,2], [1,2,3,4]), True)
        self.assertEqual(mathfunctionize.isOpenSet([1,5], [1,2,3,4]), False)
        self.assertEqual(mathfunctionize.isOpenSet([], [1,2,3]), True)

    def test_cartesianProduct(self):
        self.assertEqual(mathfunctionize.cartesianProduct([1,2], [3,4]), [[1,3],[1,4],[2,3],[2,4]])
        self.assertEqual(mathfunctionize.cartesianProduct([1], [2,3]), [[1,2],[1,3]])
        self.assertEqual(mathfunctionize.cartesianProduct([], [1,2]), [])

    def test_isMemberOfSet(self):
        self.assertEqual(mathfunctionize.isMemberOfSet(1, [1,2,3]), True)
        self.assertEqual(mathfunctionize.isMemberOfSet(5, [1,2,3]), False)
        self.assertEqual(mathfunctionize.isMemberOfSet(1, []), False)

    def test_isSubset(self):
        self.assertEqual(mathfunctionize.isSubset([1,2], [1,2,3]), True)
        self.assertEqual(mathfunctionize.isSubset([1,4], [1,2,3]), False)
        self.assertEqual(mathfunctionize.isSubset([], [1,2,3]), True)
        self.assertEqual(mathfunctionize.isSubset([1,2,3], [1,2,3]), True)

    def test_setEquality(self):
        self.assertEqual(mathfunctionize.setEquality([1,2,3], [3,2,1]), True)
        self.assertEqual(mathfunctionize.setEquality([1,2,3], [1,2]), False)
        self.assertEqual(mathfunctionize.setEquality([1,2], [1,2,3]), False)
        self.assertEqual(mathfunctionize.setEquality([], []), True)

    def test_complement(self):
        self.assertEqual(mathfunctionize.complement([1,2], [1,2,3,4,5]), [3,4,5])
        self.assertEqual(mathfunctionize.complement([], [1,2,3]), [1,2,3])
        self.assertEqual(mathfunctionize.complement([1,2,3], [1,2,3]), [])

    def test_cardinality(self):
        self.assertEqual(mathfunctionize.cardinality([1,2,3]), 3)
        self.assertEqual(mathfunctionize.cardinality([]), 0)
        self.assertEqual(mathfunctionize.cardinality([1]), 1)

    def test_isProperSubset(self):
        self.assertEqual(mathfunctionize.isProperSubset([1,2], [1,2,3]), True)
        self.assertEqual(mathfunctionize.isProperSubset([1,2,3], [1,2,3]), False)
        self.assertEqual(mathfunctionize.isProperSubset([], [1]), True)
        self.assertEqual(mathfunctionize.isProperSubset([], []), False)

    def test_isSuperset(self):
        self.assertEqual(mathfunctionize.isSuperset([1,2,3], [1,2]), True)
        self.assertEqual(mathfunctionize.isSuperset([1,2], [1,2,3]), False)
        self.assertEqual(mathfunctionize.isSuperset([1,2,3], [1,2,3]), True)

    def test_isProperSuperset(self):
        self.assertEqual(mathfunctionize.isProperSuperset([1,2,3], [1,2]), True)
        self.assertEqual(mathfunctionize.isProperSuperset([1,2,3], [1,2,3]), False)
        self.assertEqual(mathfunctionize.isProperSuperset([1], [1,2]), False)

    def test_isDisjoint(self):
        self.assertEqual(mathfunctionize.isDisjoint([1,2], [3,4]), True)
        self.assertEqual(mathfunctionize.isDisjoint([1,2], [2,3]), False)
        self.assertEqual(mathfunctionize.isDisjoint([], [1,2]), True)

    def test_isEmpty(self):
        self.assertEqual(mathfunctionize.isEmpty([]), True)
        self.assertEqual(mathfunctionize.isEmpty([1]), False)
        self.assertEqual(mathfunctionize.isEmpty([1,2,3]), False)

class TestZFCSetTheory(unittest.TestCase):
    def test_extensionality(self):
        self.assertEqual(mathfunctionize.extensionality([1,2,3], [3,2,1]), True)
        self.assertEqual(mathfunctionize.extensionality([1,2], [1,2,3]), False)
        self.assertEqual(mathfunctionize.extensionality([], []), True)

    def test_emptySet(self):
        self.assertEqual(mathfunctionize.emptySet(), [])

    def test_pairing(self):
        self.assertEqual(mathfunctionize.pairing(1, 2), [1, 2])
        self.assertEqual(mathfunctionize.pairing([1], [2]), [[1], [2]])

    def test_axiomOfUnion(self):
        self.assertEqual(mathfunctionize.axiomOfUnion([[1,2], [3,4]]), [1,2,3,4])
        self.assertEqual(mathfunctionize.axiomOfUnion([[1,2], [2,3]]), [1,2,3])
        self.assertEqual(mathfunctionize.axiomOfUnion([[], [1]]), [1])
        self.assertEqual(mathfunctionize.axiomOfUnion([]), [])

    def test_separation(self):
        self.assertEqual(mathfunctionize.separation([1,2,3,4,5], lambda x: x > 3), [4,5])
        self.assertEqual(mathfunctionize.separation([1,2,3,4,5], lambda x: x % 2 == 0), [2,4])
        self.assertEqual(mathfunctionize.separation([], lambda x: x > 0), [])

    def test_replacement(self):
        self.assertEqual(mathfunctionize.replacement([1,2,3], lambda x: x * 2), [2,4,6])
        self.assertEqual(mathfunctionize.replacement([1,2,3,4], lambda x: x % 2), [1,0])
        self.assertEqual(mathfunctionize.replacement([], lambda x: x), [])

    def test_infinitySet(self):
        self.assertEqual(mathfunctionize.infinitySet(0), [])
        self.assertEqual(mathfunctionize.infinitySet(1), [[]])
        self.assertEqual(mathfunctionize.infinitySet(2), [[], [[]]])
        self.assertEqual(mathfunctionize.infinitySet(3), [[], [[]], [[], [[]]]])

    def test_regularity(self):
        self.assertEqual(mathfunctionize.regularity([1,2,3]), True)
        self.assertEqual(mathfunctionize.regularity([]), True)

    def test_axiomOfChoice(self):
        self.assertEqual(mathfunctionize.axiomOfChoice([[1,2], [3,4], [5,6]]), [1,3,5])
        self.assertEqual(mathfunctionize.axiomOfChoice([[10], [20]]), [10,20])
        with self.assertRaises(Exception):
            mathfunctionize.axiomOfChoice([[1,2], []])

class TestMetricSpaces(unittest.TestCase):
    def test_dist_euclidean(self):
        self.assertAlmostEqual(mathfunctionize.dist([0,0], [3,4]), 5.0, places=5)
        self.assertAlmostEqual(mathfunctionize.dist([1,2,3], [1,2,3]), 0.0, places=5)

    def test_dist_manhattan(self):
        self.assertEqual(mathfunctionize.dist([0,0], [3,4], "manhattan"), 7)
        self.assertEqual(mathfunctionize.dist([1,1], [4,5], "manhattan"), 7)

    def test_dist_chebyshev(self):
        self.assertEqual(mathfunctionize.dist([0,0], [3,4], "chebyshev"), 4)
        self.assertEqual(mathfunctionize.dist([1,1], [4,5], "chebyshev"), 4)

    def test_isMetricSpace(self):
        def eucl(a, b):
            return mathfunctionize.dist(a, b, "euclidean")
        S = [[0,0], [1,0], [0,1]]
        self.assertEqual(mathfunctionize.isMetricSpace(eucl, S), True)

        def bad_metric(a, b):
            return -1
        self.assertEqual(mathfunctionize.isMetricSpace(bad_metric, S), False)

class TestCalculus(unittest.TestCase):
    def test_derivative(self):
        self.assertAlmostEqual(mathfunctionize.derivative(lambda x: x**2, 3), 6.0, places=3)
        self.assertAlmostEqual(mathfunctionize.derivative(lambda x: x**3, 2), 12.0, places=3)

    def test_limit(self):
        self.assertAlmostEqual(mathfunctionize.limit(lambda x: x**2, None, 3), 9.0, places=3)

    def test_concavity(self):
        self.assertEqual(mathfunctionize.concavity(lambda x: x**2, 0), "concave up")
        self.assertEqual(mathfunctionize.concavity(lambda x: -(x**2), 0), "concave down")

    def test_integral(self):
        self.assertAlmostEqual(mathfunctionize.integral(lambda x: x**2, 0, 1), 1/3, places=3)
        self.assertAlmostEqual(mathfunctionize.integral(lambda x: x, 0, 10), 50.0, places=3)

    def test_continuity(self):
        self.assertEqual(mathfunctionize.continuity(lambda x: x**2, 2), True)

class TestComplexAnalysis(unittest.TestCase):
    def test_conjugate(self):
        self.assertEqual(mathfunctionize.conjugate("3+4i"), "3-4i")
        self.assertEqual(mathfunctionize.conjugate("3-4i"), "3+4i")

    def test_rootsOfUnity(self):
        roots = mathfunctionize.rootsOfUnity(4)
        self.assertEqual(len(roots), 4)
        self.assertEqual(roots[0], "1.0+0.0i")

class TestNumberTheory(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(mathfunctionize.isPrime(2), True)
        self.assertEqual(mathfunctionize.isPrime(3), True)
        self.assertEqual(mathfunctionize.isPrime(4), False)
        self.assertEqual(mathfunctionize.isPrime(17), True)
        self.assertEqual(mathfunctionize.isPrime(1), False)
        self.assertEqual(mathfunctionize.isPrime(0), False)
        self.assertEqual(mathfunctionize.isPrime(-5), False)

class TestTopology(unittest.TestCase):
    def test_smooth(self):
        self.assertEqual(mathfunctionize.smooth(lambda x: x**2, 1), True)
        self.assertEqual(mathfunctionize.smooth(lambda x: mathfunctionize.sine(x), 0), True)

class TestPolynomials(unittest.TestCase):
    def test_polyEval(self):
        self.assertEqual(mathfunctionize.polyEval([1, 0, -1], 2), 3)
        self.assertEqual(mathfunctionize.polyEval([1, -3, 2], 1), 0)

    def test_divide(self):
        quot, rem = mathfunctionize.divide([1, -3, 2], [1, -1])
        self.assertAlmostEqual(quot[0], 1.0, places=5)
        self.assertAlmostEqual(quot[1], -2.0, places=5)
        self.assertTrue(all(abs(r) < 1e-10 for r in rem))

    def test_zeros(self):
        self.assertEqual(mathfunctionize.zeros([1, -3]), [3.0])
        roots = mathfunctionize.zeros([1, -3, 2])
        self.assertIn(1, roots)
        self.assertIn(2, roots)

    def test_factor(self):
        factors = mathfunctionize.factor([1, -3, 2])
        self.assertEqual(len(factors), 2)

if __name__ == '__main__':
    unittest.main()