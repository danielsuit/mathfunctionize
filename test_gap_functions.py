import unittest

from mathfunctionize import mathfunctionize, upcoming


class TestStatisticsGapFunctions(unittest.TestCase):
    def test_variance_and_sample_statistics(self):
        values = [2, 4, 4, 4, 5, 5, 7, 9]

        self.assertEqual(mathfunctionize.variance(values), 4)
        self.assertEqual(mathfunctionize.standardDeviation(values), 2)
        self.assertAlmostEqual(mathfunctionize.sampleVariance(values), 32 / 7)
        self.assertAlmostEqual(mathfunctionize.sampleStandardDeviation(values), (32 / 7) ** 0.5)

    def test_quartiles_percentile_and_correlation(self):
        values = [7, 1, 3, 5, 9]

        self.assertEqual(mathfunctionize.quartiles(values), [2.0, 5, 8.0])
        self.assertEqual(mathfunctionize.interquartileRange(values), 6.0)
        self.assertEqual(mathfunctionize.percentile([0, 10], 25), 2.5)
        self.assertEqual(mathfunctionize.zScore(14, 10, 2), 2)
        self.assertEqual(mathfunctionize.covariance([1, 2, 3], [2, 4, 6]), 4 / 3)
        self.assertAlmostEqual(mathfunctionize.correlation([1, 2, 3], [2, 4, 6]), 1)


class TestProbabilityGapFunctions(unittest.TestCase):
    def test_distribution_helpers(self):
        self.assertEqual(mathfunctionize.bernoulliPMF(1, 0.25), 0.25)
        self.assertAlmostEqual(mathfunctionize.binomialPMF(2, 4, 0.5), 0.375)
        self.assertAlmostEqual(mathfunctionize.binomialCDF(1, 3, 0.5), 0.5)
        self.assertAlmostEqual(mathfunctionize.poissonPMF(2, 3), 0.22404180765538775)
        self.assertAlmostEqual(mathfunctionize.exponentialCDF(1, 2), 1 - (mathfunctionize.e ** -2))
        self.assertAlmostEqual(mathfunctionize.gammaPDF(2, 3, 2), 0.29305022221974686)

    def test_probability_summary_helpers(self):
        self.assertEqual(mathfunctionize.expectedValue([1, 2, 3], [0.2, 0.3, 0.5]), 2.3)
        self.assertEqual(mathfunctionize.conditionalProbability(0.2, 0.4), 0.5)
        self.assertTrue(mathfunctionize.independent(0.5, 0.5, 0.25))


class TestComplexGapFunctions(unittest.TestCase):
    def test_complex_arithmetic_and_polar_forms(self):
        self.assertEqual(mathfunctionize.parseComplex("3-4i"), [3.0, -4.0])
        self.assertEqual(mathfunctionize.formatComplex(3, -4), "3-4i")
        self.assertEqual(mathfunctionize.complex_addition("3+4i", "2-1i"), "5+3i")
        self.assertEqual(mathfunctionize.complex_subtraction("3+4i", "2-1i"), "1+5i")
        self.assertEqual(mathfunctionize.complex_multiplication("3+4i", "2-1i"), "10+5i")
        self.assertEqual(mathfunctionize.complex_division("3+4i", "1-2i"), "-1+2i")
        self.assertEqual(mathfunctionize.complex_modulus("3+4i"), 5)
        self.assertEqual(mathfunctionize.rectangularToPolar("1+0i")[0], 1)
        self.assertEqual(mathfunctionize.polarToRectangular(1, 0), "1+0i")


class TestNumberTheoryGapFunctions(unittest.TestCase):
    def test_number_theory_basics(self):
        self.assertEqual(mathfunctionize.gcd(54, 24), 6)
        self.assertEqual(mathfunctionize.lcm(6, 8), 24)
        self.assertEqual(mathfunctionize.extendedGcd(240, 46), [2, -9, 47])
        self.assertEqual(mathfunctionize.modularExponent(2, 10, 1000), 24)
        self.assertEqual(mathfunctionize.modInverse(3, 11), 4)
        self.assertEqual(mathfunctionize.primeFactors(84), [2, 2, 3, 7])
        self.assertEqual(mathfunctionize.sieve(10), [2, 3, 5, 7])
        self.assertEqual(mathfunctionize.eulerTotient(9), 6)
        self.assertTrue(mathfunctionize.isCoprime(14, 15))
        self.assertEqual(mathfunctionize.divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertTrue(mathfunctionize.isPerfectNumber(28))


class TestLinearAlgebraGapFunctions(unittest.TestCase):
    def test_matrix_and_vector_helpers(self):
        matrix = [[4, 7], [2, 6]]

        self.assertEqual(mathfunctionize.identityMatrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(mathfunctionize.trace(matrix), 10)
        self.assertEqual(mathfunctionize.matrixMinor(matrix, 0, 0), [[6]])
        self.assertEqual(mathfunctionize.cofactorMatrix(matrix), [[6, -2], [-7, 4]])
        self.assertEqual(mathfunctionize.inverseMatrix(matrix), [[0.6, -0.7], [-0.2, 0.4]])
        self.assertEqual(mathfunctionize.rank([[1, 2], [2, 4]]), 1)
        self.assertEqual(mathfunctionize.dotProduct([1, 2, 3], [4, 5, 6]), 32)
        self.assertEqual(mathfunctionize.crossProduct([1, 0, 0], [0, 1, 0]), [0, 0, 1])
        self.assertEqual(mathfunctionize.vectorNorm([3, 4]), 5)


class TestGapFunctionsReplacePlaceholders(unittest.TestCase):
    def test_implemented_gap_functions_do_not_raise_upcoming_placeholder(self):
        implemented_names = [
            "gcd",
            "quartiles",
            "complex_multiplication",
            "identityMatrix",
            "binomialPMF",
        ]

        for name in implemented_names:
            self.assertTrue(upcoming.is_upcoming_function(name))
            self.assertNotIn("planned mathfunctionize API", getattr(mathfunctionize, name).__doc__ or "")


if __name__ == "__main__":
    unittest.main()
