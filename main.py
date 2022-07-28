import csv
import card_classes as cc

# ------CREATING DECK-DICTS-------
with open('cards/action.csv', 'r', encoding='UTF-8') as f:
    reader_csv = csv.DictReader(f)
    deck_csv = list(reader_csv)

act_deck = cc.Deck('action', deck_csv)

with open('cards/resources.csv', 'r', encoding='UTF-8') as f:
    reader_csv = csv.DictReader(f)
    deck_csv = list(reader_csv)

res_deck = cc.Deck('resources', deck_csv)

with open('cards/upgrades.csv', 'r', encoding='UTF-8') as f:
    reader_csv = csv.DictReader(f)
    deck_csv = list(reader_csv)

upg_deck = cc.Deck('upgrades', deck_csv)

with open('cards/player1.csv', 'r', encoding='UTF-8') as f:
    reader_csv = csv.DictReader(f)
    deck_csv = list(reader_csv)

p1_deck = cc.Deck('player 1', deck_csv)

with open('cards/player2.csv', 'r', encoding='UTF-8') as f:
    reader_csv = csv.DictReader(f)
    deck_csv = list(reader_csv)

p2_deck = cc.Deck('player 2', deck_csv)

print(act_deck)
print('---')
print(res_deck)
print('---')
print(upg_deck)
print('---')
print(p1_deck)
print('---')
print(p2_deck)
print('---')
