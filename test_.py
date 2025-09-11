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
        self.assertEqual(mathfunctionize.addition(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(mathfunctionize.subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(mathfunctionize.multiplication(3, 4), 12)

    def test_division(self):
        self.assertEqual(mathfunctionize.division(10, 2), 5)

    def test_power(self):
        self.assertEqual(mathfunctionize.power(2, 3), 8)

    def test_modulo(self):
        self.assertEqual(mathfunctionize.modulo(10, 3), 1)

    def test_flatDivision(self):
        self.assertEqual(mathfunctionize.flatDivision(10, 3), 3)

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

if __name__ == '__main__':
    unittest.main()