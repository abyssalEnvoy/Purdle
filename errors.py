import time
import pygame

class Errors:
    NOT_IN_LIST = pygame.Rect(0, 0, 54, 8)
    ENOUGH_LETTERS = pygame.Rect(0, 8, 54, 14)
    
    alpha = []
    length = ""
    prev_time = time.time()
    delta_time = 0

    def update(self):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

        for i in range(len(self.alpha)):
            self.alpha[i] -= 1 * self.delta_time

    def render(self, target, error):
        num = len(self.length)
        for i in range(num):
            if self.alpha[0] <= 0:
                self.length = self.length[1::]
                self.alpha.pop(0)
                i -= 1

        for i in range(len(self.length)):
            error_type = self.NOT_IN_LIST
            offset_y = 0
            if self.length[i] == "1":
                error_type = self.NOT_IN_LIST
            else:
                error_type = self.ENOUGH_LETTERS
            
            for n in range(i):
                if self.length[n] == "1":
                    offset_y += 9
                elif self.length[n] == "0":
                    offset_y += 15
            
            sprite = error.subsurface(error_type)
            target.blit(sprite, (133, 48 + offset_y))