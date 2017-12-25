
import random
import sys
import copy

# Variable columns from 6 to 11
BOARDWIDTH = 6
# Each column has different number of rows- Input given in an array
ARRAYOFCOLUMNS = [5,4,3,5,5,5]
# Max of that array will be the board height
BOARDHEIGHT = max(ARRAYOFCOLUMNS)
# Dont care at 2 positions
DONTCARE = [[4,3],[6,2]]

# For analysis later, we store the number of wins of each player and draws
PLAYER1WINS = 0
PLAYER2WINS = 0
NUMBEROFDRAWS = 0

# Default we take 80 iterations for both players (For Monte-Carlo search)
PLAYER1ITERATIONS = 80
PLAYER2ITERATIONS = 80

def main():
    typeOfGame = getTypeOfGame() # 1 for Human-Computer, 2 for Computer-Computer
    player1Choice, player2Choice = getChoiceForPlayer1() # X or O for First player
    player = getFirstPlayer() # Who goes first
    print("________________________________NEW GAME__________________________________")
    print('%s will go first.' % player.title())
    mainBoard = Board(initialiseNewBoard()) # Initialises an empty board

    while True:
        if player == 'Player 1':
            mainBoard.drawBoard()
            if typeOfGame == 1:
                # if human v computer game then
                # Get input column from human
                move = getHumanMove(player1Choice, mainBoard)
                mainBoard.makeMove(player1Choice, move)
            elif typeOfGame == 2:
                # if computer v computer game then
                # Get best move by Monte carlo search
                move = getOptimalMove(player1Choice, mainBoard, PLAYER1ITERATIONS)
                mainBoard.makeMove(player1Choice, move)
            if mainBoard.isWinner(player1Choice):
                # Check winner (End of game detection)
                winner = 'Player 1'
                global PLAYER1WINS
                PLAYER1WINS += 1
                break
            player = 'Player 2'
        else:
            mainBoard.drawBoard()
            print('The computer is thinking...')
            # Get best move by Monte carlo search
            move = getOptimalMove(player2Choice, mainBoard, PLAYER2ITERATIONS)
            mainBoard.makeMove(player2Choice, move)
            if mainBoard.isWinner(player2Choice):
                # Check winner (End of game detection)
                winner = 'Player 2'
                global PLAYER2WINS
                PLAYER2WINS += 1
                break
            player = 'Player 1'

        # Check if the board is full, if yes it is a draw game!
        if mainBoard.isBoardFull():
            winner = 'Draw game'
            global NUMBEROFDRAWS
            NUMBEROFDRAWS += 1
            break

    mainBoard.drawBoard()
    print('Winner is: %s' % winner)

def getTypeOfGame():
    print("Enter 1 for Human vs computer, 2 otherwise")
    number = ''
    while not (number == '1' or number == '2'):
        number = input()
        if number == '1':
            print("--------------Human vs Computer game beginning---------------")
        elif number == '2':
            print("--------------Computer vs Computer game beginning------------")
    return int(number)

def getChoiceForPlayer1():
    choice = ''
    while not (choice == 'X' or choice == 'O'):
        print('Will Player 1 be X or O?')
        choice = input().upper()

    # the first element in the array is the Player 1's choice, the second is the Player 2's choice.
    if choice == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def getFirstPlayer():
    # Randomly choose who goes first: if 0 then Player 1 else if 1 then Player 2
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def getEnemyType(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

class Board:
    # This class contains all the functions related to a board instance
    def __init__(self, board):
        self.height = BOARDHEIGHT
        self.width = BOARDWIDTH
        self.board = board

    def isWinner(self, move):
        # End of Game detection in 4 different cases
        # Check horizontal line of 4
        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH - 3):
                if self.board[x][y] == move and self.board[x+1][y] == move and \
                 self.board[x+2][y] == move and self.board[x+3][y] == move:
                    return True

        # check vertical line of 4
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT - 3):
                if self.board[x][y] == move and self.board[x][y+1] == move and \
                 self.board[x][y+2] == move and self.board[x][y+3] == move:
                    return True

        # check forward / diagonal line of 4
        for x in range(BOARDWIDTH - 3):
            for y in range(3, BOARDHEIGHT):
                if self.board[x][y] == move and self.board[x+1][y-1] == move and \
                self.board[x+2][y-2] == move and self.board[x+3][y-3] == move:
                    return True

        # check backward \ diagonal line of 4
        for x in range(BOARDWIDTH - 3):
            for y in range(BOARDHEIGHT - 3):
                if self.board[x][y] == move and self.board[x+1][y+1] == move and \
                self.board[x+2][y+2] == move and self.board[x+3][y+3] == move:
                    return True

        # If none of the above cases match means there is no winner 
        # for this board on this move
        return False

    def isValidMove(self, move):
        if move < 0 or move >= (BOARDWIDTH):
            # Move out of limits of columns
            return False

        difference = BOARDHEIGHT - ARRAYOFCOLUMNS[move]
        if difference > 0:
            if self.board[move][difference] != ' ' and self.board[move][difference] != '.':
                # Checking if the short columns are already filled (but not filled with dont-care)
                return False
        if self.board[move][0] != ' ' and self.board[move][0] != '#':
            # Check if the column is a short one with unplayable cells at top
            return False

        # Else valid move
        return True


    def isBoardFull(self):
        # Returns True if atleast one position in the board is empty ' '
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if self.board[x][y] == ' ':
                    return False
        return True

    def makeMove(self, player, column):
        for y in range(BOARDHEIGHT-1, -1, -1):
            # if the player plays in dont-care cell, place lowercase x or o 
            # Since these are not to be counted in a line of 4
            if self.board[column][y] == '.':
                self.board[column][y] = player.lower()
                return
            # Else place uppercase X or O in that cell
            if self.board[column][y] == ' ':
                self.board[column][y] = player
                return


    def drawBoard(self):
        # Prints the board in a visually effective manner
        print()
        print(' ', end='')
        for x in range(1, BOARDWIDTH + 1):
            print(' %s  ' % x, end='')
        print()

        print(('====' * (BOARDWIDTH)))

        for y in range(BOARDHEIGHT):
            for x in range(BOARDWIDTH):
                print(' %s |' % self.board[x][y], end='')
            print()

            print('----' + ('----' * (BOARDWIDTH - 1)))


def initialiseNewBoard():
    # Initialise new board and fill the shorter rows with '#' and dont-care cells with '.'
    board = []
    for x in range(BOARDWIDTH):
        difference = BOARDHEIGHT - ARRAYOFCOLUMNS[x]
        board.append(['#'] * difference + [' '] * ARRAYOFCOLUMNS[x])
    
    board[DONTCARE[0][0]-1][DONTCARE[0][1]-1] = '.'
    board[DONTCARE[1][0]-1][DONTCARE[1][1]-1] = '.'
    return board


def getHumanMove(player, board):
    # Get column input where human wants to play his move
    while True:
        print('Enter column number: (1-%s) or "quit" to quit game' % (BOARDWIDTH))
        move = input()
        if move.lower().startswith('q'):
            sys.exit()
        if not move.isdigit():
            continue
        move = int(move) - 1
        if board.isValidMove(move):
            return move
        else:
            print("Move not allowed, please re enter!")
            continue

# def getEnemyWinMove(player, board):
#     enemyWinMove = None
#     for i in range(board.width):
#         dupboard = copy.deepcopy(board)
#         dupboard.makeMove(player, i)
#         if dupboard.isWinner(player):
#             enemyWinMove = i
#             break
#     return enemyWinMove

def getOptimalMove(player, board, numberofIterations):
    # Monte carlo search method here
    
    # enemyWinMove = getEnemyWinMove(getEnemyType(player), board)
    # if enemyWinMove is not None:
    #     print("Preventing a loss.. Playing in column {}".format(enemyWinMove))
    #     return enemyWinMove

    print("Number of iterations {}".format(numberofIterations))
    arrayofNodes = list()
    bestRatio = 0
    bestMove = 0
    for i in range(0, board.width):
        # Add a node for each column
        arrayofNodes.append(Node(board))
    for i in range(numberofIterations):
        # Randomly pick a column and copy the board and play that move in copied board
        randomColumn = random.randint(1, board.width)
        dupelicateBoard = copy.deepcopy(board)
        childToPlay = arrayofNodes[randomColumn - 1]
        dupelicateBoard.makeMove(player, randomColumn - 1)
        childToPlay.incrementVisits() # Increment visit for that node
        if (dupelicateBoard.isWinner(player)):
            # If it is a winning situation, increment wins for that node
            childToPlay.incrementWins()

    for i in range(0, board.width):
        # if arrayofNodes[i].visits == 0:
        #     continue
        ratio = float(arrayofNodes[i].wins / arrayofNodes[i].visits)
        if (ratio > bestRatio):
            # Takes the best win:visit ratio out of all the nodes
            # And play that move which has best ratio
            bestRatio = ratio
            bestMove = i
    if bestMove == 0:
        # If ratio is 0 for all nodes, randomly pick one move
        bestMove = random.randint(1, board.width) - 1
    print("Best ratio is : {}".format(bestRatio))
    print("Best move is : {}".format(bestMove + 1))
    return bestMove

class Node:
    def __init__(self, board):
        # Node is used to represent a state of a board and then play using MCTS
        self.board = board
        self.visits = 0
        self.wins = 0    

    def incrementVisits(self):
        self.visits += 1
    
    def incrementWins(self):
        self.wins += 1

if __name__ == '__main__':
    main()
