from IPython.display import clear_output

WINS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
SYMBOLS = ['O', 'X']


def display_board(board):
  '''
  A 3x3 matrix representation of the board
  '''
  for i, square in enumerate(board):
      if i % 3 == 0:
        if i != 0:
          print()
        print('{0:=<13}'.format(''))
        print('|', end="")
      if square == 0:
        print('{0:>4}'.format('|'), end="")
      else:
         print('{0:^3}|'.format(square), end="")
  print('\n{0:=<13}'.format(''))

def starting_board(board):
  for i, square in enumerate(board):
      if i % 3 == 0:
        if i != 0:
           print()
        print('{0:=<13}'.format(''))
        print('|', end="")
      print('{0:^3}|'.format(i), end="")
  print('\n{0:=<13}'.format(''))
    
   
def get_user_input():
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    possible_choices = [str(x) for x in range(0, 9)]
    
    # While the choice is not a digit, keep asking for input.
    while choice not in possible_choices:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Pick a position to replace (0-8): ")
        
        if choice not in possible_choices:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, but you did not choose a valid position (0-8)")
            
    
    # Optionally you can clear everything after running the function
    # clear_output()
    
    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)

def is_winner(board):
   for win in WINS:
      if board[win[0]] and board[win[0]] == board[win[1]] == board[win[2]]:
         return board[win[0]]
   return False

def print_turn(player):
  print("It is {}'s turn".format(SYMBOLS[player]))

def play_game():
   
   # Print the rules
  game_over = False
  player = 1 # This corresponds to player X
  board = [0] * 9
  starting_board(board)

  while not game_over:
     print_turn(player)
     pos = get_user_input()


     if board[pos] != 0:
        # Someone has already played here, print error and loop again, don't change the player
        print("That spot is already taken, try again.")
        continue
     
     board[pos] = SYMBOLS[player]
     display_board(board)
     game_over = is_winner(board)
     player = (player + 1) % 2

  #Game over, game over is not the winning char
  print('Congratulations player {0}!!!'.format(game_over))

play_game()


      
