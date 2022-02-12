import pygame

class Keyboard:

    player_one = []
    player_two = []

    words = []
    turn = 0

    user_text = ""

    def __init__(self):
        word_file = open("content/PurdleWords.txt", "r")
        words = word_file.readlines()
        word_file.close()
    
    def update(self):
        pass

    def render(self):
        pass

    def get_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < 6:
                for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    if (event.unicode).upper == i:
                        self.user_text += event.unicode