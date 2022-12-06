import pygame


class DialogWindow:
    def __init__(self):
        pass

class Button:
    def __init__(self, screen, widht, heigth, pas_clr_button="white", act_clr_button="white"):
        self.widht = widht
        self.heigth = heigth
        self.pas_clr_button = pas_clr_button
        self.act_clr_button = act_clr_button
        self.screen = screen

    def draw(self, x, y, text, size, clr_font='black', act=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.widht:
            if y < mouse[1] < y + self.heigth:
                pass
        pygame.draw.rect(self.screen, self.pas_clr_button, (x, y, self.widht, self.heigth), border_radius=5)

        print_text(self.screen, text, x +  self.widht // 2 - size // 5,
                   y + self.heigth // 2 - size // 3, size=size, clr_font=clr_font)


class Board:
    def __init__(self, size):
        self.board = [[0 for i in range(size)] for j in range(size)]

    def board_checking(self):
        pass


def print_text(screen, text, x, y, size=30, clr_font='black'):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, clr_font)
    screen.blit(text, (x, y))



def wellcome():
    # Окно приветствия
    background = (104, 51, 7)
    clr_b = (250, 185, 100)
    pygame.init()
    pygame.display.set_caption('PyGo')
    size = width, height = 630, 720
    screen = pygame.display.set_mode(size)
    screen.fill(background)
    font = pygame.font.Font(None, 60)
    text = font.render("Hello, PyGo!", True, clr_b)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 9 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (250, 185, 100), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 3)
    # Кнопки
    butt_5 = Button(screen, 170, 170, pas_clr_button=clr_b)
    butt_5.draw(40, 170, '5', size=200, clr_font=background)


wellcome()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()