# What's this?
A repository for reviewing ideas of quantitative trading strategies. Each idea has the following documents:
 - A simply structured text file for introducing the idea and its formulation.
 - A pine script implementation for TradingView.
 - A python implementation with Backtrader library.
 - Some graphs and backtest performance metrics.

# What's the outcome?
The outcome of this work is to answer the following question with ONE word (Yes/No):

> Does this idea have any predictive power (i.e. profitability in future), with a "High Enough Probability" (HEP)?

The HEP here is 0.05 p-value, 0.95 significanse, above "+2 x Sigma" of histogram of mean returns, or simply 95% probability - All of them are same thing.

In addition, and built from those "Yes/No"s, we will have a valubale knowledge base of many trading ideas that PROBABLY won't work, along with some PROBABLY profitable ones!

# How ideas are tested?
All ideas are backtested on BTCUSDT starting from 2018-01-01 (a big and available market crash on Binance exchange) to 2020-12-30. Test details are as follows:
 - All tests have $ 100K on initial cash, and the order amount is 1 BTC.
 - A backtest is performed on the data mentioned above. Timeframe is based on what the idea suggests. 
 - Applying "Monte Carlo Permutation" (MCP) test with 10,000 random (i.e. non profitable) tests on same data.
 - Giving a Yes, if the mean return of the implemented idea is above "+2 x Sigma" of histogram of mean returns of those 10K random tests, and a No otherwise.

# Why the word "Idea"? 
The trading idea is merely Enter/Exit rules, without any risk/money management and without any optimization. If the bare idea is profitable, it has merit of strategy development and optimization efforts.

# Some FAQs:
 - Why keeping "No" ideas, too? Because it's also worth knowing that which ones are not working! So other researchers can get their results with less time-wasting tests.
 - Does a "No" means garbage? Of course NOT! I have several profitable strategies based on NO ideas! It just means that this implementation, on this instrument, with this timeframe, won't be profitable with 95% probability. Maybe it's got a bad lock, maybe a simple risk management rule elevates it's performance considerably, or any other reason. However, it's still a wise decision to concentrate on "Yes" ones first!
 - How can I find "Yes" ones? Simply view "ideas/yes" folder.
 - Do you have a similar work for trading strategies? Not, yet. And it won't be free and open source, too.
 - What's the scientific background of this work? Mainly statistical inference.
 - Any reference about this method? The book "Evidence-based Technical Analysis".
 - Why you do this? Because I like it, and I can devote my time on quantitative trading strategy development, completely!
 - Who are you? See the next section.

# Who am I?
![Amin Saqi](https://stackexchange.com/users/flair/2030508.png)
 - A software engineer.
 - A full-time algo trader.
 - An Instructor and mentor of crypto algo trading.
 - Founder of https://quantinvestor.ir
 - Founder of https://quantct.com (Under Construction ...)
