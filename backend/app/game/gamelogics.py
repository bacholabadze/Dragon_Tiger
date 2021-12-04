from ..models.docs import Player

"""
The function returns higher card, or tie
gets two arguments (cards): dragon & tiger
"""


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


"""
The function helps above function to rate card mass and then compare.
(Note: Ace is the lowest card in the game and King is the highest)
"""


def cardMass(card):
    try:
        card = int(card)
    except ValueError:
        pass
    if type(card) == int:
        return card
    elif card.lower() == 'a':
        return 1
    elif card.lower() == 'j':
        return 11
    elif card.lower() == 'd':
        return 12
    else:
        return 13

