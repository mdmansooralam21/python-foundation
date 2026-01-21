#Rock Paper Scissor Game

import random 

user_choice=input(f"Enter your move [Rock 🪨, Paper 📰, Scissor ✂️ ] \n").upper()

options_list=["Rock", "Paper", "Scissor"]
auto_choice=random.choice(options_list).upper()

if user_choice == "ROCK" and auto_choice == "ROCK":
    print(f"\n")
    print("Oops! It's a tie....Play again ")
    print("Reason: Your choice and Bot's choice were same ")
    print(f"\n")

elif user_choice == "ROCK" and auto_choice == "PAPER":
    print(f"\n")
    print("You LOST!!...BOT 🤖 WON")
    print("Reason: Paper covers the Rock ")
    print(f"\n")

elif user_choice == "ROCK" and auto_choice == "SCISSOR":
    print(f"\n")
    print("Wohoo!! You WON ✨✨...") 
    print("Reason: Rock breaks the scissor ")
    print(f"\n")

elif user_choice == "PAPER" and auto_choice == "PAPER":
    print(f"\n")
    print("Oops! It's a tie....Play again ")
    print("Reason: Your choice and Bot's choice were same ")
    print(f"\n")

elif user_choice == "PAPER" and auto_choice == "ROCK":
    print(f"\n")
    print("Wohoo!! You WON ✨✨...") 
    print("Reason: Paper covers the Rock ")
    print(f"\n")

elif user_choice == "PAPER" and auto_choice == "SCISSOR":
    print(f"\n")
    print("You LOST!!...BOT 🤖 WON")
    print("Reason: Scissor cuts the Paper ") 
    print(f"\n")

elif user_choice == "SCISSOR" and auto_choice == "SCISSOR":
    print(f"\n")
    print("Oops! It's a tie....Play again ")
    print("Reason: Your choice and Bot's choice were same ")
    print(f"\n")

elif user_choice == "SCISSOR" and auto_choice == "PAPER":
    print(f"\n")
    print("Wohoo!! You WON ✨✨...")
    print("Reason: Scissor cuts the Paper ") 
    print(f"\n")

elif user_choice == "SCISSOR" and auto_choice == "ROCK":
    print(f"\n")
    print("You LOST!!...BOT 🤖 WON")
    print("Reason: Rock breaks the scissor ")
    print(f"\n")

else:
    print(f"\n")
    print(f"Invalid choice entered!! Please enter the choice from {options_list}")
    print(f"\n")

#-----------------------------------------------------------------------------------------------------------------

#Dice Rolling Game

import random

dice1=random.randint(1, 6)
dice2=random.randint(1, 6)

user_choice=input("Do you want to roll the die? (y/n): ")

if user_choice=='y':
    print(f"\n")
    print(f"({dice1}, {dice2})")
    print(f"\n")

elif user_choice=='n':
    print(f"\n")
    print("Thank you playing...See you next time")
    print(f"\n")

else: 
    print(f"\n")
    print("Invlid key entered!! ")
    print(f"\n")