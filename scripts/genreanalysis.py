"""
Analysis of genre with graphs
"""

import matplotlib.pyplot as plt


class GenreAnalysis:
    """
    Class for analyzing and visualizing movie genre statistics.
    """

    def __init__(self, df):
        self.df = df

    def explore_movie_distribution_by_genre(self):
        """
        Explore and visualize the distribution of movies across different genres.
        """
        plt.figure(figsize=(10, 6))
        self.df["Genre"].value_counts().plot(kind="bar")
        plt.title("Distribution of Movies Across Different Genres")
        plt.xlabel("Genre")
        plt.ylabel("Number of Movies")

    def analyze_average_gross_by_genre(self):
        """
        Analyze and visualize the average gross for each movie genre.
        """
        genre_stats = self.df.groupby("Genre")["Gross"].mean()
        plt.figure(figsize=(12, 6))
        genre_stats.sort_values(ascending=False).plot(kind="bar")
        plt.title("Average Gross for Each Genre")
        plt.xlabel("Genre")
        plt.ylabel("Average Gross")

    def analyze_average_tickets_by_genre(self):
        """
        Analyze and visualize the average tickets sold for each movie genre.
        """
        genre_stats = self.df.groupby("Genre")["Tickets Sold"].mean()
        plt.figure(figsize=(12, 6))
        genre_stats.sort_values(ascending=False).plot(kind="bar", color="orange")
        plt.title("Average Tickets Sold for Each Genre")
        plt.xlabel("Genre")
        plt.ylabel("Average Tickets Sold")

    def perform_analysis(self, analysis_type):
        """
        Perform the specified analysis based on the provided analysis type.
        """
        try:
            if analysis_type == "distribution":
                self.explore_movie_distribution_by_genre()
            elif analysis_type == "average gross":
                self.analyze_average_gross_by_genre()
            elif analysis_type == "average ts":
                self.analyze_average_tickets_by_genre()
            else:
                raise ValueError(f"Unknown analysis type: {analysis_type}")
        except ValueError as e:
            print(f"Error: {e}")
