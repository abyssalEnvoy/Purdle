import random
import pygame

from errors import Errors

class Keyboard:

    player_one = []
    player_two = []

    won_one = False
    won_two = False

    win_one_num = 7
    win_one_num = 7

    game_over = False
    restart = False

    pos_one = (62, 50)
    pos_two = (195, 50)

    pos_render = (0, 0)

    words_list = []
    word_one = ""
    word_two = ""
    turn = 0
    enter = False

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

        self.word_one = self.words_list[random.randint(0, len(self.words_list) - 1)]
        self.word_two = self.words_list[random.randint(0, len(self.words_list) - 1)]

        self.previous_key = pygame.key.get_pressed()
    
    def update(self):
        self.errors.update()

        keys_down = pygame.key.get_pressed()

        if (keys_down[pygame.K_RETURN] and not self.previous_key[pygame.K_RETURN]) or self.enter == True:
            if not(self.game_over):
                word_in_list = False
                for n in self.words_list:
                    if self.user_text == n.upper():
                        if self.turn == 0:
                            self.player_one.append(self.user_text)
                            if self.won_two:
                                self.spacing += 14
                        else:
                            self.player_two.append(self.user_text)
                            self.spacing += 14

                        if not(self.won_two or self.won_one):
                            self.turn += 1
                        else:
                            self.turn += 2
                        
                        if self.turn % 2 == 0:
                            self.turn = 0
                        else:
                            self.turn = 1

                        self.user_text = ""
                        word_in_list = True
                        break

                if not(word_in_list):
                    if len(self.user_text) < 5:
                        self.errors.length = "0" + self.errors.length
                    else:
                        self.errors.length = "1" + self.errors.length
                    self.errors.alpha.insert(0, 1)
                    self.errors.wait_time.insert(0, 0.8)
            else:
                self.restart = True

            for n in range(len(self.player_one)):
                if self.player_one[n] == self.word_one.upper():
                    self.won_one = True
                    self.win_one_num = n

            for n in range(len(self.player_two)):
                if self.player_two[n] == self.word_two.upper():
                    self.won_two = True
                    self.win_two_num = n

            if len(self.player_two) >= 6 or (len(self.player_one) >= 6 and self.won_two) or (self.won_two and self.won_one):
                self.game_over = True

        self.enter = False

        if self.turn == 0:
            self.pos_render =  (self.pos_one[0], self.pos_one[1] + self.spacing)
        else:
            self.pos_render =  (self.pos_two[0], self.pos_two[1] + self.spacing)

        self.previous_key = keys_down
            

    def render(self, target, font, errors):
        for i in range(len(self.player_one)):
            font.render(target, self.player_one[i], (self.pos_one[0], self.pos_one[1] + i * 14))
        
        for i in range(len(self.player_two)):
            font.render(target, self.player_two[i], (self.pos_two[0], self.pos_two[1] + i * 14))
        
        font.render(target, self.user_text, self.pos_render)
        #font.render(target, self.word_one.upper(), (0, 0))
        #font.render(target, self.word_two.upper(), (257, 0))
        self.errors.render(target, errors)

    def get_input(self, event):
        if len(self.player_two) <= 5 and not(self.game_over):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                elif len(self.user_text) < 5:
                    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        if str(event.unicode).upper() == i:
                            self.user_text += i