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