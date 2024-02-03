import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

armory = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while player_score < 2 and computer_score < 2:
    player_weapon = input("Choose your weapon!\n(rock/paper/scissors)\n")
    computer_weapon = random.choice(armory)

    print("\nPlayer's Choice:")
    print(eval(player_weapon))
    print("\nComputer's Choice:")
    print(eval(computer_weapon))

    if player_weapon == computer_weapon:
        result = "DRAW!"
    elif (player_weapon == "rock" and computer_weapon == "scissors") or \
            (player_weapon == "paper" and computer_weapon == "rock") or \
            (player_weapon == "scissors" and computer_weapon == "paper"):
        result = "YOU WIN!"
        player_score += 1
    else:
        result = "YOU LOSE!"
        computer_score += 1

    print("\nResult:")
    print(result)
    print(f"Player Score: {player_score} | Computer Score: {computer_score}")

if player_score >= 2:
    print("You win the game! Best 2 out of 3.")
else:
    print("Computer wins the game! Best 2 out of 3.")
