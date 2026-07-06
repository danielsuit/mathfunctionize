import unittest

from mathfunctionize import mathfunctionize, upcoming


class TestUpcomingRoadmapCode(unittest.TestCase):
    def test_professional_catalog_counts_are_in_code(self):
        catalog_entries = [
            entry
            for entry in upcoming.UPCOMING_FUNCTION_ENTRIES
            if entry.source == "professional_function_catalog.md"
        ]
        catalog_topics = {}
        for entry in catalog_entries:
            catalog_topics.setdefault(entry.topic, set()).add(entry.name)

        self.assertEqual(len(catalog_topics), 86)
        self.assertEqual(len(catalog_entries), 8600)
        self.assertTrue(all(len(names) == 100 for names in catalog_topics.values()))

    def test_upcoming_md_function_mentions_are_in_code(self):
        self.assertTrue(upcoming.is_upcoming_function("gcd"))
        self.assertTrue(hasattr(mathfunctionize, "gcd"))
        with self.assertRaises(upcoming.UpcomingFunctionNotImplemented):
            mathfunctionize.gcd(12, 8)

    def test_professional_catalog_function_is_callable_placeholder(self):
        name = "measureTheoryValidateSigmaAlgebra"
        self.assertTrue(upcoming.is_upcoming_function(name))
        self.assertIn(name, upcoming.list_upcoming_functions("Measure Theory"))
        self.assertTrue(hasattr(mathfunctionize, name))

        with self.assertRaises(upcoming.UpcomingFunctionNotImplemented):
            getattr(mathfunctionize, name)([])

    def test_existing_functions_are_not_overwritten(self):
        self.assertEqual(mathfunctionize.addition([1, 2, 3]), 6)
        self.assertNotIsInstance(
            mathfunctionize.addition,
            upcoming.UpcomingFunctionNotImplemented,
        )


if __name__ == "__main__":
    unittest.main()
