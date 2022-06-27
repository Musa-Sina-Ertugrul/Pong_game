import pygame

pygame.init()


class Circle(pygame.sprite.Sprite):
    def __init__(self, screen, rect1, rect2):
        super().__init__()
        self.screen = screen
        self.rect1 = rect1
        self.rect2 = rect2
        self.x = self.screen.get_width() / 2
        self.y = self.screen.get_height() / 2
        self.dy = 3
        self.dx = 3
        self.circle = pygame.draw.circle(self.screen, "White", (self.x, self.y), 10)

    # moves circle
    def movement(self):
        self.circle = pygame.draw.circle(self.screen, "White", (self.x, self.y), 10)
        self.y += self.dy
        self.x += self.dx
        if self.x < 10 or self.x > 490:
            self.dx *= -1
        if self.y < 10 or self.y > 290:
            self.dy *= -1

    # finish game
    def gameover(self):
        if self.x - 10 <= 10 or self.x + 10 >= 490:
            return False
        return True

    # bounce circle
    def collision(self):
        if self.x - 20 == self.rect1.left_x + 10 or self.x + 20 == self.rect2.right_x:
            if (self.rect1.left_y + 60 >= self.y >= self.rect1.left_y) or (
                    self.rect2.right_y + 60 >= self.y >= self.rect2.right_y):
                print("True")
                self.dx *= -1
                self.dy *= -1

    def update(self):
        self.movement()
        self.collision()
