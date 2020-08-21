#This is a game of tic tac toe
#This game uses the Misère rules
#This means that both players play X's and the first player to make 3 in a row looses
#There can also be multiple boards
#In that case, you can play on any board you like
#But, if 3 in a row is made on a board, it is considered dead and you can not play on it
#The player that makes the final 3 in a row looses
#The the first board is board '0'
#The positions of the board are numbered as follows:

#    |   |
#  0 | 1 | 2
# ___|___|___
#    |   |
#  3 | 4 | 5
# ___|___|___
#    |   |
#  6 | 7 | 8
#    |   |

#The algorithm that the computer uses to play against the player is based on this paper by Thane E. Plambeck and Greg Whitehead:
#https://arxiv.org/pdf/1301.1672v1.pdf

import numpy as np
import random

boardCharKey = {
    False: " ",
    True: "X"
}

possibleLooses = np.array([[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])

Q = ["","a","b","ab","bb","abb","c","ac","bc","abc","cc","acc","bcc","abcc","d","ad","bd","abd"]

P = ["a","bb","bc","cc"]

QReduction = {
    "aa": "",
    "bbb": "b",
    "bbc": "c",
    "ccc": "acc",
    "bbd": "d",
    "cd": "ad",
    "dd": "cc"
}

boardStateValue = {
    "000000000": "c",
    "100000000": "",
    "010000000": "",
    "000010000": "cc",
    "110000000": "ad",
    "101000000": "b",
    "100010000": "b",
    "100001000": "b",
    "100000001": "a",
    "010100000": "a",
    "010010000": "b",
    "010000010": "a",
    "110100000": "b",
    "110010000": "ab",
    "110001000": "d",
    "110000100": "a",
    "110000010": "d",
    "110000001": "d",
    "101010000": "a",
    "101000100": "ab",
    "101000010": "a",
    "100011000": "a",
    "100001010": "",
    "010110000": "ab",
    "010101000": "b",
    "110110000": "a",
    "110101000": "a",
    "110100001": "a",
    "110011000": "b",
    "110010100": "b",
    "110001100": "b",
    "110001010": "ab",
    "110001001": "ab",
    "110000110": "b",
    "110000101": "b",
    "110000011": "a",
    "101010100": "",
    "101010010": "b",
    "101000101": "a",
    "100011010": "b",
    "010101010": "a",
    "110101010": "b",
    "110101001": "b",
    "110011100": "a",
    "110001110": "a",
    "110001101": "a",
    "101010101": "",
    "110101011": "a",
}

def printBoard():
    print("")
    print("   |   |      " * size)
    print("".join([" " + boardCharKey[i[0]] + " | " + boardCharKey[i[1]] + " | " + boardCharKey[i[2]] + "    " for i in board]))
    print("___|___|___   " * size)
    print("   |   |      " * size)
    print("".join([" " + boardCharKey[i[3]] + " | " + boardCharKey[i[4]] + " | " + boardCharKey[i[5]] + "    " for i in board]))
    print("___|___|___   " * size)
    print("   |   |      " * size)
    print("".join([" " + boardCharKey[i[6]] + " | " + boardCharKey[i[7]] + " | " + boardCharKey[i[8]] + "    " for i in board]))
    print("   |   |      " * size)

def boardDead(testBoard):
    global possibleLooses

    looseList = []
    loose = False
    for i in possibleLooses:
        for j in i:
            looseList.append(testBoard[j])
        if not(False in looseList):
            loose = True
            break
        else:
            looseList = []
    return loose

def updateDeadBoards():
    global board
    global deadBoards

    deadBoards = [boardDead(board[i]) for i in range(0, size)]

def playerLoose():
    global deadBoards
    return not(False in deadBoards)

def playerPlay():
    global board

    c = False
    while c == False:
        try:
            playBoard = int(input("Which board would you like to play on? "))
            if boardDead(board[playBoard]):
                print("That board is dead.\nPlease pick another board.")
            else:
                c = True
        except (IndexError, ValueError, TypeError):
            print("That is not a valid board.\nPlease enter another board.")
    
    c = False
    while c == False:
        try:
            play = int(input("Where would you like to play? "))
            if board[playBoard][play]:
                print("That spot has already been taken.\nPlease choose another spot.")
            else:
                c = True
        except (IndexError, ValueError, TypeError):
            print("That is not a valid spot to play.\nPlease pick another spot.")

    board[playBoard][play] = True

def compPlay():
    global board
    global P
    c = False
    testBoard = board
    for i in range(0, size):
        for j in range(0,9):
            if boardDead(board[i]):
                continue
            if board[i][j] == False:
                testBoard[i][j] = True
                q = quotient(testBoard)
                if q in P:
                    board[i][j] = True
                    c = True
                    break
                else:
                    testBoard[i][j] = False
        if c:
            break
    if not(c):
        while True:
            boardPlay = int(random.random() * size)
            if boardDead(board[boardPlay]):
                continue
            while True:
                play = int(random.random() * 9)
                if board[boardPlay][play]:
                    continue
                else:
                    board[boardPlay][play] = True
                    break
            break



def rotate(board):
    return [board[6], board[3], board[0], board[7], board[4], board[1], board[8], board[5], board[2]]

def flip(board):
    return [board[2], board[1], board[0], board[5], board[4], board[3], board[8], board[7], board[6]]

def boardValue(board):
    if boardDead(board):
        return ""
    for j in range(0,8):
        try:
            state = ""
            for i in board:
                if i == True:
                    state = state + "1"
                else:
                    state = state + "0"
            return boardStateValue[state]
        except (KeyError):
            board = rotate(board)
            if j == 3:
                board = flip(board)
    
    raise Exception("could not get board value")

def quotient(board):
    global Q

    q = ""

    for i in board:
        q = q + boardValue(i)
    q = "".join(sorted(q))

    c = -1
    while not(q in Q):
        c += 1
        if c == (12 * size):
            raise Exception("Getting quotient took too long")
        for i in QReduction.keys():
            if i in q:
                for j in i:
                    q = q.replace(j, "", 1)
                q = q + QReduction[i]
                q = "".join(sorted(q))
        if "c" in q and "d" in q:
            q = q.replace("c", "a", 1)
            q = "".join(sorted(q))
    return q

c = False
while c == False:
    try:
        size = int(input("How many boards would you like? "))
        if size >= 0:
            c = True
        else:
            print("That is not a valid number of boards")
    except (IndexError, ValueError, TypeError):
        print("That is not a valid number of boards.")

c = False
while c == False:
    try:
        style = input("Would you like to play with 2 players (2p), 1 player and 1 computer (1p1c), or with 2 computers (2c)? ")
        if style in ["2p", "1p1c", "2c"]:
            c = True
        else:
            print("I didn't understand what you said.")
    except (IndexError, ValueError, TypeError):
        print("I didn't understand what you said.")

if style == "1p1c":
    c = False
    while c == False:
        try:
            first = int(input("Would you like to go first (1) or second (2)? "))
            if first == 1 or first == 2:
                c = True
            else:
                print("That is not a 1 or 2.")
        except (IndexError, ValueError, TypeError):
            print("That is not a valid number.")

board = np.zeros((size, 9), dtype=bool)

deadBoards = np.zeros((size), dtype=bool)

printBoard()

while True:
    print("\nPlayer 1:")
    if style == "1p1c":
        if first == 1:
            playerPlay()
        else:
            compPlay()
    elif style == "2p":
        playerPlay()
    else:
        compPlay()
    updateDeadBoards()
    printBoard()
    if playerLoose():
        print("Player 2 has won!")
        c = False
        while c == False:
            try:
                a = input("Would you like to play again (y/n)? ")
                if a == "y":
                    con = True
                    c = True
                elif a == "n":
                    con = False
                    c = True
                else:
                    print("I didn't understand what you said.")
            except (IndexError, ValueError, TypeError):
                print("I didn't understand what you said.")
        
        if con == True:
            c = False
            while c == False:
                try:
                    size = int(input("How many boards would you like? "))
                    if size >= 0:
                        c = True
                    else:
                        print("That is not a valid number of boards")
                except (IndexError, ValueError, TypeError):
                    print("That is not a valid number of boards.")
            c = False
            while c == False:
                try:
                    style = input("Would you like to play with 2 players (2p), 1 player and 1 computer (1p1c), or with 2 computers (2c)? ")
                    if style in ["2p", "1p1c", "2c"]:
                        c = True
                    else:
                        print("I didn't understand what you said.")
                except (IndexError, ValueError, TypeError):
                    print("I didn't understand what you said.")
            if style == "1p1c":
                c = False
                while c == False:
                    try:
                        first = int(input("Would you like to go first (1) or second (2)? "))
                        if first == 1 or first == 2:
                            c = True
                        else:
                            print("That is not a 1 or 2.")
                    except (IndexError, ValueError, TypeError):
                        print("That is not a valid number.")
            board = np.zeros((size,9), dtype=bool)
            updateDeadBoards()
            printBoard()
            continue
        else:
            break
    
    print("\nPlayer 2:")
    if style == "1p1c":
        if first == 1:
            compPlay()
        else:
            playerPlay()
    elif style == "2p":
        playerPlay()
    else:
        compPlay()
    updateDeadBoards()
    printBoard()
    if playerLoose():
        print("Player 1 has won!")
        c = False
        while c == False:
            try:
                a = input("Would you like to play again (y/n)? ")
                if a == "y":
                    con = True
                    c = True
                elif a == "n":
                    con = False
                    c = True
                else:
                    print("I didn't understand what you said.")
            except (IndexError, ValueError, TypeError):
                print("I didn't understand what you said.")
        
        if con == True:
            c = False
            while c == False:
                try:
                    size = int(input("How many boards would you like? "))
                    if size >= 0:
                        c = True
                    else:
                        print("That is not a valid number of boards")
                except (IndexError, ValueError, TypeError):
                    print("That is not a valid number of boards.")
            c = False
            while c == False:
                try:
                    style = input("Would you like to play with 2 players (2p), 1 player and 1 computer (1p1c), or with 2 computers (2c)? ")
                    if style in ["2p", "1p1c", "2c"]:
                        c = True
                    else:
                        print("I didn't understand what you said.")
                except (IndexError, ValueError, TypeError):
                    print("I didn't understand what you said.")
            if style == "1p1c":
                c = False
                while c == False:
                    try:
                        first = int(input("Would you like to go first (1) or second (2)? "))
                        if first == 1 or first == 2:
                            c = True
                        else:
                            print("That is not a 1 or 2.")
                    except (IndexError, ValueError, TypeError):
                        print("That is not a valid number.")
            board = np.zeros((size,9), dtype=bool)
            updateDeadBoards()
            printBoard()
            continue
        else:
            break