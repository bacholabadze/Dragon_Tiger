import random
cards=[]


def addCards(cveti):
    global cards
    for i in range(1,14):
        if i==1:
            cards.append('A'+ cveti)
        elif i==11:
            cards.append('J' + cveti)
        elif i==12:
            cards.append('D' + cveti)
        elif i==13:
            cards.append('K'+ cveti)
        else:
            cards.append(str(i)+cveti)


#Amatebs Dastashi Kartebs da shemdeg chexavs
def getCards():
    num_deck = 8 #Ramdeni Dastaa Tamasshi
    for _ in range(num_deck): 
        cveti='C' #Jvari
        addCards(cveti)
        cveti='H' #Guli
        addCards(cveti)
        cveti='S' #Kvavi
        addCards(cveti)
        cveti='D' #Aguri
        addCards(cveti)
        random.shuffle(cards)

def cardMass(card):
    try:
        card = int(card)
    except:
        pass
    if type(card) == int:
        return card
    elif card == 'A':
        return 1
    elif card == 'J':
        return 11
    elif card == 'D':
        return 12
    else:
        return 13

def winner(drag,tig):
    drag = cardMass(drag[:-1])
    tig = cardMass(tig[:-1])
    if drag > tig:
        return 1
    elif tig > drag:
        return 2
    else:
        print('[!] ',drag,' ',tig)
        return 3
    

def playGame():
    getCards()
    rules = """
    1) Dragon
    2) Tiger
    3) Tie
    """
    ans = -1
    while ans<1 or ans>3:
        print(rules)
        ans = int(input("Sheikvane Cifri: "))
    dragon = cards.pop()
    tiger = cards.pop()
    print(dragon, tiger)
    print(winner(dragon,tiger))

playGame()