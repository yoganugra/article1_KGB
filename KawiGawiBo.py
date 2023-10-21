import random   #      
import os       #

# biar clear atasnya
os.system("clear")

# HEADER =======================================================================================================================
print("\n")
print(f"{'안 내면 술래 가위바위보!':^63}")
print("="*63)
print(f'{"Kawi":^21} || {"Gawi":^21} || {"Bo":^21}')
print("="*63)

print(f'{"-attention-":^63}'.upper())
print(f'{"This game can be played in any language but we will use English":^63}')
print('''
Remember! 
Gawi (가위)\t\t= scissors
Bawi (바위)\t\t= rock
Bo (보)\t\t\t= paper''')

# MAIN PROGRAM =================================================================================================================
# DISPLAY SEEN BY THE USER WHEN THE PROGRAM STARTS
while True:
    #input options   
    moves = ('scissors','paper','rock')
    # This will keep looping if the user enters an option other than the provided choices
    while True:
        print('-'*63)
        user_choise = input("Select your move\t: ").lower()
        if user_choise in moves:
            break
        else:
            print('Opsy, something is wrong. Check your spelling and select again!')
            continue

    # After exiting the loop, the computer will randomly select an input from the available options
    computer_choise = random.choice(moves).lower()

# DISPLAY SEEN BY THE USER AFTER MAKING A CHOICE
    print("RESULT".center(63,'-'))
    print("Your choice\t\t: {}".format(user_choise))
    print("Opponent Choose\t\t: {}".format(computer_choise))

    # CONDITIONAL STATEMENTS - IF ELIF ELSE STATEMENT
# -- PAPER ---------------------------------------------------------------------------------------------------------------------
    #paper wins
    if user_choise == 'paper' and computer_choise == 'rock':
        print("Paper covers rock. You win!")
    #paper loses
    elif user_choise == 'paper' and computer_choise == 'scissors':
        print("Oops, you lose. Scissors cuts paper.")

# -- ROCK ----------------------------------------------------------------------------------------------------------------------
    #rock wins
    elif user_choise == 'rock' and computer_choise == 'scissors':
        print("Rock crushes scissors. You win!")
    #rock loses
    elif user_choise == 'rock' and computer_choise == 'paper':
        print("Oops, you lose. Paper covers rock.")
    
# -- SCISSORS ------------------------------------------------------------------------------------------------------------------
    #scissors wins
    elif user_choise == 'scissors' and computer_choise == 'paper':
        print("Scissors cuts paper. You win!")
    #scissors loses
    elif user_choise == 'scissors' and computer_choise == 'rock':
        print("Oops, you lose. Rock crushes scissors")
    
# -- TIE ------------------------------------------------------------------------------------------------------------------------
    else:
        print(f"It's a tie! Both of you selected {computer_choise} ")
        continue
    print('\n')     # new line

# Continue the game? ======================================================================================================================
    while True:
        again = input("Try again? (yes/no)\t: ").lower()
        if again == 'yes' or again == 'no':
            break
        elif again != 'yes' or again != 'no':
            print('check your spelling please!')

    if again == 'yes':
        continue
    else:
        break

# END OF PROGRAM ===============================================================================================================
print("Thanks for playing!".upper().center(63,"-"))