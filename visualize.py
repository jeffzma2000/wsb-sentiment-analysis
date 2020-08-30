from wsb_plot import plot_scores
from wsb_scraper import scrape_for

results = scrape_for('tsla', 30)
plot_scores(results, 'TSLA Sentiment Scores', 'TSLA')