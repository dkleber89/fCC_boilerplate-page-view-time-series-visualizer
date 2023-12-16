"""Visualizer Module for time series data"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=["date"], index_col="date")

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    """Draw line plot

    Returns:
        Figure: figure for tests
    """
    # Draw line plot
    fig, axes = plt.subplots(figsize=(10,5))

    axes.plot(df.index, df['value'])
    axes.set(
        title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
        ylabel="Page Views",
        xlabel="Date"
    )

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')

    return fig

def draw_bar_plot():
    """Draw Bar plot

    Returns:
        Figure: figure for tests
    """
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(10,7), legend=True, ylabel="Average Page Views", xlabel="Years").figure

    plt.legend([
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ])

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')

    return fig

def draw_box_plot():
    """Draw Box plot

    Returns:
        Figure: figure for tests
    """
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_sort'] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_sort")

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(figsize=(14, 5), nrows=1, ncols=2)

    axes[0] = sns.boxplot(y=df_box["value"], x=df_box["year"], ax = axes[0])
    axes[0].set(
        title='Year-wise Box Plot (Trend)',
        ylabel="Page Views",
        xlabel="Year"
    )

    axes[1] = sns.boxplot(y=df_box["value"], x=df_box["month"], ax = axes[1])
    axes[1].set(
        title='Month-wise Box Plot (Seasonality)',
        ylabel="Page Views",
        xlabel="Month"
    )

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')

    return fig
