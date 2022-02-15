import pygame

class Keys:
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    keys = []
    action_keys = []

    key_row_one = (28, 132)
    key_row_two = (10, 144)
    key_row_three = (34, 156)

    keyboard = object

    x_spacing = 14
    previous_key = []

    def __init__(self, keyboard):
        self.keyboard = keyboard

        self.keys.clear()
        self.action_keys.clear()

        for i in range(len(self.letters)):
            pos = (0, 0)
            offset_x = i

            if offset_x > 18:
                pos = self.key_row_three
                offset_x -= 18
            elif offset_x > 9:
                pos = self.key_row_two
                offset_x -= 8
            else:
                pos = self.key_row_one
            
            rect = pygame.Rect(pos[0] + offset_x * 12, pos[1], 11, 11)
            self.keys.append(rect)
        
        self.action_keys.append(pygame.Rect(28, 156, 17, 11))
        self.action_keys.append(pygame.Rect(130, 156, 17, 11))

        self.previous_key = pygame.mouse.get_pressed()

    def update(self, mouse_pos):
        keys_down = pygame.mouse.get_pressed()
        
        actual_keys = []
        actual_action_keys = []

        if self.keyboard.turn == 0:
            for i in self.keys:
                actual_keys.append(i)
            for i in self.action_keys:
                actual_action_keys.append(i)
        else:
            for i in self.keys:
                actual_keys.append(pygame.Rect(i[0] + 137, i[1], i[2], i[3]))
            for i in self.action_keys:
                actual_action_keys.append(pygame.Rect(i[0] + 137, i[1], i[2], i[3]))

        if keys_down[0] and not self.previous_key[0]:
            for i in range(len(actual_action_keys)):
                if actual_action_keys[i].collidepoint(mouse_pos):
                    if i == 0:
                        self.keyboard.enter = True
                    else:
                        if len(self.keyboard.player_two) <= 5 and not(self.keyboard.game_over):
                            self.keyboard.user_text = self.keyboard.user_text[:-1]

            for i in range(len(actual_keys)):
                if actual_keys[i].collidepoint(mouse_pos):
                    if len(self.keyboard.player_two) <= 5 and not(self.keyboard.game_over):
                        if len(self.keyboard.user_text) < 5:
                            self.keyboard.user_text += self.letters[i]

        self.previous_key = keys_down