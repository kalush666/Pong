import random
import pygame

class Ball:
    def __init__(self, x, y, radius):
        """
        Initialize the Ball object with its position, size, velocity, and color.

        Args:
            x (int): The x-coordinate of the ball.
            y (int): The y-coordinate of the ball.
            radius (int): The radius of the ball.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity_x = 5  # Initial horizontal velocity of the ball.
        self.velocity_y = 5  # Initial vertical velocity of the ball.
        self.color = (255, 255, 255)  # Initial color of the ball is white.

    def draw(self, screen):
        """
        Draw the ball on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the ball on.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, player1, player2):
        """
        Update the ball's position, handle wall and paddle collisions,
        and change its color and speed if it hits a paddle.

        Args:
            player1 (Paddle): The first player's paddle.
            player2 (Paddle): The second player's paddle.
        """
        # Update the ball's position.
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Check for collisions with the top and bottom walls.
        if self.y - self.radius <= 0 or self.y + self.radius >= 720:
            # Reverse the vertical velocity upon collision.
            self.velocity_y = -self.velocity_y

        # Check for collisions with player1's paddle.
        if (
            self.x - self.radius <= player1.x + player1.width and
            player1.y <= self.y <= player1.y + player1.height
        ):
            self.velocity_x = -self.velocity_x  # Reverse horizontal velocity.
            self.change_color()  # Change the ball's color.
            if abs(self.velocity_x) < 6:  # Increase speed if below the threshold.
                self.velocity_x *= 1.5

        # Check for collisions with player2's paddle.
        if (
            self.x + self.radius >= player2.x and
            player2.y <= self.y <= player2.y + player2.height
        ):
            self.velocity_x = -self.velocity_x  # Reverse horizontal velocity.
            self.change_color()  # Change the ball's color.
            if abs(self.velocity_x) < 6:  # Increase speed if below the threshold.
                self.velocity_x *= 1.5

    def change_color(self):
        """
        Change the ball's color to a random RGB value.
        """
        self.color = (
            random.randint(0, 255),  # Random red component.
            random.randint(0, 255),  # Random green component.
            random.randint(0, 255),  # Random blue component.
        )

    def reset(self, x, y):
        """
        Reset the ball's position, direction, speed, and color after a point is scored.

        Args:
            x (int): The new x-coordinate for the ball.
            y (int): The new y-coordinate for the ball.
        """
        self.x = x
        self.y = y
        self.velocity_x *= -1  # Reverse horizontal direction.
        self.velocity_y = 5  # Reset vertical speed.
        self.color = (255, 255, 255)  # Reset color to white.
