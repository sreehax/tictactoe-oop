from tictactoe import TicTacToe # import backend
game = TicTacToe()
while True:
	game.play()
	if game.result == 'X':
		print('Hooray! X has won the game!')
	elif game.result == 'O':
		print('Hooray! O has won the game!')
	elif game.result == 'tie':
		print('The game is a tie!')
	else:
		print('Error! The game has not finished!')


	if not game.playAgain():
		break
