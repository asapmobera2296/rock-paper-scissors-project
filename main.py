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

#Write your code below this line 👇
choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors \n"))
if choice > 2:
  print("You have typed an invalid number. You lose.\n")
if choice == 0:
  print(rock)
if choice == 1:
  print(paper)
if choice == 2:
  print(scissors)

print("computer chose:\n")

computer_choice =[rock, paper, scissors]
num_items = len(computer_choice)
cpu_choice = random.randint(0, num_items - 1)
final_choice = computer_choice[cpu_choice]

print(final_choice)

if choice == cpu_choice:
    print(f"Both players selected {choice}. It's a tie!")
elif choice == 0:
    if cpu_choice == 2:
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif choice == 1:
    if cpu_choice == 0:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif choice == 2:
    if cpu_choice == 1:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")