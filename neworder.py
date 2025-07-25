import pygame
from math import pi, sqrt, atan, sin, cos, acos, tan
import time
pygame.font.init()

FPS = 120

class Table:
    def __init__(self, window_size, screen):
        self.b_16 = None
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
        self.score=0
        # self.balls = [self.b_1, self.b_2, self.b_3, self.b_4, self.b_5, self.b_6, self.b_7, self.b_8, self.b_9, self.b_10, self.b_11, self.b_12, self.b_13, self.b_14, self.b_15, self.b_16]
        self.sq = min(window_size[0], window_size[1])
        self.ball_size = (6 * (sq // 8)) // 52
        self.screen = screen
        self.window_size = window_size
        self.array = None
        self.table_size = list()
        self.clock = pygame.time.Clock()
        self.start()

    def f_line_chousen(self, k, x_0, y_0, x):
        return k * (x - x_0) + y_0

    def x_f_line_chousen(self, k, x_0, y_0, y):
        return (y - y_0) / k + x_0

    def find_perese(self, k, num, deltax, deltay):
        cur_closest = [1000, 1000]
        second_dot_possible = [0, 0]
        if k != 'x=0' and k != 'y=0':
            for i in range(len(self.array)):
                if i == num:
                    continue
                else:
                    if self.array[i][3]:
                        # if deltax > 0:
                        #     k1 = 1
                        # else:
                        #     k1 = -1
                        # if deltay > 0:
                        #     k2 = 1
                        # else:
                        #     k2 = -1
                        # if i == 9:
                            # print((self.array[i][0] - self.array[num][0]) * k1 + (self.array[i][1] - self.array[num][1]) * k * k2, (self.array[i][0] - self.array[num][0]) * k1, (self.array[i][1] - self.array[num][1]) * k * k2, k, k1, k2, 333)
                        # if (self.array[i][0] - self.array[num][0]) * k1 + (self.array[i][1] - self.array[num][1]) * k * k2 >= 0:
                        if (self.f_line_chousen(-1 / k, self.array[num][0], self.array[num][1], self.array[i][0]) - self.array[i][1]) * pow(-1, (deltay < 0)) < 0:
                            # print(i)
                            x_meet = (self.array[i][0] / k + self.array[i][1] + k * self.array[num][0] - self.array[num][1]) / (
                                        k + 1 / k)
                            y_meet = self.f_line_chousen(k, self.array[num][0], self.array[num][1], x_meet)
                            # print((self.array[i][0], self.array[i][1]), x_meet, y_meet, i, 111)
                            # if i == 9:
                            #     print(sqrt((x_meet - self.array[i][0]) ** 2 + (y_meet - self.array[i][1]) ** 2), self.ball_size // 2)
                            if sqrt((x_meet - self.array[i][0]) ** 2 + (y_meet - self.array[i][1]) ** 2) <= self.ball_size:
                                if sqrt((self.array[i][0] - self.array[num][0]) ** 2 + (
                                        self.array[i][1] - self.array[num][1]) ** 2) < sqrt(
                                        (cur_closest[0] - self.array[num][0]) ** 2 + (
                                                cur_closest[1] - self.array[num][1]) ** 2):
                                    second_dot_possible = [x_meet, y_meet]
                                    cur_closest = [self.array[i][0], self.array[i][1]]
                                    # print(second_dot_possible, cur_closest, i, 222)
                            else:
                                continue
        elif k == 'x=0':
            # if deltay != 0:
                # x_meet0 = self.array[num][0]
                # y_meet0 = self.table_size[1+pow(-1, deltay < 0)]
                # second_dot_possible = [x_meet0, y_meet0]
            for i in range(len(self.array)):
                if i == num:
                    continue
                else:
                    if self.array[i][3]:
                        if deltay > 0:
                            if self.array[i][1] - self.array[num][1] > 0 and self.array[i][0] > self.array[num][0] - self.ball_size and self.array[i][0] < self.array[num][0] + self.ball_size:
                                x_meet = self.array[num][0]
                                y_meet = self.array[i][1]

                                if self.array[i][1] - self.array[num][1] > 0 and sqrt((self.array[i][0] - self.array[num][0]) ** 2 + (self.array[i][1] - self.array[num][1]) ** 2) < sqrt((cur_closest[0] - self.array[num][0]) ** 2 + (cur_closest[1] - self.array[num][1]) ** 2):

                                    cur_closest = [self.array[i][0], self.array[i][1]]
                                    second_dot_possible = [x_meet, y_meet]
                        if deltay < 0:
                            if self.array[i][1] - self.array[num][1]< 0 and self.array[i][0] > self.array[num][
                                0] - self.ball_size // 2 and self.array[i][0] < self.array[num][
                                0] + self.ball_size // 2:
                                x_meet = self.array[num][0]
                                y_meet = self.array[i][1]
                                if self.array[i][1] - self.array[num][1] < 0 and sqrt(
                                    (self.array[i][0] - self.array[num][0]) ** 2 + (
                                            self.array[i][1] - self.array[num][1]) ** 2) < sqrt(
                                (cur_closest[0] - self.array[num][0]) ** 2 + (
                                        cur_closest[1] - self.array[num][1]) ** 2):
                                    second_dot_possible = [x_meet, y_meet]
                                    cur_closest = [self.array[i][0], self.array[i][1]]
            # else:
            #     second_dot_possible = [self.array[num][0], self.array[num][1]]
        elif k == 'y=0':
            # x_meet0 = self.table_size[2 + pow(-1, deltax >= 0)]
            # y_meet0 = self.array[num][0]
            # second_dot_possible = [x_meet0, y_meet0]
            for i in range(len(self.array)):
                if i == num:
                    continue
                else:
                    if self.array[i][3]:
                        if deltax > 0:
                            if self.array[i][0] - self.array[num][0] > 0 and self.array[i][1] > self.array[num][
                                1] - self.ball_size and self.array[i][1] < self.array[num][
                                1] + self.ball_size:
                                print(i)
                                x_meet = self.array[i][0]
                                y_meet = self.array[num][1]
                                if sqrt((self.array[i][0] - self.array[num][0]) ** 2 + (self.array[i][1] - self.array[num][1]) ** 2) < sqrt((cur_closest[0] - self.array[num][0]) ** 2 + (cur_closest[1] - self.array[num][1]) ** 2):
                                    second_dot_possible = [x_meet, y_meet]
                                    cur_closest = [self.array[i][0], self.array[i][1]]
                        if deltax < 0:
                            if self.array[i][0] - self.array[num][0] < 0 and self.array[i][1] > self.array[num][
                                1] - self.ball_size // 2 and self.array[i][1] < self.array[num][
                                1] + self.ball_size // 2:
                                x_meet = self.array[i][0]
                                y_meet = self.array[num][1]
                                if self.array[i][0] - self.array[num][0] < 0 and sqrt(
                                    (self.array[i][0] - self.array[num][0]) ** 2 + (
                                            self.array[i][1] - self.array[num][1]) ** 2) < sqrt(
                                (cur_closest[0] - self.array[num][0]) ** 2 + (
                                        cur_closest[1] - self.array[num][1]) ** 2):
                                    second_dot_possible = [x_meet, y_meet]
                                    cur_closest = [self.array[i][0], self.array[i][1]]
                    else:
                        continue
        if second_dot_possible == [0, 0]:
            # print('________________________________________________________')
            if deltax != 0 and deltay != 0:
                kl = abs(k)
                if deltax > 0 and deltay > 0:
                    perese_with_2_bort = self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                             self.table_size[1])
                    if perese_with_2_bort > self.table_size[2]:
                        second_dot = [
                            self.x_f_line_chousen(k, self.array[num][0], self.array[num][1], self.table_size[2]) - (
                                        self.ball_size // 2 / kl), self.table_size[2] - (self.ball_size // 2), 2]
                    else:
                        second_dot = [self.table_size[1] - (self.ball_size // 2),
                                      self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                          self.table_size[1]) - kl * (self.ball_size // 2), 1]
                elif deltax > 0 and deltay < 0:
                    perese_with_2_bort = self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                             self.table_size[1])
                    if perese_with_2_bort < self.table_size[0]:
                        second_dot = [
                            self.x_f_line_chousen(k, self.array[num][0], self.array[num][1], self.table_size[0]) - (
                                        self.ball_size // 2 / kl), self.table_size[0] + (self.ball_size // 2), 0]
                    else:
                        second_dot = [self.table_size[1] - (self.ball_size // 2),
                                      self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                          self.table_size[1]) + kl * (self.ball_size // 2), 1]
                elif deltax < 0 and deltay > 0:
                    perese_with_4_bort = self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                             self.table_size[3])
                    if perese_with_4_bort > self.table_size[2]:
                        second_dot = [
                            self.x_f_line_chousen(k, self.array[num][0], self.array[num][1], self.table_size[2]) + (
                                        self.ball_size // 2 / kl), self.table_size[2] - (self.ball_size // 2), 2]
                    else:
                        second_dot = [self.table_size[3] + (self.ball_size // 2),
                                      self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                          self.table_size[3]) - kl * (self.ball_size // 2), 3]
                elif deltax < 0 and deltay < 0:
                    perese_with_4_bort = self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                             self.table_size[3])
                    if perese_with_4_bort < self.table_size[0]:
                        second_dot = [
                            self.x_f_line_chousen(k, self.array[num][0], self.array[num][1], self.table_size[0]) + (
                                        self.ball_size // 2 / kl), self.table_size[0] + (self.ball_size // 2), 0]
                    else:
                        second_dot = [self.table_size[3] + (self.ball_size // 2),
                                      self.f_line_chousen(k, self.array[num][0], self.array[num][1],
                                                          self.table_size[3]) + kl * (self.ball_size // 2), 3]
            elif deltax == 0 or deltay == 0:
                print(1234124521344)
                if deltay == 0:
                    if deltax > 0:
                        second_dot = [self.table_size[1] - (self.ball_size // 2), self.array[num][1], 1]
                    elif deltax < 0:
                        second_dot = [self.table_size[3] + (self.ball_size // 2), self.array[num][1], 3]
                    else:
                        second_dot = [self.array[num][0], self.array[num][1]]
                elif deltax == 0:
                    if deltay > 0:
                        second_dot = [self.array[num][0], self.table_size[2] - (self.ball_size // 2), 2]
                    elif deltay < 0:
                        second_dot = [self.array[num][0], self.table_size[0] + (self.ball_size // 2), 0]
                    else:
                        second_dot = [self.array[num][0], self.array[num][1]]
        else:
            second_dot = second_dot_possible
            number = self.closest(second_dot, num)
            qas = sqrt((second_dot[0] - self.array[number][0]) ** 2 + (second_dot[1] - self.array[number][1]) ** 2)
            if qas <= self.ball_size // 2:
                alpha = acos(qas / (self.ball_size // 2))
                qas2 = (self.ball_size // 2) * sin(alpha) + (self.ball_size // 2)

                if deltax != 0:
                    if deltax < 0 and deltay >= 0:
                        second_dot = [second_dot[0] + qas2 * cos(atan(abs(k))), second_dot[1] - qas2 * sin(atan(abs(k))), -1, number]
                    elif deltax < 0 and deltay < 0:
                        second_dot = [second_dot[0] + qas2 * cos(atan(abs(k))), second_dot[1] + qas2 * sin(atan(abs(k))), -1, number]
                    elif deltax > 0 and deltay >= 0:
                        second_dot = [second_dot[0] - qas2 * cos(atan(abs(k))), second_dot[1] - qas2 * sin(atan(abs(k))), -1, number]
                    elif deltax > 0 and deltay < 0:
                        second_dot = [second_dot[0] - qas2 * cos(atan(abs(k))), second_dot[1] + qas2 * sin(atan(abs(k))), -1, number]
                else:
                    if deltay > 0:
                        second_dot = [second_dot[0], second_dot[1] - self.ball_size // 2, -1]
                    else:
                        second_dot = [second_dot[0], second_dot[1] + self.ball_size // 2, -1]
            else:
                second_dot = [second_dot_possible[0], second_dot_possible[1], -1]
        return second_dot


    def closest(self, posi, num):
        cur = sqrt(self.window_size[0] ** 2 + self.window_size[1] ** 2)
        cur_ = num
        for i in range(len(self.array)):
            if i == num:
                continue
            else:
                if self.array[i][3]:
                    if sqrt((posi[0] - self.array[i][0]) ** 2 + (posi[1] - self.array[i][1]) ** 2) < cur:
                        cur = sqrt((posi[0] - self.array[i][0]) ** 2 + (posi[1] - self.array[i][1]) ** 2)
                        cur_ = i
        return cur_

    def chousen(self, num):
        pressed = pygame.mouse.get_pressed()
        while not pressed[0]:
            # if pressed[2]:
            #     return
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # if i.type == pygame.MOUSEBUTTONDOWN:
                    # pressed = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            self.dr_table()
            pygame.draw.circle(self.screen, (225, 225, 0), [self.array[num][0], self.array[num][1]], 4 * self.ball_size, 5)
            deltax = - (pos[0] - self.array[num][0])
            deltay = - (pos[1] - self.array[num][1])
            if abs(deltay) + abs(deltax) != 0:
                sin_d = deltay / sqrt(pow(deltay, 2) + pow(deltax, 2))
                cos_d = deltax / sqrt(pow(deltay, 2) + pow(deltax, 2))
            first_dot = [self.array[num][0] + cos_d * self.ball_size // 2, self.array[num][1] + sin_d * self.ball_size // 2]
            if deltax == 0:
                k = 'x=0'
            elif deltay == 0:
                k = 'y=0'
            elif deltax != 0:
                k = deltay / deltax
            second_dot = self.find_perese(k, num, deltax, deltay)
            # print(second_dot)


            pygame.draw.aaline(self.screen, (0, 0, 255), first_dot, (second_dot[0], second_dot[1]))
            pygame.draw.circle(self.screen, (255, 255, 255), (second_dot[0], second_dot[1]), self.ball_size // 2, 2)
            pygame.display.flip()
            self.clock.tick(FPS)
            pressed = pygame.mouse.get_pressed()
            if pressed[1]:
                self.dr_table()
                pygame.display.flip()
                return
        # dot = pygame.mouse.get_pos()
            rast = sqrt((pos[0] - self.array[num][0]) ** 2 + (pos[1] - self.array[num][1]) ** 2)

            deltax_ = - (pos[0] - self.array[num][0])
            deltay_ = - (pos[1] - self.array[num][1])
            if rast >= 4 * self.ball_size:
                mul_ = 1
            else:
                mul_ = rast / (4 * self.ball_size)
            if deltay_ == 0:
                k_ = 0
            elif deltax_ == 0:
                k_ = 'x=0'
            else:
                k_ = abs(deltay_ / deltax_)
            print(second_dot)
            napr_ = [pow(-1, deltax_ < 0), pow(-1, deltay_ < 0)]
        # self.move(num, k_, mul_, napr_, deltax_, deltay_, second_dot, 0)
        race = 15 * self.ball_size * mul_
        match num + 1:
            case 1:
                self.b_1.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 2:
                self.b_2.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 3:
                self.b_3.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 4:
                self.b_4.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 5:
                self.b_5.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 6:
                self.b_6.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 7:
                self.b_7.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 8:
                self.b_8.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 9:
                self.b_9.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 10:
                self.b_10.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 11:
                self.b_11.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 12:
                self.b_12.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 13:
                self.b_13.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 14:
                self.b_14.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 15:
                self.b_15.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())
            case 16:
                self.b_16.moving(1, k_, race, napr_, deltax_, deltay_, second_dot, time.time())

# def moving(self, k_, race, napr_, deltax_, deltay_, second_dot):
#_________________________________________________________________________
    def new_k(self, second_dot_, k_, deltax_, deltay_, num, napr_, r, t):
        number = self.closest(second_dot_, num)
        deltax = self.array[number][0] - second_dot_[0]
        deltay = self.array[number][1] - second_dot_[1]
        if deltax != 0 and deltay != 0:
            if napr_[0] == 1 and napr_[1] == 1:
                k = deltay / deltax
                n = - 1 / k
                alpha = atan(k_ * napr_[0] * napr_[1])
                alphax = atan(n)
                x = alphax - alpha
                if n < 0:
                    if k <= k_:
                        napr_new_0 = [-1, 1]
                        print(11)
                    else:
                        napr_new_0 = [1, -1]
                        print(12)
                elif n > 0:
                    napr_new_0 = [1, 1]
                    print(13)
            elif napr_[0] == 1 and napr_[1] == -1:
                k = deltay / deltax
                n = - 1 / k
                alpha = atan(k_ * napr_[0] * napr_[1])
                alphax = atan(n)
                x = alphax - alpha
                if n > 0:
                    if abs(k) <= abs(k_):
                        napr_new_0 = [-1, -1]
                    else:
                        napr_new_0 = [1, 1]
                elif n < 0:
                    napr_new_0 = [1, -1]
            elif napr_[0] == -1 and napr_[1] == 1:
                k = deltay / deltax
                n = - 1 / k
                alpha = atan(k_ * napr_[0] * napr_[1])
                alphax = atan(n)
                x = alphax - alpha
                if n > 0:
                    if abs(k) <= abs(k_):
                        napr_new_0 = [1, 1]
                    else:
                        napr_new_0 = [-1, -1]
                elif n < 0:
                    napr_new_0 = [-1, 1]
            elif napr_[0] == -1 and napr_[1] == -1:
                k = deltay / deltax
                n = - 1 / k
                alpha = atan(k_ * napr_[0] * napr_[1])
                alphax = atan(n)
                x = alphax - alpha
                if n < 0:
                    if abs(k) <= abs(k_):
                        napr_new_0 = [1, -1]
                    else:
                        napr_new_0 = [-1, 1]
                elif n > 0:
                    napr_new_0 = [-1, -1]
            r0 = r * abs(sin(x))
            r1 = r * abs(cos(x))
            napr_new_1 = [pow(-1, deltax < 0), pow(-1, deltay < 0)]
            second_dot_new_0 = self.find_perese(n, num, napr_new_0[0], napr_new_0[1])
            second_dot_new_1 = self.find_perese(k, number, napr_new_1[0], napr_new_1[1])
            # def help1(self, num, move, k_, race, napr_, deltax_, deltay_, second_dot, t):
            self.help1(number, 1, abs(k), r1, napr_new_1, deltax, deltay, second_dot_new_1, time.time())
            # print(number, 1, k, r1, napr_new_1, deltax, deltay, second_dot_new_1, time.time())
            # print(second_dot_new_0, second_dot_new_1, k_, k, n, deltax, deltay)
            print([n, napr_new_0, napr_new_0[0], napr_new_0[1], second_dot_new_0, r0, t])
            return [abs(n), napr_new_0, napr_new_0[0], napr_new_0[1], second_dot_new_0, r0, t]
            # ['x=0', napr_, deltax_, deltay_, second_dot_, race, starting_time]
            #self.move(num, n, 4, napr_new_0, napr_new_0[0], napr_new_0[1], second_dot_new_0, 2, r * cos(abs(x)), t)
            #self.move(number, k, 4, napr_new_1, napr_new_1[0], napr_new_1[1], second_dot_new_1, 3, r * sin(abs(x)))
            # self.move2(num, n, napr_new_0, deltax, deltay, second_dot_new_0, r0, t, number, k, napr_new_1, deltax, deltay, second_dot_new_1, r1, 0)

        elif deltay == 0:
            if k_ == 0:
                napr_new_1 = [pow(-1, deltax < 0), pow(-1, deltay < 0)]
                second_dot_new_1 = self.find_perese('y=0', number, deltax, deltay)
                # self.help1()
                self.help1(number, 1, 0, r, napr_new_1, deltax, deltay, second_dot_new_1, time.time())
                return [0, 0, -0, -0, 0, 0, 0]
                # self.move(number, 0, 0, napr_new_0, deltax, deltay, second_dot_new_0, 1, r, time.time())
            else:
                napr_new_0 = [pow(-1, deltax > 0), pow(-1, deltay > 0)]
                napr_new_1 = [pow(-1, deltax < 0), pow(-1, deltay < 0)]
                second_dot_new_0 = self.find_perese('x=0', num, deltax, deltay)
                second_dot_new_1 = self.find_perese('y=0', number, deltax, deltay)
                x = atan(k_)
                r0 = r * abs(sin(x))
                r1 = r * abs(cos(x))
                self.help1(number, 1, 0, r1, napr_new_1, deltax, deltay, second_dot_new_1, time.time())
                return ['x=0', napr_new_0, -deltax, -deltay, second_dot_new_0, r0, t]
                # ['x=0', napr_, deltax_, deltay_, second_dot_, race, starting_time]
                # self.help1(number, 1, k, r1, napr_new_1, deltax, deltay, second_dot_new_1, time.time())
                # self.move2(num, 'x=0', napr_new_0, deltax, deltay, second_dot_new_0, r0, t, number, 0, napr_new_0, deltax, deltay, second_dot_new_1, r1, 0)
                # self.move(number, 'x=0', 0, napr_new_1, deltax, deltay, second_dot_new_1, 1, r, time.time())

        elif deltax == 0:
            if k_ == 'x=0':
                napr_new_1 = [pow(-1, deltax < 0), pow(-1, deltay < 0)]
                second_dot_new_1 = self.find_perese('x=0', number, deltax, deltay)
                self.help1(number, 1, k_, r, napr_new_1, deltax, deltay, second_dot_new_1, time.time())
                return [0, 0, -0, -0, 0, 0, 0]
            else:
                napr_new_1 = [pow(-1, deltax < 0), pow(-1, deltay < 0)]
                napr_new_0 = [pow(-1, deltax > 0), pow(-1, deltay > 0)]
                second_dot_new_0 = self.find_perese('y=0', num, deltax, deltay)
                second_dot_new_1 = self.find_perese('x=0', number, deltax, deltay)
                x = atan(k_)
                r0 = r * abs(sin(x))
                r1 = r * abs(cos(x))
                self.help1(number, 1, 'x=0', r1, napr_new_1, deltax, deltay, second_dot_new_1, time.time())
                return [0, napr_new_0, -deltax, -deltay, second_dot_new_0, r0, t]
                # self.move2(num, 'y=0', napr_new_0, deltax, deltay, second_dot_new_0, r0, t, number, 'x=0', napr_new_0, deltax, deltay, second_dot_new_1, r1, 0)


#     def move2(self, num0, k0, napr0, dx0, dy0, second_0, r0, t0_, num1, k1, napr1, dx1, dy1, second_1, r1, t1_):
#         g = 10
#         mu = 0.25
#         race0 = r0
#         race1 = r1
#         t0 = t0_
#         if t1_ == 0:
#             t1 = time.time()
#         else:
#             t1 = time.time() - t1_
#         if k0 == 'y=0' and k1 == 'x=0':
#             while race0 > 0 or race1 > 0:
#                 self.change(num0, napr0, race0, k0, 0)
#                 self.change(num1, napr1, race1, k1, 1)
#                 race0 = race0 - (time.time() - t0) / 120 * mu * g
#                 race1 = race1 - (time.time() - t1) / 120 * mu * g
#                 if race0 < 0:
#                     race0 = 0
#                 if race1 < 0:
#                     race1 = 0
#                 self.dr_table()
#                 # print(self.array[num])
#                 if abs(self.array[num0][0] - second_0[0]) <= 5 and abs(self.array[num0][1] - second_0[1]) <= 5:
#                     print(33333333333333333333)
#                     if second_0[2] == 0:
#                         second_dor_new = self.find_perese(pow(-1, dx0 * dy0 > 0) * k0, num0, dx0, -dy0)
#                         napr_new = [napr0[0], -napr0[1]]
#                     #     # self.move(num, k_, mul_, napr_new, deltax_, -deltay_, second_dor_new, 1, race, starting_time)
#                     #     self.move2(num, 'y=0', napr_new_0, deltax, deltay, second_dot_new_0, r0, t, number, 'x=0',
#                     #                napr_new_0,
#                     #                deltax, deltay, second_dot_new_1, r1, 0)
#                     # elif second_dot_[2] == 1:
#                     #     second_dor_new = self.find_perese(pow(-1, deltax_ * deltay_ > 0) * k_, num, -deltax_, deltay_)
#                     #     napr_new = [-napr_[0], napr_[1]]
#                     #     self.move(num, k_, mul_, napr_new, -deltax_, deltay_, second_dor_new, 1, race, starting_time)
#                     # elif second_dot_[2] == 2:
#                     #     second_dor_new = self.find_perese(pow(-1, deltax_ * deltay_ > 0) * k_, num, deltax_, -deltay_)
#                     #     napr_new = [napr_[0], -napr_[1]]
#                     #     self.move(num, k_, mul_, napr_new, deltax_, -deltay_, second_dor_new, 1, race, starting_time)
#                     # elif second_dot_[2] == 3:
#                     #     second_dor_new = self.find_perese(pow(-1, deltax_ * deltay_ > 0) * k_, num, -deltax_, deltay_)
#                     #     napr_new = [-napr_[0], napr_[1]]
#                     #     self.move(num, k_, mul_, napr_new, -deltax_, deltay_, second_dor_new, 1, race, starting_time)
#                     # elif second_dot_[2] == -1:
#                     #     self.new_k(second_dot_, k_, deltax_, deltay_, num, napr_, race, starting_time)
#
# #_______________________________________________________________________________________________________________________
    def change(self, num, napr_, race, k_, t):
        if t == 0:
            match num + 1:
                case 1:
                    self.b_1.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 2:
                    self.b_2.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 3:
                    self.b_3.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 4:
                    self.b_4.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 5:
                    self.b_5.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 6:
                    self.b_6.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 7:
                    self.b_7.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 8:
                    self.b_8.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 9:
                    self.b_9.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                    self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 10:
                    self.b_10.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                     self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 11:
                    self.b_11.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                     self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 12:
                    self.b_12.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                     self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 13:
                    self.b_13.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                     self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 14:
                    self.b_14.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                     self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 15:
                    self.b_15.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                     self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
                case 16:
                    self.b_16.koo_in(self.array[num][0] + napr_[0] * race * cos(atan(k_)) / 120,
                                     self.array[num][1] + napr_[1] * race * sin(atan(k_)) / 120)
        else:
            match num + 1:
                case 1:
                    self.b_1.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 2:
                    self.b_2.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 3:
                    self.b_3.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 4:
                    self.b_4.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 5:
                    self.b_5.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 6:
                    self.b_6.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 7:
                    self.b_7.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 8:
                    self.b_8.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 9:
                    self.b_9.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                    self.array[num][1] + napr_[1] * race * 1 / 120)
                case 10:
                    self.b_10.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                     self.array[num][1] + napr_[1] * race * 1 / 120)
                case 11:
                    self.b_11.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                     self.array[num][1] + napr_[1] * race * 1 / 120)
                case 12:
                    self.b_12.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                     self.array[num][1] + napr_[1] * race * 1 / 120)
                case 13:
                    self.b_13.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                     self.array[num][1] + napr_[1] * race * 1 / 120)
                case 14:
                    self.b_14.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                     self.array[num][1] + napr_[1] * race * 1 / 120)
                case 15:
                    self.b_15.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                     self.array[num][1] + napr_[1] * race * 1 / 120)
                case 16:
                    self.b_16.koo_in(self.array[num][0] + napr_[0] * race * 0 / 120,
                                     self.array[num][1] + napr_[1] * race * 1 / 120)
    # def helf_r(self, num, ):


    def move(self, num, race, k_, napr_, deltax_, deltay_, second_dot_, st_time=0):
        # print(second_dot_)
        mu = 0.25
        g = 9.8
        # if type == 0:
        #     starting_race = 20 * self.ball_size * mul_ # starting race = 15 m/c
        #     starting_time = time.time()
        # elif type == 1:
        #     starting_race = st_r
        #     starting_time = st_time
        # race = starting_race
        # print(starting_race)
        starting_time = st_time
        # def moving(self, move, k_, race, napr_, deltax_, deltay_, second_dot, t):
        if k_ != 'x=0':
            while race > 0:
                self.change(num, napr_, race, k_, 0)
                race = race - (time.time() - starting_time) / 120 * mu * g
                # self.dr_table()
                # print(self.array[num])
                if abs(self.array[num][0] - second_dot_[0]) <= 3 and abs(self.array[num][1] - second_dot_[1]) <= 3:
                    print(33333333333333333333)
                    if second_dot_[2] == 0:
                        if second_dot_[0] <= self.table_size[3] + self.ball_size or second_dot_[0] >= self.table_size[1] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese(pow(-1, deltax_ * deltay_ > 0) * k_, num, deltax_, -deltay_)
                        napr_new = [napr_[0], -napr_[1]]
                        return [k_, napr_new, deltax_, -deltay_, second_dot_new, race, starting_time]
                        # self.move(num, k_, mul_, napr_new, deltax_, -deltay_, second_dor_new, 1, race, starting_time)
                    elif second_dot_[2] == 1:
                        if second_dot_[1] <= self.table_size[0] + self.ball_size or second_dot_[1] >= self.table_size[2] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese(pow(-1, deltax_ * deltay_ > 0) * k_, num, -deltax_, deltay_)
                        napr_new = [-napr_[0], napr_[1]]
                        return [k_, napr_new, -deltax_, deltay_, second_dot_new, race, starting_time]
                        # self.move(num, k_, mul_, napr_new, -deltax_, deltay_, second_dor_new, 1, race, starting_time)
                    elif second_dot_[2] == 2:
                        if second_dot_[0] <= self.table_size[3] + self.ball_size or second_dot_[0] >= self.table_size[1] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese(pow(-1, deltax_ * deltay_ > 0) * k_, num, deltax_, -deltay_)
                        napr_new = [napr_[0], -napr_[1]]
                        return [k_, napr_new, deltax_, -deltay_, second_dot_new, race, starting_time]
                        # self.move(num, k_, mul_, napr_new, deltax_, -deltay_, second_dor_new, 1, race, starting_time)
                    elif second_dot_[2] == 3:
                        if second_dot_[1] <= self.table_size[0] + self.ball_size or second_dot_[1] >= self.table_size[2] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese(pow(-1, deltax_ * deltay_ > 0) * k_, num, -deltax_, deltay_)
                        napr_new = [-napr_[0], napr_[1]]
                        return [k_, napr_new, -deltax_, deltay_, second_dot_new, race, starting_time]
                        # self.move(num, k_, mul_, napr_new, -deltax_, deltay_, second_dor_new, 1, race, starting_time)
                    elif second_dot_[2] == -1:
                        return self.new_k(second_dot_, k_, deltax_, deltay_, num, napr_, race, starting_time)
                    break
                    return
                return [k_, napr_, deltax_, deltay_, second_dot_, race, starting_time]
        elif k_ == 'x=0':
            while race > 0:
                self.change(num, napr_, race, k_, 1)
                race = race - (time.time() - starting_time) / 120 * mu * g
                # self.dr_table()
                if abs(self.array[num][0] - second_dot_[0]) <= 5 and abs(self.array[num][1] - second_dot_[1]) <= 5:
                    if second_dot_[2] == 0:
                        if second_dot_[0] <= self.table_size[3] + self.ball_size or second_dot_[0] >= self.table_size[1] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese('x=0', num, deltax_, -deltay_)
                        napr_new = [napr_[0], -napr_[1]]
                        return ['x=0', napr_new, deltax_, -deltay_, second_dot_new, race, starting_time]
                        # self.move(num, 'x=0', mul_, napr_new, deltax_, -deltay_, second_dor_new, 1, race, starting_time)
                    elif second_dot_[2] == 1:
                        if second_dot_[1] <= self.table_size[0] + self.ball_size or second_dot_[1] >= self.table_size[2] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese('x=0', num, -deltax_, deltay_)
                        napr_new = [-napr_[0], napr_[1]]
                        return ['x=0', napr_new, -deltax_, deltay_, second_dot_new, race, starting_time]
                        # self.move(num, 'x=0', mul_, napr_new, -deltax_, deltay_, second_dor_new, 1, race, starting_time)
                    elif second_dot_[2] == 2:
                        if second_dot_[0] <= self.table_size[3] + self.ball_size or second_dot_[0] >= self.table_size[1] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese('x=0', num, deltax_, -deltay_)
                        napr_new = [napr_[0], -napr_[1]]
                        return ['x=0', napr_new, deltax_, -deltay_, second_dot_new, race, starting_time]
                        # self.move(num, 'x=0', mul_, napr_new, deltax_, -deltay_, second_dor_new, 1, race, starting_time)
                    elif second_dot_[2] == 3:
                        if second_dot_[1] <= self.table_size[0] + self.ball_size or second_dot_[1] >= self.table_size[2] - self.ball_size:
                            self.help2(num)
                            return [0, 0, 0, 0, 0, 0, 0]
                        second_dot_new = self.find_perese('x=0', num, -deltax_, deltay_)
                        napr_new = [-napr_[0], napr_[1]]
                        return ['x=0', napr_new, -deltax_, deltay_, second_dot_new, race, starting_time]
                        # self.move(num, 'x=0', mul_, napr_new, -deltax_, deltay_, second_dot_new, 1, race, starting_time)
                    elif second_dot_[2] == -1:
                        return self.new_k(second_dot_, 'x=0', deltax_, deltay_, num, napr_, race, starting_time)
                    break
                    return
                return ['x=0', napr_, deltax_, deltay_, second_dot_, race, starting_time]


    def game(self):
        while 1:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    pressed = pygame.mouse.get_pressed()
                    pos = pygame.mouse.get_pos()
                    if pressed[2]:
                        for i in range(1, 17):
                            elem = self.array[i - 1]
                            if abs(elem[0]) + abs(elem[1]) == 0:
                                continue
                            else:
                                if pos[0] <= elem[0] + self.ball_size // 2 and elem[0] - self.ball_size // 2 <= pos[0] and pos[1] <= elem[1] + self.ball_size // 2 and elem[1] - self.ball_size // 2 <= pos[1]:
                                    self.chousen(i - 1)
            self.dr_table()
                                    # while not pressed[0]:

                                    # xelem = elem[0] + random.randint(-100, 100)
                                    # yelem = elem[1] + random.randint(-100, 100)
                                    # match i:
                                    #     case 1:
                                    #         self.b_1.koo_in(xelem, yelem)
                                    #     case 2:
                                    #         self.b_2.koo_in(xelem, yelem)
                                    #     case 3:
                                    #         self.b_3.koo_in(xelem, yelem)
                                    #     case 4:
                                    #         self.b_4.koo_in(xelem, yelem)
                                    #     case 5:
                                    #         self.b_5.koo_in(xelem, yelem)
                                    #     case 6:
                                    #         self.b_6.koo_in(xelem, yelem)
                                    #     case 7:
                                    #         self.b_7.koo_in(xelem, yelem)
                                    #     case 8:
                                    #         self.b_8.koo_in(xelem, yelem)
                                    #     case 9:
                                    #         self.b_9.koo_in(xelem, yelem)
                                    #     case 10:
                                    #         self.b_10.koo_in(xelem, yelem)
                                    #     case 11:
                                    #         self.b_11.koo_in(xelem, yelem)
                                    #     case 12:
                                    #         self.b_12.koo_in(xelem, yelem)
                                    #     case 13:
                                    #         self.b_13.koo_in(xelem, yelem)
                                    #     case 14:
                                    #         self.b_14.koo_in(xelem, yelem)
                                    #     case 15:
                                    #         self.b_15.koo_in(xelem, yelem)
                                    #     case 16:
                                    #         self.b_16.koo_in(xelem, yelem)
                                    # self.dr_table()

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

    # def moving(self, move, k_, race, napr_, deltax_, deltay_, second_dot, t):
    def help1(self, num, move, k_, race, napr_, deltax_, deltay_, second_dot, t):
        match num + 1:
            case 1:
                self.b_1.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 2:
                self.b_2.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 3:
                self.b_3.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 4:
                self.b_4.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 5:
                self.b_5.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 6:
                self.b_6.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 7:
                self.b_7.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 8:
                self.b_8.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 9:
                self.b_9.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 10:
                self.b_10.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 11:
                self.b_11.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 12:
                self.b_12.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 13:
                self.b_13.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 14:
                self.b_14.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 15:
                self.b_15.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)
            case 16:
                self.b_16.moving(move, k_, race, napr_, deltax_, deltay_, second_dot, t)

    def help2(self, num):
        match num + 1:
            case 1:
                self.b_1.koo_in(0,0)
                self.b_1.end()
            case 2:
                self.b_2.koo_in(0, 0)
                self.b_2.end()
            case 3:
                self.b_3.koo_in(0, 0)
                self.b_3.end()
            case 4:
                self.b_4.koo_in(0, 0)
                self.b_4.end()
            case 5:
                self.b_5.koo_in(0, 0)
                self.b_5.end()
            case 6:
                self.b_6.koo_in(0, 0)
                self.b_6.end()
            case 7:
                self.b_7.koo_in(0, 0)
                self.b_7.end()
            case 8:
                self.b_8.koo_in(0, 0)
                self.b_8.end()
            case 9:
                self.b_9.koo_in(0, 0)
                self.b_9.end()
            case 10:
                self.b_10.koo_in(0, 0)
                self.b_10.end()
            case 11:
                self.b_11.koo_in(0, 0)
                self.b_11.end()
            case 12:
                self.b_12.koo_in(0, 0)
                self.b_12.end()
            case 13:
                self.b_13.koo_in(0, 0)
                self.b_13.end()
            case 14:
                self.b_14.koo_in(0, 0)
                self.b_14.end()
            case 15:
                self.b_15.koo_in(0, 0)
                self.b_15.end()
            case 16:
                self.b_16.koo_in(0, 0)
                self.b_16.end()

    def dr_table(self):
        background_color = (0, 0, 255)  # синий

        # заполняем фон заданным цветом
        screen.fill(background_color)
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
            self.table_size = [ 2.5 * (sq // 8), e + sq // 8 + 6 * (sq // 8) , 2.5 * (sq // 8) + 3 * (sq // 8), e + sq // 8]
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
            # pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8, e + 2.5 * (sq // 8)), self.ball_size + 4)
            pygame.draw.circle(self.screen, (12, 186, 22),
                               (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8)), self.ball_size + 10)
            # pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8)), self.ball_size + 4)
            pygame.draw.circle(self.screen, (12, 186, 22),
                               (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 10)
            # pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 4)
            pygame.draw.circle(self.screen, (12, 186, 22),
                               (sq // 8, e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 10)
            # pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8, e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 4)

            pygame.draw.rect(self.screen, (0, 255, 0), (sq // 8, e + 2.5 * (sq // 8), 6 * (sq // 8), 3 * (sq // 8)))

            # pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8, e + 2.5 * (sq // 8)), self.ball_size + 4)
            # pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8)),
            #                    self.ball_size + 4)
            # pygame.draw.circle(self.screen, (120, 120, 10),
            #                    (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size + 4)
            # pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8, e + 2.5 * (sq // 8) + 3 * (sq // 8)),
            #                    self.ball_size + 4)
            pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8, e + 2.5 * (sq // 8)), self.ball_size)
            pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8)),
                               self.ball_size)
            pygame.draw.circle(self.screen, (120, 120, 10),
                               (sq // 8 + 6 * (sq // 8), e + 2.5 * (sq // 8) + 3 * (sq // 8)), self.ball_size)
            pygame.draw.circle(self.screen, (120, 120, 10), (sq // 8, e + 2.5 * (sq // 8) + 3 * (sq // 8)),
                               self.ball_size)
            self.table_size = [e + 2.5 * (sq // 8), sq // 8 + 6 * (sq // 8) , e + 2.5 * (sq // 8) + 3 * (sq // 8),
                               (sq // 8)]
        self.array = self.comm_ball()
        self.score = 16 - len([x for x in self.array if x[3] == 1])
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(f'SCORE:{self.score}', True, (180, 0, 0))
        self.screen.blit(text1, (10, 50))
        for i in range(len(self.array)):
            # print('__-__', self.array[15])
            if self.array[i][4] == 1:
                if self.array[i][8] <= 0:
                    # self.array[i][4] = 0
                    self.help1(i, 0,0,0,0,0,0,0,0)
                    # def moving(self, move, k_, race, napr_, deltax_, deltay_, second_dot, t):
                else:
                    w = self.move(i, self.array[i][8], self.array[i][5],  self.array[i][6], self.array[i][9], self.array[i][10], self.array[i][7], self.array[i][11])
                    self.help1(i, 1, w[0], w[5], w[1], w[2], w[3], w[4], w[6])
                    # ['x=0', napr_, deltax_, deltay_, second_dot_, race, starting_time]
        #             ['x=0', napr_, deltax_, deltay_, second_dot_, race, starting_time]
        #  def help1(self, num, move, k_, race, napr_, deltax_, deltay_, second_dot, t):
        #     def move(self, num, k_, mul_, napr_, deltax_, deltay_, second_dot_, type, st_r=0, st_time=0):
        pygame.display.flip()
        self.clock.tick(FPS)

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
        self.move = 0
        self.k = None
        self.ar = [0, 0]
        self.second = [0, 0]
        self.race = 0
        self.deltax = 0
        self.deltay = 0
        self.time = 0
        # self.move()

    def koo(self):
        if self.state:
            return (self.x, self.y, self.color, self.state, self.move, self.k, self.ar, self.second, self.race, self.deltax, self.deltay, self.time)
        else:
            return (0,0, self.color, 0, 0, self.k, self.ar, self.second, self.race, self.deltax, self.deltay, self.time)

    def koo_in(self, x, y):
        self.x = x
        self.y = y

    def moving(self, move, k_, race, napr_, deltax_, deltay_, second_dot, t):
        self.move = move
        self.k = k_
        self.race = race
        self.ar = napr_
        self.deltax = deltax_
        self.deltay = deltay_
        self.second = second_dot
        self.time = t

    def end(self):
        self.state = False


# self.move(num, k_, mul_, napr_, deltax_, deltay_, second_dot, 0)


if __name__ == '__main__':
    pygame.init()
    window_size = (700, 700)
    pygame.display.set_caption("Бильярдный стол")
    screen = pygame.display.set_mode(window_size)
    # background_color = (0, 0, 255)  # синий
    #
    # # заполняем фон заданным цветом
    # screen.fill(background_color)
    sq = min(window_size[0], window_size[1])
    ball_size = (6 * (sq // 8)) // 52

    table = Table(window_size, screen)
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             exit()