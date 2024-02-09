# Imported libaries
import random
from time import sleep
# Score, changed when user either wins or loses
win = 0
loss = 0

# List for computer random choice
rps = ["Rock","Paper","Scissors"]

# Color for items
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Casino difficulty (Impossible)
def casinoDifficulty():
    global loss
    global win
    # A list of numbers for the computer to choose, if 7 or below you lose, if 8 or 9 you draw else you win
    list = [1,2,3,4,5,6,7,8,9,10]
    # Randomly choosing the number
    difficultyChooser = random.choice(list)
    # Menu
    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", color.END)
    userChoice = input("Please enter an option Rock (R), Paper (P),Scissors (S)\n> ")
    # Pause game for 2 seconds to add suspense
    sleep(0.2)
    # Losing scenarioes
    if difficultyChooser <= 7:
        if userChoice.upper() == 'R':
            print(f"I choose Paper, you {color.RED}{color.BOLD}lose!{color.END}")
            loss = loss + 1
        if userChoice.upper() == 'P':
            print(f"I choose Scissors, you {color.RED}{color.BOLD}lose!{color.END}")
            loss = loss + 1
        if userChoice.upper() == 'S':
            print(f"I choose Rock, you {color.RED}{color.BOLD}lose!{color.END}")
            loss = loss + 1

    # Winning scenario
    elif difficultyChooser == 10:
        if userChoice.upper() == 'R':
            print(f"I choose Scissors, you {color.GREEN}{color.BOLD}win!{color.END}")
            win = win + 1
        if userChoice.upper() == 'P':
            print(f"I choose Rock, you {color.GREEN}{color.BOLD}win!{color.END}")
            win = win + 1
        elif userChoice.upper() == 'S':
            print(f"I choose Paper, you {color.GREEN}{color.BOLD}win!{color.END}")
            win = win + 1
        
    # Draw scenario
    elif difficultyChooser == 8 or 9:
        print("I chose the same, damn.")

    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", color.END)


# Normal difficulty, player has same chance as computer to win
def normalDifficulty():
    global loss
    global win
    # Menu
    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", color.END)
    userChoice = input("Please enter an option Rock (R), Paper (P),Scissors (S)\n> ")
    # Computer selects their choice
    computerChoice = random.choice(rps)
    # Pause for 2 seconds to add suspense
    sleep(0.2)    
    # Draw scenario
    if userChoice.upper() == computerChoice:
            print("I chose the same, damn.")
    # Losing scenario
    elif userChoice.upper() == 'P' and computerChoice == 'Scissors':
            print(f"I choose Scissors, you {color.RED}{color.BOLD}lose!{color.END}")
            loss = loss + 1
    elif userChoice.upper() == 'S' and computerChoice == 'Rock':
            print(f"I choose Rock, you {color.RED}{color.BOLD}lose!{color.END}")
            loss = loss + 1
    elif userChoice.upper() == 'R' and computerChoice == 'Paper':
            print(f"I choose Paper, you {color.RED}{color.BOLD}lose!{color.END}")
            loss = loss + 1
    # Winning scenario
    elif userChoice.upper() == 'R' and computerChoice == 'Scissors':
            print(f"I choose Scissors, you {color.GREEN}{color.BOLD}win!{color.END}")
            win = win + 1
    elif userChoice.upper() == 'S' and computerChoice == 'Paper':
            print(f"I choose Paper, you {color.GREEN}{color.BOLD}win!{color.END}")
            win = win + 1
    elif userChoice.upper() == 'P' and computerChoice == 'Rock':
            print(f"I choose Rock, you {color.GREEN}{color.BOLD}win!{color.END}")
            win = win + 1

    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", color.END)

# User chooses difficulty
def play():
    # Menu
    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", color.END)
    print(color.BOLD,color.UNDERLINE,"Choose Difficulty",color.END,"\n")
    print(color.BOLD,"1) Normal",color.END)
    print(color.BOLD,"2) Casino",color.END)
    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-", color.END)

    # User inputs choice, either 1 or 2, if userChoice does not match 1 or 2 they will input again
    flag = True
    while flag:
        userChoice = input("Please choose an option (1-2)\n> ")
        if userChoice == '1':
            flag = False
            normalDifficulty()
        elif userChoice == '2':
            flag = False
            casinoDifficulty()
        else:
            print(f"{color.BOLD}INVALID OPTION, PLEASE CHOOSE AGAIN{color.END}")
 

# Main menu where user can pick what option to play
def mainMenu():
    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=", color.END)
    print(color.BOLD,color.UNDERLINE,"Rock Paper Scissors",color.END)
    print(color.BOLD,"\n1) Play\n2) Exit")
    print(color.GREEN,"=-=-=-=-=-=-=-=-=-=", color.END)
    # Checks to see if user entered valid option
    flag = True
    while flag:
        menuChoice = input(f"{color.BOLD}Select an option (1-2){color.END}\n> ")
        if menuChoice != '1':
            if menuChoice != '2':
                print(color.BOLD,"PLEASE CHOOSE A VALID OPTION",color.END) 
        
        if menuChoice == '1':
            flag = False
            play()
        elif menuChoice == '2':
            exit()

# Starts the game by going to the mainMenu function
mainMenu()

# Asks user to play again
flag = True
while flag:
    print(color.BOLD,"Play again? (Y-N)",color.END)
    playAgain = input("> ")
    if 'y' in playAgain.lower():
        mainMenu()
    elif 'n' in playAgain.lower():
        flag = False
    else:
        print(color.BOLD,"OPTION NOT FOUND",color.END,"\n")

# Calculating win loss percentage based of how many games user has won and lost, includes casino

print(color.GREEN,"=-=-=-=-=-=-=-=-=-=", color.END)
print(color.BOLD,color.UNDERLINE,"Your Win Loss Ratio",color.END)
print(color.BOLD,"Won: ",color.END,color.GREEN,win,color.END)
print(color.BOLD,"Lost: ",color.END,color.RED,loss,color.END)

# As we cannot divide by 0, we indicate to the computer that percentage will equal wins
if loss == 0:
    percentage = win
elif loss != 0: 
    percentage = (win/loss)
print(color.BOLD,"Total W/L ratio: ",color.END,color.YELLOW,percentage,color.END)
sleep(120)
