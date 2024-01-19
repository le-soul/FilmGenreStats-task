"""
Process FilmGenreStats dataset
"""
# pylint:disable=E1120
import os
import sys
import click
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append("scripts")
from genreanalysis import GenreAnalysis
from filterdata import FilterData


def filtering_(df, year=None, fgenre=None, tickets=None):
    """
    Function to filter by year and genre
    """
    if year:
        df = FilterData(df).filter_by_year(year)

    elif fgenre:
        df = FilterData(df).filter_by_genre(fgenre)

    elif tickets:
        df = FilterData(df).filter_by_tickets(tickets)

    print(df.head())
    print(df.shape)
    return df


def analysis_(df, genre, output):
    """
    Function to analyse and save the dataframe with graphs
    """
    if genre:
        GenreAnalysis(df).perform_analysis(genre)
        if not os.path.exists(output):
            os.makedirs(output)

        if genre == "distribution":
            plt.savefig(f"{output}/DistributionPlot.png")
        elif genre == "average gross":
            plt.savefig(f"{output}/AverageGrossforEachGenre.png")
        elif genre == "average ts":
            plt.savefig(f"{output}/AverageTicketsSoldforEachGenre.png")


@click.command(short_help="Parser to manage inputs for FilmGenreStats")
@click.option("-id", "--input_data", required=True, help="Path to my Input dataset")
@click.option("-o", "--output", default="outputs", help="Folder to save all outputs")
@click.option("-a", "--analysis", is_flag=True, help="Analyse the data or not")
@click.option("-g","--genre", type=str, help="Type of movie analysis (distribution, average, popular_genre)")
@click.option("-f", "--filtering", is_flag=True, help="Set a filtering or not")
@click.option("-y", "--year", type=int, help="Filter films by year")
@click.option("-fg", "--fgenre", type=str, help="Filter films by genre")
@click.option("-t", "--tickets", type=int, help="Filter films by tickets sold, more than")
def main(input_data, output, analysis, genre, filtering, year, fgenre, tickets):
    """
    Deal with the input data and send it to other function
    """
    print("Here second")
    print(f"This is my input data variable:{input_data}")
    try:
        df = pd.read_csv(input_data)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error Reading the file: {input_data}") from e

    if filtering:
        print("I am filtering")
        filtering_(df, year, fgenre, tickets)

    try:
        df.to_csv(f"{output}/FilmGenreStatsAnalysis.csv", index=None)
    except Exception:
        if not os.path.exists(output):
            os.makedirs(output)
        df.to_csv(f"{output}/FilmGenreStatsAnalysis.csv", index=None)

    if analysis:
        print("I am analysing")
        analysis_(df, genre, output)


if __name__ == "__main__":
    print("Step 2")
    main()
