
# Trade Idea: Momentum
It seems that on trending instruments, when the 10-days and 5-days momentum indicators are positive, the market can be considered bullish.

## Long-only logic
* When both momentum indicators are positive, asset is considered rising (bullish), and we can enter the market.
* When any of momentum indicators becomes negative, it's time to exit the market.

## Long/Short logic
* When both momentum indicators are positive, asset is considered rising (bullish), and we can go _Long_.
* When both momentum indicators are negative, asset is considered falling (bearish) and we can go _Short_.
* Otherwise, asset is considered ranging. 

# Formulation

## Long-only
* **Enter**: mom(10) > 0 AND mom(5) > 0
* **Exit**: mom(10) < 0 OR mom(5) < 0

## Long/Short
* **Enter _Long_**: mom(10) > 0 AND mom(5) > 0
* **Exit _Long_**: mom(10) < 0 OR mom(5) < 0
* **Enter _Short_**: mom(10) < 0 AND mom(5) < 0
* **Exit _Short_**: mom(10) > 0 OR mom(5) > 0
	
