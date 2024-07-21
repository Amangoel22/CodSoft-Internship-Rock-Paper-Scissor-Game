#Roc-Paper-Scissors (TASK-4)
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

game=True
user_score=0
computer_score=0
draw=0
images=[rock, paper, scissors]

while game:
    user=input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors, or 00 to exit:\n")

    if user=="00":
        game=False
        print("\nThanks for playing.")
        break

    user=int(user)
    print(images[user])

    computer=random.randint(0, 2)
    print("Computer chose:")
    print(images[computer])

    if user==0 and computer==2:
        print("You win!")
        user_score+=1
    elif computer==0 and user==2:
        print("You lose")
        computer_score+=1
    elif computer>user:
        print("You lose")
        computer_score+=1
    elif user>computer:
        print("You win!")
        user_score+=1
    elif computer==user:
        print("It's a draw")
        draw+=1
    print("\nUser score:",user_score)
    print("Computer score:",computer_score)
    print("Draws:",draw)
    print("\n")
