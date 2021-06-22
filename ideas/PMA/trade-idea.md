
# Trade Idea: PMA
PMA (Pivot Moving average) is a set of 3 EMAs on HLC/3 data. When all PMAs are rising, market is considered bullish. When all PMAs are falling, market is considered bearish. Otherwise, market is considered ranging.

It seems that PMAs of 10, 20, 30 on daily chart has predictive power.

## Long-only logic
* When all EMAs are rising, asset is considered rising (bullish), and we can enter the market.
* When any of EMA indicators becomes negative, it's time to exit the market.

## Long/Short logic
* When all EMAs are rising, asset is considered rising (bullish), and we can go _Long_.
* When all EMAs are falling, asset is considered falling (bearish) and we can go _Short_.
* Otherwise, asset is considered ranging. 

# Formulation

## Long-only
* **Enter**: pma(10) is rising AND pma(20) is rising AND pma(30) is rising
* **Exit**: pma(10) is falling OR pma(20) is falling OR pma(30) is falling

## Long/Short
* **Enter _Long_**: pma(10) is rising AND pma(20) is rising AND pma(30) is rising
* **Exit _Long_**: pma(10) is falling OR pma(20) is falling OR pma(30) is falling
* **Enter _Short_**: pma(10) is falling AND pma(20) is falling AND pma(30) is falling
* **Exit _Short_**: pma(10) is rising OR pma(20) is rising OR pma(30) is rising
	
