import pygame

class Blocks:
    SQUARE_BLUE = pygame.Rect(0, 0, 13, 13)
    SQUARE_GREEN = pygame.Rect(13, 0, 13, 13)
    SQUARE_YELLOW = pygame.Rect(26, 0, 13, 13)

    CIRCLE_BLUE = pygame.Rect(39, 0, 11, 11)
    CIRCLE_GREEN = pygame.Rect(50, 0, 11, 11)
    CIRCLE_YELLOW = pygame.Rect(61, 0, 11, 11)

    keyboard = object

    player_one = []
    player_two = []

    letters_one = []
    letters_two = []

    letters = "QWERRTYUIOPASDFGHJKLZXCVBNM"

    key_row_one = (20, 136)
    key_row_two = (14, 148)
    key_row_three = (38, 160)

    pos_one = (59, 48)
    pos_two = (192, 48)

    x_spacing = 14
    y_spacing = 14

    def __init__(self, keyboard):
        self.keyboard = keyboard

    def update(self):
        # Player one
        self.player_one.clear()
        self.letters_one.clear()
        
        for word in self.keyboard.player_one:
            for char in range(len(word)):
                has = False
                for i in self.letters_one:
                    if char == i:
                        has = True
                if not(has):
                    self.letters_one.append(word[char])

                placed = False
                for letter in range(len(self.keyboard.word)):
                    if word[char] == self.keyboard.word[letter].upper():
                        if char == letter:
                            # Green
                            if not(placed):
                                self.player_one.append(self.SQUARE_GREEN)
                                placed = True
                        else:
                            # Yellow
                            if not(placed):
                                self.player_one.append(self.SQUARE_YELLOW)
                                placed = True
                # Blue
                if not(placed):
                    self.player_one.append(self.SQUARE_BLUE)

        # Player two
        self.player_two.clear()
        self.letters_two.clear()
        
        for word in self.keyboard.player_two:
            for char in range(len(word)):
                has = False
                for i in self.letters_two:
                    if word[char] == i:
                        has = True
                if not(has):
                    self.letters_two.append(word[char])

                placed = False
                for letter in range(len(self.keyboard.word)):
                    if word[char] == self.keyboard.word[letter].upper():
                        if char == letter:
                            # Green
                            self.player_two.append(self.SQUARE_GREEN)
                            placed = True
                        else:
                            # Yellow
                            self.player_two.append(self.SQUARE_YELLOW)
                            placed = True
                # Blue
                if not(placed):
                    self.player_two.append(self.SQUARE_BLUE)
    
    def render(self, target, blocks):
        for i in range(len(self.player_one)):
            mod_x = i - (i // 5) * 5
            pos_x = self.pos_one[0] + mod_x * self.x_spacing

            mod_y = i // 5
            pos_y = self.pos_one[1] + mod_y * self.y_spacing

            sprite = blocks.subsurface(self.player_one[i])
            target.blit(sprite, (pos_x, pos_y))
        
        for i in range(len(self.player_two)):
            mod_x = i - (i // 5) * 5
            pos_x = self.pos_two[0] + mod_x * self.x_spacing

            mod_y = i // 5
            pos_y = self.pos_two[1] + mod_y * self.y_spacing

            sprite = blocks.subsurface(self.player_two[i])
            target.blit(sprite, (pos_x, pos_y))
        
        # player one's keyboad letter colours
        for i in range(len(self.letters_one)):
            num = 0
            for n in range(len(self.letters)):
                if self.letters_one[i] == self.letters[n]:
                    num = n
            
            pos = (0, 0)
            offset_x = num

            if offset_x > 19:
                pos = self.key_row_three
                offset_x -= 19
            elif offset_x > 10:
                pos = self.key_row_two
                offset_x -= 9
            else:
                pos = self.key_row_one


            sprite = blocks.subsurface(self.CIRCLE_BLUE)
            for word in self.keyboard.player_one:
                for char in range(len(word)):
                    if word[char] == self.letters[num]:
                        if self.player_one[char] == self.SQUARE_YELLOW: 
                            sprite = blocks.subsurface(self.CIRCLE_YELLOW)
                        elif self.player_one[char] == self.SQUARE_GREEN:
                            sprite = blocks.subsurface(self.CIRCLE_GREEN)

            target.blit(sprite, (pos[0] + offset_x * 12, pos[1]) )
        
        # Player two's keyboard letter colours
        for i in range(len(self.letters_two)):
            num = 0
            for n in range(len(self.letters)):
                if self.letters_two[i] == self.letters[n]:
                    num = n
            
            pos = (0, 0)
            offset_x = num

            if offset_x > 19:
                pos = self.key_row_three
                offset_x -= 19
            elif offset_x > 10:
                pos = self.key_row_two
                offset_x -= 9
            else:
                pos = self.key_row_one


            sprite = blocks.subsurface(self.CIRCLE_BLUE)
            for word in self.keyboard.player_two:
                for char in range(len(word)):
                    if word[char] == self.letters[num]:
                        if self.player_two[char] == self.SQUARE_YELLOW: 
                            sprite = blocks.subsurface(self.CIRCLE_YELLOW)
                        elif self.player_two[char] == self.SQUARE_GREEN:
                            sprite = blocks.subsurface(self.CIRCLE_GREEN)

            target.blit(sprite, (pos[0] + offset_x * 12 + 137, pos[1]) )
