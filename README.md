# WSB Sentiment Analysis
![WSB logo](https://miro.medium.com/max/360/0*qNLy1P3pAfcivIbz)

## Idea

I scraped posts and comments with stock ticker information from r/wallstreetbets. I used this data to perform sentiment analysis on each submission to get an average sentiment for a stock at various timeframes. I matched this up with stock/option movements to try to infer future movements.

## Todo

* Conduct sentiment analysis.
  * Need to adjust for options terminology (i.e. puts, calls, bear, bull)
* Get average sentiment.
* Plot average sentiment as a function of time.
* Overlay stock/option movements on plot and test for correlation.
