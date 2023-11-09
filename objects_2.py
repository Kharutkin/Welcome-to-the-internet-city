from objects import *


class CityGrid_2(CityGrid):
    def welcome_to_internet_city_2(self, r=2):
        for i in range(1, 4):
            self.find_space_2(r, i)

    def find_space_2(self, r, iter):
        s = (2 * r + 1) ** 2
        for k in range(s, 0, -1):
            for i in range(self.length):
                for j in range(self.width):
                    if self.check_cor_2(i, j, r, iter) == k and self.grid[i][j][0] and self.tower_map[i][j] != 1:
                        self.add_tower(i, j, r)

    def check_cor_2(self, x, y, r, iter):
        count_without_signal = 0
        for i in range(x - r, x + r + 1):
            for j in range(y - r, y + r + 1):
                if (i, j) in self.we_need_signal:
                    if self.we_need_tower[(i, j)] < iter:
                        count_without_signal += 1
        return count_without_signal
