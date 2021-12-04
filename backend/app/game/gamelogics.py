def cardMass(card):
    try:
        card = int(card)
    except ValueError:
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


def find_winner(drag, tig):
    drag = cardMass(drag[:-1])
    tig = cardMass(tig[:-1])
    if drag > tig:
        return 'dragon'
    elif tig > drag:
        return 'tiger'
    else:
        print('[!] ', drag, ' ', tig)
        return 'tie'
