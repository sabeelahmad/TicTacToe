#INFO 
print('Square Numbering Explanation')

def info(): 

	print(f'  1 | 2 | 3   ')
	print('----------------')
	print(f'  4 | 5 | 6  ')
	print('----------------')
	print(f'  7 | 8 | 9  ')


info()

# Function for displaying board
def display_board(board):
	# Clear board everytime this function is called
	print('\n'*100)
	# Now print board with latest status
	print(f'  {board[1]}    |    {board[2]}    |    {board[3]}   ')
	print('----------------------------')
	print(f'  {board[4]}    |    {board[5]}    |    {board[6]}   ')
	print('----------------------------')
	print(f'  {board[7]}    |    {board[8]}    |    {board[9]}   ')

# Function to take input from player
def player_input():
	choice  = ''
	while choice != 'X' and choice != 'O':
		choice = input("Please Enter The Choice Of Your Marker : 'X' or 'O' ---> ")
	return choice

# Function to place 'X' or 'O' on board at the position desired by the player
def place_X_O(board, choice, position):
	# placing choice at position
	board[position] = choice

# Function to check if 'X' or 'O' has won
def win_check(board, choice):

	# Check for all possible winning cases
	if  (board[1] == choice and board[2] == choice and board[3] == choice):
		return True
	elif(board[1] == choice and board[4] == choice and board[7] == choice):
		return True
	elif(board[1] == choice and board[5] == choice and board[9] == choice):
		return True
	elif(board[2] == choice and board[5] == choice and board[8] == choice):
		return True
	elif(board[3] == choice and board[6] == choice and board[9] == choice):
		return True
	elif(board[3] == choice and board[5] == choice and board[7] == choice):
		return True
	elif(board[4] == choice and board[5] == choice and board[6] == choice):
		return True
	elif(board[7] == choice and board[8] == choice and board[9] == choice):
		return True
	else:
		return False


# Function to randomly choose which player goes first
import random

def choose_player():
	return random.randint(1,2)

# Function to check if space available on board
def space(board, position):
	# If board[position] = empty string returns true
	return board[position] == ' '
	

# Function to check if board is full
def board_full(board):
	# if no empty string present in board returns true
	return not(' ' in board)

# Function that takes position of choice of 'X' or 'O' from player
# Then checks if the entered position using space function is free or not
def player_choice(player):
	position = -1
	while position not in range(1, 10):
		position = int(input(f"Player {player}, Please Enter Your Next Position (1-9): "))
	
	return position
# Function asking for a replay of game
def replay():
	rep = input('Do you want to play again? Yes or No: ')
	return rep.lower() == 'yes'
		
# Using while loops and the functions above to make the game come together
playing = True
while playing:
	print('Hello! Welcome to Tic Tac Toe')
	# Initially board contains nothings, index 0 will be #
	board = ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	# choosing which player goes first randomly
	first_p = choose_player()
	second_p = -1
	if first_p == 1:
		second_p = 2
	else:
		second_p = 1
	print(f'Player {first_p} will go first!')
	p1_choice = player_input()
	p2_choice = ''
	if(p1_choice == 'X'):
		p2_choice = 'O'
	else:
		p2_choice = 'X'
	# display board intially
	display_board(board)
	flag = 0
	# game will be on till board is not full or one of the players doesn't win
	while (not board_full(board)):

		# first_p turn
		pos1 = player_choice(first_p)

		# place marker of first_p at chosen position
		place_X_O(board, p1_choice, pos1)
		display_board(board)
		# check if first_p has won after a move
		if win_check(board, p1_choice):
			print(f'Player {first_p} has WON!! Congratulations')
			flag = 1
			break

		# check if board full
		if board_full(board):
			break
		# player 2 turn
		pos2 = player_choice(second_p)

		# placing player 2 marker
		place_X_O(board, p2_choice, pos2)
		display_board(board)
		# win check for player 2
		if win_check(board, p2_choice):
			print(f'Player {second_p} has WON!! Congratulations')
			flag = 1
			break

	if flag == 0:
		print('Game has ended in a DRAW!!')
	# Ask for replay
	if replay():
		playing = True
	else:
		print('Thank You For Playing')
		break


# Print My First Python Project
print('\n'*100)

print('=============================================================')
print('\n'*5)
print('             DEVELOPED BY : SABEEL AHMAD'               )
print('\n'*5)
print('=============================================================')
