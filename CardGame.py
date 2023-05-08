import random
import PySimpleGUI as sg

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suit_values = {'Diamonds': 1, 'Hearts': 2, 'Spades': 3, 'Clubs': 4}

#Creating images -> struggle calling images on GUI
card_images = {'2': '2.png','3': '3.png','4': '4.png','5': '5.png','6': '6.png','7': '7.png','8': '8.png','9': '9.png','10': '10.png','J': 'J.png','Q': 'Q.png','K': 'K.png','A': 'A.png',}
deck = [(value, suit) for value in card_values.keys() for suit in suit_values.keys()]
random.shuffle(deck)
# Creating a GUI
layout = [
    [sg.Text('Player 1')],
    [sg.Text('', key='player1_hand')],
    [sg.Text('Score: '), sg.Text('', key='player1_score')],
    [sg.Text('Player 2')],
    [sg.Text('', key='player2_hand')],
    [sg.Text('Score: '), sg.Text('', key='player2_score')],
    [sg.Text('Player 3')],
    [sg.Text('', key='player3_hand')],
    [sg.Text('Score: '), sg.Text('', key='player3_score')],
    [sg.Text('Player 4')],
    [sg.Text('', key='player4_hand')],
    [sg.Text('Score: '), sg.Text('', key='player4_score')],
    [sg.Text('Player 5')],
    [sg.Text('', key='player5_hand')],
    [sg.Text('Score: '), sg.Text('', key='player5_score')],
    [sg.Text('Player 6')],
    [sg.Text('', key='player6_hand')],
    [sg.Text('Score: '), sg.Text('', key='player6_score')],
    [sg.Text('Winner(s): '), sg.Text('', key='winners')],
    [sg.Button('Deal Cards'), sg.Button('Exit')]
]


# Creating a window
window = sg.Window('Card Game', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # Dealing 5 cards
    players = [deck[i*5:(i+1)*5] for i in range(6)]

    scores = [sum([card_values[card[0]] for card in hand]) for hand in players]
    # max score among all players
    max_score = max(scores)

    # Finding players who have the max score
    winners = [i for i, score in enumerate(scores) if score == max_score]

    for i, hand in enumerate(players):
        window[f'player{i+1}_hand'].update(', '.join([f'{card[0]} of {card[1]}' for card in hand]))
        window[f'player{i+1}_score'].update(scores[i])
    # Findin the indices of the players who have the max score
    window['winners'].update(', '.join([f'Player {w+1}' for w in winners]))

window.close()

# def main():
#     deck = [(value, suit) for value in card_values.keys() 