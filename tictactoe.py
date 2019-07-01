# this code is the backend, and needs a frontend to function.
import random
class TicTacToe:
	def __init__(self):
		self.board = [' '] * 10
		self.result = None
	def __repr__(self):
		return "<TicTacToe result='{}'>".format(self.result)
	def drawBoard(self):
		print('   |   |')
		print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
		print('   |   |')
	def makeMove(self, letter, move):
		self.board[move] = letter
	def isWinner(self, le):
		return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or
		(self.board[4] == le and self.board[5] == le and self.board[6] == le) or
		(self.board[1] == le and self.board[2] == le and self.board[3] == le) or
		(self.board[7] == le and self.board[4] == le and self.board[1] == le) or
		(self.board[8] == le and self.board[5] == le and self.board[2] == le) or
		(self.board[9] == le and self.board[6] == le and self.board[3] == le) or
		(self.board[7] == le and self.board[5] == le and self.board[3] == le) or
		(self.board[9] == le and self.board[5] == le and self.board[1] == le))
	def getBoardCopy(self):
		board2 = []
		for i in self.board:
			board2.append(i)
		return board2
	def isSpaceFree(self, move):
		return self.board[move] == ' '
	def isBoardFull(self):
		for i in range(1, 10):
			if self.isSpaceFree(i):
				return False
		return True
	def makeBorder(self):
		choices = ['+', '-', '*', '=', '.', ':', '>', '<', '#']
		bchar = random.choice(choices)
		return bchar*40
	def getPlayerMove(self, letter):
		print()
		print(self.makeBorder())
		print("[It is {}\'s move]".format(letter))
		move = ' '
		while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
			print('What is your next move? (1-9)')
			move = input(">>> ")
		return int(move)
	def introduce(self):
		print("Welcome to Tic Tac Toe!")
		print("Player 1 is X")
		print("Player 2 is O")
	def playAgain(self):
		print('Do you want to play again? (yes or no)')
		return input("> ").lower().startswith('y')
	def play(self):
		self.introduce()
		gameIsPlaying = True
		turn = 'X'
		while gameIsPlaying:
			if(turn == 'X'):
				self.drawBoard()
				move = self.getPlayerMove('X')
				self.makeMove('X', move)
				if self.isWinner('X'):
					self.drawBoard()
					self.result = 'X'
					gameIsPlaying = False
				else:
					if self.isBoardFull():
						self.drawBoard()
						self.result = 'tie'
						break
					else:
						turn = 'O'
						continue
			else:
				self.drawBoard()
				move = self.getPlayerMove('O')
				self.makeMove('O', move)
				if self.isWinner('O'):
					self.drawBoard()
					self.result = 'O'
					gameIsPlaying = False
				else:
					if self.isBoardFull():
						self.drawBoard()
						self.result = 'tie'
						break
					else:
						turn = 'X'
						continue
