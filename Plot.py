import sqlite3
import matplotlib.pyplot as plt


conn =sqlite3.connect("Coins.db")
c = conn.cursor()


def printAny(val, num):
    c.execute("SELECT %s FROM Cryptopia WHERE tradePairID='%d'"%(val,num))
    value = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(value[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('%s'%val)
    plt.ylabel('%s'%val)

    return X_Val, Y_Val



def printAskPrice(num):
    plt.figure(1)
    plt.subplot(212)
    c.execute("SELECT askPrice FROM Cryptopia WHERE tradePairID='%d'"%num)
    askPrice = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(askPrice[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('AskPrice')
    plt.ylabel('AskPrice')

    plt.plot(X_Val, Y_Val)



def printBidPrice(num):
    plt.figure(1)
    plt.subplot(211)
    c.execute("SELECT bidPrice FROM Cryptopia WHERE tradePairID='%d'"%num)
    bidPrice = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(bidPrice[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('BidPrice')
    plt.ylabel('BidPrice')

    plt.plot(X_Val, Y_Val)


def printLow(num):
    plt.figure(3)
    c.execute("SELECT low FROM Cryptopia WHERE tradePairID='%d'"%num)
    low = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(low[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('Low')
    plt.ylabel('Low')

    plt.plot(X_Val, Y_Val)


def printHigh(num):
    plt.figure(4)
    c.execute("SELECT High FROM Cryptopia WHERE tradePairID='%d'"%num)
    High = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(High[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('High')
    plt.ylabel('High')

    plt.plot(X_Val, Y_Val)


def printVolume(num):
    plt.figure(5)
    c.execute("SELECT volume FROM Cryptopia WHERE tradePairID='%d'"%num)
    volume = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(volume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('volume')
    plt.ylabel('volume')

    plt.plot(X_Val, Y_Val)


def printLastPrice(num):
    plt.figure(6)
    c.execute("SELECT lastPrice FROM Cryptopia WHERE tradePairID='%d'" % num)
    lastPrice = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(lastPrice[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('lastPrice')
    plt.ylabel('lastPrice')
    plt.plot(X_Val, Y_Val)


def printBuyVolume(num):
    plt.figure(7)
    c.execute("SELECT buyVolume FROM Cryptopia WHERE tradePairID='%d'" % num)
    buyVolume = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(buyVolume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('buyVolume')
    plt.ylabel('buyVolume')
    plt.plot(X_Val, Y_Val)


def printSellVolume(num):
    plt.figure(8)
    c.execute("SELECT sellVolume FROM Cryptopia WHERE tradePairID='%d'" % num)
    sellVolume = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(sellVolume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('sellVolume')
    plt.ylabel('sellVolume')
    plt.plot(X_Val, Y_Val)



def printChange(num):
    plt.figure(9)
    c.execute("SELECT change FROM Cryptopia WHERE tradePairID='%d'" % num)
    change = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(change[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('change')
    plt.ylabel('change')
    plt.plot(X_Val, Y_Val)


def printOpen(num):
    plt.figure(10)
    c.execute("SELECT open FROM Cryptopia WHERE tradePairID='%d'" % num)
    open = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(open[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('open')
    plt.ylabel('open')

    plt.plot(X_Val, Y_Val)




def printClose(num):
    plt.figure(11)
    c.execute("SELECT close FROM Cryptopia WHERE tradePairID='%d'" % num)
    close = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(close[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('close')
    plt.ylabel('close')

    plt.plot(X_Val, Y_Val)



def printBaseVolume(num):
    plt.figure(12)
    c.execute("SELECT baseVolume FROM Cryptopia WHERE tradePairID='%d'" % num)
    baseVolume = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(baseVolume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('baseVolume')
    plt.ylabel('baseVolume')

    plt.plot(X_Val, Y_Val)


def printBuyBaseVol(num):
    plt.figure(14)
    plt.subplot(212)
    c.execute("SELECT buyBaseVolume FROM Cryptopia WHERE tradePairID='%d'"%num)
    Buy = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(Buy[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('BuyBaseVolume')
    plt.ylabel('BuyBaseVolume')
    plt.plot(X_Val, Y_Val)


def printSellBaseVol(num):
    plt.figure(14)
    plt.subplot(211)
    c.execute("SELECT SellBaseVolume FROM Cryptopia WHERE tradePairID='%d'"%num)
    Sell = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(reps):
        X_Val.append(x)
        Y_Val.append(Sell[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('SellBaseVolume')
    plt.ylabel('SellBaseVolume')
    plt.plot(X_Val, Y_Val)





#tradePairID, label, askPrice, bidPrice, low, High, volume, lastPrice, buyVolume, sellVolume, change, open, close, baseVolume, buyBaseVolume, sellBaseVolume,  TimeStamp


reps = 1022

#enter the id of the coin you wish to graph
coinID = 4948


#call out any graphing function you wish
printSellBaseVol(coinID)
printBuyBaseVol(coinID)
printAskPrice(coinID)
printBidPrice(coinID)
plt.show()

