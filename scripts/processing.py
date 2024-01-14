"""
Process FilmGenreStats dataset
"""

import pandas as pd 
import click
import matplotlib.pyplot as plt
import os

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
        self.df['Genre'].value_counts().plot(kind='bar')
        plt.title('Distribution of Movies Across Different Genres')
        plt.xlabel('Genre')
        plt.ylabel('Number of Movies')

    def analyze_average_gross_by_genre(self):
        """
        Analyze and visualize the average gross for each movie genre.
        """
        genre_stats = self.df.groupby('Genre')['Gross'].mean()
        plt.figure(figsize=(12, 6))
        genre_stats.sort_values(ascending=False).plot(kind='bar')
        plt.title('Average Gross for Each Genre')
        plt.xlabel('Genre')
        plt.ylabel('Average Gross')

    def analyze_average_tickets_by_genre(self):
        """
        Analyze and visualize the average tickets sold for each movie genre.
        """
        genre_stats = self.df.groupby('Genre')['Tickets Sold'].mean()
        plt.figure(figsize=(12, 6))
        genre_stats.sort_values(ascending=False).plot(kind='bar', color='orange')
        plt.title('Average Tickets Sold for Each Genre')
        plt.xlabel('Genre')
        plt.ylabel('Average Tickets Sold')

    def perform_analysis(self, analysis_type):
        """
        Perform the specified analysis based on the provided analysis type.
        """
        if analysis_type == 'distribution':
            self.explore_movie_distribution_by_genre()
        elif analysis_type == 'average gross':
            self.analyze_average_gross_by_genre()
        elif analysis_type == 'average ts':
            self.analyze_average_tickets_by_genre()
        else:
            print(f"Unknown analysis type: {analysis_type}")


@click.command(short_help="Parser to manage inputs for FilmGenreStats")
@click.option("-id", "--input_data", required=True, help="Path to my Input dataset")
@click.option("-o", "--output", default="outputs", help="Folder to save all outputs")
@click.option("-a", "--analysis", is_flag=True, help="Analyse the data or not")
@click.option("-g", "--genre", type=str, help="Type of movie analysis (distribution, average, popular_genre)")


def main(input_data, output, analysis, genre):
    """
    Deal with the input data and send it to other function
    """
    print("Here second")
    print(f"This is my input data variable:{input_data}")
    try:
        df = pd.read_csv(input_data)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error Reading the file: {e}")
    
    if analysis:
        print("I am analysing")

    try:
        df.to_csv(f"{output}/FilmGenreStatsAnalysis.csv", index=None)
    except Exception as e:
        if not os.path.exists(output):
            os.makedirs(output)
        df.to_csv(f"{output}/FilmGenreStatsAnalysis.csv", index=None)

if __name__=="__main__":
    print("Step 2")
    main()
    

    

