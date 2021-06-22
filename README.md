# What's this?
A repository for reviewing strategy ideas implemented in [QunatCT App](https://app.quantct.com/). Each idea has the following documents:
 - A simply structured text file for introducing the idea and its formulation.
 - A pine script implementation for TradingView.
 - Some graphs and backtest performance metrics.

# What's the outcome?
The outcome of this work is to show that:
1. Strategy ideas used in [QuantCT App](https://app.quantct.com/) are profitable.
1. The probability of having a winning trade and it's expected(average) return, if using [QuantCT Screeners](https://app.quantct.com/screeners).

In addition, and built from those "Yes/No"s, we will have a valubale knowledge base of many trading ideas that PROBABLY won't work, along with some PROBABLY profitable ones!

# How ideas are tested?
## For Outcome (1)
We want to answer the following question by means of specific statistical tests: 

> Does this idea have any predictive power (i.e. profitability in future), with a "High Enough Probability" (HEP)?

The HEP here is 0.05 p-value, 0.95 significanse, above "+2 x Sigma" of histogram of mean returns, or simply 95% probability - All of them are same thing.

To do so, each strategy idea is backtested on BTCUSDT starting from 2018-01-01 (a big and available market crash on Binance exchange) to 2020-12-30.

Test details are as follows:
 - All tests have $ 100K on initial cash, and the order amount is 1 BTC.
 - A backtest is performed on the data mentioned above. Timeframe is based on what the idea suggests (mainly 1d and 4h). 
 - Applying "Monte Carlo Permutation" (MCP) test with 10,000 random (i.e. non profitable) tests on same data.
 - Giving a `Yes`, if the mean return of the implemented idea is above "+2 x Sigma" of histogram of mean returns of those 10K random tests, and a `No` otherwise.

## For outcome(2)
Right now, you can assess each strategy idea in tradingview, as implemented in [QuantCT App](https://app.quantct.com/), and review its win rate, profit factor, etc., and decide to wether use its signals or not for each coin.

In future releases, I will integrate such insightfull informations into the [QuantCT Screeners](https://app.quantct.com/screeners), so that you don't need to leave the app.

# Why the word "Idea"? 
The trading/strategy idea is merely Enter/Exit rules, without any risk/money management and without any optimization. If the bare idea is profitable, it has merit of strategy development and optimization efforts.

So, you should _NOT_ blindely follow screener or alert outputs. at least you should consider proper risk and money management for your trade setups.

I will publish several tutorial videos about how to properly use [QuantCT Screeners](https://app.quantct.com/screeners) on [QuantCT youtube channel](https://www.youtube.com/channel/UCmNmuYbCVWrCluVGqX4XMyA).

# Some FAQs:
### Does a `No` result in statistical tests means a useless idea? 
> Of course NOT!
>
>I have several profitable strategies based on `No` ideas! It just means that this implementation, on this instrument, with this timeframe, won't be profitable with 95% probability.
>
> Maybe it's got a bad luck based on test data, maybe a simple risk management rule elevates it's performance considerably, or any other reason.
>
> However, it's still a wise decision to concentrate on `Yes` ones first!

### How can I find `Yes` ones for all other coins and timeframes? 
> This is an under development service of the [QuantCT App](https://app.quantct.com/)!

### Do you have a similar work for fully optimized trading strategies? 
> Not, `YET`. Maybe a future feature of the [QuantCT App](https://app.quantct.com/).

### What's the scientific background of this work?
> Mainly statistical inference.

### Any reference about this method?
> The book "Evidence-based Technical Analysis".

### Why you do this?
> Because I believe you have the _right_ to know what would be the result of using a screener or a signaling/alerting service!
>
> A screener which only combines indicators without giving any insight on the future results, is both useless and dangerous!

### Why there is a limited set of strategies ideas in QuantCT screeners?
> Because there are several _dynamic-but-insightless_ crypto screeners right now.
>
> Also, most traders (if not all of them!) ultimately want to trade profitably, rather than struggling with unlimited possible combinations of insightless dynamic screeners. 

# Who are you?
![Amin Saqi](https://stackexchange.com/users/flair/2030508.png)
* Software Engineer.
* Professional crypto algotrader.
* Instructor of crypto algotrading.
* Algorithmic artist.
* Founder of https://quantinvestor.ir
* Founder of https://algoart-gallery.com
* Founder of https://quantct.com
