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

    def filter_by_genre(self, fgenre):
        """
        Filter data by a given genre
        """
        return self.df[self.df["Genre"] == fgenre]

    def filter_by_tickets(self, tickets):
        """
        Filter data by a given tickets sold
        """
        return self.df[self.df["Tickets Sold"] > tickets]
