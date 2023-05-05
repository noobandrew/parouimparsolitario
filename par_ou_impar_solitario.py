import random

print("Vamos jogar 'Par ou Ímpar'!")

player1_name = input("Nome do Jogador 1: ")
player2_name = "CPU"

player1_choice = input(f"{player1_name}, escolha 'par' ou 'ímpar': ")
while player1_choice != 'par' and player1_choice != 'ímpar':
    player1_choice = input(f"{player1_name}, escolha 'par' ou 'ímpar': ")

if player1_choice == 'par':
    player2_choice = 'ímpar'
else:
    player2_choice = 'par'

print(f"{player2_name} escolheu {player2_choice}.")

player1_number = int(input(f"{player1_name}, escolha um número entre 0 e 10: "))
while player1_number < 0 or player1_number > 10:
    player1_number = int(input(f"{player1_name}, escolha um número entre 0 e 10: "))

player2_number = random.randint(0, 10)

print(f"{player2_name} escolheu o número {player2_number}.")

sum_numbers = player1_number + player2_number

if sum_numbers % 2 == 0:
    winner = player1_name if player1_choice == 'par' else player2_name
else:
    winner = player1_name if player1_choice == 'ímpar' else player2_name

print(f"O resultado foi {sum_numbers}, portanto {winner} venceu!")
