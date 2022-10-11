from random import randint

print("## WELCOME TO PYTHON CASINO")

pc_choice = randint(1, 50)

playing = True

while playing:
    user_choice = int(input("Choose number:"))
    if (user_choice == pc_choice):
        print("You Win!")
        playing = False
    elif (user_choice > pc_choice):
        print("Lower! Computer choice:", pc_choice)
    elif (user_choice < pc_choice):
        print("Higher! Computer choice:", pc_choice)
