#THIS IS A MEME GENERATOR WITH DRAKE HOT LINK BLINK

import pygame
import requests
import io
import textwrap

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# Update this to the specified font path
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
FONT_SIZE = 50

# Load image from URL (Optional function, not used in this case)
def load_image_from_url(url):
    r = requests.get(url)
    img = io.BytesIO(r.content)
    return pygame.image.load(img, namehint="")

# Render text with stroke
def render_text_with_stroke(font, text, text_color, stroke_color, stroke_width):
    text_surface = font.render(text, True, text_color)
    w, h = text_surface.get_size()
    surface = pygame.Surface((w + 2 * stroke_width, h + 2 * stroke_width), pygame.SRCALPHA)
    for dx in range(-stroke_width, stroke_width + 1):
        for dy in range(-stroke_width, stroke_width + 1):
            if dx != 0 or dy != 0:
                surface.blit(font.render(text, True, stroke_color), (dx + stroke_width, dy + stroke_width))
    surface.blit(text_surface, (stroke_width, stroke_width))
    return surface

# Create a meme
def create_meme(image_path, top_text, bottom_text, font_path, font_size):
    # Load image
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(image, (0, 0))

    # Load font
    font = pygame.font.Font(font_path, font_size)

    #text position and size
    top_text = textwrap.fill(top_text, width=20)
    bottom_text = textwrap.fill(bottom_text, width=20)

    #top text
    top_surface = render_text_with_stroke(font, top_text, (255, 255, 255), (0, 0, 0), 2)
    top_rect = top_surface.get_rect(center=(SCREEN_WIDTH * 1.0, SCREEN_HEIGHT * 0.25))  # Adjusted to the right
    screen.blit(top_surface, top_rect.topleft)

    # bottom text
    bottom_surface = render_text_with_stroke(font, bottom_text, (255, 255, 255), (0, 0, 0), 2)
    bottom_rect = bottom_surface.get_rect(center=(SCREEN_WIDTH * 1.0, SCREEN_HEIGHT * 0.75))  # Adjusted to the right
    screen.blit(bottom_surface, bottom_rect.topleft)

    pygame.display.update()

    # Save the final image
    pygame.image.save(screen, "meme_output.png")

# Example usage with local image path
image_path = "/Users/jeshurunbiney/Downloads/Drake-Hotline-Bling (2).jpg"
create_meme(
    image_path,
    "MAKING GAMES\nFOR HACKATON",
    "MAKING MEMES",
    FONT_PATH,
    FONT_SIZE
)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
