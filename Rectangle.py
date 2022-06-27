import pygame

pygame.init()


class Rectangle(pygame.sprite.Sprite):

    def __init__(self, type, screen):
        super().__init__()
        self.width = 10
        self.height = 60
        self.type = type
        self.screen = screen
        self.left_x = 10
        self.left_y = 100
        self.right_x = self.screen.get_width() - 20
        self.right_y = 100
        if self.get_type() == "left":
            self.rectangle = pygame.draw.rect(self.get_screen(), "White", (self.get_left_x(), self.get_left_y(),
                                                                           self.get_width(), self.get_height()), 0, 3)
        else:
            self.rectangle = pygame.draw.rect(self.get_screen(), "White", (self.get_right_x(), self.get_right_y(),
                                                                           self.get_width(), self.get_height()), 0, 3)

    # getter and some setters
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_type(self):
        return self.type

    def get_screen(self):
        return self.screen

    def get_left_x(self):
        return self.left_x

    def get_left_y(self):
        return self.left_y

    def get_right_x(self):
        return self.right_x

    def get_right_y(self):
        return self.right_y

    def set_left_y(self, n):
        self.left_y = n

    def set_left_x(self, n):
        self.left_x = n

    def get_rectangle(self):
        return self.rectangle

    # organize movements of rectangles
    def movement(self):
        keys = pygame.key.get_pressed()
        if self.type == "left":
            self.rectangle = pygame.draw.rect(self.screen, "White", (self.left_x, self.left_y, self.width, self.height),
                                              0,
                                              3)
            if keys[pygame.K_DOWN] and self.left_y < self.screen.get_height() - 60:
                self.left_y += 3
            if keys[pygame.K_UP] and self.left_y > 0:
                self.left_y -= 3
        else:
            self.rectangle = pygame.draw.rect(self.screen, "White",
                                              (self.right_x, self.right_y, self.width, self.height), 0, 3)
            if keys[pygame.K_s] and self.right_y < self.screen.get_height() - 60:
                self.right_y += 3
            if keys[pygame.K_w] and self.right_y > 0:
                self.right_y -= 3

    # updates methods
    def update(self):
        self.movement()
