import sys, time
import pygame

from keyboard import Keyboard
from font import Font
from blocks import Blocks
from keys import Keys

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
BLOCK = pygame.image.load("content/PurdleBlocks.png").convert_alpha()
FONT = pygame.image.load("content/PurdleFont.png").convert_alpha()
KEYBOARD = pygame.image.load("content/PurdleKeyboard.png").convert_alpha()
ERRORS = pygame.image.load("content/PurdleErrors.png").convert_alpha()
END = pygame.image.load("content/PurdleEnd.png").convert_alpha()
ICON = pygame.image.load("content/PurdleIcon.png").convert()
CURSOR = pygame.image.load("content/PurdleCursor.png").convert_alpha()

def render(keyboard, blocks, font):
    GRAPHICS.fill(CLEAR_COLOR)
    TARGET.blit(BACKGROUND, (0, 0))

    blocks.render(TARGET, BLOCK)
    TARGET.blit(KEYBOARD, (32, 136))
    
    keyboard.render(TARGET, font, ERRORS)

    if keyboard.game_over:
        TARGET.blit(END, (132, 40))
        if keyboard.won_one and keyboard.won_two:
            if keyboard.win_one_num <= keyboard.win_two_num:
                font.render(TARGET, "ONE", (137, 53))
                font.render(TARGET, "TWO", (149, 102))
            else:
                font.render(TARGET, "TWO", (137, 53))
                font.render(TARGET, "ONE", (149, 102))  
        elif keyboard.won_one:
            font.render(TARGET, "ONE", (137, 53))
            font.render(TARGET, "TWO", (149, 102))
        elif keyboard.won_two:
            font.render(TARGET, "TWO", (137, 53))
            font.render(TARGET, "ONE", (149, 102))  
        else:
            font.render(TARGET, "NIL", (137, 53))
            font.render(TARGET, "NIL", (149, 102))
        
        font.render(TARGET, keyboard.word_one.upper(), (keyboard.pos_one[0], keyboard.pos_one[1] - 14))
        font.render(TARGET, keyboard.word_two.upper(), (keyboard.pos_two[0], keyboard.pos_two[1] - 14))

    #region Render target resizing

    window_width, window_height = GRAPHICS.get_size()
    scale = min(window_width / VIEW_WIDTH, window_height / VIEW_HEIGHT)

    bar_width = int((window_width - int(VIEW_WIDTH * scale)) / 2)
    bar_height = int((window_height - int(VIEW_HEIGHT * scale)) / 2)

    TARGET.blit(CURSOR, ((pygame.mouse.get_pos()[0] - bar_width) / scale - 4, (pygame.mouse.get_pos()[1] - bar_height) / scale - 4))

    resized = pygame.transform.scale(TARGET, (int(VIEW_WIDTH * scale), int(VIEW_HEIGHT * scale)))
    GRAPHICS.blit(resized, (bar_width, bar_height))
    
    pygame.display.update()

    #endregion

def main():
    # Objects
    keyboard = Keyboard()
    keyboard.player_one = []
    keyboard.player_two = []
    font = Font(FONT)
    blocks = Blocks(keyboard)
    keys = Keys(keyboard)

    pygame.init()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("Purdle")
    pygame.mouse.set_visible(False)

    prev_time = time.time()
    delta_time = 0

    while True:
        main_clock.tick(FRAMERATE)
        #pygame.display.set_caption("Purdle FPS: {}".format(main_clock.get_fps()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keyboard.get_input(event)

        current_time = time.time()
        delta_time = current_time - prev_time
        prev_time = current_time
        
        keyboard.update()
        blocks.update()

        window_width, window_height = GRAPHICS.get_size()
        scale = min(window_width / VIEW_WIDTH, window_height / VIEW_HEIGHT)

        bar_width = int((window_width - int(VIEW_WIDTH * scale)) / 2)
        bar_height = int((window_height - int(VIEW_HEIGHT * scale)) / 2)

        keys.update((int((pygame.mouse.get_pos()[0] - bar_width) / scale - 4), int((pygame.mouse.get_pos()[1] - bar_height) / scale - 4)))

        render(keyboard, blocks, font)

        # Restart game
        if keyboard.restart:
            main()

if __name__ == "__main__":
    main()