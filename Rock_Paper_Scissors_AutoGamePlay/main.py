import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors")

# Define colors
WHITE = (255, 255, 255)

# Load the original images
# Replace with your rock image
rock_image = pygame.image.load("rock_image.png")
# Replace with your paper image
paper_image = pygame.image.load("paper_image.png")
# Replace with your scissors image
scissors_image = pygame.image.load("scissors_image.png")

# Resize the images to 25x25 pixels
rock_image = pygame.transform.scale(rock_image, (25, 25))
paper_image = pygame.transform.scale(paper_image, (25, 25))
scissors_image = pygame.transform.scale(scissors_image, (25, 25))

# Create instances of each choice with the resized images


class Rock:
    def __init__(self):
        self.image = rock_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)
        self.velocity = [random.uniform(-1, -0.1) if random.random() < 0.5 else random.uniform(0.1, 1),
                         random.uniform(-1, -0.1) if random.random() < 0.5 else random.uniform(0.1, 1)]
        self.max_velocity = 3
        # self.acceleration = [
        #    random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]

    def update(self, choices):
        # Randomly adjust the velocity of the Rock instance
        self.velocity[0] += random.uniform(-0.1, 0.1)
        self.velocity[1] += random.uniform(-0.1, 0.1)

        # Limit the maximum velocity to avoid too fast or erratic movement
        if abs(self.velocity[0]) > self.max_velocity:
            self.velocity[0] = self.max_velocity if self.velocity[0] > 0 else - \
                self.max_velocity
        if abs(self.velocity[1]) > self.max_velocity:
            self.velocity[1] = self.max_velocity if self.velocity[1] > 0 else - \
                self.max_velocity

        # Update the position of the Rock instance based on its velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        for choice in choices:
            if choice != self and self.rect.colliderect(choice.rect):
                if isinstance(choice, Paper):
                    self.__class__ = Paper
                    self.image = paper_image  # Convert to Paper if collides with Paper
                elif isinstance(choice, Scissors):
                    choice.__class__ = Rock  # Convert Scissors to Rock if collided by Scissors
                    choice.velocity = self.velocity  # Update Scissors velocity to Rock's velocity
                    choice.image = rock_image
                    return  # No further collision checks needed for this instance

        # Check window boundaries
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.velocity[1] *= -1


class Paper:
    def __init__(self):
        self.image = paper_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)
        self.velocity = [random.uniform(-1, -0.1) if random.random() < 0.5 else random.uniform(0.1, 1),
                         random.uniform(-1, -0.1) if random.random() < 0.5 else random.uniform(0.1, 1)]
        self.max_velocity = 3
        # self.acceleration = [
        #    random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]

    def update(self, choices):
        # Randomly adjust the velocity of the Rock instance
        self.velocity[0] += random.uniform(-0.1, 0.1)
        self.velocity[1] += random.uniform(-0.1, 0.1)

        # Limit the maximum velocity to avoid too fast or erratic movement
        if abs(self.velocity[0]) > self.max_velocity:
            self.velocity[0] = self.max_velocity if self.velocity[0] > 0 else - \
                self.max_velocity
        if abs(self.velocity[1]) > self.max_velocity:
            self.velocity[1] = self.max_velocity if self.velocity[1] > 0 else - \
                self.max_velocity

        # Update the position of the Rock instance based on its velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        for choice in choices:
            if choice != self and self.rect.colliderect(choice.rect):
                if isinstance(choice, Rock):
                    choice.__class__ = Paper  # Convert Rock to Paper if collided by Rock
                    choice.velocity = self.velocity  # Update Rock's velocity to Paper's velocity
                    choice.image = paper_image
                    return  # No further collision checks needed for this instance
                elif isinstance(choice, Scissors):
                    self.__class__ = Scissors
                    self.image = scissors_image  # Convert to Scissors if collides with Scissors
                    return  # No further collision checks needed for this instance

        # Check window boundaries
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.velocity[1] *= -1


class Scissors:
    def __init__(self):
        self.image = scissors_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)
        self.velocity = [random.uniform(-1, -0.1) if random.random() < 0.5 else random.uniform(0.1, 1),
                         random.uniform(-1, -0.1) if random.random() < 0.5 else random.uniform(0.1, 1)]
        self.max_velocity = 3
        # self.acceleration = [
        #    random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]

    def update(self, choices):
        # Randomly adjust the velocity of the Rock instance
        self.velocity[0] += random.uniform(-0.1, 0.1)
        self.velocity[1] += random.uniform(-0.1, 0.1)

        # Limit the maximum velocity to avoid too fast or erratic movement
        if abs(self.velocity[0]) > self.max_velocity:
            self.velocity[0] = self.max_velocity if self.velocity[0] > 0 else - \
                self.max_velocity
        if abs(self.velocity[1]) > self.max_velocity:
            self.velocity[1] = self.max_velocity if self.velocity[1] > 0 else - \
                self.max_velocity

        # Update the position of the Rock instance based on its velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        for choice in choices:
            if choice != self and self.rect.colliderect(choice.rect):
                if isinstance(choice, Paper):
                    choice.__class__ = Scissors  # Convert Paper to Scissors if collided by Paper
                    choice.velocity = self.velocity  # Update Paper's velocity to Scissors's velocity
                    choice.image = scissors_image
                    return  # No further collision checks needed for this instance
                elif isinstance(choice, Rock):
                    self.__class__ = Rock  # Convert to Rock if collides with Rock
                    self.image = rock_image
                    return  # No further collision checks needed for this instance

        # Check window boundaries
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
            self.velocity[1] *= -1


# Create instances of each choice
rocks = [Rock() for _ in range(5)]
papers = [Paper() for _ in range(5)]
scissors = [Scissors() for _ in range(5)]

choices = rocks + papers + scissors

# Main game loop
font = pygame.font.Font(None, 24)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    counts = {'Rock': 0, 'Paper': 0, 'Scissors': 0}
    window.fill(WHITE)

    for choice in choices:
        choice.update(choices)
        window.blit(choice.image, choice.rect)
        # Display the class of each instance as text on the window
        # text = font.render(str(choice.__class__.__name__),True, (0, 0, 0))  # Get class name as text
        # Display text above the instance
        #window.blit(text, (choice.rect.x, choice.rect.y - 20))
        # Update counts for each class
        counts[choice.__class__.__name__] += 1

    # Check if all instances are of a single class type
    # Inside the main game loop, after the game has ended
    if any(count == len(choices) for count in counts.values()):
        # Find the winning class
        winning_class = max(counts, key=counts.get)

        # Create a font object for displaying text
        font = pygame.font.Font(None, 72)

        # Render text with the winning class
        # Red color for visibility
        text = font.render(f"Winner: {winning_class}", True, (255, 0, 0))
        text_rect = text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        # Display the text on the window
        window.fill(WHITE)  # Clear the window
        window.blit(text, text_rect)
        pygame.display.update()

        # Delay to show the message for a few seconds before closing the window
        pygame.time.delay(3000)  # Display the message for 3 seconds

        running = False  # End the game loop and close the window

    pygame.display.update()
    clock.tick(60)

pygame.quit()
