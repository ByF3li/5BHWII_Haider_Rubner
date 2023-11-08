import random

def drawCard(amountCards):
    drawnCards = []
    isLessThanDrawnCards = True
    while isLessThanDrawnCards:
        randomCard = random.randint(1,52)
        if(not(randomCard in drawnCards)):
            drawnCards.append(randomCard)
        if(len(drawnCards) == amountCards):
            isLessThanDrawnCards = False
    return drawnCards

def checkWhichColour(drawnCards):
    colour = []
    for i in drawnCards:
        colour.append(i // 13)
    return colour

def checkWhichSymbol(drawnCards):
    symbol = []
    for i in drawnCards:
        symbol.append(i % 13)
    return symbol

def checkDuplicates(list):
    tmp = set()
    dups = set(x for x in list if (x in tmp or tmp.add(x)))
    return tmp,dups

def checkPair(drawnCards):
    symbols = checkWhichSymbol(drawnCards)
    tmp = checkDuplicates(symbols)[0]
    dups = checkDuplicates(symbols)[1]
    #print(symbols)
    return len(tmp) == 4 and len(dups) == 1

def checkTwoPairs(drawnCards):
    symbols = checkWhichSymbol(drawnCards)
    tmp = checkDuplicates(symbols)[0]
    dups = checkDuplicates(symbols)[1]
    #print(symbols)
    return len(tmp) == 3 and len(dups) == 2

def checkThreeOfKind(drawnCards):
    symbols = checkWhichSymbol(drawnCards)
    tmp = checkDuplicates(symbols)[0]
    dups = checkDuplicates(symbols)[1]
    #print(symbols)
    return len(tmp) == 3 and len(dups) == 1

def checkPoker(drawnCards):
    symbols = checkWhichSymbol(drawnCards)
    tmp = checkDuplicates(symbols)[0]
    dups = checkDuplicates(symbols)[1]
    #print(symbols)
    return len(tmp) == 2 and len(dups) == 1

def checkFullHouse(drawnCards):
    symbols = checkWhichSymbol(drawnCards)
    tmp = checkDuplicates(symbols)[0]
    dups = checkDuplicates(symbols)[1]
    #print(symbols)
    return len(tmp) == 2 and len(dups) == 2

def checkFlush(drawnCards):
    colour = checkWhichColour(drawnCards)
    #print(colour)
    return len(set(colour)) == 1

def checkStraight(drawnCards):
    symbol = checkWhichSymbol(drawnCards)
    symbol.sort()
    isStraight = False
    for i in range(10):
        if(symbol == [-1+i,0+i,1+i,2+i,3+i] or symbol == [0,9,10,11,12]):
            isStraight = True
    #print(symbol)
    return isStraight


def checkStraightFlush(drawnCards):
    return checkFlush(drawnCards) and checkStraight(drawnCards)

def checkRoyalFlush(drawnCards):
    symbol = checkWhichSymbol(drawnCards)
    symbol.sort()
    return checkFlush(drawnCards) and symbol == [0,9,10,11,12]

def main(amountDraws, amountCards):
    possibilities = {"highCard": 0,
                     "pair": 0,
                     "2pair": 0,
                     "3kind": 0,
                     "straight": 0,
                     "flush": 0,
                     "fullHouse": 0,
                     "4kind": 0,
                     "straigtFlush": 0,
                     "roayalFlush": 0}
    for i in range(amountDraws):
        cards = drawCard(amountCards)
        if(checkRoyalFlush(cards)):
            possibilities["roayalFlush"] = possibilities["roayalFlush"] + 1
        elif(checkStraightFlush(cards)):
            possibilities["straigtFlush"] = possibilities["straigtFlush"] + 1
        elif(checkPoker(cards)):
            possibilities["4kind"] = possibilities["4kind"] + 1
        elif(checkFullHouse(cards)):
            possibilities["fullHouse"] = possibilities["fullHouse"] + 1
        elif(checkFlush(cards)):
            possibilities["flush"] = possibilities["flush"] + 1
        elif(checkStraight(cards)):
            possibilities["straight"] = possibilities["straight"] + 1
        elif(checkThreeOfKind(cards)):
            possibilities["3kind"] = possibilities["3kind"] + 1
        elif(checkTwoPairs(cards)):
            possibilities["2pair"] = possibilities["2pair"] + 1
        elif(checkPair(cards)):
            possibilities["pair"] = possibilities["pair"] + 1
        else:
            possibilities["highCard"] = possibilities["highCard"] + 1
    for i in possibilities:
        possibilities[i] = possibilities[i] / amountDraws * 100
    return possibilities


data = main(10000000, 5)
print(data)
