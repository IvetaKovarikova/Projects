import pyglet
import colorsys

import Shapes
from pyglet import shapes

from MenuAndGameField import HEIGHT, MENU_LEFT_X

NEXT_SHAPE_SQUARE_SIZE = 180

S = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

Z = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

I = [[0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

O = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

J = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

L = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0]]

T = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

next_shapes = [S, Z, I, O, J, L, T]


def lighten_color(color):
    """ Method that will return lighter color that the one given by parameter."""
    clr = (color[0] / 255, color[1] / 255, color[2] / 255)  # rgb numbers between 0...1 (not 0...255)
    h, l, s = colorsys.rgb_to_hls(*clr)  # color represented in hls

    new_l = 1 - 0.2 * (1-l)  # new value representing lightness

    rgb = colorsys.hls_to_rgb(h, new_l, s)  # color represented in rgb again but will be lighter
    return int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)  # returning the color in (0...255) and as integer




def draw_next_shape(n):
    """
     Draws the next-shape (given by index n ) and a border with color of the next shape :)
     """
    color = Shapes.shape_colors[n]
    lightened = lighten_color(color)
    m = next_shapes[n]

    ns_label = pyglet.text.Label("Next block: ", font_name='bauhaus', font_size=20, bold=True,
                                 x=MENU_LEFT_X, y=HEIGHT - 160,
                                 color=(251, 255, 0, 255))
    next_shape = shapes.BorderedRectangle(x=MENU_LEFT_X, y=HEIGHT - 360, border=4, border_color=color,
                                          color=lightened,
                                          width=NEXT_SHAPE_SQUARE_SIZE, height=NEXT_SHAPE_SQUARE_SIZE)
    ns_label.draw()
    next_shape.draw()

    for x in range(6):
        for y in range(6):
            if m[x][y] == 1:
                shapes.Rectangle(x=30 * y + 340, y=30 * x + 300, width=30, height=30, color=color).draw()
