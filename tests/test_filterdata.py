"""
Test filtering
"""

import unittest
import pandas as pd
from scripts.filterdata import FilterData


class TestFilterData(unittest.TestCase):
    """
    Class to test FilterData class
    """
    def setUp(self):
        data = {
            "Genre": ["Adventure", "Action", "Adventure", "Drama"],
            "Year": [2010, 2008, 2002, 2005],
        }
        self.df = pd.DataFrame(data)

    def test_filter_by_year(self):
        """
        Test to see if the function filter by year
        """
        filtered_df = FilterData(self.df).filter_by_year(2005)
        self.assertNotEqual(filtered_df.shape[0], 0)

    def test_filter_by_genre(self):
        """
        Test to see if the function filter by genre
        """
        filtered_df = FilterData(self.df).filter_by_genre("Adventure")
        self.assertNotEqual(filtered_df.shape[0], 0)


if __name__ == "__main__":
    unittest.main()
