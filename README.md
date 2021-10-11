# Python web scrapper 
### Installation 
Download coinInfo.py file from src/ to your project folder
###  Usage
``` python

from CoinInfo import CoinInfo

scrapper = CoinInfo()

```
Using scrapper object it is possible to retrieve news about any cryptocurrency availible in coinmarketcap.com. 
``` python
>>> news = scrapper.get_paragraphs('bitcoin') # now news is a list of dictionaries
```
List has the following structure:
``` python
[{'title': 'One Month Of BTC: Ups And Downs Of El Salvador’s Bitcoin Adoption', 
'body': 'Technical glitches and other issues have plagued BTC adoption among Salvadorans in the last month. Let&rsquo;s see what happened in the last month of BTC as a legal tender in El Salvador.&nbsp;\nControversial BTC Tender In Action\nIt has been a month since the Central American coun...',
'link': '/headlines/news/one-month-of-btc-ups-and-downs-of-el-salvadors-btc-adoption/'}, {...}, ...]
```
Where title is obviously a title of an article, body it's first paragraph, link it's article web address
### Examples
``` python
>>> news[0]["title"] 
'One Month Of BTC: Ups And Downs Of El Salvador’s Bitcoin Adoption'

>>> news[0]["body"] 
'Technical glitches and other issues have plagued BTC adoption among Salvadorans in the last month. Let&rsquo;s see what happened in the last month of BTC as a legal tender in El Salvador.&nbsp;\nControversial BTC Tender In Action\nIt has been a month since the Central American coun...'

>>> for i in range(5):                     
...     print(str(i+1) + ") " + news[i]["title"])
... 
'1) One Month Of BTC: Ups And Downs Of El Salvador’s Bitcoin Adoption'
'2) XRP Surges 13%, Michael Dell Passes on Bitcoin, Vitalik Buterin Slams El Salvador’s BTC Experiment: Crypto News Digest by U.Today'
'3) Why crypto exchange Kraken predicts a $100,000 value for Bitcoin (BTC)?'
'4) Ted Cruz Believes Texas’ Abundant Energy Is Opportunity for Bitcoin'
'5) Bitcoin trades $8,000 below its all-time high as it’s on track to hit $57k'

>>> for i in range(5):                    
...     print(str(i+1) + ") " + news[i]["link"]))
... 
'1) /headlines/news/one-month-of-btc-ups-and-downs-of-el-salvadors-btc-adoption/'
'2) https://u.today/xrp-surges-13-michael-dell-passes-on-bitcoin-vitalik-buterin-slams-el-salvadors-btc-experiment'
'3) /headlines/news/why-crypto-exchange-kraken-predicts-a-100000-value-for-bitcoin-btc/'
'4) https://decrypt.co/83147/ted-cruz-believes-texas-abundant-energy-is-opportunity-bitcoin?&utm_medium=referral&utm_campaign=feed&utm_source=coinmarketcap'
'5) https://finbold.com/bitcoin-trades-8000-below-its-all-time-high/'
```

