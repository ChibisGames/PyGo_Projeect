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
            pygame.draw.circle(self.screen, (30, 30, 30), (self.x, self.y), radius=65)
        else:
            pygame.draw.circle(self.screen, (230, 230, 230), (self.x, self.y), radius=65)

class Board:
    def __init__(self, size):
        self.size_board = size
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.player = (20, 20, 20)

    def change_value(self, i, j, value):
        self.board[j][i] = value

    def board_checking(self):
        list_to_del = []
        for j in range(self.size_board):
            for i in range(self.size_board):
                if self.board[j][i] == 1:
                    list_to_del.append((i, j))
        del_machine(split_to_group(list_to_del), self.board)

        list_to_del = []
        for j in range(self.size_board):
            for i in range(self.size_board):
                if self.board[j][i] == -1:
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


def draw_point(screen, x, y, pos):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x - 10 < mouse[0] < x + 10 and y - 10 < mouse[1] < y + 10:
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
    Возращает словарь с групами точек (требуется для проверки)
    '''
    dict_group = {}
    count = 0
    for x, y in m:
        for val in list(dict_group.values()):
            if (x - 1, y) in val or (x, y - 1) in val:
                val.append((x, y))
                break
        else:
            dict_group[count] = [(x, y)]
            count += 1
    return dict_group


def del_machine(groups: dict, board):
    '''
    groups: словарь с группами
    board: поле, которое изменяем
    Основа проверики доски, изменяет массив поля, удаляя "задохнувшиеся" вишки
    '''
    for group in list(groups.values()):
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
    pygame.display.set_caption('PyGo партия')
    size = width, height = 760, 765
    screen = pygame.display.set_mode(size)
    screen.fill(background)
    # инициализация точек
    point_1_1 = PointAction(screen, 100, 100, (0, 0))
    point_1_2 = PointAction(screen, 100, 240, (0, 1))
    point_1_3 = PointAction(screen, 100, 380, (0, 2))
    point_1_4 = PointAction(screen, 100, 520, (0, 3))
    point_1_5 = PointAction(screen, 100, 660, (0, 4))
    point_2_1 = PointAction(screen, 240, 100, (1, 0))
    point_2_2 = PointAction(screen, 240, 240, (1, 1))
    point_2_3 = PointAction(screen, 240, 380, (1, 2))
    point_2_4 = PointAction(screen, 240, 520, (1, 3))
    point_2_5 = PointAction(screen, 240, 660, (1, 4))
    point_3_1 = PointAction(screen, 380, 100, (2, 0))
    point_3_2 = PointAction(screen, 380, 240, (2, 1))
    point_3_3 = PointAction(screen, 380, 380, (2, 2))
    point_3_4 = PointAction(screen, 380, 520, (2, 3))
    point_3_5 = PointAction(screen, 380, 660, (2, 4))
    point_4_1 = PointAction(screen, 520, 100, (3, 0))
    point_4_2 = PointAction(screen, 520, 240, (3, 1))
    point_4_3 = PointAction(screen, 520, 380, (3, 2))
    point_4_4 = PointAction(screen, 520, 520, (3, 3))
    point_4_5 = PointAction(screen, 520, 660, (3, 4))
    point_5_1 = PointAction(screen, 660, 100, (4, 0))
    point_5_2 = PointAction(screen, 660, 240, (4, 1))
    point_5_3 = PointAction(screen, 660, 380, (4, 2))
    point_5_4 = PointAction(screen, 660, 520, (4, 3))
    point_5_5 = PointAction(screen, 660, 660, (4, 4))
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(background)
        pygame.draw.line(screen, init_board.player, (0, 763), (760, 763), width=10)
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
        init_board.board_checking()
        clock.tick(20)
        pygame.display.flip()


board_size = [[5, 6, 7], [8, 9, 11], [13, 15, 19]]
init_board = ''

choice_board_size_menu()
create_board_5()
