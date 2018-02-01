import requests
import time
import datetime
import json
import sqlite3


r = requests.get("https://www.cryptopia.co.nz/api/GetMarkets/BTC").json()

listOFpairIDs = []
curr_dict = {}
for i in range(len(r["Data"])):
    pairID = r["Data"][i]["TradePairId"]
    listOFpairIDs.append(pairID)
    curr_dict.update({str(pairID): i})






def getTradePairId(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["TradePairId"]

def getLabel(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Label"]

def getAskPrice(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["AskPrice"]

def getBidPrice(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BidPrice"]

def getLow(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Low"]

def getHigh(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["High"]

def getVolume(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Volume"]

def getLastPrice(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["LastPrice"]

def getBuyVolume(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BuyVolume"]

def getSellVolume(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["SellVolume"]

def getChange(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Change"]

def getOpen(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Open"]

def getClose(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Close"]

def getBaseVolume(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BaseVolume"]

def getBuyBaseVolume(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BuyBaseVolume"]

def getSellBaseVolume(TradePairId):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["SellBaseVolume"]









							#*** if you wanted it printed uncomment these lines ***#
# for i in range(len(listOFpairIDs)):
# 	pairID = r["Data"][i]["TradePairId"]
# 	print pairID
# 	print(getLabel(pairID))
# 	print(getAskPrice(pairID))
# 	print(getBidPrice(pairID))
# 	print(getLow(pairID))
# 	print(getHigh(pairID))
# 	print(getVolume(pairID))
# 	print(getLastPrice(pairID))
# 	print(getLastPrice(pairID))
# 	print(getBuyVolume(pairID))
# 	print(getBuyVolume(pairID))
# 	print(getSellVolume(pairID))
# 	print(getChange(pairID))
# 	print(getOpen(pairID))
# 	print(getClose(pairID))
# 	print(getBaseVolume(pairID))
# 	print(getBuyBaseVolume(pairID))
# 	print(getSellBaseVolume(pairID))
# 	print("\n")





conn = sqlite3.connect("Coins.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Cryptopia(tradePairID REAL, label TEXT, askPrice REAL, bidPrice REAL, low REAL, High REAL, volume REAL, lastPrice REAL, buyVolume REAL, sellVolume REAL, change REAL, open REAL, close REAL, baseVolume REAL, buyBaseVolume REAL, sellBaseVolume REAL)") 	#ADD THESE: occuranceID REAL, time, buyBaseVolume REAL, name TEXT


# or if you wanted just the calls for functions, this will loop through all the coins and there shouldnt be any future errors
TimeStamp = 0

for x in range(1000):
	r = requests.get("https://www.cryptopia.co.nz/api/GetMarkets/BTC").json()

	conn = sqlite3.connect("Coins.db")
	c = conn.cursor()



	for i in range(len(listOFpairIDs)):
		pairID = r["Data"][i]["TradePairId"]
		Label = getLabel(pairID)
		AskPrice = getAskPrice(pairID)
		BidPrice = getBidPrice(pairID)
		Low = getLow(pairID)
		High = getHigh(pairID)
		Volume = getVolume(pairID)
		LastPrice = getLastPrice(pairID)
		BuyVolume = getBuyVolume(pairID)
		SellVolume = getSellVolume(pairID)
		Change = getChange(pairID)
		Open = getOpen(pairID)
		Close = getClose(pairID)
		BaseVolume = getBaseVolume(pairID)
		BuyBaseVolume = getBuyBaseVolume(pairID)
		SellBaseVolume = getSellBaseVolume(pairID)
																#***Enter all data of every coin in Cryptopia onto a sqlite database***#
		c.execute("INSERT INTO Cryptopia VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (pairID,Label,AskPrice,BidPrice,Low,High,Volume,LastPrice,BuyVolume,SellVolume,Change,Open,Close,BaseVolume,BuyBaseVolume,SellBaseVolume))
	TimeStamp += 1
	print "Got it", x

	conn.commit()
	# c.close()
	# conn.close()

	time.sleep(2)



