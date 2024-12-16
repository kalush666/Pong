import pygame
from pygame.locals import *
import mysql.connector
from mysql.connector import Error

def connect_to_db():
    """
    Establish a connection to the MySQL database.
    """
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jonathan06",  # Replace with your MySQL password
            database="pong_game"
        )

        if db_connection.is_connected():
            print("Connected to MySQL database")
        return db_connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None


def get_high_scores():
    """
    Fetch the top 10 scores from the MySQL database.
    """
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor()
        query = """
        SELECT player1_name, player2_name, player1_score, player2_score
        FROM game_results
        ORDER BY GREATEST(player1_score, player2_score) DESC
        LIMIT 10
        """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db_connection.close()
        return results
    else:
        print("Failed to fetch high scores: No database connection")
        return []


def display_high_scores(screen, font):
    """
    Display the top 10 high scores in the pygame window.
    """
    scores = get_high_scores()

    screen.fill((0, 0, 0))  # Clear the screen (black background).
    title_text = font.render("Top 10 High Scores", True, (255, 255, 255))
    screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 50))

    # Render each score entry on the screen.
    y_offset = 120
    for i, (player1_name, player2_name, player1_score, player2_score) in enumerate(scores):
        score_text = f"{i+1}. {player1_name} ({player1_score}) vs {player2_name} ({player2_score})"
        score_surface = font.render(score_text, True, (255, 255, 255))
        screen.blit(score_surface, (50, y_offset))
        y_offset += 50

    # Render the "Press Enter to Continue" message.
    continue_text = font.render("Press Enter to continue...", True, (200, 200, 200))
    screen.blit(continue_text, (WINDOW_WIDTH // 2 - continue_text.get_width() // 2, y_offset + 30))

    pygame.display.update()

    # Wait for the player to press Enter.
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN and event.key == K_RETURN:  # Press Enter to continue.
                waiting = False


def display_name_input(screen, font):
    """
    Displays a prompt for players to input their names.
    """
    player1_name = ""
    player2_name = ""

    # Create an input box for player 1
    input_box_player1 = pygame.Rect(WINDOW_WIDTH // 4 - 100, WINDOW_HEIGHT // 2 - 40, 200, 50)
    input_box_player2 = pygame.Rect(WINDOW_WIDTH // 4 - 100, WINDOW_HEIGHT // 2 + 40, 200, 50)

    active_player1 = False
    active_player2 = False

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color_player1 = color_inactive
    color_player2 = color_inactive

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if active_player1:
                    if event.key == K_RETURN:
                        active_player1 = False
                    elif event.key == K_BACKSPACE:
                        player1_name = player1_name[:-1]
                    else:
                        player1_name += event.unicode
                if active_player2:
                    if event.key == K_RETURN:
                        active_player2 = False
                    elif event.key == K_BACKSPACE:
                        player2_name = player2_name[:-1]
                    else:
                        player2_name += event.unicode

            if event.type == MOUSEBUTTONDOWN:
                if input_box_player1.collidepoint(event.pos):
                    active_player1 = True
                    active_player2 = False
                elif input_box_player2.collidepoint(event.pos):
                    active_player2 = True
                    active_player1 = False

        # Fill the screen with a color
        screen.fill((0, 0, 0))

        # Render the current text.
        txt_surface_player1 = font.render(player1_name, True, (255, 255, 255))
        txt_surface_player2 = font.render(player2_name, True, (255, 255, 255))

        # Position the input boxes.
        width_player1 = max(200, txt_surface_player1.get_width()+10)
        width_player2 = max(200, txt_surface_player2.get_width()+10)

        input_box_player1.w = width_player1
        input_box_player2.w = width_player2

        # Draw the input boxes
        pygame.draw.rect(screen, color_player1, input_box_player1, 2)
        pygame.draw.rect(screen, color_player2, input_box_player2, 2)

        # Draw the text.
        screen.blit(txt_surface_player1, (input_box_player1.x+5, input_box_player1.y+5))
        screen.blit(txt_surface_player2, (input_box_player2.x+5, input_box_player2.y+5))

        # Render the "Enter names" prompt.
        prompt_text = font.render("Enter Player 1 and Player 2 Names", True, (255, 255, 255))
        screen.blit(prompt_text, (WINDOW_WIDTH // 2 - prompt_text.get_width() // 2, WINDOW_HEIGHT // 4))

        pygame.display.update()
        clock.tick(30)

        # Break the loop once both players have entered their names
        if not active_player1 and not active_player2:
            return player1_name, player2_name


# Game window setup
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Font for displaying text
font = pygame.font.Font(None, 50)

def main():
    """
    Main function to run the Pong game.
    Handles game initialization, input processing, game logic, and rendering.
    """
    # Show the high scores before starting the game
    display_high_scores(screen, font)

    # Ask players for their names
    player1_name, player2_name = display_name_input(screen, font)

    # Initialize game objects and loop (not implemented here for brevity)
    print(f"Player 1: {player1_name}, Player 2: {player2_name}")
    # You can continue with your game code after this...


if __name__ == '__main__':
    main()
