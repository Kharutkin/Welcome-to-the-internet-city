from random import randint
import numpy as np


class CityGrid:
    def __init__(self, width, length, percentage_of_occurrence_of_blocked_blocks):
        self.we_need_signal = {}
        self.we_need_tower = {}
        for i in range(length):
            for j in range(width):
                self.we_need_signal[(i, j)] = True
        for i in range(length):
            for j in range(width):
                self.we_need_tower[(i, j)] = 0
        self.grid = [[(True, 0)] * width for _ in range(length)]
        self.tower_map = [[0] * width for _ in range(length)]
        self.signal_map = []
        self.width = width
        self.length = length
        self.signal_map = []
        self.tower_connectivity = {}
        count_of_blocked_blocks = width * length * percentage_of_occurrence_of_blocked_blocks // 100
        count_of_blocked_blocks += [0, 1][width * length * percentage_of_occurrence_of_blocked_blocks / 100 % 1 >= 0.5]
        self.add_block_blocks(count_of_blocked_blocks, width, length)

    def display_blocked_tower(self):
        for i in self.grid:
            for j in i:
                print([1, 0][j[0]], end='  ')
            print()

    def create_signal_map(self):
        self.signal_map = [[0] * self.width for _ in range(self.length)]
        for i in range(self.length):
            for j in range(self.width):
                if self.tower_map[i][j]:
                    for k in range(i - self.tower_map[i][j], i + self.tower_map[i][j] + 1):
                        for b in range(j - self.tower_map[i][j], j + self.tower_map[i][j] + 1):
                            if 0 <= k < self.length and 0 <= b < self.width:
                                self.signal_map[k][b] += 1

    def create_tower_connectivity(self, r):
        for i in range(self.length):
            for j in range(self.width):
                if self.tower_map[i][j]:
                    for k in range(i - r, i + r + 1):
                        for b in range(j - r, j + r + 1):
                            if (0 <= k < self.length and 0 <= b < self.width) and ((i != k) or (j != b)):
                                if self.tower_map[k][b]:
                                    if self.tower_map[i][j] in self.tower_connectivity:
                                        self.tower_connectivity[self.tower_map[i][j]].append(self.tower_map[k][b])
                                    else:
                                        self.tower_connectivity[self.tower_map[i][j]] = [self.tower_map[k][b]]

    def display_signal_map(self):
        for i in self.signal_map:
            for j in i:
                print(j, end=' ')
            print()

    def display_tower_map(self):
        for i in self.tower_map:
            print(*i)
        print()

    def add_block_blocks(self, count_of_blocked_blocks, width, length):
        current_count = 0
        while current_count < count_of_blocked_blocks:
            cor_a, cor_b = randint(0, length - 1), randint(0, width - 1)
            if self.grid[cor_a][cor_b][0]:
                self.grid[cor_a][cor_b] = (False, 0)
                current_count += 1

    def add_tower(self, cor_a, cor_b, r):
        if self.grid[cor_a][cor_b][0]:
            self.tower_map[cor_a][cor_b] = r
            for i in range(cor_a - r, cor_a + r + 1):
                for j in range(cor_b - r, cor_b + r + 1):
                    if 0 <= j < self.width and 0 <= i < self.length:
                        tower, value = self.grid[i][j]
                        self.grid[i][j] = (tower, value - 1)
                        self.we_need_signal[(i, j)] = False
                        self.we_need_tower[(i, j)] += 1

    def welcome_to_internet_city(self, r=2):
        self.find_space(r)

    def find_space(self, r):
        if isinstance(r, int):
            s = (2 * r + 1) ** 2
            for k in range(s, 0, -1):
                for i in range(r - 1, self.length - r + 1):
                    for j in range(r - 1, self.width - r + 1):
                        if self.check_cor(i, j, r) == k and self.grid[i][j][0]:
                            self.add_tower(i, j, r)
        if isinstance(r, list):
            s_list = []
            for i in r:
                s_list.append((2 * i + 1) ** 2)
            s_list.append(0)
            r.append(0)
            r.sort(reverse=True)
            s_list.sort(reverse=True)
            for s in range(len(s_list) - 1):
                for k in range(s_list[s], s_list[s + 1], -1):
                    for i in range(r[s] - 1, self.length - r[s] + 1):
                        for j in range(r[s] - 1, self.width - r[s] + 1):
                            if self.check_cor(i, j, r[s]) == k and self.grid[i][j][0]:
                                self.add_tower(i, j, r[s])

    def check_cor(self, x, y, r):
        count_without_signal = 0
        for i in range(x - r, x + r + 1):
            for j in range(y - r, y + r + 1):
                if (i, j) in self.we_need_signal:
                    if self.we_need_signal[(i, j)]:
                        count_without_signal += 1
        return count_without_signal

    def tower_numbering(self):
        number = 1
        for i in range(self.length):
            for j in range(self.width):
                if self.tower_map[i][j]:
                    self.tower_map[i][j] = number
                    number += 1
        return number - 1

    def find_a_communication_channel(self, tower1, tower2):
        return self.__find_next(tower1, tower2, str(tower1))

    def __find_next(self, tower1, tower2, towers):
        if tower1 == tower2:
            return towers
        for i in self.tower_connectivity[tower1]:
            if str(i) in towers:
                continue
            else:
                towers += f' {str(i)}'
                return self.__find_next(i, tower2, towers)
        else:
            return "towers can't communicate((("
