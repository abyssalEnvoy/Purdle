import pygame

class Font:
    
    spacing = 6
    char_width = 8
    char_order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters = {}

    def __init__(self, font):
        char_count = 0 
        for x in range(font.get_width()):
            if x != 0 and x % self.char_width == 0:
                char = self.clip(font, x - self.char_width, 0, self.char_width, font.get_height()) 
                self.characters[self.char_order[char_count]] = char
                if char_count < 25:
                    char_count += 1
    
    def clip(self, surf, x, y, width, height):
        sprite = surf.subsurface(pygame.Rect(x, y, width, height))
        return sprite

    def render(self, target, text, pos):
        x_offset = 0
        for n in text:
            target.blit(self.characters[n], (pos[0] + x_offset, pos[1]))
            x_offset += self.char_width + self.spacing