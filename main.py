import pygame


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
    def __init__(self, screen, x, y, pos):
        self.screen = screen
        self.x = x
        self.y = y
        self.pos = pos

    def select_shape(self):
        value = init_board.return_value(self.pos[0], self.pos[1])
        if value == 0:
            draw_point(self.screen, self.x, self.y, self.pos)
        elif value == 1:
            pygame.draw.circle(self.screen, (30, 30, 30), (self.x, self.y), radius = init_board.rad)
        else:
            pygame.draw.circle(self.screen, (230, 230, 230), (self.x, self.y), radius = init_board.rad)


class Board:
    def __init__(self, size):
        self.size_board = size
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.player = (20, 20, 20)
        self.sound_chips = pygame.mixer.Sound('data/Sound-chips.wav')
        if size == 5:
            self.rad = 65
        elif size == 13:
            self.rad = 15


    def change_value(self, i, j, value):
        init_board.sound_chips.play()
        self.board[j][i] = value

    def board_checking(self, colour):
        if colour[0] == 20:
            obj = 1
        else:
            obj = -1
        list_to_del = []
        for j in range(self.size_board):
            for i in range(self.size_board):
                if self.board[j][i] == obj:
                    list_to_del.append((i, j))
        del_machine(split_to_group(list_to_del), self.board)

        list_to_del = []
        for j in range(self.size_board):
            for i in range(self.size_board):
                if self.board[j][i] == -1 * obj:
                    list_to_del.append((i, j))
        del_machine(split_to_group(list_to_del), self.board)

    def return_value(self, i, j):
        return self.board[j][i]


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
    icon = pygame.image.load('data/PyGo_icon.png')
    pygame.display.set_icon(icon)
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
    butt_13 = Button(screen, b_size, b_size, pas_clr_button=clr_b)
    # butt_19 = Button(screen, b_size, b_size, pas_clr_button=clr_b) # standart
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
        butt_13.draw(2 * inter + 1 * b_size, 0 * inter + 1 * b_size, '13', size=font_size,
                     clr_font=background, act='set_board')
        # standart
        #butt_19.draw(3 * inter + 2 * b_size, 0 * inter + 1 * b_size, '19', size=font_size,
        #             clr_font=background, act='set_board')
        pygame.display.update()
        if init_board != '':
            running = False


def draw_point(screen, x, y, pos):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x - 20 < mouse[0] < x + 20 and y - 20 < mouse[1] < y + 20:
        pygame.draw.circle(screen, (70, 35, 40), (x, y), radius=5)
        if click[0] == 1:
            if init_board.player == (20, 20, 20): # black player
                init_board.change_value(pos[0], pos[1], 1)
                init_board.player = (230, 230, 230)
            elif init_board.player == (230, 230, 230): # white player
                init_board.change_value(pos[0], pos[1], -1)
                init_board.player = (20, 20, 20)
    else:
        pygame.draw.circle(screen, (40, 15, 20), (x, y), radius=5)


def split_to_group(m: list):
    '''
    m: матрица ввиде двойного списка
    Возращает список с групами точек (требуется для проверки)
    '''
    list_group = []
    for x, y in m:
        for val in list_group:
            if (x - 1, y) in val or (x, y - 1) in val:
                val.append((x, y))
                break
        else:
            list_group.append([(x, y)])
    list_group = check_groups(list_group)
    return list_group


def check_groups(groups: list):
    '''
    Необходимая проверка групп (чтобы 2 группы не соединились неправильно)
    groups: группы точек одного цвета
    Возвращает скорректированные группы точек
    '''
    extra_list = []
    for group in range(len(groups)):
        for x, y in groups[group]:
            for val in groups:
                if groups[group] != val:
                    if (x - 1, y) in val or (x, y - 1) in val:
                        groups[group] += val
                        extra_list.append(val)
    for i in extra_list:
        groups.remove(i)
    return groups


def del_machine(groups: dict, board):
    '''
    Основа проверики доски, изменяет массив поля, удаляя "задохнувшиеся" вишки
    groups: словарь с группами
    board: поле, которое изменяем
    Ничего не возвращает
    '''
    for group in groups:
        delete = True
        for x, y in group:
            if 0 < x < len(board) - 1 and 0 < y < len(board) - 1:
                if board[y][x - 1] != 0 and board[y][x + 1] != 0 and \
                        board[y - 1][x] != 0 and board[y + 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # левая граница
            if x == 0 and 0 < y < len(board) - 1:
                if board[y][x + 1] != 0 and \
                        board[y - 1][x] != 0 and board[y + 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # вверхняя граница
            if y == 0 and 0 < x < len(board) - 1:
                if board[y][x - 1] != 0 and board[y][x + 1] != 0 and \
                        board[y + 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # правая граница
            if x == len(board) - 1 and 0 < y < len(board) - 1:
                if board[y][x - 1] != 0 and \
                        board[y - 1][x] != 0 and board[y + 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # нижняя граница
            if y == len(board) - 1 and 0 < x < len(board) - 1:
                if board[y][x - 1] != 0 and board[y][x + 1] != 0 and \
                        board[y - 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # л-в угл
            if x == 0 and y == 0:
                if board[y][x + 1] != 0 and board[y + 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # п-в угл
            if x == len(board) - 1 and y == 0:
                if board[y][x - 1] != 0 and board[y + 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # п-н угл
            if x == len(board) - 1 and y == len(board) - 1:
                if board[y][x - 1] != 0 and board[y - 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
            # л-н угл
            if x == 0 and y == len(board) - 1:
                if board[y][x + 1] != 0 and board[y - 1][x] != 0:
                    pass
                else:
                    delete = False
                    break
        # удаление группы точек
        if delete:
            for x, y in group:
                board[y][x] = 0


def create_board_5():
    background = (104, 51, 7)
    clr_b = (250, 185, 100)
    pygame.init()
    icon = pygame.image.load('data/PyGo_icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption(f'PyGo партия {init_board.size_board}x{init_board.size_board}')
    size = width, height = 860, 765
    screen = pygame.display.set_mode(size)
    screen.fill(background)

    background_image = pygame.image.load('data/background.png').convert_alpha(screen)
    background_image = pygame.transform.scale(background_image, (860, 765))
    background_image.set_colorkey((104, 51, 7, 10))

    # инициализация точек
    point_1_1 = PointAction(screen, 150, 100, (0, 0))
    point_1_2 = PointAction(screen, 150, 240, (0, 1))
    point_1_3 = PointAction(screen, 150, 380, (0, 2))
    point_1_4 = PointAction(screen, 150, 520, (0, 3))
    point_1_5 = PointAction(screen, 150, 660, (0, 4))
    point_2_1 = PointAction(screen, 290, 100, (1, 0))
    point_2_2 = PointAction(screen, 290, 240, (1, 1))
    point_2_3 = PointAction(screen, 290, 380, (1, 2))
    point_2_4 = PointAction(screen, 290, 520, (1, 3))
    point_2_5 = PointAction(screen, 290, 660, (1, 4))
    point_3_1 = PointAction(screen, 430, 100, (2, 0))
    point_3_2 = PointAction(screen, 430, 240, (2, 1))
    point_3_3 = PointAction(screen, 430, 380, (2, 2))
    point_3_4 = PointAction(screen, 430, 520, (2, 3))
    point_3_5 = PointAction(screen, 430, 660, (2, 4))
    point_4_1 = PointAction(screen, 570, 100, (3, 0))
    point_4_2 = PointAction(screen, 570, 240, (3, 1))
    point_4_3 = PointAction(screen, 570, 380, (3, 2))
    point_4_4 = PointAction(screen, 570, 520, (3, 3))
    point_4_5 = PointAction(screen, 570, 660, (3, 4))
    point_5_1 = PointAction(screen, 710, 100, (4, 0))
    point_5_2 = PointAction(screen, 710, 240, (4, 1))
    point_5_3 = PointAction(screen, 710, 380, (4, 2))
    point_5_4 = PointAction(screen, 710, 520, (4, 3))
    point_5_5 = PointAction(screen, 710, 660, (4, 4))
    running = True
    clock = pygame.time.Clock()
    clock.tick(10)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(background)
        screen.blit(background_image, (0, 0))
        pygame.draw.line(screen, init_board.player, (0, 763), (760, 763), width=10)
        pygame.draw.line(screen, (60, 25, 30), (150, 100), (710, 100), width=3)
        pygame.draw.line(screen, (60, 25, 30), (150, 240), (710, 240), width=3)
        pygame.draw.line(screen, (60, 25, 30), (150, 380), (710, 380), width=3)
        pygame.draw.line(screen, (60, 25, 30), (150, 520), (710, 520), width=3)
        pygame.draw.line(screen, (60, 25, 30), (150, 660), (710, 660), width=3)

        pygame.draw.line(screen, (60, 25, 30), (150, 100), (150, 660), width=3)
        pygame.draw.line(screen, (60, 25, 30), (290, 100), (290, 660), width=3)
        pygame.draw.line(screen, (60, 25, 30), (430, 100), (430, 660), width=3)
        pygame.draw.line(screen, (60, 25, 30), (570, 100), (570, 660), width=3)
        pygame.draw.line(screen, (60, 25, 30), (710, 100), (710, 660), width=3)
        point_1_1.select_shape()
        point_1_2.select_shape()
        point_1_3.select_shape()
        point_1_4.select_shape()
        point_1_5.select_shape()
        point_2_1.select_shape()
        point_2_2.select_shape()
        point_2_3.select_shape()
        point_2_4.select_shape()
        point_2_5.select_shape()
        point_3_1.select_shape()
        point_3_2.select_shape()
        point_3_3.select_shape()
        point_3_4.select_shape()
        point_3_5.select_shape()
        point_4_1.select_shape()
        point_4_2.select_shape()
        point_4_3.select_shape()
        point_4_4.select_shape()
        point_4_5.select_shape()
        point_5_1.select_shape()
        point_5_2.select_shape()
        point_5_3.select_shape()
        point_5_4.select_shape()
        point_5_5.select_shape()
        init_board.board_checking(init_board.player)
        clock.tick(14)
        pygame.display.flip()


def create_board_13():
    background = (104, 51, 7)
    clr_b = (250, 185, 100)
    pygame.init()
    icon = pygame.image.load('data/PyGo_icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption(f'PyGo партия {init_board.size_board}x{init_board.size_board}')
    size = width, height = 860, 765
    screen = pygame.display.set_mode(size)
    screen.fill(background)

    background_image = pygame.image.load('data/background.png').convert_alpha(screen)
    background_image = pygame.transform.scale(background_image, (860, 765))
    background_image.set_colorkey((104, 51, 7, 10))

    # инициализация точек
    interval_y = 44
    y0 = 100
    x0 = 150
    interval_x = 46
    point_1_1 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 0, (0, 0))
    point_1_2 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 1, (0, 1))
    point_1_3 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 2, (0, 2))
    point_1_4 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 3, (0, 3))
    point_1_5 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 4, (0, 4))
    point_1_6 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 5, (0, 5))
    point_1_7 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 6, (0, 6))
    point_1_8 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 7, (0, 7))
    point_1_9 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 8, (0, 8))
    point_1_10 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 9, (0, 9))
    point_1_11 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 10, (0, 10))
    point_1_12 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 11, (0, 11))
    point_1_13 = PointAction(screen, x0 + interval_x * 0, y0 + interval_y * 12, (0, 12))

    point_2_1 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 0, (1, 0))
    point_2_2 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 1, (1, 1))
    point_2_3 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 2, (1, 2))
    point_2_4 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 3, (1, 3))
    point_2_5 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 4, (1, 4))
    point_2_6 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 5, (1, 5))
    point_2_7 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 6, (1, 6))
    point_2_8 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 7, (1, 7))
    point_2_9 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 8, (1, 8))
    point_2_10 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 9, (1, 9))
    point_2_11 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 10, (1, 10))
    point_2_12 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 11, (1, 11))
    point_2_13 = PointAction(screen, x0 + interval_x * 1, y0 + interval_y * 12, (1, 12))

    point_3_1 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 0, (2, 0))
    point_3_2 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 1, (2, 1))
    point_3_3 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 2, (2, 2))
    point_3_4 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 3, (2, 3))
    point_3_5 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 4, (2, 4))
    point_3_6 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 5, (2, 5))
    point_3_7 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 6, (2, 6))
    point_3_8 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 7, (2, 7))
    point_3_9 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 8, (2, 8))
    point_3_10 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 9, (2, 9))
    point_3_11 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 10, (2, 10))
    point_3_12 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 11, (2, 11))
    point_3_13 = PointAction(screen, x0 + interval_x * 2, y0 + interval_y * 12, (2, 12))

    point_4_1 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 0, (3, 0))
    point_4_2 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 1, (3, 1))
    point_4_3 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 2, (3, 2))
    point_4_4 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 3, (3, 3))
    point_4_5 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 4, (3, 4))
    point_4_6 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 5, (3, 5))
    point_4_7 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 6, (3, 6))
    point_4_8 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 7, (3, 7))
    point_4_9 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 8, (3, 8))
    point_4_10 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 9, (3, 9))
    point_4_11 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 10, (3, 10))
    point_4_12 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 11, (3, 11))
    point_4_13 = PointAction(screen, x0 + interval_x * 3, y0 + interval_y * 12, (3, 12))

    point_5_1 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 0, (4, 0))
    point_5_2 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 1, (4, 1))
    point_5_3 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 2, (4, 2))
    point_5_4 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 3, (4, 3))
    point_5_5 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 4, (4, 4))
    point_5_6 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 5, (4, 5))
    point_5_7 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 6, (4, 6))
    point_5_8 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 7, (4, 7))
    point_5_9 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 8, (4, 8))
    point_5_10 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 9, (4, 9))
    point_5_11 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 10, (4, 10))
    point_5_12 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 11, (4, 11))
    point_5_13 = PointAction(screen, x0 + interval_x * 4, y0 + interval_y * 12, (4, 12))

    point_6_1 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 0, (5, 0))
    point_6_2 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 1, (5, 1))
    point_6_3 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 2, (5, 2))
    point_6_4 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 3, (5, 3))
    point_6_5 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 4, (5, 4))
    point_6_6 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 5, (5, 5))
    point_6_7 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 6, (5, 6))
    point_6_8 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 7, (5, 7))
    point_6_9 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 8, (5, 8))
    point_6_10 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 9, (5, 9))
    point_6_11 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 10, (5, 10))
    point_6_12 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 11, (5, 11))
    point_6_13 = PointAction(screen, x0 + interval_x * 5, y0 + interval_y * 12, (5, 12))

    point_7_1 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 0, (6, 0))
    point_7_2 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 1, (6, 1))
    point_7_3 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 2, (6, 2))
    point_7_4 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 3, (6, 3))
    point_7_5 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 4, (6, 4))
    point_7_6 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 5, (6, 5))
    point_7_7 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 6, (6, 6))
    point_7_8 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 7, (6, 7))
    point_7_9 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 8, (6, 8))
    point_7_10 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 9, (6, 9))
    point_7_11 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 10, (6, 10))
    point_7_12 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 11, (6, 11))
    point_7_13 = PointAction(screen, x0 + interval_x * 6, y0 + interval_y * 12, (6, 12))

    point_8_1 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 0, (7, 0))
    point_8_2 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 1, (7, 1))
    point_8_3 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 2, (7, 2))
    point_8_4 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 3, (7, 3))
    point_8_5 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 4, (7, 4))
    point_8_6 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 5, (7, 5))
    point_8_7 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 6, (7, 6))
    point_8_8 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 7, (7, 7))
    point_8_9 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 8, (7, 8))
    point_8_10 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 9, (7, 9))
    point_8_11 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 10, (7, 10))
    point_8_12 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 11, (7, 11))
    point_8_13 = PointAction(screen, x0 + interval_x * 7, y0 + interval_y * 12, (7, 12))

    point_9_1 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 0, (8, 0))
    point_9_2 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 1, (8, 1))
    point_9_3 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 2, (8, 2))
    point_9_4 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 3, (8, 3))
    point_9_5 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 4, (8, 4))
    point_9_6 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 5, (8, 5))
    point_9_7 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 6, (8, 6))
    point_9_8 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 7, (8, 7))
    point_9_9 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 8, (8, 8))
    point_9_10 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 9, (8, 9))
    point_9_11 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 10, (8, 10))
    point_9_12 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 11, (8, 11))
    point_9_13 = PointAction(screen, x0 + interval_x * 8, y0 + interval_y * 12, (8, 12))

    point_10_1 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 0, (9, 0))
    point_10_2 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 1, (9, 1))
    point_10_3 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 2, (9, 2))
    point_10_4 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 3, (9, 3))
    point_10_5 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 4, (9, 4))
    point_10_6 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 5, (9, 5))
    point_10_7 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 6, (9, 6))
    point_10_8 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 7, (9, 7))
    point_10_9 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 8, (9, 8))
    point_10_10 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 9, (9, 9))
    point_10_11 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 10, (9, 10))
    point_10_12 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 11, (9, 11))
    point_10_13 = PointAction(screen, x0 + interval_x * 9, y0 + interval_y * 12, (9, 12))

    point_11_1 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 0, (10, 0))
    point_11_2 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 1, (10, 1))
    point_11_3 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 2, (10, 2))
    point_11_4 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 3, (10, 3))
    point_11_5 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 4, (10, 4))
    point_11_6 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 5, (10, 5))
    point_11_7 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 6, (10, 6))
    point_11_8 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 7, (10, 7))
    point_11_9 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 8, (10, 8))
    point_11_10 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 9, (10, 9))
    point_11_11 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 10, (10, 10))
    point_11_12 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 11, (10, 11))
    point_11_13 = PointAction(screen, x0 + interval_x * 10, y0 + interval_y * 12, (10, 12))

    point_12_1 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 0, (11, 0))
    point_12_2 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 1, (11, 1))
    point_12_3 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 2, (11, 2))
    point_12_4 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 3, (11, 3))
    point_12_5 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 4, (11, 4))
    point_12_6 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 5, (11, 5))
    point_12_7 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 6, (11, 6))
    point_12_8 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 7, (11, 7))
    point_12_9 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 8, (11, 8))
    point_12_10 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 9, (11, 9))
    point_12_11 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 10, (11, 10))
    point_12_12 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 11, (11, 11))
    point_12_13 = PointAction(screen, x0 + interval_x * 11, y0 + interval_y * 12, (11, 12))

    point_13_1 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 0, (12, 0))
    point_13_2 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 1, (12, 1))
    point_13_3 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 2, (12, 2))
    point_13_4 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 3, (12, 3))
    point_13_5 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 4, (12, 4))
    point_13_6 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 5, (12, 5))
    point_13_7 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 6, (12, 6))
    point_13_8 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 7, (12, 7))
    point_13_9 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 8, (12, 8))
    point_13_10 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 9, (12, 9))
    point_13_11 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 10, (12, 10))
    point_13_12 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 11, (12, 11))
    point_13_13 = PointAction(screen, x0 + interval_x * 12, y0 + interval_y * 12, (12, 12))

    running = True
    clock = pygame.time.Clock()
    clock.tick(10)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(background)
        screen.blit(background_image, (0, 0))
        pygame.draw.line(screen, init_board.player, (0, 763), (860, 763), width=10)

        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 0),
                         (x0 + interval_x * 12, y0 + interval_y * 0), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 1),
                         (x0 + interval_x * 12, y0 + interval_y * 1), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 2),
                         (x0 + interval_x * 12, y0 + interval_y * 2), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 3),
                         (x0 + interval_x * 12, y0 + interval_y * 3), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 4),
                         (x0 + interval_x * 12, y0 + interval_y * 4), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 5),
                         (x0 + interval_x * 12, y0 + interval_y * 5), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 6),
                         (x0 + interval_x * 12, y0 + interval_y * 6), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 7),
                         (x0 + interval_x * 12, y0 + interval_y * 7), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 8),
                         (x0 + interval_x * 12, y0 + interval_y * 8), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 9),
                         (x0 + interval_x * 12, y0 + interval_y * 9), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 10),
                         (x0 + interval_x * 12, y0 + interval_y * 10), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 11),
                         (x0 + interval_x * 12, y0 + interval_y * 11), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0, y0 + interval_y * 12),
                         (x0 + interval_x * 12, y0 + interval_y * 12), width=3)

        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 0, y0),
                         (x0 + interval_x * 0, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 1, y0),
                         (x0 + interval_x * 1, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 2, y0),
                         (x0 + interval_x * 2, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 3, y0),
                         (x0 + interval_x * 3, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 4, y0),
                         (x0 + interval_x * 4, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 5, y0),
                         (x0 + interval_x * 5, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 6, y0),
                         (x0 + interval_x * 6, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 7, y0),
                         (x0 + interval_x * 7, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 8, y0),
                         (x0 + interval_x * 8, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 9, y0),
                         (x0 + interval_x * 9, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 10, y0),
                         (x0 + interval_x * 10, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 11, y0),
                         (x0 + interval_x * 11, y0 + interval_y * 12), width=3)
        pygame.draw.line(screen, (60, 25, 30), (x0 + interval_x * 12, y0),
                         (x0 + interval_x * 12, y0 + interval_y * 12), width=3)

        point_1_1.select_shape()
        point_1_2.select_shape()
        point_1_3.select_shape()
        point_1_4.select_shape()
        point_1_5.select_shape()
        point_1_6.select_shape()
        point_1_7.select_shape()
        point_1_8.select_shape()
        point_1_9.select_shape()
        point_1_10.select_shape()
        point_1_11.select_shape()
        point_1_12.select_shape()
        point_1_13.select_shape()

        point_2_1.select_shape()
        point_2_2.select_shape()
        point_2_3.select_shape()
        point_2_4.select_shape()
        point_2_5.select_shape()
        point_2_6.select_shape()
        point_2_7.select_shape()
        point_2_8.select_shape()
        point_2_9.select_shape()
        point_2_10.select_shape()
        point_2_11.select_shape()
        point_2_12.select_shape()
        point_2_13.select_shape()

        point_3_1.select_shape()
        point_3_2.select_shape()
        point_3_3.select_shape()
        point_3_4.select_shape()
        point_3_5.select_shape()
        point_3_6.select_shape()
        point_3_7.select_shape()
        point_3_8.select_shape()
        point_3_9.select_shape()
        point_3_10.select_shape()
        point_3_11.select_shape()
        point_3_12.select_shape()
        point_3_13.select_shape()

        point_4_1.select_shape()
        point_4_2.select_shape()
        point_4_3.select_shape()
        point_4_4.select_shape()
        point_4_5.select_shape()
        point_4_6.select_shape()
        point_4_7.select_shape()
        point_4_8.select_shape()
        point_4_9.select_shape()
        point_4_10.select_shape()
        point_4_11.select_shape()
        point_4_12.select_shape()
        point_4_13.select_shape()

        point_5_1.select_shape()
        point_5_2.select_shape()
        point_5_3.select_shape()
        point_5_4.select_shape()
        point_5_5.select_shape()
        point_5_6.select_shape()
        point_5_7.select_shape()
        point_5_8.select_shape()
        point_5_9.select_shape()
        point_5_10.select_shape()
        point_5_11.select_shape()
        point_5_12.select_shape()
        point_5_13.select_shape()

        point_6_1.select_shape()
        point_6_2.select_shape()
        point_6_3.select_shape()
        point_6_4.select_shape()
        point_6_5.select_shape()
        point_6_6.select_shape()
        point_6_7.select_shape()
        point_6_8.select_shape()
        point_6_9.select_shape()
        point_6_10.select_shape()
        point_6_11.select_shape()
        point_6_12.select_shape()
        point_6_13.select_shape()

        point_7_1.select_shape()
        point_7_2.select_shape()
        point_7_3.select_shape()
        point_7_4.select_shape()
        point_7_5.select_shape()
        point_7_6.select_shape()
        point_7_7.select_shape()
        point_7_8.select_shape()
        point_7_9.select_shape()
        point_7_10.select_shape()
        point_7_11.select_shape()
        point_7_12.select_shape()
        point_7_13.select_shape()

        point_8_1.select_shape()
        point_8_2.select_shape()
        point_8_3.select_shape()
        point_8_4.select_shape()
        point_8_5.select_shape()
        point_8_6.select_shape()
        point_8_7.select_shape()
        point_8_8.select_shape()
        point_8_9.select_shape()
        point_8_10.select_shape()
        point_8_11.select_shape()
        point_8_12.select_shape()
        point_8_13.select_shape()

        point_9_1.select_shape()
        point_9_2.select_shape()
        point_9_3.select_shape()
        point_9_4.select_shape()
        point_9_5.select_shape()
        point_9_6.select_shape()
        point_9_7.select_shape()
        point_9_8.select_shape()
        point_9_9.select_shape()
        point_9_10.select_shape()
        point_9_11.select_shape()
        point_9_12.select_shape()
        point_9_13.select_shape()

        point_10_1.select_shape()
        point_10_2.select_shape()
        point_10_3.select_shape()
        point_10_4.select_shape()
        point_10_5.select_shape()
        point_10_6.select_shape()
        point_10_7.select_shape()
        point_10_8.select_shape()
        point_10_9.select_shape()
        point_10_10.select_shape()
        point_10_11.select_shape()
        point_10_12.select_shape()
        point_10_13.select_shape()

        point_11_1.select_shape()
        point_11_2.select_shape()
        point_11_3.select_shape()
        point_11_4.select_shape()
        point_11_5.select_shape()
        point_11_6.select_shape()
        point_11_7.select_shape()
        point_11_8.select_shape()
        point_11_9.select_shape()
        point_11_10.select_shape()
        point_11_11.select_shape()
        point_11_12.select_shape()
        point_11_13.select_shape()

        point_12_1.select_shape()
        point_12_2.select_shape()
        point_12_3.select_shape()
        point_12_4.select_shape()
        point_12_5.select_shape()
        point_12_6.select_shape()
        point_12_7.select_shape()
        point_12_8.select_shape()
        point_12_9.select_shape()
        point_12_10.select_shape()
        point_12_11.select_shape()
        point_12_12.select_shape()
        point_12_13.select_shape()

        point_13_1.select_shape()
        point_13_2.select_shape()
        point_13_3.select_shape()
        point_13_4.select_shape()
        point_13_5.select_shape()
        point_13_6.select_shape()
        point_13_7.select_shape()
        point_13_8.select_shape()
        point_13_9.select_shape()
        point_13_10.select_shape()
        point_13_11.select_shape()
        point_13_12.select_shape()
        point_13_13.select_shape()
        init_board.board_checking(init_board.player)
        clock.tick(10)
        pygame.display.flip()


board_size = [[5, 6, 7], [8, 9, 11], [13, 15, 19]]
while True:
    init_board = ''
    choice_board_size_menu()
    if init_board.size_board == 5:
        create_board_5()
    elif init_board.size_board == 13:
        create_board_13()
    pygame.quit()
