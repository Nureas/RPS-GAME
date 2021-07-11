import random

comp_win = 0
user_win = 0

def User_option():
    choice = input('Choose Rock, Paper or Scissors: ')
    if choice in ['Rock', 'rock' , 'r', 'R']:
        choice = 'r'
    elif choice in ['Paper', 'paper' , 'p', 'P']:
        choice = 'p'
    elif choice in ['Scissors', 'scissors' , 's', 'S']:
        choice = 's'  
    else:
        print('WRONG INPUT BRO!')
    return choice

def Comp_option():
    number = random.randint(1, 3)
    if number == 1:
        choice = 'r'
    elif number == 2:
        choice = 'p'
    elif number == 3:
        choice = 's'
    return choice

while True:
    comp_choice = Comp_option()
    user_choice = User_option()
    
    if user_choice == comp_choice:
        print('You tied!')
    elif user_choice == 'r':
        if comp_choice == 'p':
            print('you chose rock and the computer chose paper. you lost!')
            comp_win += 1
        elif comp_choice == 's':
            print('you chose rock and the computer chose scissor. you won!')
            user_win += 1
    
    elif user_choice == 'p':
        if comp_choice == 'r':
            print('you chose paper and the computer chose rock. you won!')
            user_win += 1
        elif comp_choice == 's':
            print('you chose paper and the computer chose scissors. you lost!')
            comp_win += 1
    
    elif user_choice == 's':
        if comp_choice == 'p':
            print('you chose scissors and the computer chose paper. you won!')
            user_win += 1
        elif comp_choice == 'r':
            print('you chose scissors and the computer chose rock. you lost!')
            comp_win += 1


    print("")
    print("Player wins: " + str(user_win))
    print("Computer wins: " + str(comp_win))
    print("")
    
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break

