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

    pos_one = (59, 48)
    pos_two = (192, 48)

    x_spacing = 14
    y_spacing = 14

    def __init__(self, keyboard):
        self.keyboard = keyboard

    def update(self):
        # Player one
        self.player_one.clear()
        
        for w in self.keyboard.player_one:
            for c in range(len(w)):
                placed = False
                for n in range(len(self.keyboard.word)):
                    if w[c] == self.keyboard.word[n].upper():
                        if c == n:
                            # Green
                            self.player_one.append(self.SQUARE_GREEN)
                            placed = True
                        else:
                            # Yellow
                            self.player_one.append(self.SQUARE_YELLOW)
                            placed = True
                # Blue
                if not(placed):
                    self.player_one.append(self.SQUARE_BLUE)

        # Player two
        self.player_two.clear()
        
        for w in self.keyboard.player_two:
            for c in range(len(w)):
                placed = False
                for n in range(len(self.keyboard.word)):
                    if w[c] == self.keyboard.word[n].upper():
                        if c == n:
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
