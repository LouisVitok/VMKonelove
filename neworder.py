import pygame
from math import pi, sqrt
import random


class Table:
    def __init__(self, window_size, screen):
        self.b_15 = None
        self.b_14 = None
        self.b_13 = None
        self.b_12 = None
        self.b_11 = None
        self.b_10 = None
        self.b_9 = None
        self.b_8 = None
        self.b_7 = None
        self.b_6 = None
        self.b_4 = None
        self.b_3 = None
        self.b_2 = None
        self.b_1 = None
        self.b_5 = None
        self.sq = min(window_size[0], window_size[1])
        self.ball_size = (6 * (sq // 8)) // 52
        self.screen = screen
        self.window_size = window_size
        self.array = None
        self.start()

    def game(self):
        while 1:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    pressed = pygame.mouse.get_pressed()
                    pos = pygame.mouse.get_pos()
                    if pressed[0]:
                        for i in range(1, 17):
                            elem = self.array[i - 1]
                            if abs(elem[0]) + abs(elem[1]) == 0:
                                continue
                            else:
                                if pos[0] <= elem[0] + self.ball_size // 2 and elem[0] - self.ball_size // 2 <= pos[0] and pos[1] <= elem[1] + self.ball_size // 2 and elem[1] - self.ball_size // 2 <= pos[1]:
                                    xelem = elem[0] + random.randint(-100, 100)
                                    yelem = elem[1] + random.randint(-100, 100)
                                    match i:
                                        case 1:
                                            self.b_1.koo_in(xelem, yelem)
                                        case 2:
                                            self.b_2.koo_in(xelem, yelem)
                                        case 3:
                                            self.b_3.koo_in(xelem, yelem)
                                        case 4:
                                            self.b_4.koo_in(xelem, yelem)
                                        case 5:
                                            self.b_5.koo_in(xelem, yelem)
                                        case 6:
                                            self.b_6.koo_in(xelem, yelem)
                                        case 7:
                                            self.b_7.koo_in(xelem, yelem)
                                        case 8:
                                            self.b_8.koo_in(xelem, yelem)
                                        case 9:
                                            self.b_9.koo_in(xelem, yelem)
                                        case 10:
                                            self.b_10.koo_in(xelem, yelem)
                                        case 11:
                                            self.b_11.koo_in(xelem, yelem)
                                        case 12:
                                            self.b_12.koo_in(xelem, yelem)
                                        case 13:
                                            self.b_13.koo_in(xelem, yelem)
                                        case 14:
                                            self.b_14.koo_in(xelem, yelem)
                                        case 15:
                                            self.b_15.koo_in(xelem, yelem)
                                        case 16:
                                            self.b_16.koo_in(xelem, yelem)
                                    self.dr_table()

    def start(self):
        sq = min(self.window_size[0], self.window_size[1])
        r = sq // 2
        e = self.window_size[0] // 2 - r
        if self.window_size[0] > self.window_size[1]:
            self.b_1 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4, 2.5 * (sq // 8) + 3 * (sq // 8) // 2, self.ball_size, self.screen,
                       (255, 255, 255), self.window_size)
            self.b_2 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - int(self.ball_size * sqrt(3) / 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2 - int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_3 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - int(self.ball_size * sqrt(3) / 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2 + int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_4 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 2 * int(self.ball_size * sqrt(3) // 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_5 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 2 * int(self.ball_size * sqrt(3) // 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2, self.ball_size, self.screen, (255, 255, 255), self.window_size)
            self.b_6 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 2 * int(self.ball_size * sqrt(3) // 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_7 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 3 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_8 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 1 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_9 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                       2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 3 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_10 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                        2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 1 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_11 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 4 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_12 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_13 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 0 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_14 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_15 = Ball(e + sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 4 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)

            self.b_16 = Ball(e + sq // 8 + 3 * (6 * (sq // 8)) // 4, 2.5 * (sq // 8) + 3 * (sq // 8) // 2,
                             self.ball_size,
                             self.screen,
                             (255, 0, 0), self.window_size)
        else:
            self.b_1 = Ball(sq // 8 + (6 * (sq // 8)) // 4, e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2, self.ball_size, self.screen,
                       (255, 255, 255), self.window_size)
            self.b_2 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - int(self.ball_size * sqrt(3) / 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 - int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_3 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - int(self.ball_size * sqrt(3) / 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 + int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_4 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 2 * int(self.ball_size * sqrt(3) // 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_5 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 2 * int(self.ball_size * sqrt(3) // 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2, self.ball_size, self.screen, (255, 255, 255), self.window_size)
            self.b_6 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 2 * int(self.ball_size * sqrt(3) // 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_7 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 3 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_8 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 1 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_9 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                       e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 3 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                       self.window_size)
            self.b_10 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 3 * int(self.ball_size * sqrt(3) // 2),
                        e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 1 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_11 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 4 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_12 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_13 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 - 0 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_14 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 2 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)
            self.b_15 = Ball(sq // 8 + (6 * (sq // 8)) // 4 - 4 * int(self.ball_size * sqrt(3) // 2),
                        e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2 + 4 * int(self.ball_size * 0.5), self.ball_size, self.screen, (255, 255, 255),
                        self.window_size)

            self.b_16 = Ball(sq // 8 + 3 * (6 * (sq // 8)) // 4, e + 2.5 * (sq // 8) + 3 * (sq // 8) // 2,
                             self.ball_size,
                             self.screen,
                             (255, 0, 0), self.window_size)
        self.dr_table()
        self.game()



    def dr_table(self):
        if self.window_size[0] > self.window_size[1]:
            t = 1
        else:
            t = 0
        sq = min(self.window_size[0], self.window_size[1])
        r = sq // 2
        if t == 1:
            e = self.window_size[0] // 2 - r

            pygame.draw.rect(self.screen, (12, 186, 22),
                             (e + sq // 8, 2.5 * (sq // 8) - self.ball_size - 10, 6 * (sq // 8), self.ball_size + 10))
            pygame.draw.rect(self.screen, (12, 186, 22),
                             (e + sq // 8, 2.5 * (sq // 8) + 3 * (sq // 8), 6 * (sq // 8), self.ball_size + 10))
            pygame.draw.rect(self.screen, (12, 186, 22),
                             (e + sq // 8 - ball_size - 10, 2.5 * (sq // 8), self.ball_size + 10, 3 * (sq // 8)))
            pygame.draw.rect(self.screen, (12, 186, 22),
                             (e + sq // 8 + 6 * (sq // 8), 2.5 * (sq // 8), self.ball_size + 10, 3 * (sq // 8)))

            pygame.draw.circle(self.screen, (12, 186, 22), (e + sq // 8, 2.5 * (sq // 8)), self.ball_size + 10)
            pygame.draw.circle(self.screen, (12, 186, 22), (e + sq // 8 + 6 * (sq // 8), 2.5 * (sq // 8)))
            pygame.draw.circle(self.screen, (12, 186, 22), (e + sq // 8 + 6 * (sq // 8), 2.5 * (sq // 8) + 3 * (sq // 8)),
                               self.ball_size + 10)
            pygame.draw.circle(self.screen, (12, 186, 22), (e + sq // 8, 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 10)

            pygame.draw.rect(self.screen, (0, 255, 0), (e + sq // 8, 2.5 * (sq // 8), 6 * (sq // 8), 3 * (sq // 8)))
        else:
            e = self.window_size[1] // 2 - r
            pygame.draw.rect(self.screen, (12, 186, 22),
                             (sq // 8, e + 2.5 * (sq // 8) - self.ball_size - 10, 6 * (sq // 8), self.ball_size + 10))
            pygame.draw.rect(self.screen, (12, 186, 22),
                             (sq // 8, e + 2.5 * (sq // 8) + 3 * (sq // 8), 6 * (sq // 8), self.ball_size + 10))
            pygame.draw.rect(self.screen, (12, 186, 22),
                             (sq // 8 - self.ball_size - 10, e + 2.5 * (sq // 8), self.ball_size + 10, 3 * (sq // 8)))
            pygame.draw.rect(self.screen, (12, 186, 22),
                             (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8), self.ball_size + 10, 3 * (sq // 8)))

            pygame.draw.circle(self.screen, (12, 186, 22), (sq // 8, e + 2.5 * (sq // 8)), self.ball_size + 10)
            pygame.draw.circle(self.screen, (12, 186, 22),
                               (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8)), self.ball_size + 10)
            pygame.draw.circle(self.screen, (12, 186, 22),
                               (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 10)
            pygame.draw.circle(self.screen, (12, 186, 22),
                               (sq // 8, e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 10)

            pygame.draw.rect(self.screen, (0, 255, 0), (sq // 8, e + 2.5 * (sq // 8), 6 * (sq // 8), 3 * (sq // 8)))
        self.array = self.comm_ball()
        pygame.display.flip()

    def comm_ball(self):
        lst = [self.b_1.koo(), self.b_2.koo(), self.b_3.koo(), self.b_4.koo(), self.b_5.koo(), self.b_6.koo(), self.b_7.koo(), self.b_8.koo(), self.b_9.koo(), self.b_10.koo(), self.b_11.koo(), self.b_12.koo(), self.b_13.koo(), self.b_14.koo(), self.b_15.koo(), self.b_16.koo()]
        for elem in lst:
            if abs(elem[0]) + abs(elem[1]) != 0:
                pygame.draw.circle(self.screen, elem[2], (elem[0], elem[1]), self.ball_size // 2)
        return lst

class Ball:
    def __init__(self, st_x, st_y, size, screen, color, window_size):
        self.x = st_x
        self.y = st_y
        self.size = size
        self.screen = screen
        # pygame.draw.circle(self.screen, color, (self.x, self.y), self.size // 2)
        # pygame.display.flip()
        self.color = color
        self.window_size = window_size
        self.state = True # in game
        # self.move()

    def koo(self):
        if self.state:
            return (self.x, self.y, self.color)
        else:
            return (0,0, self.color)

    def koo_in(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        while 1:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    pressed = pygame.mouse.get_pressed()
                    pos = pygame.mouse.get_pos()
                    if pressed[0]:
                        if pos[0] <= self.x + self.size // 2 and self.x - self.size // 2 <= pos[0] and pos[1] <= self.y + self.size // 2 and self.y - self.size // 2 <= pos[1]:
                            self.x += random.randint(-100, 100)
                            self.y += random.randint(-100, 100)
                            # dr_table(self.screen, self.window_size[0], self.window_size[1], self.size)


if __name__ == '__main__':
    pygame.init()
    window_size = (700, 700)
    pygame.display.set_caption("Бильярдный стол")
    screen = pygame.display.set_mode(window_size)
    background_color = (0, 0, 255)  # синий

    # заполняем фон заданным цветом
    screen.fill(background_color)
    sq = min(window_size[0], window_size[1])
    ball_size = (6 * (sq // 8)) // 52

    table = Table(window_size, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()