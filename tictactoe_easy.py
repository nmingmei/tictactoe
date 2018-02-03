''' 
 ============================================================================
 File Name   : tictactoe_easy.py
 Author      : Mingmei Niu
 Revision History: None
 Date             Version     Change ID    Author          Comment
 02-02-18         1.0         NA           Mingmei Niu     None
 ============================================================================
 
 Description: This is a very simple tic-tac-toe game using 2D arrays.
 User goes first in the first game and has the option of continuing playing
 after game ends. The loser of the previous game gets to go first for the next 
 game. The computer decides randomly among available spaces where to put his 
 piece.

'''

import random,time

userChoice = (input('''
    Welcome to tic-tac-toe! Do you want to be X or O? ''')).upper()
if userChoice == 'X':
    computerChoice = 'O' 
else:
    computerChoice = 'X'

board = [[' ', ' ', ' '] for i in range(3)]
playingGame = True 


def isThereAWinner():
    allXs = ['X', 'X', 'X']
    allOs = ['O', 'O', 'O']

    #check rows
    for i in range(3):
        if board[i] == allXs or board[i] == allOs:
            print("row found")
            return True
        else:
            continue 
    
    #check columns
    col = []
    for k in range(3):
        for j in range(3):
            col.append(board[j][k])
        if col == allXs or col == allOs:
            print("col found")
            return True
        col = []
    
    # check diagonals
    if ( (board[0][0] == board[1][1] == board[2][2] == 'X') or 
        (board[0][2] == board[1][1] == board[2][0] == 'O') or 
        (board[0][2] == board[1][1] == board[2][0] == 'X') or
        (board[0][2] == board[1][1] == board[2][0] == 'O') ):
        print("diagonals")
        return True
    else:
        return False 
    return False 


def printBoard():
    for i in range(3):
        print(board[i])


while playingGame: 
    turnNumber = 0 
    userTurn = True 
    while userTurn and turnNumber < 10: 
        userRow = input("\n" + "Which row? (top, middle, bottom): ")
        if userRow == 'top':
            userRow = 0
        elif userRow == 'middle':
            userRow = 1
        elif userRow == 'bottom':
            userRow = 2 
        else:
            print('Invalid entry. Middle position chosen by default.')
            userRow = 1 

        userPosition = input("Which location? (left, middle, or right): ")
        if userPosition == 'left':
            userPosition = 0
        elif userPosition == 'middle':
            userPosition = 1
        elif userPosition == 'right':
            userPosition = 2 
        else:
            print('Invalid entry. Middle position chosen by default.')
            userPosition = 1 

        if board[userRow][userPosition] == ' ':
            turnNumber += 1 
            userTurn = False 
            board[userRow][userPosition] = userChoice
        else:
            print("This spot is taken, please choose again.")

    print("\n")
    printBoard()

    if isThereAWinner():
        playingGame = False
        playAgain = (input("You won! Play again? Y/N ")).upper()
        if playAgain == "Y":
            board = [[' ', ' ', ' '] for i in range(3)]
            playingGame = True  
        else: 
            print("Goodbye!")
            break  

    time.sleep(1) 
    print("\n" + "Great, now it's my turn: " + "\n") 
    time.sleep(1) 

    computerShulffleOn = True 
    while computerShulffleOn:
        computerRow = random.choice([0,1,2]) 
        computerPosition = random.choice([0,1,2])
        if board[computerRow][computerPosition] == ' ':
            board[computerRow][computerPosition] = computerChoice
            computerShulffleOn = False 
            turnNumber += 1 
        else:
            computerShulffleOn = True 

    printBoard()

    if isThereAWinner():
        playingGame = False 
        playAgain = (input("I won, sorry! Play again? Y/N ")).upper()
        if playAgain == "Y":
            board = [[' ', ' ', ' '] for i in range(3)]
            playingGame = True  
        else: 
            print("Goodbye!")
            break 
    else:
        if turnNumber == 9:
            playAgain = (input("There is a draw! Play again? Y/N ")).upper()
            if playAgain == "Y":
                board = [[' ', ' ', ' '] for i in range(3)]
                playingGame = True 
            else: 
                print("Goodbye!")
                break 