import random
import pygame

from errors import Errors

class Keyboard:

    player_one = []
    player_two = []

    pos_one = (62, 50)
    pos_two = (195, 50)

    pos_render = (0, 0)

    words_list = []
    word = ""
    turn = 0

    spacing = 0
    user_text = ""
    previous_key = []

    errors = Errors()

    def __init__(self):
        word_file = open("content/PurdleWords.txt", "r")
        self.words_list = word_file.readlines()
        word_file.close()

        for i in range(len(self.words_list)):
            self.words_list[i] = self.words_list[i].strip()

        self.word = self.words_list[random.randint(0, len(self.words_list) - 1)]
    
    def update(self):
        self.errors.update()

        if self.turn == 0:
            self.pos_render =  (self.pos_one[0], self.pos_one[1] + self.spacing)
        else:
            self.pos_render =  (self.pos_two[0], self.pos_two[1] + self.spacing)

        keys_down = pygame.key.get_pressed()

        if keys_down[pygame.K_RETURN] and not self.previous_key[pygame.K_RETURN]:
            word_in_list = False
            for n in self.words_list:
                if self.user_text == n.upper():
                    if self.turn == 0:
                        self.player_one.append(self.user_text)
                    else:
                        self.player_two.append(self.user_text)
                        self.spacing += 14

                    self.turn += 1
                    if self.turn > 1:
                        self.turn = 0
                    self.user_text = ""
                    word_in_list = True
                    break

            if not(word_in_list):
                if len(self.user_text) < 5:
                    self.errors.length += "0"
                else:
                    self.errors.length += "1"
                self.errors.alpha.append(1)

        self.previous_key = keys_down
            

    def render(self, target, font, errors):
        for i in range(len(self.player_one)):
            font.render(target, self.player_one[i], (self.pos_one[0], self.pos_one[1] + i * 14))
        
        for i in range(len(self.player_two)):
            font.render(target, self.player_two[i], (self.pos_two[0], self.pos_two[1] + i * 14))
        
        font.render(target, self.user_text, self.pos_render)
        font.render(target, self.word.upper(), (0, 0))
        self.errors.render(target, errors)


    def get_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < 5:
                for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    if str(event.unicode).upper() == i:
                        self.user_text += i