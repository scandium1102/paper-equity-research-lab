import unittest
from datetime import date

from freshness import Observation, select_observation


class FreshnessTests(unittest.TestCase):
    def test_official_priority_and_fallback(self):
        today = date(2026, 1, 10)
        official = Observation("official", date(2026, 1, 6), "exchange fixture")
        secondary = Observation("secondary", date(2026, 1, 9), "secondary fixture")
        future = Observation("official", date(2026, 1, 11), "future fixture")
        self.assertEqual(select_observation([future, official, secondary], today, 4), official)
        self.assertEqual(select_observation([future, official, secondary], today, 3), secondary)
        self.assertIsNone(select_observation([future, official, secondary], today, 0))


if __name__ == "__main__":
    unittest.main()
