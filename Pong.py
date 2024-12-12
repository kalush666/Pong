import pygame
from Paddle import Paddle
from pygame.locals import *
from Ball import Ball

import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        # Establish a connection to the MySQL server
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jonathan06",
            database="pong_game"
        )

        if db_connection.is_connected():
            print("Connected to MySQL database")
        return db_connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None




def save_game_result(player1_score, player2_score):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor()

        query = """
        INSERT INTO game_results (player1_score, player2_score)
        VALUES (%s, %s)
        """
        data = (player1_score, player2_score)

        cursor.execute(query, data)
        db_connection.commit()

        cursor.close()
        db_connection.close()
    else:
        print("Failed to save game result: No database connection")



# Example usage after each game
player1_score = 10  # Example score
player2_score = 8  # Example score
winner = "Player 1"  # Example winner



# Define the dimensions of the game window.
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

# Tuple for screen size.
size = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Initialize pygame and create the display.
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")  # Set the title of the game window.

def main():
    """
    Main function to run the Pong game.

    Handles game initialization, input processing, game logic, and rendering.
    """
    running = True  # Game loop control variable.

    # Create the ball and paddles.
    ball = Ball(320, 240, 10)  # Initialize the ball at the center of the screen.
    player1 = Paddle(10, 200, 10, 80)  # Paddle for player 1 (left side).
    player2 = Paddle(620, 200, 10, 80)  # Paddle for player 2 (right side).

    # Initialize scores for both players.
    player1_score = 0
    player2_score = 0

    # Load the font for displaying scores.
    font = pygame.font.Font(None, 74)

    # Main game loop.
    while running:
        # Event handling for user input.
        for event in pygame.event.get():
            if event.type == QUIT:  # Check if the user closes the game window.
                running = False

        # Handle paddle movement based on keyboard input.
        keys = pygame.key.get_pressed()
        if keys[K_UP]:  # Move player 2's paddle up.
            player2.move_up()
        if keys[K_DOWN]:  # Move player 2's paddle down.
            player2.move_down()
        if keys[K_w]:  # Move player 1's paddle up.
            player1.move_up()
        if keys[K_s]:  # Move player 1's paddle down.
            player1.move_down()

        # Check if the ball goes past the left or right edge of the screen.
        if ball.x < 0:  # Ball goes out on the left side (player 1's goal).
            player2_score += 1  # Increment player 2's score.
            ball.reset(320, 240)  # Reset the ball to the center.
        elif ball.x > WINDOW_WIDTH:  # Ball goes out on the right side (player 2's goal).
            player1_score += 1  # Increment player 1's score.
            ball.reset(320, 240)  # Reset the ball to the center.

        # Clear the screen by filling it with black.
        screen.fill((0, 0, 0))

        # Render the score text.
        score_text = font.render(f"{player1_score} - {player2_score}", True, (255, 255, 255))
        # Position the score text in the center-top of the screen.
        screen.blit(score_text, (WINDOW_WIDTH // 2 - 50, 20))

        # Draw the ball and paddles on the screen.
        ball.draw(screen)
        player1.draw(screen)
        player2.draw(screen)

        # Update the ball's position and handle collision logic.
        ball.update(player1, player2)

        # Refresh the display to show updated positions.
        pygame.display.update()

        # Limit the game loop to 60 frames per second for smoother gameplay.
        pygame.time.Clock().tick(60)

    save_game_result(player1_score, player2_score)



# Run the game if this script is executed directly.
if __name__ == '__main__':
    main()
