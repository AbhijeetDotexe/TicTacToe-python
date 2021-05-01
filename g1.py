import random

def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[1]+'|'+board[2]+'|'+board[3])

    return ("\nThis is the Current Board \n")

test_board=["#",'X','O','X','0','X','O','X','O','X']
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player 1, Choose X or O : ').upper()
    player1= marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return player1, player2


def place_marker(board,marker,position):
    board[position]=marker

print(place_marker(test_board,'$',2))

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():
    first =random.randint(0,1)
    if first ==0:
        return 'player1'
    else:
        return 'player2'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board,):
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True

def player_choice(board):
    position =0
    while position not in [0,1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a Postion (1-9): '))
    return position

def replay():
    choice = input('Do You want to keep playing ? Enter Yes or NO : ')
    return choice =='Yes'



print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break