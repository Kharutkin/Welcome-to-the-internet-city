### Repository name: “Welcome-to-the-internet-city”

Nowadays, providing high-quality Internet to all corners of the city is becoming increasingly important. Especially when
it comes to residential areas, where every home or building must be connected to the Internet.

The purpose of this repository is to develop a program in Python for the optimal distribution of Internet towers
throughout the city. The developed program will generate a city in the form of a chessboard, and then arrange Internet
towers in such a way as to provide a signal to every building in the city.

In addition, the program will visualize the location of Internet towers on a city map and display the signal level from
each tower, which will allow you to clearly assess the quality of Internet coverage.

This project is of interest not only to IT specialists, but also to anyone interested in programming and software
development in Python.

### Main functions:

1. Generation of a city in the form of a chessboard with a given size.

2. Creation and placement of buildings on the city board.

3. Arrangement of Internet towers in such a way that every point of the city is covered by a signal.

4. Visualization of the location of Internet towers and display of the signal level from each of them.

### Internet tower distribution algorithm

When developing an algorithm for allocating Internet towers, I was faced with the need to create an efficient algorithm
without using a large number of nested loops, since this can significantly reduce the performance of the program. After
a thorough analysis of the problem, I decided to use the A* algorithm, which is an optimal algorithm for finding a path
in a graph. This algorithm allowed me to distribute towers throughout the city in such a way as to cover all buildings
with a signal.

### Visualization

When creating the visualization, I used the matplotlib library, which allows you to create beautiful graphs and charts.
However, I needed to render it in 3D space, which required some extra effort on my part. I spent some time exploring the
capabilities of matplotlib and writing code that allows me to plot houses as parallelepipeds and towers as pyramids. As
a result, I got a beautiful and clear visualization of the distribution of Internet towers in the city.

### Usage

The program runs by executing the main.py file. This file contains all the necessary information to run the program,
including city generation parameters, number of buildings and Internet towers, and visualization parameters. To run the
program, you need to open a terminal, go to the folder with the main.py file and run the following command:

```
python main.py
```

After launching the program, a window with a map of the city will appear on the screen, on which Internet towers will be
located and the signal level from each of them will be displayed.
