# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: Wei Wei
# ID: 30154758
# Date: 2021/10/09
# Description:

import math
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
TOTAL_COLORS = 3
RED_MODULUS = 1
BLUE_MODULUS = 2
GREEN_MODULUS = 0
HALF_OF_TICK = 5
ZERO = 0
LABEL_FROM_AXIS = 20
AXIS_COLOR = "black"


def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    # calculates modulus using equation counter and total colours
    modulus = equation_counter % TOTAL_COLORS
    # returns alternate colors based on value of modulus
    if modulus == RED_MODULUS:
        return "red"
    if modulus == BLUE_MODULUS:
        return "blue"
    if modulus == GREEN_MODULUS:
        return "green"


def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    # calculates screen x and screen y and returns those values
    screen_x = x_origin + (x * ratio)
    screen_y = y_origin + (y * ratio)
    return screen_x, screen_y


def calculate_min_value(origin, ratio):
    min_value = int(math.floor(-origin/ratio))
    return min_value


def calculate_max_value(origin, ratio):
    max_value = int(math.ceil(origin/ratio))
    return max_value


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    # calculates min and max values and returns them for x axis
    max_x_value = calculate_max_value(x_origin, ratio)
    min_x_value = calculate_min_value(x_origin, ratio)
    return min_x_value, max_x_value


def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    # calculates min and max values and returns them for y axis
    max_y_value = calculate_max_value(y_origin, ratio)
    min_y_value = calculate_min_value(y_origin, ratio)
    return min_y_value, max_y_value


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """
    pointer.penup()
    pointer.goto(screen_x1, screen_y1)
    pointer.pendown()
    pointer.goto(screen_x2, screen_y2)
    pointer.penup()


def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    # defines start and end of tick
    screen_y1 = screen_y + HALF_OF_TICK
    screen_y2 = screen_y - HALF_OF_TICK
    # draws tick on x-axis
    draw_line(pointer, screen_x, screen_y1, screen_x, screen_y2)


def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    references:
    1)writing on screen in turtle https://stackoverflow.com/questions/15141031/python-turtle-draw-text-with-on-screen-with-larger-font
    2) align text to centre in turtle https://stackoverflow.com/questions/42265682/how-to-center-text-using-turtle-module-in-python
    """
    # this goes to specified x and y location and writes text below the x axis
    pointer.penup()
    pointer.goto(screen_x, screen_y-LABEL_FROM_AXIS)
    pointer.write(label_text, align="center")


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    # defines start and end of tick
    screen_x1 = screen_x - HALF_OF_TICK
    screen_x2 = screen_x + HALF_OF_TICK
    # draws tick on y-axis
    draw_line(pointer, screen_x1, screen_y, screen_x2, screen_y)


def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    references:
    1)writing on screen in turtle https://stackoverflow.com/questions/15141031/python-turtle-draw-text-with-on-screen-with-larger-font
    """
    # this goes to specified x and y location and writes text on the left side of y axis.
    pointer.penup()
    pointer.goto(screen_x - LABEL_FROM_AXIS, screen_y)
    pointer.write(label_text)


def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # draw x axis
    draw_line(pointer, ZERO, y_origin, WIDTH, y_origin)
    # calculates minimum and maximum x values
    min_x, max_x = calc_minmax_x(x_origin, ratio)
    # x begins at minimum x value
    x = min_x
    # loops until the x value is smaller or equal to max_x
    while x <= max_x:
        screen_x, screen_y = calc_to_screen_coord(x, ZERO, x_origin, y_origin, ratio)
        draw_x_axis_tick(pointer, screen_x, screen_y)
        draw_x_axis_label(pointer, screen_x, screen_y, x)
        x = x+1


def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    pass


def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    pass


# YOU SHOULD NOT NEED TO CHANGE ANYTHING BELOW THIS LINE UNLESS YOU ARE DOING THE BONUS


def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """
    return eval(expr)


def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    draw_x_axis(pointer, x_origin, y_origin, ratio)

    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1


main()
turtle.exitonclick()
