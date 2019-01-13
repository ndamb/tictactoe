import pygame

first_run = True
SCREEN_CLR = (75, 75, 75)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

def draw_main_menu(screen):
    screen.fill(WHITE)
    pygame.font.init()
    title_font = pygame.font.SysFont("Comic Sans MS", 30)
    textsurface = title_font.render("Tic-Tac-Toe", False, (0, 0, 0))
    screen.blit(textsurface, (70, 100))
    button_font = pygame.font.SysFont("Comic Sans MS", 15)
    buttonsurface = button_font.render("Start", False, (0, 0, 0))
    pygame.draw.rect(screen, SCREEN_CLR, (30, 250, 80, 40), 0)
    screen.blit(buttonsurface, (50, 260))
    pygame.draw.rect(screen, SCREEN_CLR, (150, 250, 80, 40), 0)
    buttonsurface2 = button_font.render("Optionen", False, (0, 0, 0))
    screen.blit(buttonsurface2, (160, 260))


def draw_options(screen):
    screen.fill(WHITE)
    pygame.draw.rect(screen, SCREEN_CLR, (250, 250, 40, 40))
    button_font = pygame.font.SysFont("Comic Sans MS", 30)
    button_surface = button_font.render("<-", False, (0, 0, 0))
    screen.blit(button_surface, (260, 247))
    options = True
    return options


def draw_game_field(screen, first_run):
    screen.fill(SCREEN_CLR)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)
