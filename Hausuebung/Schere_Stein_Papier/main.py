import random
import json
import requests

merged_dic = {}

def main():
    global merged_dic
    merged_dic = requests.get("http://127.0.0.1:5000/getStats").json()
    print(merged_dic)
    while True:
        wahl_spiel = input("Wollen sie Spielen[start] \n Statistik[stats] anzeigen ").lower()
        if wahl_spiel == 'start':
            game()
            requests.post("http://127.0.0.1:5000/saveStats", json=merged_dic)
        elif wahl_spiel == 'stats':
            get_stats()

def get_stats():
    res = requests.get("http://127.0.0.1:5000/getStats")
    print(res.json())

def com():
    wahl = ['schere', 'stein', 'papier', 'echse', 'spock']
    return random.choice(wahl)

def check(com, player):
    if player == 'schere':
        merged_dic['Schere'] += 1
    elif player == 'stein':
        merged_dic['Stein'] += 1
    elif player == 'papier':
        merged_dic['Papier'] += 1
    elif player == 'echse':
        merged_dic['Echse'] += 1
    elif player == 'spock':
        merged_dic['Spock'] += 1


    if com == player:
        merged_dic['Unentschieden'] += 1
        print('Unentschieden!')
    elif player == 'schere' and (com == 'papier' or com == 'echse'):
        merged_dic['Player'] += 1
        print('Gewonnen!')
    elif player == 'stein' and (com == 'schere' or com == 'echse'):
        merged_dic['Player'] += 1
        print('Gewonnen!')
    elif player == 'papier' and (com == 'stein' or com == 'spock'):
        merged_dic['Player'] += 1
        print('Gewonnen!')
    elif player == 'echse' and (com == 'papier' or com == 'spock'):
        merged_dic['Player'] += 1
        print('Gewonnen!')
    elif player == 'spock' and (com == 'schere' or com == 'stein'):
        merged_dic['Player'] += 1
        print('Gewonnen!')
    else:
        merged_dic['Computer'] += 1
        print('Verloren!')

def game():
    wahl_spieler = input("Wählen sie Schere, Stein, Papier, Echse, Spock: ").lower()

    if wahl_spieler not in ['schere', 'stein', 'papier', 'echse', 'spock']:
        print('Falsche Eingabe!')
    else:
        wahl_com = com()
        print('Der Computer nimmt ' + wahl_com.capitalize())

        check(wahl_com, wahl_spieler)



if __name__ == "__main__":
    main()