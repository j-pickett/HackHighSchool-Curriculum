# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    animC4.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/10 14:38:12 by apickett          #+#    #+#              #
#    Updated: 2018/11/10 14:38:17 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pygame
import sys
import math

# fill board with 0s using numpy
def create_board():
	board = np.zeros((boardH,boardW))
	return board

#place piece
def drop_piece(board, row, col, piece):
	board[row][col] = piece

#checks if spot is valid
def in_bounds(board, col):
	return board[boardH-1][col] == 0
#determines if next spot is empty, if so place on top of current value
def stackpiece(board, col):
	for r in range(boardH):
		if board[r][col] == 0:
			return r
#prints board filled with 0s
def print_board(board):
	print(np.flip(board, 0))
#checks if val is in range of 4, if in a row set win to true to stop game loop
def wincond(board, piece):
	for c in range(boardW - 3):
		for r in range(boardH):
			if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
				return True

	for c in range(boardW):
		for r in range(boardH - 3):
			if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
				return True

	for c in range(boardW - 3):
		for r in range(boardH - 3):
			if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
				return True

	for c in range(boardW - 3):
		for r in range(3, boardH):
			if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
				return True

def draw_board(board):
	for c in range(boardW):
		for r in range(boardH):
			pygame.draw.rect(screen, BLUE, (c * square, r * square + square, square, square))
			pygame.draw.circle(screen, BLACK, (int(c * square + square / 2), int(r * square + square + square / 2)), RADIUS)
	
	for c in range(boardW):
		for r in range(boardH):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c * square + square / 2), height-int(r * square + square / 2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c * square + square / 2), height-int(r * square + square / 2)), RADIUS)
	pygame.display.update()

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
boardH = 6
boardW = 7
board = create_board()
print_board(board)
winning = False
turn = 0
pygame.init()
square = 100
width = boardW * square
height = (boardH + 1) * square
size = (width, height)
RADIUS = int(square / 2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("BLOKK", 125)

#loop for game, checks inside for win conditions, player input , and draws the board/pieces
while not winning:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, square))
			x = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, RED, (x, int(square / 2)), RADIUS)
			else: 
				pygame.draw.circle(screen, YELLOW, (x, int(square / 2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, square))
			#player 1 input
			if turn == 0:
				x = event.pos[0]
				col = int(math.floor(x/square))

				if in_bounds(board, col):
					row = stackpiece(board, col)
					drop_piece(board, row, col, 1)

					if wincond(board, 1):
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40,10))
						winning = True


			#player 2 input
			else:				
				x = event.pos[0]
				col = int(math.floor(x/square))

				if in_bounds(board, col):
					row = stackpiece(board, col)
					drop_piece(board, row, col, 2)

					if wincond(board, 2):
						label = myfont.render("Player 2 wins!!", 1, YELLOW)
						screen.blit(label, (40,10))
						winning = True

			print_board(board)
			draw_board(board)
#change turns, and color
			turn += 1
			turn = turn % 2

			if winning:
				pygame.time.wait(500)

