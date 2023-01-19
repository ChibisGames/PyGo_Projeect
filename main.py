import pygame, sqlite3


class DataBaseTaker:
    def __init__(self):
        self.start_game = True
        try:
            self.con = sqlite3.connect("data/database_for_setting.db")
            self.cur = self.con.cursor()
            self.volume = int(self.cur.execute("""SELECT Value FROM Setting
             WHERE NameSetting = 'Volume'""").fetchall()[0][0])
            self.chips = int(self.cur.execute("""SELECT Value FROM Setting
             WHERE NameSetting = 'Chips'""").fetchall()[0][0])
            self.clr_font_text = str_to_tuple(self.cur.execute("""SELECT Value FROM Setting
             WHERE NameSetting = 'Clr_font_text'""").fetchall()[0][0])
            self.clr_font_butt = str_to_tuple(self.cur.execute("""SELECT Value FROM Setting
             WHERE NameSetting = 'Clr_font_butt'""").fetchall()[0][0])
            self.background = str_to_tuple(self.cur.execute("""SELECT Value FROM Setting
             WHERE NameSetting = 'Background'""").fetchall()[0][0])
            self.pas_clr_button = str_to_tuple(self.cur.execute("""SELECT Value FROM Setting
             WHERE NameSetting = 'Pas_clr_button'""").fetchall()[0][0])
            self.act_clr_button = str_to_tuple(self.cur.execute("""SELECT Value FROM Setting
             WHERE NameSetting = 'Act_clr_button'""").fetchall()[0][0])
        except Exception:
            self.start_game = False
            print('Ошибка датабазы')

    def save(self, par):
        if par == 'volume':
            self.cur.execute("""UPDATE Setting SET Value = """ + str(self.volume) + """ WHERE NameSetting = 'Volume'""")
        elif par == 'chips':
            self.cur.execute("""UPDATE Setting SET Value = """ + str(self.chips) + """ WHERE NameSetting = 'Chips'""")
        elif par == 'background':
            self.cur.execute("""UPDATE Setting SET Value = '""" + ' '.join(self.background) + """' 
            WHERE NameSetting = 'Background'""")
        elif par == 'clr_text':
            self.cur.execute("""UPDATE Setting SET Value = '""" + ' '.join(self.clr_font_text) + """' 
            WHERE NameSetting = 'Clr_font_text'""")
        elif par == 'clr_text_butt':
            self.cur.execute("""UPDATE Setting SET Value = '""" + ' '.join(self.clr_font_butt) + """' 
            WHERE NameSetting = 'Clr_font_butt'""")
        elif par == 'pas_clr_button':
            self.cur.execute("""UPDATE Setting SET Value = '""" + ' '.join(self.pas_clr_button) + """' 
            WHERE NameSetting = 'Pas_clr_button'""")
        elif par == 'act_clr_button':
            self.cur.execute("""UPDATE Setting SET Value = '""" + ' '.join(self.act_clr_button) + """' 
            WHERE NameSetting = 'Act_clr_button'""")
        self.con.commit()

    def set_default(self):
        try:
            self.con = sqlite3.connect("data/database_for_setting.db")
            self.cur = self.con.cursor()
            self.volume = int(self.cur.execute("""SELECT DefaultSet FROM Setting
             WHERE NameSetting = 'Volume'""").fetchall()[0][0])
            self.chips = int(self.cur.execute("""SELECT DefaultSet FROM Setting
             WHERE NameSetting = 'Chips'""").fetchall()[0][0])
            self.clr_font_text = str_to_tuple(self.cur.execute("""SELECT DefaultSet FROM Setting
             WHERE NameSetting = 'Clr_font_text'""").fetchall()[0][0])
            self.clr_font_butt = str_to_tuple(self.cur.execute("""SELECT DefaultSet FROM Setting
             WHERE NameSetting = 'Clr_font_butt'""").fetchall()[0][0])
            self.background = str_to_tuple(self.cur.execute("""SELECT DefaultSet FROM Setting
             WHERE NameSetting = 'Background'""").fetchall()[0][0])
            self.pas_clr_button = str_to_tuple(self.cur.execute("""SELECT DefaultSet FROM Setting
             WHERE NameSetting = 'Pas_clr_button'""").fetchall()[0][0])
            self.act_clr_button = str_to_tuple(self.cur.execute("""SELECT DefaultSet FROM Setting
             WHERE NameSetting = 'Act_clr_button'""").fetchall()[0][0])
        except Exception:
            print('Ошибка датабазы')



class Button:
    def __init__(self, screen, widht, heigth,
                 pas_clr_button='white', act_clr_button='white', clr_font_butt='black'):
        self.widht = widht
        self.heigth = heigth
        self.pas_clr_button = pas_clr_button
        self.act_clr_button = act_clr_button
        self.clr_font_butt = clr_font_butt
        self.screen = screen
        self.true_box = False

    def draw(self, x, y, text, size, act=None):
        continuee = True
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.widht and y < mouse[1] < y + self.heigth:
            pygame.draw.rect(self.screen, self.act_clr_button, (x, y, self.widht, self.heigth), border_radius=5)
            if click[0] == 1:
                if act == 'set_board':
                    set_board(text)
                elif act == 'setting':
                    setting()
                    continuee = False
                elif act == 'setting_use_box':
                    if self.true_box:
                        self.true_box = False
                        self.act_clr_button = 'red'
                        self.pas_clr_button = 'white'
                    else:
                        self.true_box = True
                        self.act_clr_button = 'green'
                        self.pas_clr_button = 'green'
                elif act == 'save_setting':
                    self.true_box = True
                elif act == 'pass_step':
                    init_board.sound_pass.play()
                    if init_board.player == (20, 20, 20):
                        init_board.black_pas = True
                        init_board.player = (230, 230, 230)
                    else:
                        init_board.white_pas = True
                        init_board.player = (20, 20, 20)
                elif act == 'use_box':
                    self.true_box = True
        else:
            pygame.draw.rect(self.screen, self.pas_clr_button, (x, y, self.widht, self.heigth), border_radius=5)
        if continuee:
            print_text(self.screen, text, x + 20,
                       y + size / 5, size=size, clr_font_text=self.clr_font_butt)


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
        self.sound_pass = pygame.mixer.Sound('data/pass_sound.wav')
        self.sound_chips.set_volume(db_taker.volume / 100)
        self.sound_pass.set_volume(db_taker.volume / 100)
        self.black_chips = db_taker.chips
        self.white_chips = db_taker.chips
        self.black_kills = 0
        self.white_kills = 0
        self.black_pas = False
        self.white_pas = False
        if size == 5:
            self.rad = 65
        elif size == 13:
            self.rad = 20
        elif size == 19:
            self.rad = 15
        icon = pygame.image.load('data/PyGo_icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption(f'PyGo партия {size}x{size}')

    def change_value(self, i, j, value):
        init_board.sound_chips.play()
        self.board[j][i] = value
        if self.player == (230, 230, 230):
            self.black_pas = False
        else:
            self.white_pas = False

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


def print_text(screen, text, x, y, size=30, clr_font_text='black'):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, clr_font_text)
    screen.blit(text, (x, y))


def choice_board_size_menu():
    global init_board
    # Окно приветствия
    pygame.init()
    icon = pygame.image.load('data/PyGo_icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyGo')
    size = width, height = 630, 570
    screen = pygame.display.set_mode(size)
    screen.fill(db_taker.background)
    font = pygame.font.Font(None, 120)
    text = font.render("Hello, PyGo!", True, db_taker.clr_font_text)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 9 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y + 20))
    pygame.draw.rect(screen, db_taker.clr_font_text, (text_x - 10, text_y + 5,
                                           text_w + 20, text_h + 20), 3)
    b_size, inter = 170, 30
    butt_5 = Button(screen, b_size, b_size, clr_font_butt=db_taker.clr_font_butt,
                    pas_clr_button=db_taker.pas_clr_button, act_clr_button=db_taker.act_clr_button)
    butt_13 = Button(screen, b_size, b_size, clr_font_butt=db_taker.clr_font_butt,
                    pas_clr_button=db_taker.pas_clr_button, act_clr_button=db_taker.act_clr_button)
    # standart
    butt_19 = Button(screen, b_size, b_size, clr_font_butt=db_taker.clr_font_butt,
                    pas_clr_button=db_taker.pas_clr_button, act_clr_button=db_taker.act_clr_button)
    butt_setting = Button(screen, b_size * 3 + inter * 2, b_size, clr_font_butt=db_taker.clr_font_butt,
                    pas_clr_button=db_taker.pas_clr_button, act_clr_button=db_taker.act_clr_button)
    # цикл меню
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
        font_size = 170
        # изображение кнопок
        butt_5.draw(1 * inter + 0 * b_size, 0 * inter + 1 * b_size, ' 5', size=font_size, act='set_board')
        butt_13.draw(2 * inter + 1 * b_size, 0 * inter + 1 * b_size, '13', size=font_size, act='set_board')
        # standart
        butt_19.draw(3 * inter + 2 * b_size, 0 * inter + 1 * b_size, '19', size=font_size, act='set_board')
        butt_setting.draw(inter, inter + 2 * b_size, '  Setting', size=font_size - 5, act='setting')
        pygame.display.update()
        if init_board != '':
            running = False


def draw_point(screen, x, y, pos):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x - 15 < mouse[0] < x + 15 and y - 15 < mouse[1] < y + 15:
        pygame.draw.circle(screen, (70, 35, 40), (x, y), radius=5)
        if click[0] == 1:
            if init_board.player == (20, 20, 20): # black player
                init_board.change_value(pos[0], pos[1], 1)
                init_board.black_chips -= 1
                init_board.player = (230, 230, 230)
            elif init_board.player == (230, 230, 230): # white player
                init_board.change_value(pos[0], pos[1], -1)
                init_board.white_chips -= 1
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
            if board[group[0][1]][group[0][0]] == 1:
                init_board.white_kills += len(group)
            elif board[group[0][1]][group[0][0]] == -1:
                init_board.black_kills += len(group)
            for x, y in group:
                board[y][x] = 0


def setting():
    pygame.init()
    size = width, height = 550, 530
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('PyGo Настройки')
    screen.fill(db_taker.background)

    butt_volume = Button(screen, 20, 20, clr_font_butt='black', pas_clr_button='white', act_clr_button='red')
    butt_chips = Button(screen, 20, 20, clr_font_butt='black', pas_clr_button='white', act_clr_button='red')
    butt_backgaround = Button(screen, 20, 20, clr_font_butt='black', pas_clr_button='white', act_clr_button='red')
    butt_textcolour = Button(screen, 20, 20, clr_font_butt='black', pas_clr_button='white', act_clr_button='red')
    butt_textcolourbut = Button(screen, 20, 20, clr_font_butt='black', pas_clr_button='white', act_clr_button='red')
    butt_pascolourbut = Button(screen, 20, 20, clr_font_butt='black', pas_clr_button='white', act_clr_button='red')
    butt_actcolourbut = Button(screen, 20, 20, clr_font_butt='black', pas_clr_button='white', act_clr_button='red')

    butt_save = Button(screen, 280, 50, clr_font_butt=db_taker.clr_font_butt,
                    pas_clr_button=db_taker.pas_clr_button, act_clr_button=db_taker.act_clr_button)
    butt_default = Button(screen, 160, 50, clr_font_butt=db_taker.clr_font_butt,
                    pas_clr_button=db_taker.pas_clr_button, act_clr_button=db_taker.act_clr_button)

    running = True
    nums = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
            pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
    numpad = [pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
              pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]
    volume = db_taker.volume
    chips = db_taker.chips
    backdround = db_taker.cur.execute("""SELECT Value FROM Setting
    WHERE NameSetting = 'Background'""").fetchall()[0][0].split()
    clr_text = db_taker.cur.execute("""SELECT Value FROM Setting 
    WHERE NameSetting = 'Clr_font_text'""").fetchall()[0][0].split()
    clr_text_butt = db_taker.cur.execute("""SELECT Value FROM Setting
    WHERE NameSetting = 'Clr_font_butt'""").fetchall()[0][0].split()
    pas_clr_button = db_taker.cur.execute("""SELECT Value FROM Setting
    WHERE NameSetting = 'Pas_clr_button'""").fetchall()[0][0].split()
    act_clr_button = db_taker.cur.execute("""SELECT Value FROM Setting
    WHERE NameSetting = 'Act_clr_button'""").fetchall()[0][0].split()
    clock = pygame.time.Clock()
    clock.tick(10)
    while running:
        screen.fill(db_taker.background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if butt_volume.true_box:
                volume = setting_button(event, volume, nums, numpad, 2)
            else:
                if len(str(volume)) == 0:
                    volume == 0
                elif volume > 100:
                    volume = 100

            if butt_chips.true_box:
                chips = setting_button(event, chips, nums, numpad, 7)
            else:
                if len(str(chips)) == 0:
                    chips = 0
                elif chips > 10000000:
                    chips = 10000000

            if butt_backgaround.true_box:
                backdround = setting_button_for_str(event, backdround, nums, numpad, 8)
            else:
                backdround = setting_clr_check(backdround)

            if butt_textcolour.true_box:
                clr_text = setting_button_for_str(event, clr_text, nums, numpad, 8)
            else:
                clr_text = setting_clr_check(clr_text)

            if butt_textcolourbut.true_box:
                clr_text_butt = setting_button_for_str(event, clr_text_butt, nums, numpad, 8)
            else:
                clr_text_butt = setting_clr_check(clr_text_butt)

            if butt_pascolourbut.true_box:
                pas_clr_button = setting_button_for_str(event, pas_clr_button, nums, numpad, 8)
            else:
                pas_clr_button = setting_clr_check(pas_clr_button)

            if butt_actcolourbut.true_box:
                act_clr_button = setting_button_for_str(event, act_clr_button, nums, numpad, 8)
            else:
                act_clr_button = setting_clr_check(act_clr_button)

        print_text(screen, 'Volume', 20, 20, clr_font_text=db_taker.clr_font_text, size=50)
        print_text(screen, "enter an integer from 0 to 100 when you'll green light.", 20, 60,
                   clr_font_text=db_taker.clr_font_text, size=20)
        print_text(screen, str(volume), 370, 20, clr_font_text=db_taker.clr_font_text, size=45)
        butt_volume.draw(345, 30, ' ', 25, act='setting_use_box')

        print_text(screen, 'Chips', 20, 80, clr_font_text=db_taker.clr_font_text, size=50)
        print_text(screen, "enter an any integer (max = 10000000) when you'll green light.", 20, 120,
                   clr_font_text=db_taker.clr_font_text, size=20)
        print_text(screen, str(chips), 370, 80, clr_font_text=db_taker.clr_font_text, size=45)
        butt_chips.draw(345, 90, ' ', 25, act='setting_use_box')

        print_text(screen, "enter an 9 integer together (like 001245001,",
                   20, 150, clr_font_text=db_taker.clr_font_text, size=18)
        print_text(screen, "every 3, starting from the beginning, from 000 to 255) when you'll green light:",
                   30, 165, clr_font_text=db_taker.clr_font_text, size=18)

        print_text(screen, 'Background', 20, 180, clr_font_text=db_taker.clr_font_text, size=50)
        print_text(screen, ''.join(backdround), 370, 180,
                   clr_font_text=db_taker.clr_font_text, size=45)
        butt_backgaround.draw(345, 190, ' ', 25, act='setting_use_box')

        print_text(screen, 'Text colour', 20, 230, clr_font_text=db_taker.clr_font_text, size=50)
        print_text(screen, '(not in button)', 200, 245, clr_font_text=db_taker.clr_font_text, size=20)
        print_text(screen, ''.join(clr_text), 370, 230, clr_font_text=db_taker.clr_font_text, size=45)
        butt_textcolour.draw(345, 240, ' ', 25, act='setting_use_box')

        print_text(screen, 'Text colour', 20, 280, clr_font_text=db_taker.clr_font_text, size=50)
        print_text(screen, '(in button)', 200, 295, clr_font_text=db_taker.clr_font_text, size=20)
        print_text(screen, ''.join(clr_text_butt), 370, 280,
                   clr_font_text=db_taker.clr_font_text, size=45)
        butt_textcolourbut.draw(345, 290, ' ', 25, act='setting_use_box')

        print_text(screen, 'Button colour', 20, 330, clr_font_text=db_taker.clr_font_text, size=50)
        print_text(screen, '(norm state)', 250, 345, clr_font_text=db_taker.clr_font_text, size=20)
        print_text(screen, ''.join(pas_clr_button), 370, 330,
                   clr_font_text=db_taker.clr_font_text, size=45)
        butt_pascolourbut.draw(345, 340, ' ', 25, act='setting_use_box')

        print_text(screen, 'Button colour', 20, 380, clr_font_text=db_taker.clr_font_text, size=50)
        print_text(screen, '(aim state)', 250, 395, clr_font_text=db_taker.clr_font_text, size=20)
        print_text(screen, ''.join(act_clr_button), 370, 380,
                   clr_font_text=db_taker.clr_font_text, size=45)
        butt_actcolourbut.draw(345, 390, ' ', 25, act='setting_use_box')

        butt_save.draw(30, 430, 'Accept changes', 45, act='use_box')
        print_text(screen, 'saving works without the green color',
                   30, 490, clr_font_text=db_taker.clr_font_text, size=23)
        butt_default.draw(320, 430, 'Defalt', 45, act='use_box')
        print_text(screen, 'change on default setting',
                   320, 490, clr_font_text=db_taker.clr_font_text, size=23)

        if butt_default.true_box:
            db_taker.set_default()
            volume = db_taker.volume
            chips = db_taker.chips
            backdround = db_taker.cur.execute("""SELECT DefaultSet FROM Setting 
            WHERE NameSetting = 'Background'""").fetchall()[0][0].split()
            clr_text = db_taker.cur.execute("""SELECT DefaultSet FROM Setting 
            WHERE NameSetting = 'Clr_font_text'""").fetchall()[0][0].split()
            clr_text_butt = db_taker.cur.execute("""SELECT DefaultSet FROM Setting 
            WHERE NameSetting = 'Clr_font_butt'""").fetchall()[0][0].split()
            pas_clr_button = db_taker.cur.execute("""SELECT DefaultSet FROM Setting 
            WHERE NameSetting = 'Pas_clr_button'""").fetchall()[0][0].split()
            act_clr_button = db_taker.cur.execute("""SELECT DefaultSet FROM Setting 
            WHERE NameSetting = 'Act_clr_button'""").fetchall()[0][0].split()
            butt_default.true_box = False

        if butt_save.true_box and not butt_volume.true_box and not butt_chips.true_box and not butt_textcolour.true_box\
                and not butt_backgaround.true_box and not butt_textcolourbut.true_box\
                and not butt_pascolourbut.true_box and not butt_actcolourbut.true_box:
            if not butt_volume.true_box:
                db_taker.volume = volume
                db_taker.save('volume')
                butt_save.true_box = False

            if not butt_chips.true_box:
                db_taker.chips = chips
                db_taker.save('chips')
                butt_save.true_box = False

            if not butt_backgaround.true_box:
                if type(backdround) == list and len(backdround) == 3:
                    db_taker.background = backdround
                    db_taker.save('background')
                    db_taker.background = str_to_tuple(' '.join(backdround))
                    butt_save.true_box = False

            if not butt_textcolour.true_box:
                if type(clr_text) == list and len(clr_text) == 3:
                    db_taker.clr_font_text = clr_text
                    db_taker.save('clr_text')
                    db_taker.clr_font_text = str_to_tuple(' '.join(clr_text))
                    butt_save.true_box = False

            if not butt_textcolourbut.true_box:
                if type(clr_text_butt) == list and len(clr_text_butt) == 3:
                    db_taker.clr_font_butt = clr_text_butt
                    db_taker.save('clr_text_butt')
                    db_taker.clr_font_butt = str_to_tuple(' '.join(clr_text_butt))
                    butt_save.true_box = False

            if not butt_pascolourbut.true_box:
                if type(pas_clr_button) == list and len(pas_clr_button) == 3:
                    db_taker.pas_clr_button = pas_clr_button
                    db_taker.save('pas_clr_button')
                    db_taker.pas_clr_button = str_to_tuple(' '.join(pas_clr_button))
                    butt_save.true_box = False

            if not butt_actcolourbut.true_box:
                if type(act_clr_button) == list and len(act_clr_button) == 3:
                    db_taker.act_clr_button = act_clr_button
                    db_taker.save('act_clr_button')
                    db_taker.act_clr_button = str_to_tuple(' '.join(act_clr_button))
                    butt_save.true_box = False

            print_text(screen, 'data saved', 400, 510, clr_font_text=db_taker.clr_font_text, size=20)

        pygame.display.flip()
    pygame.quit()

    choice_board_size_menu()


def setting_button(event, parametr, nums, numpad, max):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            parametr = parametr // 10
        elif event.type == pygame.KEYDOWN and event.key in nums and len(str(parametr)) <= max:
            parametr *= 10
            parametr += nums.index(event.key)
        elif event.type == pygame.KEYDOWN and event.key in numpad and len(str(parametr)) <= max:
            parametr *= 10
            parametr += numpad.index(event.key)
    return parametr


def setting_button_for_str(event, parametr, nums, numpad, max):
    parametr = ''.join(parametr)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            parametr = parametr[:-1]
        elif event.type == pygame.KEYDOWN and event.key in nums and len(parametr) <= max:
            parametr += str(nums.index(event.key))
        elif event.type == pygame.KEYDOWN and event.key in numpad and len(str(parametr)) <= max:
            parametr += str(numpad.index(event.key))
    return parametr


def setting_clr_check(par):
    if type(par) == str:
        if len(par) < 9:
            par += '0' * (9 - len(par))
        par = [par[:3], par[3:6], par[6:]]
    else:
        if len(''.join(par)) < 9:
            par = ''.join(par)
            par += '0' * (9 - len(par))
            par = [par[:3], par[3:6], par[6:]]
    for clr in range(len(par)):
        if int(par[clr]) > 255:
            par[clr] = '255'
    return par


def create_board_5():
    background = db_taker.background
    pygame.init()
    size = width, height = 900, 765
    screen = pygame.display.set_mode(size)
    screen.fill(background)

    background_image = pygame.image.load('data/background.png').convert_alpha(screen)
    background_image = pygame.transform.scale(background_image, (width, height))
    background_image.set_colorkey((104, 51, 7, 10))

    # подсчёт координат точек
    interval_x = 150
    interval_y = 140
    x0 = 150
    x1 = x0 + interval_x
    x2 = x1 + interval_x
    x3 = x2 + interval_x
    x4 = x3 + interval_x

    y0 = 100
    y1 = y0 + interval_y
    y2 = y1 + interval_y
    y3 = y2 + interval_y
    y4 = y3 + interval_y
    # инициализация точек
    point_1_1 = PointAction(screen, x0, y0, (0, 0))
    point_1_2 = PointAction(screen, x0, y1, (0, 1))
    point_1_3 = PointAction(screen, x0, y2, (0, 2))
    point_1_4 = PointAction(screen, x0, y3, (0, 3))
    point_1_5 = PointAction(screen, x0, y4, (0, 4))

    point_2_1 = PointAction(screen, x1, y0, (1, 0))
    point_2_2 = PointAction(screen, x1, y1, (1, 1))
    point_2_3 = PointAction(screen, x1, y2, (1, 2))
    point_2_4 = PointAction(screen, x1, y3, (1, 3))
    point_2_5 = PointAction(screen, x1, y4, (1, 4))

    point_3_1 = PointAction(screen, x2, y0, (2, 0))
    point_3_2 = PointAction(screen, x2, y1, (2, 1))
    point_3_3 = PointAction(screen, x2, y2, (2, 2))
    point_3_4 = PointAction(screen, x2, y3, (2, 3))
    point_3_5 = PointAction(screen, x2, y4, (2, 4))

    point_4_1 = PointAction(screen, x3, y0, (3, 0))
    point_4_2 = PointAction(screen, x3, y1, (3, 1))
    point_4_3 = PointAction(screen, x3, y2, (3, 2))
    point_4_4 = PointAction(screen, x3, y3, (3, 3))
    point_4_5 = PointAction(screen, x3, y4, (3, 4))

    point_5_1 = PointAction(screen, x4, y0, (4, 0))
    point_5_2 = PointAction(screen, x4, y1, (4, 1))
    point_5_3 = PointAction(screen, x4, y2, (4, 2))
    point_5_4 = PointAction(screen, x4, y3, (4, 3))
    point_5_5 = PointAction(screen, x4, y4, (4, 4))
    running = True
    clock = pygame.time.Clock()
    clock.tick(10)
    clr_text = db_taker.clr_font_text
    black_pass_butt = Button(screen, 75, 600, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    white_pass_butt = Button(screen, 75, 600, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    game_over_butt = Button(screen, 500, 75, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if init_board.black_pas and init_board.white_pas or init_board.black_chips == 0 and init_board.white_chips == 0:
            screen.fill(background)
            screen.blit(background_image, (0, 0))
            print_text(screen, 'GAME OVER', 50, 50, size=150)
            game_over_butt.draw(200, 600, 'return to menu', size=50, act='use_box')
            if game_over_butt.true_box:
                running = False
        else:
            screen.fill(background)
            screen.blit(background_image, (0, 0))
            print_text(screen, 'black survivors', 10, 10, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.black_chips), 10, 30, size=25, clr_font_text=clr_text)
            print_text(screen, 'killed', 10, 60, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.black_kills), 10, 80, size=25, clr_font_text=clr_text)

            print_text(screen, 'white survivors', 765, 10, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.white_chips), 765, 30, size=25, clr_font_text=clr_text)
            print_text(screen, 'killed', 765, 60, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.white_kills), 765, 80, size=25, clr_font_text=clr_text)

            pygame.draw.line(screen, init_board.player, (0, 763), (width, 763), width=10)
            pygame.draw.line(screen, (60, 25, 30), (x0, y0), (x4, y0), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y1), (x4, y1), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y2), (x4, y2), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y3), (x4, y3), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y4), (x4, y4), width=3)

            pygame.draw.line(screen, (60, 25, 30), (x0, y0), (x0, y4), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x1, y0), (x1, y4), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x2, y0), (x2, y4), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x3, y0), (x3, y4), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x4, y0), (x4, y4), width=3)
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
            if init_board.player == (20, 20, 20):
                black_pass_butt.draw(10, 120, 'pass', size=28, act='pass_step')
            elif init_board.player == (230, 230, 230):
                white_pass_butt.draw(815, 120, 'pass', size=28, act='pass_step')
            init_board.board_checking(init_board.player)
            clock.tick(10)
        pygame.display.flip()


def create_board_13():
    background = db_taker.background
    pygame.init()
    size = width, height = 900, 765
    screen = pygame.display.set_mode(size)
    screen.fill(background)
    background_image = pygame.image.load('data/background.png').convert_alpha(screen)
    background_image = pygame.transform.scale(background_image, (width, height))
    background_image.set_colorkey((104, 51, 7, 10))

    # подсчёт координат точек
    interval_x = 50
    interval_y = 55
    x0 = 150
    x1 = x0 + interval_x
    x2 = x1 + interval_x
    x3 = x2 + interval_x
    x4 = x3 + interval_x
    x5 = x4 + interval_x
    x6 = x5 + interval_x
    x7 = x6 + interval_x
    x8 = x7 + interval_x
    x9 = x8 + interval_x
    x10 = x9 + interval_x
    x11 = x10 + interval_x
    x12 = x11 + interval_x
    y0 = 50
    y1 = y0 + interval_y
    y2 = y1 + interval_y
    y3 = y2 + interval_y
    y4 = y3 + interval_y
    y5 = y4 + interval_y
    y6 = y5 + interval_y
    y7 = y6 + interval_y
    y8 = y7 + interval_y
    y9 = y8 + interval_y
    y10 = y9 + interval_y
    y11 = y10 + interval_y
    y12 = y11 + interval_y
    # инициализация точек
    point_1_1 = PointAction(screen, x0, y0, (0, 0))
    point_1_2 = PointAction(screen, x0, y1, (0, 1))
    point_1_3 = PointAction(screen, x0, y2, (0, 2))
    point_1_4 = PointAction(screen, x0, y3, (0, 3))
    point_1_5 = PointAction(screen, x0, y4, (0, 4))
    point_1_6 = PointAction(screen, x0, y5, (0, 5))
    point_1_7 = PointAction(screen, x0, y6, (0, 6))
    point_1_8 = PointAction(screen, x0, y7, (0, 7))
    point_1_9 = PointAction(screen, x0, y8, (0, 8))
    point_1_10 = PointAction(screen, x0, y9, (0, 9))
    point_1_11 = PointAction(screen, x0, y10, (0, 10))
    point_1_12 = PointAction(screen, x0, y11, (0, 11))
    point_1_13 = PointAction(screen, x0, y12, (0, 12))

    point_2_1 = PointAction(screen, x1, y0, (1, 0))
    point_2_2 = PointAction(screen, x1, y1, (1, 1))
    point_2_3 = PointAction(screen, x1, y2, (1, 2))
    point_2_4 = PointAction(screen, x1, y3, (1, 3))
    point_2_5 = PointAction(screen, x1, y4, (1, 4))
    point_2_6 = PointAction(screen, x1, y5, (1, 5))
    point_2_7 = PointAction(screen, x1, y6, (1, 6))
    point_2_8 = PointAction(screen, x1, y7, (1, 7))
    point_2_9 = PointAction(screen, x1, y8, (1, 8))
    point_2_10 = PointAction(screen, x1, y9, (1, 9))
    point_2_11 = PointAction(screen, x1, y10, (1, 10))
    point_2_12 = PointAction(screen, x1, y11, (1, 11))
    point_2_13 = PointAction(screen, x1, y12, (1, 12))

    point_3_1 = PointAction(screen, x2, y0, (2, 0))
    point_3_2 = PointAction(screen, x2, y1, (2, 1))
    point_3_3 = PointAction(screen, x2, y2, (2, 2))
    point_3_4 = PointAction(screen, x2, y3, (2, 3))
    point_3_5 = PointAction(screen, x2, y4, (2, 4))
    point_3_6 = PointAction(screen, x2, y5, (2, 5))
    point_3_7 = PointAction(screen, x2, y6, (2, 6))
    point_3_8 = PointAction(screen, x2, y7, (2, 7))
    point_3_9 = PointAction(screen, x2, y8, (2, 8))
    point_3_10 = PointAction(screen, x2, y9, (2, 9))
    point_3_11 = PointAction(screen, x2, y10, (2, 10))
    point_3_12 = PointAction(screen, x2, y11, (2, 11))
    point_3_13 = PointAction(screen, x2, y12, (2, 12))

    point_4_1 = PointAction(screen, x3, y0, (3, 0))
    point_4_2 = PointAction(screen, x3, y1, (3, 1))
    point_4_3 = PointAction(screen, x3, y2, (3, 2))
    point_4_4 = PointAction(screen, x3, y3, (3, 3))
    point_4_5 = PointAction(screen, x3, y4, (3, 4))
    point_4_6 = PointAction(screen, x3, y5, (3, 5))
    point_4_7 = PointAction(screen, x3, y6, (3, 6))
    point_4_8 = PointAction(screen, x3, y7, (3, 7))
    point_4_9 = PointAction(screen, x3, y8, (3, 8))
    point_4_10 = PointAction(screen, x3, y9, (3, 9))
    point_4_11 = PointAction(screen, x3, y10, (3, 10))
    point_4_12 = PointAction(screen, x3, y11, (3, 11))
    point_4_13 = PointAction(screen, x3, y12, (3, 12))

    point_5_1 = PointAction(screen, x4, y0, (4, 0))
    point_5_2 = PointAction(screen, x4, y1, (4, 1))
    point_5_3 = PointAction(screen, x4, y2, (4, 2))
    point_5_4 = PointAction(screen, x4, y3, (4, 3))
    point_5_5 = PointAction(screen, x4, y4, (4, 4))
    point_5_6 = PointAction(screen, x4, y5, (4, 5))
    point_5_7 = PointAction(screen, x4, y6, (4, 6))
    point_5_8 = PointAction(screen, x4, y7, (4, 7))
    point_5_9 = PointAction(screen, x4, y8, (4, 8))
    point_5_10 = PointAction(screen, x4, y9, (4, 9))
    point_5_11 = PointAction(screen, x4, y10, (4, 10))
    point_5_12 = PointAction(screen, x4, y11, (4, 11))
    point_5_13 = PointAction(screen, x4, y12, (4, 12))

    point_6_1 = PointAction(screen, x5, y0, (5, 0))
    point_6_2 = PointAction(screen, x5, y1, (5, 1))
    point_6_3 = PointAction(screen, x5, y2, (5, 2))
    point_6_4 = PointAction(screen, x5, y3, (5, 3))
    point_6_5 = PointAction(screen, x5, y4, (5, 4))
    point_6_6 = PointAction(screen, x5, y5, (5, 5))
    point_6_7 = PointAction(screen, x5, y6, (5, 6))
    point_6_8 = PointAction(screen, x5, y7, (5, 7))
    point_6_9 = PointAction(screen, x5, y8, (5, 8))
    point_6_10 = PointAction(screen, x5, y9, (5, 9))
    point_6_11 = PointAction(screen, x5, y10, (5, 10))
    point_6_12 = PointAction(screen, x5, y11, (5, 11))
    point_6_13 = PointAction(screen, x5, y12, (5, 12))

    point_7_1 = PointAction(screen, x6, y0, (6, 0))
    point_7_2 = PointAction(screen, x6, y1, (6, 1))
    point_7_3 = PointAction(screen, x6, y2, (6, 2))
    point_7_4 = PointAction(screen, x6, y3, (6, 3))
    point_7_5 = PointAction(screen, x6, y4, (6, 4))
    point_7_6 = PointAction(screen, x6, y5, (6, 5))
    point_7_7 = PointAction(screen, x6, y6, (6, 6))
    point_7_8 = PointAction(screen, x6, y7, (6, 7))
    point_7_9 = PointAction(screen, x6, y8, (6, 8))
    point_7_10 = PointAction(screen, x6, y9, (6, 9))
    point_7_11 = PointAction(screen, x6, y10, (6, 10))
    point_7_12 = PointAction(screen, x6, y11, (6, 11))
    point_7_13 = PointAction(screen, x6, y12, (6, 12))

    point_8_1 = PointAction(screen, x7, y0, (7, 0))
    point_8_2 = PointAction(screen, x7, y1, (7, 1))
    point_8_3 = PointAction(screen, x7, y2, (7, 2))
    point_8_4 = PointAction(screen, x7, y3, (7, 3))
    point_8_5 = PointAction(screen, x7, y4, (7, 4))
    point_8_6 = PointAction(screen, x7, y5, (7, 5))
    point_8_7 = PointAction(screen, x7, y6, (7, 6))
    point_8_8 = PointAction(screen, x7, y7, (7, 7))
    point_8_9 = PointAction(screen, x7, y8, (7, 8))
    point_8_10 = PointAction(screen, x7, y9, (7, 9))
    point_8_11 = PointAction(screen, x7, y10, (7, 10))
    point_8_12 = PointAction(screen, x7, y11, (7, 11))
    point_8_13 = PointAction(screen, x7, y12, (7, 12))

    point_9_1 = PointAction(screen, x8, y0, (8, 0))
    point_9_2 = PointAction(screen, x8, y1, (8, 1))
    point_9_3 = PointAction(screen, x8, y2, (8, 2))
    point_9_4 = PointAction(screen, x8, y3, (8, 3))
    point_9_5 = PointAction(screen, x8, y4, (8, 4))
    point_9_6 = PointAction(screen, x8, y5, (8, 5))
    point_9_7 = PointAction(screen, x8, y6, (8, 6))
    point_9_8 = PointAction(screen, x8, y7, (8, 7))
    point_9_9 = PointAction(screen, x8, y8, (8, 8))
    point_9_10 = PointAction(screen, x8, y9, (8, 9))
    point_9_11 = PointAction(screen, x8, y10, (8, 10))
    point_9_12 = PointAction(screen, x8, y11, (8, 11))
    point_9_13 = PointAction(screen, x8, y12, (8, 12))

    point_10_1 = PointAction(screen, x9, y0, (9, 0))
    point_10_2 = PointAction(screen, x9, y1, (9, 1))
    point_10_3 = PointAction(screen, x9, y2, (9, 2))
    point_10_4 = PointAction(screen, x9, y3, (9, 3))
    point_10_5 = PointAction(screen, x9, y4, (9, 4))
    point_10_6 = PointAction(screen, x9, y5, (9, 5))
    point_10_7 = PointAction(screen, x9, y6, (9, 6))
    point_10_8 = PointAction(screen, x9, y7, (9, 7))
    point_10_9 = PointAction(screen, x9, y8, (9, 8))
    point_10_10 = PointAction(screen, x9, y9, (9, 9))
    point_10_11 = PointAction(screen, x9, y10, (9, 10))
    point_10_12 = PointAction(screen, x9, y11, (9, 11))
    point_10_13 = PointAction(screen, x9, y12, (9, 12))

    point_11_1 = PointAction(screen, x10, y0, (10, 0))
    point_11_2 = PointAction(screen, x10, y1, (10, 1))
    point_11_3 = PointAction(screen, x10, y2, (10, 2))
    point_11_4 = PointAction(screen, x10, y3, (10, 3))
    point_11_5 = PointAction(screen, x10, y4, (10, 4))
    point_11_6 = PointAction(screen, x10, y5, (10, 5))
    point_11_7 = PointAction(screen, x10, y6, (10, 6))
    point_11_8 = PointAction(screen, x10, y7, (10, 7))
    point_11_9 = PointAction(screen, x10, y8, (10, 8))
    point_11_10 = PointAction(screen, x10, y9, (10, 9))
    point_11_11 = PointAction(screen, x10, y10, (10, 10))
    point_11_12 = PointAction(screen, x10, y11, (10, 11))
    point_11_13 = PointAction(screen, x10, y12, (10, 12))

    point_12_1 = PointAction(screen, x11, y0, (11, 0))
    point_12_2 = PointAction(screen, x11, y1, (11, 1))
    point_12_3 = PointAction(screen, x11, y2, (11, 2))
    point_12_4 = PointAction(screen, x11, y3, (11, 3))
    point_12_5 = PointAction(screen, x11, y4, (11, 4))
    point_12_6 = PointAction(screen, x11, y5, (11, 5))
    point_12_7 = PointAction(screen, x11, y6, (11, 6))
    point_12_8 = PointAction(screen, x11, y7, (11, 7))
    point_12_9 = PointAction(screen, x11, y8, (11, 8))
    point_12_10 = PointAction(screen, x11, y9, (11, 9))
    point_12_11 = PointAction(screen, x11, y10, (11, 10))
    point_12_12 = PointAction(screen, x11, y11, (11, 11))
    point_12_13 = PointAction(screen, x11, y12, (11, 12))

    point_13_1 = PointAction(screen, x12, y0, (12, 0))
    point_13_2 = PointAction(screen, x12, y1, (12, 1))
    point_13_3 = PointAction(screen, x12, y2, (12, 2))
    point_13_4 = PointAction(screen, x12, y3, (12, 3))
    point_13_5 = PointAction(screen, x12, y4, (12, 4))
    point_13_6 = PointAction(screen, x12, y5, (12, 5))
    point_13_7 = PointAction(screen, x12, y6, (12, 6))
    point_13_8 = PointAction(screen, x12, y7, (12, 7))
    point_13_9 = PointAction(screen, x12, y8, (12, 8))
    point_13_10 = PointAction(screen, x12, y9, (12, 9))
    point_13_11 = PointAction(screen, x12, y10, (12, 10))
    point_13_12 = PointAction(screen, x12, y11, (12, 11))
    point_13_13 = PointAction(screen, x12, y12, (12, 12))

    running = True
    clock = pygame.time.Clock()
    clock.tick(10)
    clr_text = db_taker.clr_font_text
    black_pass_butt = Button(screen, 75, 600, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    white_pass_butt = Button(screen, 75, 600, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    game_over_butt = Button(screen, 500, 75, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if init_board.black_pas and init_board.white_pas or init_board.black_chips == 0 and init_board.white_chips == 0:
            screen.fill(background)
            screen.blit(background_image, (0, 0))
            print_text(screen, 'GAME OVER', 50, 50, size=150)
            game_over_butt.draw(200, 600, 'return to menu', size=50, act='use_box')
            if game_over_butt.true_box:
                running = False
        else:
            screen.fill(background)
            screen.blit(background_image, (0, 0))
            print_text(screen, 'black survivors', 10, 10, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.black_chips), 10, 30, size=25, clr_font_text=clr_text)
            print_text(screen, 'killed', 10, 60, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.black_kills), 10, 80, size=25, clr_font_text=clr_text)

            print_text(screen, 'white survivors', 765, 10, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.white_chips), 765, 30, size=25, clr_font_text=clr_text)
            print_text(screen, 'killed', 765, 60, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.white_kills), 765, 80, size=25, clr_font_text=clr_text)

            pygame.draw.line(screen, init_board.player, (0, 763), (width, 763), width=10)

            pygame.draw.line(screen, (60, 25, 30), (x0, y0), (x12, y0), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y1), (x12, y1), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y2), (x12, y2), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y3), (x12, y3), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y4), (x12, y4), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y5), (x12, y5), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y6), (x12, y6), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y7), (x12, y7), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y8), (x12, y8), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y9), (x12, y9), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y10), (x12, y10), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y11), (x12, y11), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y12), (x12, y12), width=3)

            pygame.draw.line(screen, (60, 25, 30), (x0, y0), (x0, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x1, y0), (x1, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x2, y0), (x2, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x3, y0), (x3, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x4, y0), (x4, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x5, y0), (x5, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x6, y0), (x6, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x7, y0), (x7, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x8, y0), (x8, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x9, y0), (x9, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x10, y0), (x10, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x11, y0), (x11, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x12, y0), (x12, y12), width=3)

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
            if init_board.player == (20, 20, 20):
                black_pass_butt.draw(10, 120, 'pass', size=28, act='pass_step')
            elif init_board.player == (230, 230, 230):
                white_pass_butt.draw(815, 120, 'pass', size=28, act='pass_step')
            init_board.board_checking(init_board.player)
            clock.tick(10)
        pygame.display.flip()


def create_board_19():
    background = db_taker.background
    pygame.init()
    size = width, height = 900, 765
    screen = pygame.display.set_mode(size)
    screen.fill(background)

    background_image = pygame.image.load('data/background.png').convert_alpha(screen)
    background_image = pygame.transform.scale(background_image, (width, height))
    background_image.set_colorkey((104, 51, 7, 10))

    # подсчёт координат точек
    interval_x = 34
    interval_y = 39
    x0 = 144
    x1 = x0 + interval_x
    x2 = x1 + interval_x
    x3 = x2 + interval_x
    x4 = x3 + interval_x
    x5 = x4 + interval_x
    x6 = x5 + interval_x
    x7 = x6 + interval_x
    x8 = x7 + interval_x
    x9 = x8 + interval_x
    x10 = x9 + interval_x
    x11 = x10 + interval_x
    x12 = x11 + interval_x
    x13 = x12 + interval_x
    x14 = x13 + interval_x
    x15 = x14 + interval_x
    x16 = x15 + interval_x
    x17 = x16 + interval_x
    x18 = x17 + interval_x
    y0 = 26
    y1 = y0 + interval_y
    y2 = y1 + interval_y
    y3 = y2 + interval_y
    y4 = y3 + interval_y
    y5 = y4 + interval_y
    y6 = y5 + interval_y
    y7 = y6 + interval_y
    y8 = y7 + interval_y
    y9 = y8 + interval_y
    y10 = y9 + interval_y
    y11 = y10 + interval_y
    y12 = y11 + interval_y
    y13 = y12 + interval_y
    y14 = y13 + interval_y
    y15 = y14 + interval_y
    y16 = y15 + interval_y
    y17 = y16 + interval_y
    y18 = y17 + interval_y
    # инициализация точек
    point_1_1 = PointAction(screen, x0, y0, (0, 0))
    point_1_2 = PointAction(screen, x0, y1, (0, 1))
    point_1_3 = PointAction(screen, x0, y2, (0, 2))
    point_1_4 = PointAction(screen, x0, y3, (0, 3))
    point_1_5 = PointAction(screen, x0, y4, (0, 4))
    point_1_6 = PointAction(screen, x0, y5, (0, 5))
    point_1_7 = PointAction(screen, x0, y6, (0, 6))
    point_1_8 = PointAction(screen, x0, y7, (0, 7))
    point_1_9 = PointAction(screen, x0, y8, (0, 8))
    point_1_10 = PointAction(screen, x0, y9, (0, 9))
    point_1_11 = PointAction(screen, x0, y10, (0, 10))
    point_1_12 = PointAction(screen, x0, y11, (0, 11))
    point_1_13 = PointAction(screen, x0, y12, (0, 12))
    point_1_14 = PointAction(screen, x0, y13, (0, 13))
    point_1_15 = PointAction(screen, x0, y14, (0, 14))
    point_1_16 = PointAction(screen, x0, y15, (0, 15))
    point_1_17 = PointAction(screen, x0, y16, (0, 16))
    point_1_18 = PointAction(screen, x0, y17, (0, 17))
    point_1_19 = PointAction(screen, x0, y18, (0, 18))

    point_2_1 = PointAction(screen, x1, y0, (1, 0))
    point_2_2 = PointAction(screen, x1, y1, (1, 1))
    point_2_3 = PointAction(screen, x1, y2, (1, 2))
    point_2_4 = PointAction(screen, x1, y3, (1, 3))
    point_2_5 = PointAction(screen, x1, y4, (1, 4))
    point_2_6 = PointAction(screen, x1, y5, (1, 5))
    point_2_7 = PointAction(screen, x1, y6, (1, 6))
    point_2_8 = PointAction(screen, x1, y7, (1, 7))
    point_2_9 = PointAction(screen, x1, y8, (1, 8))
    point_2_10 = PointAction(screen, x1, y9, (1, 9))
    point_2_11 = PointAction(screen, x1, y10, (1, 10))
    point_2_12 = PointAction(screen, x1, y11, (1, 11))
    point_2_13 = PointAction(screen, x1, y12, (1, 12))
    point_2_14 = PointAction(screen, x1, y13, (1, 13))
    point_2_15 = PointAction(screen, x1, y14, (1, 14))
    point_2_16 = PointAction(screen, x1, y15, (1, 15))
    point_2_17 = PointAction(screen, x1, y16, (1, 16))
    point_2_18 = PointAction(screen, x1, y17, (1, 17))
    point_2_19 = PointAction(screen, x1, y18, (1, 18))

    point_3_1 = PointAction(screen, x2, y0, (2, 0))
    point_3_2 = PointAction(screen, x2, y1, (2, 1))
    point_3_3 = PointAction(screen, x2, y2, (2, 2))
    point_3_4 = PointAction(screen, x2, y3, (2, 3))
    point_3_5 = PointAction(screen, x2, y4, (2, 4))
    point_3_6 = PointAction(screen, x2, y5, (2, 5))
    point_3_7 = PointAction(screen, x2, y6, (2, 6))
    point_3_8 = PointAction(screen, x2, y7, (2, 7))
    point_3_9 = PointAction(screen, x2, y8, (2, 8))
    point_3_10 = PointAction(screen, x2, y9, (2, 9))
    point_3_11 = PointAction(screen, x2, y10, (2, 10))
    point_3_12 = PointAction(screen, x2, y11, (2, 11))
    point_3_13 = PointAction(screen, x2, y12, (2, 12))
    point_3_14 = PointAction(screen, x2, y13, (2, 13))
    point_3_15 = PointAction(screen, x2, y14, (2, 14))
    point_3_16 = PointAction(screen, x2, y15, (2, 15))
    point_3_17 = PointAction(screen, x2, y16, (2, 16))
    point_3_18 = PointAction(screen, x2, y17, (2, 17))
    point_3_19 = PointAction(screen, x2, y18, (2, 18))

    point_4_1 = PointAction(screen, x3, y0, (3, 0))
    point_4_2 = PointAction(screen, x3, y1, (3, 1))
    point_4_3 = PointAction(screen, x3, y2, (3, 2))
    point_4_4 = PointAction(screen, x3, y3, (3, 3))
    point_4_5 = PointAction(screen, x3, y4, (3, 4))
    point_4_6 = PointAction(screen, x3, y5, (3, 5))
    point_4_7 = PointAction(screen, x3, y6, (3, 6))
    point_4_8 = PointAction(screen, x3, y7, (3, 7))
    point_4_9 = PointAction(screen, x3, y8, (3, 8))
    point_4_10 = PointAction(screen, x3, y9, (3, 9))
    point_4_11 = PointAction(screen, x3, y10, (3, 10))
    point_4_12 = PointAction(screen, x3, y11, (3, 11))
    point_4_13 = PointAction(screen, x3, y12, (3, 12))
    point_4_14 = PointAction(screen, x3, y13, (3, 13))
    point_4_15 = PointAction(screen, x3, y14, (3, 14))
    point_4_16 = PointAction(screen, x3, y15, (3, 15))
    point_4_17 = PointAction(screen, x3, y16, (3, 16))
    point_4_18 = PointAction(screen, x3, y17, (3, 17))
    point_4_19 = PointAction(screen, x3, y18, (3, 18))

    point_5_1 = PointAction(screen, x4, y0, (4, 0))
    point_5_2 = PointAction(screen, x4, y1, (4, 1))
    point_5_3 = PointAction(screen, x4, y2, (4, 2))
    point_5_4 = PointAction(screen, x4, y3, (4, 3))
    point_5_5 = PointAction(screen, x4, y4, (4, 4))
    point_5_6 = PointAction(screen, x4, y5, (4, 5))
    point_5_7 = PointAction(screen, x4, y6, (4, 6))
    point_5_8 = PointAction(screen, x4, y7, (4, 7))
    point_5_9 = PointAction(screen, x4, y8, (4, 8))
    point_5_10 = PointAction(screen, x4, y9, (4, 9))
    point_5_11 = PointAction(screen, x4, y10, (4, 10))
    point_5_12 = PointAction(screen, x4, y11, (4, 11))
    point_5_13 = PointAction(screen, x4, y12, (4, 12))
    point_5_14 = PointAction(screen, x4, y13, (4, 13))
    point_5_15 = PointAction(screen, x4, y14, (4, 14))
    point_5_16 = PointAction(screen, x4, y15, (4, 15))
    point_5_17 = PointAction(screen, x4, y16, (4, 16))
    point_5_18 = PointAction(screen, x4, y17, (4, 17))
    point_5_19 = PointAction(screen, x4, y18, (4, 18))

    point_6_1 = PointAction(screen, x5, y0, (5, 0))
    point_6_2 = PointAction(screen, x5, y1, (5, 1))
    point_6_3 = PointAction(screen, x5, y2, (5, 2))
    point_6_4 = PointAction(screen, x5, y3, (5, 3))
    point_6_5 = PointAction(screen, x5, y4, (5, 4))
    point_6_6 = PointAction(screen, x5, y5, (5, 5))
    point_6_7 = PointAction(screen, x5, y6, (5, 6))
    point_6_8 = PointAction(screen, x5, y7, (5, 7))
    point_6_9 = PointAction(screen, x5, y8, (5, 8))
    point_6_10 = PointAction(screen, x5, y9, (5, 9))
    point_6_11 = PointAction(screen, x5, y10, (5, 10))
    point_6_12 = PointAction(screen, x5, y11, (5, 11))
    point_6_13 = PointAction(screen, x5, y12, (5, 12))
    point_6_14 = PointAction(screen, x5, y13, (5, 13))
    point_6_15 = PointAction(screen, x5, y14, (5, 14))
    point_6_16 = PointAction(screen, x5, y15, (5, 15))
    point_6_17 = PointAction(screen, x5, y16, (5, 16))
    point_6_18 = PointAction(screen, x5, y17, (5, 17))
    point_6_19 = PointAction(screen, x5, y18, (5, 18))

    point_7_1 = PointAction(screen, x6, y0, (6, 0))
    point_7_2 = PointAction(screen, x6, y1, (6, 1))
    point_7_3 = PointAction(screen, x6, y2, (6, 2))
    point_7_4 = PointAction(screen, x6, y3, (6, 3))
    point_7_5 = PointAction(screen, x6, y4, (6, 4))
    point_7_6 = PointAction(screen, x6, y5, (6, 5))
    point_7_7 = PointAction(screen, x6, y6, (6, 6))
    point_7_8 = PointAction(screen, x6, y7, (6, 7))
    point_7_9 = PointAction(screen, x6, y8, (6, 8))
    point_7_10 = PointAction(screen, x6, y9, (6, 9))
    point_7_11 = PointAction(screen, x6, y10, (6, 10))
    point_7_12 = PointAction(screen, x6, y11, (6, 11))
    point_7_13 = PointAction(screen, x6, y12, (6, 12))
    point_7_14 = PointAction(screen, x6, y13, (6, 13))
    point_7_15 = PointAction(screen, x6, y14, (6, 14))
    point_7_16 = PointAction(screen, x6, y15, (6, 15))
    point_7_17 = PointAction(screen, x6, y16, (6, 16))
    point_7_18 = PointAction(screen, x6, y17, (6, 17))
    point_7_19 = PointAction(screen, x6, y18, (6, 18))

    point_8_1 = PointAction(screen, x7, y0, (7, 0))
    point_8_2 = PointAction(screen, x7, y1, (7, 1))
    point_8_3 = PointAction(screen, x7, y2, (7, 2))
    point_8_4 = PointAction(screen, x7, y3, (7, 3))
    point_8_5 = PointAction(screen, x7, y4, (7, 4))
    point_8_6 = PointAction(screen, x7, y5, (7, 5))
    point_8_7 = PointAction(screen, x7, y6, (7, 6))
    point_8_8 = PointAction(screen, x7, y7, (7, 7))
    point_8_9 = PointAction(screen, x7, y8, (7, 8))
    point_8_10 = PointAction(screen, x7, y9, (7, 9))
    point_8_11 = PointAction(screen, x7, y10, (7, 10))
    point_8_12 = PointAction(screen, x7, y11, (7, 11))
    point_8_13 = PointAction(screen, x7, y12, (7, 12))
    point_8_14 = PointAction(screen, x7, y13, (7, 13))
    point_8_15 = PointAction(screen, x7, y14, (7, 14))
    point_8_16 = PointAction(screen, x7, y15, (7, 15))
    point_8_17 = PointAction(screen, x7, y16, (7, 16))
    point_8_18 = PointAction(screen, x7, y17, (7, 17))
    point_8_19 = PointAction(screen, x7, y18, (7, 18))

    point_9_1 = PointAction(screen, x8, y0, (8, 0))
    point_9_2 = PointAction(screen, x8, y1, (8, 1))
    point_9_3 = PointAction(screen, x8, y2, (8, 2))
    point_9_4 = PointAction(screen, x8, y3, (8, 3))
    point_9_5 = PointAction(screen, x8, y4, (8, 4))
    point_9_6 = PointAction(screen, x8, y5, (8, 5))
    point_9_7 = PointAction(screen, x8, y6, (8, 6))
    point_9_8 = PointAction(screen, x8, y7, (8, 7))
    point_9_9 = PointAction(screen, x8, y8, (8, 8))
    point_9_10 = PointAction(screen, x8, y9, (8, 9))
    point_9_11 = PointAction(screen, x8, y10, (8, 10))
    point_9_12 = PointAction(screen, x8, y11, (8, 11))
    point_9_13 = PointAction(screen, x8, y12, (8, 12))
    point_9_14 = PointAction(screen, x8, y13, (8, 13))
    point_9_15 = PointAction(screen, x8, y14, (8, 14))
    point_9_16 = PointAction(screen, x8, y15, (8, 15))
    point_9_17 = PointAction(screen, x8, y16, (8, 16))
    point_9_18 = PointAction(screen, x8, y17, (8, 17))
    point_9_19 = PointAction(screen, x8, y18, (8, 18))

    point_10_1 = PointAction(screen, x9, y0, (9, 0))
    point_10_2 = PointAction(screen, x9, y1, (9, 1))
    point_10_3 = PointAction(screen, x9, y2, (9, 2))
    point_10_4 = PointAction(screen, x9, y3, (9, 3))
    point_10_5 = PointAction(screen, x9, y4, (9, 4))
    point_10_6 = PointAction(screen, x9, y5, (9, 5))
    point_10_7 = PointAction(screen, x9, y6, (9, 6))
    point_10_8 = PointAction(screen, x9, y7, (9, 7))
    point_10_9 = PointAction(screen, x9, y8, (9, 8))
    point_10_10 = PointAction(screen, x9, y9, (9, 9))
    point_10_11 = PointAction(screen, x9, y10, (9, 10))
    point_10_12 = PointAction(screen, x9, y11, (9, 11))
    point_10_13 = PointAction(screen, x9, y12, (9, 12))
    point_10_14 = PointAction(screen, x9, y13, (9, 13))
    point_10_15 = PointAction(screen, x9, y14, (9, 14))
    point_10_16 = PointAction(screen, x9, y15, (9, 15))
    point_10_17 = PointAction(screen, x9, y16, (9, 16))
    point_10_18 = PointAction(screen, x9, y17, (9, 17))
    point_10_19 = PointAction(screen, x9, y18, (9, 18))

    point_11_1 = PointAction(screen, x10, y0, (10, 0))
    point_11_2 = PointAction(screen, x10, y1, (10, 1))
    point_11_3 = PointAction(screen, x10, y2, (10, 2))
    point_11_4 = PointAction(screen, x10, y3, (10, 3))
    point_11_5 = PointAction(screen, x10, y4, (10, 4))
    point_11_6 = PointAction(screen, x10, y5, (10, 5))
    point_11_7 = PointAction(screen, x10, y6, (10, 6))
    point_11_8 = PointAction(screen, x10, y7, (10, 7))
    point_11_9 = PointAction(screen, x10, y8, (10, 8))
    point_11_10 = PointAction(screen, x10, y9, (10, 9))
    point_11_11 = PointAction(screen, x10, y10, (10, 10))
    point_11_12 = PointAction(screen, x10, y11, (10, 11))
    point_11_13 = PointAction(screen, x10, y12, (10, 12))
    point_11_14 = PointAction(screen, x10, y13, (10, 13))
    point_11_15 = PointAction(screen, x10, y14, (10, 14))
    point_11_16 = PointAction(screen, x10, y15, (10, 15))
    point_11_17 = PointAction(screen, x10, y16, (10, 16))
    point_11_18 = PointAction(screen, x10, y17, (10, 17))
    point_11_19 = PointAction(screen, x10, y18, (10, 18))

    point_12_1 = PointAction(screen, x11, y0, (11, 0))
    point_12_2 = PointAction(screen, x11, y1, (11, 1))
    point_12_3 = PointAction(screen, x11, y2, (11, 2))
    point_12_4 = PointAction(screen, x11, y3, (11, 3))
    point_12_5 = PointAction(screen, x11, y4, (11, 4))
    point_12_6 = PointAction(screen, x11, y5, (11, 5))
    point_12_7 = PointAction(screen, x11, y6, (11, 6))
    point_12_8 = PointAction(screen, x11, y7, (11, 7))
    point_12_9 = PointAction(screen, x11, y8, (11, 8))
    point_12_10 = PointAction(screen, x11, y9, (11, 9))
    point_12_11 = PointAction(screen, x11, y10, (11, 10))
    point_12_12 = PointAction(screen, x11, y11, (11, 11))
    point_12_13 = PointAction(screen, x11, y12, (11, 12))
    point_12_14 = PointAction(screen, x11, y13, (11, 13))
    point_12_15 = PointAction(screen, x11, y14, (11, 14))
    point_12_16 = PointAction(screen, x11, y15, (11, 15))
    point_12_17 = PointAction(screen, x11, y16, (11, 16))
    point_12_18 = PointAction(screen, x11, y17, (11, 17))
    point_12_19 = PointAction(screen, x11, y18, (11, 18))

    point_13_1 = PointAction(screen, x12, y0, (12, 0))
    point_13_2 = PointAction(screen, x12, y1, (12, 1))
    point_13_3 = PointAction(screen, x12, y2, (12, 2))
    point_13_4 = PointAction(screen, x12, y3, (12, 3))
    point_13_5 = PointAction(screen, x12, y4, (12, 4))
    point_13_6 = PointAction(screen, x12, y5, (12, 5))
    point_13_7 = PointAction(screen, x12, y6, (12, 6))
    point_13_8 = PointAction(screen, x12, y7, (12, 7))
    point_13_9 = PointAction(screen, x12, y8, (12, 8))
    point_13_10 = PointAction(screen, x12, y9, (12, 9))
    point_13_11 = PointAction(screen, x12, y10, (12, 10))
    point_13_12 = PointAction(screen, x12, y11, (12, 11))
    point_13_13 = PointAction(screen, x12, y12, (12, 12))
    point_13_14 = PointAction(screen, x12, y13, (12, 13))
    point_13_15 = PointAction(screen, x12, y14, (12, 14))
    point_13_16 = PointAction(screen, x12, y15, (12, 15))
    point_13_17 = PointAction(screen, x12, y16, (12, 16))
    point_13_18 = PointAction(screen, x12, y17, (12, 17))
    point_13_19 = PointAction(screen, x12, y18, (12, 18))

    point_14_1 = PointAction(screen, x13, y0, (13, 0))
    point_14_2 = PointAction(screen, x13, y1, (13, 1))
    point_14_3 = PointAction(screen, x13, y2, (13, 2))
    point_14_4 = PointAction(screen, x13, y3, (13, 3))
    point_14_5 = PointAction(screen, x13, y4, (13, 4))
    point_14_6 = PointAction(screen, x13, y5, (13, 5))
    point_14_7 = PointAction(screen, x13, y6, (13, 6))
    point_14_8 = PointAction(screen, x13, y7, (13, 7))
    point_14_9 = PointAction(screen, x13, y8, (13, 8))
    point_14_10 = PointAction(screen, x13, y9, (13, 9))
    point_14_11 = PointAction(screen, x13, y10, (13, 10))
    point_14_12 = PointAction(screen, x13, y11, (13, 11))
    point_14_13 = PointAction(screen, x13, y12, (13, 12))
    point_14_14 = PointAction(screen, x13, y13, (13, 13))
    point_14_15 = PointAction(screen, x13, y14, (13, 14))
    point_14_16 = PointAction(screen, x13, y15, (13, 15))
    point_14_17 = PointAction(screen, x13, y16, (13, 16))
    point_14_18 = PointAction(screen, x13, y17, (13, 17))
    point_14_19 = PointAction(screen, x13, y18, (13, 18))

    point_15_1 = PointAction(screen, x14, y0, (14, 0))
    point_15_2 = PointAction(screen, x14, y1, (14, 1))
    point_15_3 = PointAction(screen, x14, y2, (14, 2))
    point_15_4 = PointAction(screen, x14, y3, (14, 3))
    point_15_5 = PointAction(screen, x14, y4, (14, 4))
    point_15_6 = PointAction(screen, x14, y5, (14, 5))
    point_15_7 = PointAction(screen, x14, y6, (14, 6))
    point_15_8 = PointAction(screen, x14, y7, (14, 7))
    point_15_9 = PointAction(screen, x14, y8, (14, 8))
    point_15_10 = PointAction(screen, x14, y9, (14, 9))
    point_15_11 = PointAction(screen, x14, y10, (14, 10))
    point_15_12 = PointAction(screen, x14, y11, (14, 11))
    point_15_13 = PointAction(screen, x14, y12, (14, 12))
    point_15_14 = PointAction(screen, x14, y13, (14, 13))
    point_15_15 = PointAction(screen, x14, y14, (14, 14))
    point_15_16 = PointAction(screen, x14, y15, (14, 15))
    point_15_17 = PointAction(screen, x14, y16, (14, 16))
    point_15_18 = PointAction(screen, x14, y17, (14, 17))
    point_15_19 = PointAction(screen, x14, y18, (14, 18))

    point_16_1 = PointAction(screen, x15, y0, (15, 0))
    point_16_2 = PointAction(screen, x15, y1, (15, 1))
    point_16_3 = PointAction(screen, x15, y2, (15, 2))
    point_16_4 = PointAction(screen, x15, y3, (15, 3))
    point_16_5 = PointAction(screen, x15, y4, (15, 4))
    point_16_6 = PointAction(screen, x15, y5, (15, 5))
    point_16_7 = PointAction(screen, x15, y6, (15, 6))
    point_16_8 = PointAction(screen, x15, y7, (15, 7))
    point_16_9 = PointAction(screen, x15, y8, (15, 8))
    point_16_10 = PointAction(screen, x15, y9, (15, 9))
    point_16_11 = PointAction(screen, x15, y10, (15, 10))
    point_16_12 = PointAction(screen, x15, y11, (15, 11))
    point_16_13 = PointAction(screen, x15, y12, (15, 12))
    point_16_14 = PointAction(screen, x15, y13, (15, 13))
    point_16_15 = PointAction(screen, x15, y14, (15, 14))
    point_16_16 = PointAction(screen, x15, y15, (15, 15))
    point_16_17 = PointAction(screen, x15, y16, (15, 16))
    point_16_18 = PointAction(screen, x15, y17, (15, 17))
    point_16_19 = PointAction(screen, x15, y18, (15, 18))

    point_17_1 = PointAction(screen, x16, y0, (16, 0))
    point_17_2 = PointAction(screen, x16, y1, (16, 1))
    point_17_3 = PointAction(screen, x16, y2, (16, 2))
    point_17_4 = PointAction(screen, x16, y3, (16, 3))
    point_17_5 = PointAction(screen, x16, y4, (16, 4))
    point_17_6 = PointAction(screen, x16, y5, (16, 5))
    point_17_7 = PointAction(screen, x16, y6, (16, 6))
    point_17_8 = PointAction(screen, x16, y7, (16, 7))
    point_17_9 = PointAction(screen, x16, y8, (16, 8))
    point_17_10 = PointAction(screen, x16, y9, (16, 9))
    point_17_11 = PointAction(screen, x16, y10, (16, 10))
    point_17_12 = PointAction(screen, x16, y11, (16, 11))
    point_17_13 = PointAction(screen, x16, y12, (16, 12))
    point_17_14 = PointAction(screen, x16, y13, (16, 13))
    point_17_15 = PointAction(screen, x16, y14, (16, 14))
    point_17_16 = PointAction(screen, x16, y15, (16, 15))
    point_17_17 = PointAction(screen, x16, y16, (16, 16))
    point_17_18 = PointAction(screen, x16, y17, (16, 17))
    point_17_19 = PointAction(screen, x16, y18, (16, 18))

    point_18_1 = PointAction(screen, x17, y0, (17, 0))
    point_18_2 = PointAction(screen, x17, y1, (17, 1))
    point_18_3 = PointAction(screen, x17, y2, (17, 2))
    point_18_4 = PointAction(screen, x17, y3, (17, 3))
    point_18_5 = PointAction(screen, x17, y4, (17, 4))
    point_18_6 = PointAction(screen, x17, y5, (17, 5))
    point_18_7 = PointAction(screen, x17, y6, (17, 6))
    point_18_8 = PointAction(screen, x17, y7, (17, 7))
    point_18_9 = PointAction(screen, x17, y8, (17, 8))
    point_18_10 = PointAction(screen, x17, y9, (17, 9))
    point_18_11 = PointAction(screen, x17, y10, (17, 10))
    point_18_12 = PointAction(screen, x17, y11, (17, 11))
    point_18_13 = PointAction(screen, x17, y12, (17, 12))
    point_18_14 = PointAction(screen, x17, y13, (17, 13))
    point_18_15 = PointAction(screen, x17, y14, (17, 14))
    point_18_16 = PointAction(screen, x17, y15, (17, 15))
    point_18_17 = PointAction(screen, x17, y16, (17, 16))
    point_18_18 = PointAction(screen, x17, y17, (17, 17))
    point_18_19 = PointAction(screen, x17, y18, (17, 18))

    point_19_1 = PointAction(screen, x18, y0, (18, 0))
    point_19_2 = PointAction(screen, x18, y1, (18, 1))
    point_19_3 = PointAction(screen, x18, y2, (18, 2))
    point_19_4 = PointAction(screen, x18, y3, (18, 3))
    point_19_5 = PointAction(screen, x18, y4, (18, 4))
    point_19_6 = PointAction(screen, x18, y5, (18, 5))
    point_19_7 = PointAction(screen, x18, y6, (18, 6))
    point_19_8 = PointAction(screen, x18, y7, (18, 7))
    point_19_9 = PointAction(screen, x18, y8, (18, 8))
    point_19_10 = PointAction(screen, x18, y9, (18, 9))
    point_19_11 = PointAction(screen, x18, y10, (18, 10))
    point_19_12 = PointAction(screen, x18, y11, (18, 11))
    point_19_13 = PointAction(screen, x18, y12, (18, 12))
    point_19_14 = PointAction(screen, x18, y13, (18, 13))
    point_19_15 = PointAction(screen, x18, y14, (18, 14))
    point_19_16 = PointAction(screen, x18, y15, (18, 15))
    point_19_17 = PointAction(screen, x18, y16, (18, 16))
    point_19_18 = PointAction(screen, x18, y17, (18, 17))
    point_19_19 = PointAction(screen, x18, y18, (18, 18))

    running = True
    clock = pygame.time.Clock()
    clock.tick(10)
    clr_text = db_taker.clr_font_text
    black_pass_butt = Button(screen, 75, 600, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    white_pass_butt = Button(screen, 75, 600, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    game_over_butt = Button(screen, 500, 75, pas_clr_button=db_taker.pas_clr_button,
                             act_clr_button=db_taker.act_clr_button, clr_font_butt=db_taker.clr_font_butt)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if init_board.black_pas and init_board.white_pas or init_board.black_chips == 0 and init_board.white_chips == 0:
            screen.fill(background)
            screen.blit(background_image, (0, 0))
            print_text(screen, 'GAME OVER', 50, 50, size=150)
            game_over_butt.draw(200, 600, 'return to menu', size=50, act='use_box')
            if game_over_butt.true_box:
                running = False
        else:
            screen.fill(background)
            screen.blit(background_image, (0, 0))
            print_text(screen, 'black survivors', 10, 10, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.black_chips), 10, 30, size=25, clr_font_text=clr_text)
            print_text(screen, 'killed', 10, 60, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.black_kills), 10, 80, size=25, clr_font_text=clr_text)

            print_text(screen, 'white survivors', 765, 10, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.white_chips), 765, 30, size=25, clr_font_text=clr_text)
            print_text(screen, 'killed', 765, 60, size=25, clr_font_text=clr_text)
            print_text(screen, str(init_board.white_kills), 765, 80, size=25, clr_font_text=clr_text)

            pygame.draw.line(screen, init_board.player, (0, 763), (width, 763), width=10)

            pygame.draw.line(screen, (60, 25, 30), (x0, y0), (x18, y0), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y1), (x18, y1), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y2), (x18, y2), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y3), (x18, y3), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y4), (x18, y4), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y5), (x18, y5), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y6), (x18, y6), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y7), (x18, y7), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y8), (x18, y8), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y9), (x18, y9), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y10), (x18, y10), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y11), (x18, y11), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y12), (x18, y12), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y13), (x18, y13), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y14), (x18, y14), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y15), (x18, y15), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y16), (x18, y16), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y17), (x18, y17), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x0, y18), (x18, y18), width=3)

            pygame.draw.line(screen, (60, 25, 30), (x0, y0), (x0, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x1, y0), (x1, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x2, y0), (x2, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x3, y0), (x3, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x4, y0), (x4, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x5, y0), (x5, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x6, y0), (x6, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x7, y0), (x7, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x8, y0), (x8, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x9, y0), (x9, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x10, y0), (x10, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x11, y0), (x11, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x12, y0), (x12, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x13, y0), (x13, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x14, y0), (x14, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x15, y0), (x15, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x16, y0), (x16, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x17, y0), (x17, y18), width=3)
            pygame.draw.line(screen, (60, 25, 30), (x18, y0), (x18, y18), width=3)

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
            point_1_14.select_shape()
            point_1_15.select_shape()
            point_1_16.select_shape()
            point_1_17.select_shape()
            point_1_18.select_shape()
            point_1_19.select_shape()

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
            point_2_14.select_shape()
            point_2_15.select_shape()
            point_2_16.select_shape()
            point_2_17.select_shape()
            point_2_18.select_shape()
            point_2_19.select_shape()

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
            point_3_14.select_shape()
            point_3_15.select_shape()
            point_3_16.select_shape()
            point_3_17.select_shape()
            point_3_18.select_shape()
            point_3_19.select_shape()

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
            point_4_14.select_shape()
            point_4_15.select_shape()
            point_4_16.select_shape()
            point_4_17.select_shape()
            point_4_18.select_shape()
            point_4_19.select_shape()

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
            point_5_14.select_shape()
            point_5_15.select_shape()
            point_5_16.select_shape()
            point_5_17.select_shape()
            point_5_18.select_shape()
            point_5_19.select_shape()

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
            point_6_14.select_shape()
            point_6_15.select_shape()
            point_6_16.select_shape()
            point_6_17.select_shape()
            point_6_18.select_shape()
            point_6_19.select_shape()

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
            point_7_14.select_shape()
            point_7_15.select_shape()
            point_7_16.select_shape()
            point_7_17.select_shape()
            point_7_18.select_shape()
            point_7_19.select_shape()

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
            point_8_14.select_shape()
            point_8_15.select_shape()
            point_8_16.select_shape()
            point_8_17.select_shape()
            point_8_18.select_shape()
            point_8_19.select_shape()

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
            point_9_14.select_shape()
            point_9_15.select_shape()
            point_9_16.select_shape()
            point_9_17.select_shape()
            point_9_18.select_shape()
            point_9_19.select_shape()

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
            point_10_14.select_shape()
            point_10_15.select_shape()
            point_10_16.select_shape()
            point_10_17.select_shape()
            point_10_18.select_shape()
            point_10_19.select_shape()

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
            point_11_14.select_shape()
            point_11_15.select_shape()
            point_11_16.select_shape()
            point_11_17.select_shape()
            point_11_18.select_shape()
            point_11_19.select_shape()

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
            point_12_14.select_shape()
            point_12_15.select_shape()
            point_12_16.select_shape()
            point_12_17.select_shape()
            point_12_18.select_shape()
            point_12_19.select_shape()

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
            point_13_14.select_shape()
            point_13_15.select_shape()
            point_13_16.select_shape()
            point_13_17.select_shape()
            point_13_18.select_shape()
            point_13_19.select_shape()

            point_14_1.select_shape()
            point_14_2.select_shape()
            point_14_3.select_shape()
            point_14_4.select_shape()
            point_14_5.select_shape()
            point_14_6.select_shape()
            point_14_7.select_shape()
            point_14_8.select_shape()
            point_14_9.select_shape()
            point_14_10.select_shape()
            point_14_11.select_shape()
            point_14_12.select_shape()
            point_14_13.select_shape()
            point_14_14.select_shape()
            point_14_15.select_shape()
            point_14_16.select_shape()
            point_14_17.select_shape()
            point_14_18.select_shape()
            point_14_19.select_shape()

            point_15_1.select_shape()
            point_15_2.select_shape()
            point_15_3.select_shape()
            point_15_4.select_shape()
            point_15_5.select_shape()
            point_15_6.select_shape()
            point_15_7.select_shape()
            point_15_8.select_shape()
            point_15_9.select_shape()
            point_15_10.select_shape()
            point_15_11.select_shape()
            point_15_12.select_shape()
            point_15_13.select_shape()
            point_15_14.select_shape()
            point_15_15.select_shape()
            point_15_16.select_shape()
            point_15_17.select_shape()
            point_15_18.select_shape()
            point_15_19.select_shape()

            point_16_1.select_shape()
            point_16_2.select_shape()
            point_16_3.select_shape()
            point_16_4.select_shape()
            point_16_5.select_shape()
            point_16_6.select_shape()
            point_16_7.select_shape()
            point_16_8.select_shape()
            point_16_9.select_shape()
            point_16_10.select_shape()
            point_16_11.select_shape()
            point_16_12.select_shape()
            point_16_13.select_shape()
            point_16_14.select_shape()
            point_16_15.select_shape()
            point_16_16.select_shape()
            point_16_17.select_shape()
            point_16_18.select_shape()
            point_16_19.select_shape()

            point_17_1.select_shape()
            point_17_2.select_shape()
            point_17_3.select_shape()
            point_17_4.select_shape()
            point_17_5.select_shape()
            point_17_6.select_shape()
            point_17_7.select_shape()
            point_17_8.select_shape()
            point_17_9.select_shape()
            point_17_10.select_shape()
            point_17_11.select_shape()
            point_17_12.select_shape()
            point_17_13.select_shape()
            point_17_14.select_shape()
            point_17_15.select_shape()
            point_17_16.select_shape()
            point_17_17.select_shape()
            point_17_18.select_shape()
            point_17_19.select_shape()

            point_18_1.select_shape()
            point_18_2.select_shape()
            point_18_3.select_shape()
            point_18_4.select_shape()
            point_18_5.select_shape()
            point_18_6.select_shape()
            point_18_7.select_shape()
            point_18_8.select_shape()
            point_18_9.select_shape()
            point_18_10.select_shape()
            point_18_11.select_shape()
            point_18_12.select_shape()
            point_18_13.select_shape()
            point_18_14.select_shape()
            point_18_15.select_shape()
            point_18_16.select_shape()
            point_18_17.select_shape()
            point_18_18.select_shape()
            point_18_19.select_shape()

            point_19_1.select_shape()
            point_19_2.select_shape()
            point_19_3.select_shape()
            point_19_4.select_shape()
            point_19_5.select_shape()
            point_19_6.select_shape()
            point_19_7.select_shape()
            point_19_8.select_shape()
            point_19_9.select_shape()
            point_19_10.select_shape()
            point_19_11.select_shape()
            point_19_12.select_shape()
            point_19_13.select_shape()
            point_19_14.select_shape()
            point_19_15.select_shape()
            point_19_16.select_shape()
            point_19_17.select_shape()
            point_19_18.select_shape()
            point_19_19.select_shape()
            if init_board.player == (20, 20, 20):
                black_pass_butt.draw(10, 120, 'pass', size=28, act='pass_step')
            elif init_board.player == (230, 230, 230):
                white_pass_butt.draw(815, 120, 'pass', size=28, act='pass_step')
            init_board.board_checking(init_board.player)
            clock.tick(10)
        pygame.display.flip()


def str_to_tuple(string):
    return tuple(map(lambda x: int(x), string.split()))


board_size = [[5, 6, 7], [8, 9, 11], [13, 15, 19]]
db_taker = DataBaseTaker()
while db_taker.start_game:
    init_board = ''
    choice_board_size_menu()
    if init_board.size_board == 5:
        create_board_5()
    elif init_board.size_board == 13:
        create_board_13()
    elif init_board.size_board == 19:
        create_board_19()
    pygame.quit()
