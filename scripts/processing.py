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


@click.command(short_help="Parser to manage inputs for FilmGenreStats")
@click.option("-id", "--input_data", required=True, help="Path to my Input dataset")
@click.option("-o", "--output", default="outputs", help="Folder to save all outputs")
@click.option("-a", "--analysis", is_flag=True, help="Analyse the data or not")


def main(input_data, output, analysis):
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
    

    

