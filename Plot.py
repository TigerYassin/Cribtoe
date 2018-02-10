import sqlite3
import matplotlib.pyplot as plt


conn =sqlite3.connect("Coins9.db")
c = conn.cursor()


def printAny(val, num):
    c.execute("SELECT '%s' FROM Cryptopia WHERE tradePairID='%d'"%(val,num))
    value = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(value[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('%s'%val)
    plt.ylabel('%s'%val)




def printAskPrice(num):
    c.execute("SELECT askPrice FROM Cryptopia WHERE tradePairID='%d'"%num)
    askPrice = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(askPrice[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('AskPrice')
    plt.ylabel('AskPrice')

    plt.plot(X_Val, Y_Val)
    plt.show()



def printBidPrice(num):
    c.execute("SELECT bidPrice FROM Cryptopia WHERE tradePairID='%d'"%num)
    bidPrice = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(bidPrice[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('BidPrice')
    plt.ylabel('BidPrice')

    plt.plot(X_Val, Y_Val)
    plt.show()


def printLow(num):
    c.execute("SELECT low FROM Cryptopia WHERE tradePairID='%d'"%num)
    low = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(low[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('Low')
    plt.ylabel('Low')

    plt.plot(X_Val, Y_Val)
    plt.show()


def printHigh(num):
    c.execute("SELECT High FROM Cryptopia WHERE tradePairID='%d'"%num)
    High = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(High[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('High')
    plt.ylabel('High')

    plt.plot(X_Val, Y_Val)
    plt.show()


def printVolume(num):
    c.execute("SELECT volume FROM Cryptopia WHERE tradePairID='%d'"%num)
    volume = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(volume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('volume')
    plt.ylabel('volume')

    plt.plot(X_Val, Y_Val)
    plt.show()


def printLastPrice(num):
    c.execute("SELECT lastPrice FROM Cryptopia WHERE tradePairID='%d'" % num)
    lastPrice = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(lastPrice[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('lastPrice')
    plt.ylabel('lastPrice')

    plt.plot(X_Val, Y_Val)
    plt.show()


def printBuyVolume(num):
    c.execute("SELECT buyVolume FROM Cryptopia WHERE tradePairID='%d'" % num)
    buyVolume = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(buyVolume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('buyVolume')
    plt.ylabel('buyVolume')

    plt.plot(X_Val, Y_Val)
    plt.show()



def printSellVolume(num):
    c.execute("SELECT sellVolume FROM Cryptopia WHERE tradePairID='%d'" % num)
    sellVolume = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(sellVolume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('sellVolume')
    plt.ylabel('sellVolume')

    plt.plot(X_Val, Y_Val)
    plt.show()




def printChange(num):
    c.execute("SELECT change FROM Cryptopia WHERE tradePairID='%d'" % num)
    change = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(change[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('change')
    plt.ylabel('change')

    plt.plot(X_Val, Y_Val)
    plt.show()



def printOpen(num):
    c.execute("SELECT open FROM Cryptopia WHERE tradePairID='%d'" % num)
    open = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(open[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('open')
    plt.ylabel('open')

    plt.plot(X_Val, Y_Val)
    plt.show()





def printClose(num):
    c.execute("SELECT close FROM Cryptopia WHERE tradePairID='%d'" % num)
    close = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(close[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('close')
    plt.ylabel('close')

    plt.plot(X_Val, Y_Val)
    plt.show()




def printBaseVolume(num):
    c.execute("SELECT baseVolume FROM Cryptopia WHERE tradePairID='%d'" % num)
    baseVolume = c.fetchall()
    X_Val, Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(baseVolume[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('baseVolume')
    plt.ylabel('baseVolume')

    plt.plot(X_Val, Y_Val)
    plt.show()



def printSellBaseVol(num):
    c.execute("SELECT SellBaseVolume FROM Cryptopia WHERE tradePairID='%d'"%num)
    Sell = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(Sell[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('SellBaseVolume')
    plt.ylabel('SellBaseVolume')


    plt.plot(X_Val, Y_Val)
    plt.show()




def printBuyBaseVol(num):
    c.execute("SELECT buyBaseVolume FROM Cryptopia WHERE tradePairID='%d'"%num)
    Buy = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(Buy[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('BuyBaseVolume')
    plt.ylabel('BuyBaseVolume')


    plt.plot(X_Val, Y_Val)
    plt.show()


def printSellBaseVol(num):
    c.execute("SELECT SellBaseVolume FROM Cryptopia WHERE tradePairID='%d'"%num)
    Sell = c.fetchall()
    X_Val,Y_Val = [], []
    for x in range(1100):
        X_Val.append(x)
        Y_Val.append(Sell[x])
    print(X_Val)
    print(Y_Val)
    plt.xlabel('time (s)')
    plt.title('SellBaseVolume')
    plt.ylabel('SellBaseVolume')

    plt.plot(X_Val, Y_Val)
    plt.show()





#tradePairID, label, askPrice, bidPrice, low, High, volume, lastPrice, buyVolume, sellVolume, change, open, close, baseVolume, buyBaseVolume, sellBaseVolume,  TimeStamp


printSellBaseVol(5203)
printBuyBaseVol(5203)
printAskPrice(5203)





