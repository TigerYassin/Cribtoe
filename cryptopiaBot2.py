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
		return requests.get("https://www.cryptopia.co.nz/api/GetMarkets/BTC").json()
	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print (e)
		sys.exit(1)


def generateIndexes(r):
	listOFpairIDs = []
	curr_dict = {}
	try:
		r_length = len(r["Data"])
	except TypeError:
		return
	for i in range(r_length):
		pairID = r["Data"][i]["TradePairId"]
		listOFpairIDs.append(pairID)
		curr_dict.update({str(pairID): i})
	return [listOFpairIDs,curr_dict]



def getTradePairId(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["TradePairId"]

def getLabel(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Label"]

def getAskPrice(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["AskPrice"]

def getBidPrice(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BidPrice"]

def getLow(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Low"]

def getHigh(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["High"]

def getVolume(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Volume"]

def getLastPrice(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["LastPrice"]

def getBuyVolume(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BuyVolume"]

def getSellVolume(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["SellVolume"]

def getChange(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Change"]

def getOpen(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Open"]

def getClose(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["Close"]

def getBaseVolume(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BaseVolume"]

def getBuyBaseVolume(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["BuyBaseVolume"]

def getSellBaseVolume(TradePairId,r,curr_dict):
	return r["Data"][int(curr_dict.get(str(TradePairId)))]["SellBaseVolume"]



conn = sqlite3.connect("coins.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Cryptopia(tradePairID REAL, label TEXT, askPrice REAL, bidPrice REAL, low REAL, High REAL, volume REAL, lastPrice REAL, buyVolume REAL, sellVolume REAL, change REAL, open REAL, close REAL, baseVolume REAL, buyBaseVolume REAL, sellBaseVolume REAL, TimeStamp REAL)") 	#ADD THESE: occuranceID REAL, time, buyBaseVolume REAL, name TEXT


def threaded_function():
	x = 0
	while True:
		# t = datetime.utcnow()
		# sleeptime = 1 - (t.second + t.microsecond/1000000.0)
		sleeptime = 5
		r = getRequest()
		listgenerated = generateIndexes(r)
		listOFpairIDs = listgenerated[0]
		curr_dict = listgenerated[1]

		conn = sqlite3.connect("coins.db")
		c = conn.cursor()
		TimeStamp = time.time()

		for i in range(len(listOFpairIDs)):
			TradePairId = r["Data"][i]["TradePairId"]
			Label = getLabel(TradePairId,r,curr_dict)
			AskPrice = getAskPrice(TradePairId,r,curr_dict)
			BidPrice = getBidPrice(TradePairId,r,curr_dict)
			Low = getLow(TradePairId,r,curr_dict)
			High = getHigh(TradePairId,r,curr_dict)
			Volume = getVolume(TradePairId,r,curr_dict)
			LastPrice = getLastPrice(TradePairId,r,curr_dict)
			BuyVolume = getBuyVolume(TradePairId,r,curr_dict)
			SellVolume = getSellVolume(TradePairId,r,curr_dict)
			Change = getChange(TradePairId,r,curr_dict)
			Open = getOpen(TradePairId,r,curr_dict)
			Close = getClose(TradePairId,r,curr_dict)
			BaseVolume = getBaseVolume(TradePairId,r,curr_dict)
			BuyBaseVolume = getBuyBaseVolume(TradePairId,r,curr_dict)
			SellBaseVolume = getSellBaseVolume(TradePairId,r,curr_dict)
			#TimeStamp = time.time()

			#***Enter all data of every coin in Cryptopia onto a sqlite database***#
			c.execute("INSERT INTO Cryptopia VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (TradePairId,Label,AskPrice,BidPrice,Low,High,Volume,LastPrice,
                   BuyVolume,SellVolume,Change,Open,Close,BaseVolume,BuyBaseVolume, SellBaseVolume,TimeStamp))

		print ("Got it", x)
		x+=1
		print (time.time())

		conn.commit()
		# c.close()
		# conn.close()
		sleep(sleeptime)


if __name__ == "__main__":
    thread = Thread(target = threaded_function)
    thread.start()
    thread.join()
    print ("Threading has finished") #not going to happen lol


