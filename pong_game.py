import pygame
import sys
from Rectangle import Rectangle
from Circle import Circle

# initilizing pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Pong Game")
text_font = pygame.font.Font(None, 30)
rect1 = Rectangle("left", screen)
rect2 = Rectangle("", screen)
circle = Circle(screen, rect1, rect2)
game_active = True
game_start = False
start_time = 0


# count score
def get_score():

    current_time = pygame.time.get_ticks() - start_time
    score = int(current_time / 1000)
    score_text = text_font.render(f"Score: {score}", True, "White")
    score_text_rect = score_text.get_rect(center=(250, 20))
    pygame.draw.rect(screen, "Blue", score_text_rect, 0, 10)
    screen.blit(score_text, score_text_rect)


# main() of game
while True:
    clock.tick(60)
    # provide functionality of x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # when user press space game starts
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True
                circle.x = screen.get_width() / 2
                circle.y = screen.get_height() / 2
                game_start = True
                start_time = pygame.time.get_ticks()

    if game_start:
        if game_active:

            screen.fill("Black")
            get_score()
            circle.update()
            rect1.update()
            rect2.update()
            game_active = circle.gameover()
        else:
            screen.fill("Black")
            gameover_text = text_font.render("Game Over", True, "White")
            gameover_text_rect = gameover_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(gameover_text, gameover_text_rect)
    else:
        screen.fill("Black")
        game_start_text = text_font.render("Press space for play", True, "White")
        game_start_text_rect = game_start_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(game_start_text, game_start_text_rect)
    pygame.display.update()
