import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit - all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create years for prediction
    years_extended = pd.Series(range(1880, 2051))
    line1 = slope * years_extended + intercept
    ax.plot(years_extended, line1, 'r', label='Best fit 1880-2050')

    # Second line of best fit - from 2000
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, std2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    years_recent = pd.Series(range(2000, 2051))
    line2 = slope2 * years_recent + intercept2
    ax.plot(years_recent, line2, 'green', label='Best fit 2000-2050')

    # Labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save
    plt.savefig('sea_level_plot.png')
    return fig
