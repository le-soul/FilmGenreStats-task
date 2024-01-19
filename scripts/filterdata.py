"""
Filtering by year and genre
"""


class FilterData:
    """
    Class to filter data by various criteria
    """

    def __init__(self, df):
        self.df = df

    def filter_by_year(self, year):
        """
        Filter data by a given year
        """
        return self.df[self.df["Year"] == year]

    def filter_by_genre(self, genre):
        """
        Filter data by a given genre
        """
        return self.df[self.df["Genre"] == genre]
