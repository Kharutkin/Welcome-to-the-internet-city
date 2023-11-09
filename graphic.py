import numpy as np
import matplotlib.pyplot as plt
from objects import CityGrid
from objects_2 import CityGrid_2
from random import randint


def create_building(cor_x, cor_y, ax_3d):
    height = randint(1, 5)
    x = np.arange(cor_x + 0.1, cor_x + 1, 0.1)
    y = np.arange(cor_y + 0.1, cor_y + 1, 0.1)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = xgrid // xgrid * height
    ax_3d.plot_surface(xgrid, ygrid, zgrid, color='#c6ccd8', edgecolor='#c6ccd8')

    x = np.arange(cor_x + 0.1, cor_x + 1, 0.1)
    z = np.arange(0, height + 1, 1)
    xgrid, zgrid = np.meshgrid(x, z)
    ygrid = (xgrid // xgrid) * (cor_y + 0.1)
    ax_3d.plot_surface(xgrid, ygrid, zgrid, color='#274b69', edgecolor='#274b69')

    z = np.arange(0, height + 1, 1)
    y = np.arange(cor_y + 0.1, cor_y + 1, 0.1)
    zgrid, ygrid = np.meshgrid(z, y)
    xgrid = (ygrid // ygrid) * (cor_x + 0.9)
    ax_3d.plot_surface(xgrid, ygrid, zgrid, color='#85a1c1', edgecolor='#85a1c1')


def create_tower(cor_x, cor_y, ax_3d, color='#9A4D53'):
    x = np.arange(cor_x, cor_x + 1.1, 0.1)
    y = np.arange(cor_y, cor_y + 1.1, 0.1)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = (((abs((xgrid - cor_x - 0.5) * (ygrid - cor_y - 0.5)) * (-50)) + 7) ** 0.5) ** 2
    ax_3d.plot_surface(xgrid, ygrid, zgrid, color=color, edgecolor=color)


def create_signal(cor_x, cor_y, ax_3d, r, delta=0):
    x = np.arange(cor_x - r - 1, cor_x + r + 1, 1)
    y = np.arange(cor_y - r - 1, cor_y + r + 1, 1)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = ((xgrid + 10) // (xgrid + 10)) * 10 + delta
    ax_3d.plot_surface(xgrid, ygrid, zgrid, color='g', edgecolor='g')


def create_blocked_block(cor_x, cor_y, ax_3d):
    x = np.arange(cor_x, cor_x + 2, 1)
    y = np.arange(cor_y, cor_y + 2, 1)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = ((xgrid + 10) // (xgrid + 10)) - 1
    ax_3d.plot_surface(xgrid, ygrid, zgrid, color='#9A4D53', edgecolor='#9A4D53')


def show_city(length, width, percentage_of_occurrence_of_blocked_blocks=30, tower_operating_radius=2):
    city = CityGrid(length, width, percentage_of_occurrence_of_blocked_blocks)
    city.welcome_to_internet_city(tower_operating_radius)
    fig1 = plt.figure(figsize=(city.length, city.width))
    ax_3d = fig1.add_subplot(projection='3d')

    for i in range(city.length):
        for j in range(city.width):
            if city.tower_map[i][j]:
                create_tower(i, j, ax_3d)
            else:
                create_building(i, j, ax_3d)

    ax_3d.set_xlabel("x")
    ax_3d.set_ylabel("y")
    ax_3d.set_zlabel('z')
    plt.show()


def show_towers_and_signal(length, width, percentage_of_occurrence_of_blocked_blocks=30, tower_operating_radius=2):
    city = CityGrid(length, width, percentage_of_occurrence_of_blocked_blocks)
    city.welcome_to_internet_city(tower_operating_radius)
    fig1 = plt.figure(figsize=(city.length, city.width))
    ax_3d = fig1.add_subplot(projection='3d')

    for i in range(city.length):
        for j in range(city.width):
            if city.tower_map[i][j]:
                create_tower(i, j, ax_3d, color='g')
                create_signal(i, j, ax_3d, city.tower_map[i][j])
            if not city.grid[i][j][0]:
                create_blocked_block(i, j, ax_3d)

    city.display_tower_map()
    city.create_signal_map()
    print('-' * 20)
    city.display_signal_map()

    ax_3d.set_xlabel("x")
    ax_3d.set_ylabel("y")
    ax_3d.set_zlabel('z')
    plt.show()


def i_wanted_path(length, width, path, percentage_of_occurrence_of_blocked_blocks=30, tower_operating_radius=2):
    city = CityGrid_2(length, width, percentage_of_occurrence_of_blocked_blocks)
    city.welcome_to_internet_city_2(tower_operating_radius)

    last_tower = city.tower_numbering()

    if last_tower < path[0] or last_tower < path[1]:
        raise ValueError(f"One of the towers that you entered is not assigned such a number."
                         f" with your city size, the towers take values from 1 to {last_tower}")

    fig1 = plt.figure(figsize=(city.length, city.width))
    ax_3d = fig1.add_subplot(projection='3d')
    delta = 0

    for i in range(city.length):
        for j in range(city.width):
            if city.tower_map[i][j]:
                create_tower(i, j, ax_3d, color='g')
                create_signal(i, j, ax_3d, tower_operating_radius, delta)
                delta += 0.1
            if not city.grid[i][j][0]:
                create_blocked_block(i, j, ax_3d)

    city.create_tower_connectivity(tower_operating_radius)
    print(city.find_a_communication_channel(path[0], path[1]))

    ax_3d.set_xlabel("x")
    ax_3d.set_ylabel("y")
    ax_3d.set_zlabel('z')
    plt.show()
