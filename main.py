import sys, time
import pygame

from keyboard import Keyboard
from font import Font

# Screen size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360
VIEW_WIDTH = 320
VIEW_HEIGHT = 180

GRAPHICS = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
TARGET = pygame.Surface((VIEW_WIDTH, VIEW_HEIGHT))

# Color
CLEAR_COLOR = ((41,40,49))

# Time
FRAMERATE = 60
main_clock = pygame.time.Clock()

# Sprites
BACKGROUND = pygame.image.load("content/PurdleBackground.png").convert()
FONT = pygame.image.load("content/PurdleFont.png").convert_alpha()
KEYBOARD = pygame.image.load("content/PurdleKeyboard.png").convert_alpha()

# Objects
keyboard = Keyboard()
font = Font(FONT)

def render():
    GRAPHICS.fill(CLEAR_COLOR)
    TARGET.blit(BACKGROUND, (0, 0))
    TARGET.blit(KEYBOARD, (32, 136))

    font.render(TARGET, "HAHAH", (0, 0))
    #region Render target resizing

    window_width, window_height = GRAPHICS.get_size()
    scale = min(window_width / VIEW_WIDTH, window_height / VIEW_HEIGHT)

    bar_width = int((window_width - int(VIEW_WIDTH * scale)) / 2)
    bar_height = int((window_height - int(VIEW_HEIGHT * scale)) / 2)

    resized = pygame.transform.scale(TARGET, (int(VIEW_WIDTH * scale), int(VIEW_HEIGHT * scale)))
    GRAPHICS.blit(resized, (bar_width, bar_height))
    
    pygame.display.update()

    #endregion

def main():
    pygame.init()
    pygame.display.set_caption("Purdle")

    prev_time = time.time()
    delta_time = 0

    user_text = ""

    while True:
        main_clock.tick(FRAMERATE)
        pygame.display.set_caption("Purdle FPS: {}".format(main_clock.get_fps()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keyboard.get_input(event)

        current_time = time.time()
        delta_time = current_time - prev_time
        prev_time = current_time
        
        keyboard.update()

        render()

if __name__ == "__main__":
    main()