#ZAD1
user_input = input("Podaj liczby rozdzielone przecinkiem: ")

lista = [int(x) for x in user_input.split(",")]

max = lista[0]
min = lista[0]

#Wyszukiwanie max i min
for num in lista:
    if num > max:
        max = num
    if num < min:
        min = num

print("Wartość maksymalna to:", max)
print("Wartość minimalna to:", min)

#ZAD2
import random

lista_miast = ["Warszawa", "Poznań", "Bydgoszcz", "Łódz", "Serock", "Wołomin", "Szczecin", "Lublin", "Białystok", "Gdańsk"]
plan_wycieczki = []


while len(plan_wycieczki) < 4:
    miasto = random.choice(lista_miast)
    if miasto not in plan_wycieczki:
        plan_wycieczki.append(miasto)


print("Twoja wycieczka obejmie następujące miasta:")
for i, miasto in enumerate(plan_wycieczki):
    print(f"{i+1}. {miasto}")


#ZAD3
import random

print("Witaj w grze papier, nożyce, kamień!")
num_rounds = int(input("Ile rund chcesz rozegrać? "))

player1_name = input("Podaj imię gracza 1: ")
player2_name = ""

play_mode = input("Wybierz tryb gry (1 - gra z komputerem, 2 - gra z drugim graczem): ")

if play_mode == "2":
    player2_name = input("Podaj imię gracza 2: ")

player1_score = 0
player2_score = 0

for i in range(num_rounds):
    print(f"Runda {i+1}:")
    print(f"{player1_name} ({player1_score}) vs {player2_name} ({player2_score})")

    player1_choice = input(f"{player1_name}, wybierz papier, nożyce lub kamień: ")

    if play_mode == "1":
        computer_choice = random.choice(["papier", "nożyce", "kamień"])
        print(f"Komputer wybrał: {computer_choice}")
        player2_choice = computer_choice
    else:
        player2_choice = input(f"{player2_name}, wybierz papier, nożyce lub kamień: ")

    print(f"{player1_name} wybrał: {player1_choice}")
    print(f"{player2_name} wybrał: {player2_choice}")

    if player1_choice == player2_choice:
        print("Remis!")
    elif player1_choice == "papier" and player2_choice == "nożyce":
        print(f"{player2_name} wygrał rundę!")
        player2_score += 1
    elif player1_choice == "papier" and player2_choice == "kamień":
        print(f"{player1_name} wygrał rundę!")
        player1_score += 1
    elif player1_choice == "nożyce" and player2_choice == "papier":
        print(f"{player1_name} wygrał rundę!")
        player1_score += 1
    elif player1_choice == "nożyce" and player2_choice == "kamień":
        print(f"{player2_name} wygrał rundę!")
        player2_score += 1
    elif player1_choice == "kamień" and player2_choice == "papier":
        print(f"{player2_name} wygrał rundę!")
        player2_score += 1
    elif player1_choice == "kamień" and player2_choice == "nożyce":
        print(f"{player1_name} wygrał rundę!")
        player1_score += 1

print(f"Koniec gry! Wyniki:")
print(f"{player1_name}: {player1_score}")
print(f"{player2_name}: {player2_score}")
if player1_score > player2_score:
    print(f"{player1_name} wygrał grę!")
elif player1_score < player2_score:
    print(f"{player2_name} wygrał grę!")







