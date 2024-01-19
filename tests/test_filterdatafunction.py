"""
Test filtering function
"""

import unittest
import pandas as pd
from scripts.processing import filtering_


class TestFilterDataFunction(unittest.TestCase):
    """ 
    Class to test the function that performs FilterData in main
    """

    def setUp(self):
        data = {
            "Genre": ["Adventure", "Action", "Adventure", "Drama"],
            "Year": [2010, 2008, 2002, 2005],
        }
        self.df = pd.DataFrame(data)

    def test_filter_by_year(self):
        """
        Test to see if the result filters by year
        """
        result_df = filtering_(self.df, year=2010)
        assert result_df.shape[0] == 1

    def test_filter_by_genre(self):
        """
        Test to see if the results filters by genre
        """
        result_df = filtering_(self.df, fgenre="Adventure")
        assert result_df.shape[0] == 2


if __name__ == "__main__":
    unittest.main()
