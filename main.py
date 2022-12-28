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
        if x < mouse[0] < x + self.widht and y < mouse[1] < y + self.heigth:
            pygame.draw.rect(self.screen, self.act_clr_button, (x, y, self.widht, self.heigth), border_radius=5)
            if click[0] == 1:
                if act == 'set_board':
                    set_board(text)
        else:
            pygame.draw.rect(self.screen, self.pas_clr_button, (x, y, self.widht, self.heigth), border_radius=5)
        print_text(self.screen, text, x + 20,
                   y + size / 5, size=size, clr_font=clr_font)


class PointAction:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        x = self.x
        y = self.y
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x - 5 < mouse[0] < x + 5 and y - 5 < mouse[1] < y + 5:
            pygame.draw.circle(self.screen, (70, 35, 40), (x, y), radius=5)
            if click[0] == 1:
                print('stand up')
        else:
            pygame.draw.circle(self.screen, (40, 15, 20), (x, y), radius=5)


class Board:
    def __init__(self, size):
        self.size_board = size
        self.board = [[0 for i in range(size)] for j in range(size)]

    def create_board_5(self):
        background = (104, 51, 7)
        clr_b = (250, 185, 100)
        pygame.init()
        pygame.display.set_caption('PyGo партия')
        size = width, height = 840, 840
        screen = pygame.display.set_mode(size)
        screen.fill(background)
        # инициализация точек
        point_1_1 = PointAction(screen, 110, 110)
        point_1_2 = PointAction(screen, 110, 260)
        point_1_3 = PointAction(screen, 110, 410)
        point_1_4 = PointAction(screen, 110, 560)
        point_1_5 = PointAction(screen, 110, 710)
        point_2_1 = PointAction(screen, 260, 110)
        point_2_2 = PointAction(screen, 260, 260)
        point_2_3 = PointAction(screen, 260, 410)
        point_2_4 = PointAction(screen, 260, 560)
        point_2_5 = PointAction(screen, 260, 710)
        point_3_1 = PointAction(screen, 410, 110)
        point_3_2 = PointAction(screen, 410, 260)
        point_3_3 = PointAction(screen, 410, 410)
        point_3_4 = PointAction(screen, 410, 560)
        point_3_5 = PointAction(screen, 410, 710)
        point_4_1 = PointAction(screen, 560, 110)
        point_4_2 = PointAction(screen, 560, 260)
        point_4_3 = PointAction(screen, 560, 410)
        point_4_4 = PointAction(screen, 560, 560)
        point_4_5 = PointAction(screen, 560, 710)
        point_5_1 = PointAction(screen, 710, 110)
        point_5_2 = PointAction(screen, 710, 260)
        point_5_3 = PointAction(screen, 710, 410)
        point_5_4 = PointAction(screen, 710, 560)
        point_5_5 = PointAction(screen, 710, 710)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            point_1_1.draw()
            point_1_2.draw()
            point_1_3.draw()
            point_1_4.draw()
            point_1_5.draw()
            point_2_1.draw()
            point_2_2.draw()
            point_2_3.draw()
            point_2_4.draw()
            point_2_5.draw()
            point_3_1.draw()
            point_3_2.draw()
            point_3_3.draw()
            point_3_4.draw()
            point_3_5.draw()
            point_4_1.draw()
            point_4_2.draw()
            point_4_3.draw()
            point_4_4.draw()
            point_4_5.draw()
            point_5_1.draw()
            point_5_2.draw()
            point_5_3.draw()
            point_5_4.draw()
            point_5_5.draw()
            pygame.display.flip()

    def board_checking(self):
        pass


def set_board(str_size):
    global init_board
    init_board = Board(int(str_size))


def print_text(screen, text, x, y, size=30, clr_font='black'):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, clr_font)
    screen.blit(text, (x, y))


def choice_board_size_menu():
    global init_board
    # Окно приветствия
    background = (104, 51, 7)
    clr_b = (250, 185, 100)
    pygame.init()
    pygame.display.set_caption('PyGo')
    size = width, height = 630, 770
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
    b_size, inter = 170, 30
    butt_5 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_6 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_7 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_8 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_9 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_11 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_13 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_15 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    #butt_19 = Button(screen, 170, 170, pas_clr_button=clr_b) # standart
    # цикл меню
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        font_size = 170
        # изображение кнопок
        butt_5.draw(1 * inter + 0 * b_size, 0 * inter + 1 * b_size, ' 5', size=font_size,
                    clr_font=background, act='set_board')

        #butt_6.draw(2 * inter + 1 * b_size, 0 * inter + 1 * b_size, ' 6', size=font_size,
        #            clr_font=background, act='set_board')

        #butt_7.draw(3 * inter + 2 * b_size, 0 * inter + 1 * b_size, ' 7', size=font_size,
        #            clr_font=background, act='set_board')

        #butt_8.draw(1 * inter + 0 * b_size, 1 * inter + 2 * b_size, ' 8', size=font_size,
        #            clr_font=background, act='set_board')

        #butt_9.draw(2 * inter + 1 * b_size, 1 * inter + 2 * b_size, ' 9', size=font_size,
        #            clr_font=background, act='set_board')

        #butt_11.draw(3 * inter + 2 * b_size, 1 * inter + 2 * b_size, '11', size=font_size,
        #             clr_font=background, act='set_board')

        #butt_13.draw(1 * inter + 0 * b_size, 2 * inter + 3 * b_size, '13', size=font_size,
        #             clr_font=background, act='set_board')

        #butt_15.draw(2 * inter + 1 * b_size, 2 * inter + 3 * b_size, '15', size=font_size,
        #             clr_font=background, act='set_board')

        # standart
        #butt_19.draw(3 * inter + 2 * b_size, 2 * inter + 3 * b_size, '19', size=font_size,
        #             clr_font=background, act='set_board')
        pygame.display.update()
        if init_board != '':
            running = False


board_size = [[5, 6, 7], [8, 9, 11], [13, 15, 19]]
init_board = ''
choice_board_size_menu()
init_board.create_board_5()


#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    pygame.display.flip()
#pygame.quit()