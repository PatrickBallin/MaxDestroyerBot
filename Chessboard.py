import pygame
import sys
import sys
import pygame
import contextlib
import io
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Chessboard and piece images
BOARD_SIZE = 500
SQUARE_SIZE = BOARD_SIZE // 8
LIGHT_COLOR = (240, 217, 181)
DARK_COLOR = (181, 136, 99)

# Load piece images (You can replace these paths with actual images)
piece_images = {
    # Pawns
    'w_ba': pygame.image.load('.idea/chessPieces/white_pawn.png'),
    's_ba': pygame.image.load('.idea/chessPieces/black_pawn.png'),

    # Knights
    'w_pf': pygame.image.load('.idea/chessPieces/white_horse.png'),
    's_pf': pygame.image.load('.idea/chessPieces/black_horse.png'),

    # Bishop
    'w_la': pygame.image.load('.idea/chessPieces/white_bishop.png'),
    's_la': pygame.image.load('.idea/chessPieces/black_bishop.png'),

    # Rooks
    'w_tu': pygame.image.load('.idea/chessPieces/white_rook.png'),
    's_tu': pygame.image.load('.idea/chessPieces/black_rook.png'),

    # Queens
    'w_da': pygame.image.load('.idea/chessPieces/white_queen.png'),
    's_da': pygame.image.load('.idea/chessPieces/black_queen.png'),

    # Kings
    'w_ko': pygame.image.load('.idea/chessPieces/white_king.png'),
    's_ko': pygame.image.load('.idea/chessPieces/black_king.png'),
    # Add other pieces: rooks, bishops, queens, kings
}

# Create a screen for the board
# Initialize Pygame

screen = None


def init_this_thing():
    global screen
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        pygame.init()
        screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        pygame.display.set_caption("Chessboard")


def draw_chessboard():
    global screen
    for row in range(8):
        for col in range(8):
            color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# Function to draw a piece on the board given its 64-bit integer and position
def draw_pieces(figuren):
    # board = "figuren[figur]" - figur
    # peice_typpe = figur - figur name
    # Iterate through the 64 bits of the integer
    for figur in figuren:
        for i in range(64):
            if figuren[figur] & (1 << i):  # Check if there's a piece on this square
                row = 7 - (i // 8)  # Calculate row (0-7)
                col = 7 - (i % 8)  # Calculate column (0-7)
                piece_image = piece_images[figur]
                screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))


# Function to update the board from another file
def update_board(figuren):
    draw_chessboard()  # Draw the chessboard

    # Draw the pieces based on the updated board state
    draw_pieces(figuren)

    # Update the display
    pygame.display.flip()



