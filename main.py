import pygame


class DialogWindow:
    def __init__(self):
        pass


class Board:
    def __init__(self, size):
        self.board = [[0 for i in range(size)] for j in range(size)]

    def board_checking(self):
        pass


pygame.init()
pygame.display.set_caption('PyGo')
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

screen.fill((0, 0, 0))
font = pygame.font.Font(None, 50)
text = font.render("Hello, PyGo!", True, (100, 255, 100))
text_x = width // 2 - text.get_width() // 2
text_y = height // 2 - text.get_height() // 2
text_w = text.get_width()
text_h = text.get_height()
screen.blit(text, (text_x, text_y))
pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                       text_w + 20, text_h + 20), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()