import random
print("welcome to rock paper scissors game!")
while True:
 if input("do you want to play rock paper scissors? (yes/no): ").lower() != "yes":
    print("Thanks for playing!")
    print("come back soon!")
    break
 user_choice = input("enter your choice(rock,paper,scissors):")
 choices = ["rock","paper","scissors"]
 computer=random.choice(choices)
 if user_choice==computer:
      print("tie")
 elif (user_choice=="rock" and computer=="scissors") or (user_choice=="paper" and computer=="rock") or (user_choice=="scissors" and 
                                                                                                        computer=="paper"):
    print("you win")
 else:
    print("computer wins")