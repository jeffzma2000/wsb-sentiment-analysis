import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data
import pandas as pd

def get_mean(df):

    mean_scores = df.groupby(['Date']).mean()
    mean_scores = mean_scores.xs('compound', axis="columns").transpose()

    return mean_scores

def plot_scores(df, title, symbol):

    mean_scores = get_mean(df)
    

    start = df['Date'].min()
    end = df['Date'].max()
    stock_output = get_historical_data(symbol, start, end, output_format='pandas')

    plt.rcParams['figure.figsize'] = [10, 6]

    ax = mean_scores.plot(kind='bar')
    ax2 = stock_output['close'].plot(secondary_y=True, use_index=False)

    plt.xticks(rotation=45)
    plt.xlabel('Date')
    ax.set_ylabel('Sentiment')
    ax2.set_ylabel('Price')
    plt.title(title)
    plt.show()

