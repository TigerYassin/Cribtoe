import requests
import time
from datetime import datetime
import json
import sqlite3
from threading import Thread
from time import sleep

import sys


def getRequest():
	try:
		r = requests.get("https://www.cryptopia.co.nz/api/GetMarkets/BTC").json()
		return r
	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print e
		sys.exit(1)


listOFpairIDs = []
curr_dict = {}
r = getRequest()
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



conn = sqlite3.connect("Coins.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Cryptopia(tradePairID REAL, label TEXT, askPrice REAL, bidPrice REAL, low REAL, High REAL, volume REAL, lastPrice REAL, buyVolume REAL, sellVolume REAL, change REAL, open REAL, close REAL, baseVolume REAL, buyBaseVolume REAL, sellBaseVolume REAL, TimeStamp REAL)") 	#ADD THESE: occuranceID REAL, time, buyBaseVolume REAL, name TEXT


def threaded_function():

    for x in range(1000):
	# t = datetime.utcnow()
	# sleeptime = 1 - (t.second + t.microsecond/1000000.0)
	sleeptime = 1

	r = getRequest()

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
		TimeStamp = time.time()

		#***Enter all data of every coin in Cryptopia onto a sqlite database***#
		c.execute("INSERT INTO Cryptopia VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (pairID,Label,AskPrice,BidPrice,Low,High,Volume,LastPrice,BuyVolume,SellVolume,Change,Open,Close,BaseVolume,BuyBaseVolume,SellBaseVolume,TimeStamp))
	print "Got it", x
	print time.time()

	conn.commit()
	# c.close()
	# conn.close()
        sleep(sleeptime)


if __name__ == "__main__":
    thread = Thread(target = threaded_function)
    thread.start()
    thread.join()
    print ("Threading has finished") #not going to happen lol


