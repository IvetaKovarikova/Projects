import pyglet
from pyglet import shapes
import os

path = os.path.join(os.path.dirname(__file__), "resources")

# loading font
pyglet.font.add_file(os.path.join(path, "Bauhaus 5.ttf"))
bauhaus = pyglet.font.load('bauhaus')

# window constants
WIDTH = 530
HEIGHT = 660
OFFSET_BOTTOM = 30

# field constants
OFFSET_LEFT = 30
OFFSET_TOP = 30
OFFSET_RIGHT = 200

FIELD_HEIGHT = HEIGHT - OFFSET_BOTTOM - OFFSET_TOP
FIELD_WIDTH = WIDTH - OFFSET_LEFT - OFFSET_RIGHT

SQUARE_WIDTH = FIELD_WIDTH // 10  # ten in columns
SQUARE_HEIGHT = FIELD_HEIGHT // 20  # twenty squares in rows

# menu constants
MENU_LEFT_X = 340
MENU_RIGHT_X = 520

# game constants
tik = 300
score = 0
elapsed_time = 0


def draw_logo():
    """
    Draws the logo from resources file.
    """
    tetris_logo = pyglet.sprite.Sprite(pyglet.image.load(os.path.join(path, "TetrisLogo.png")),
                                       x=MENU_LEFT_X, y=HEIGHT - 90)
    tetris_logo.draw()


def draw_score():
    """
    Draws score and its value.
    """
    score_label = pyglet.text.Label(f"Score: {score}", font_name='bauhaus', font_size=20, bold=True,
                                    x=MENU_LEFT_X, y=HEIGHT - 120,
                                    color=(251, 255, 0, 255))
    score_label.draw()


def draw_info_bottom():
    """
    Draws manual at the bottom of the screen.
    """
    pyglet.text.Label("WSAD - to rotate and move, "
                      "SPACE - pause the game", font_size=14, font_name='bauhaus', bold=True,
                      x=50, y=10, color=(251, 255, 0, 255)).draw()


def draw_game_background():
    """
    Draws the game-field / grid where the tetris pieces will be.
    """
    game_background = shapes.BorderedRectangle(x=OFFSET_LEFT, y=OFFSET_BOTTOM,
                                               width=FIELD_WIDTH, height=FIELD_HEIGHT,
                                               border=2,
                                               border_color=(255, 255, 255),
                                               color=(140, 160, 160))
    game_background.draw()
    for row in range(OFFSET_BOTTOM, FIELD_HEIGHT + OFFSET_BOTTOM, SQUARE_HEIGHT):
        row_line = shapes.Line(x=OFFSET_LEFT, y=row, x2=OFFSET_LEFT + FIELD_WIDTH, y2=row)
        row_line.draw()
    for column in range(OFFSET_LEFT, FIELD_WIDTH + OFFSET_LEFT, SQUARE_WIDTH):
        column_line = shapes.Line(x=column, y=OFFSET_BOTTOM, x2=column, y2=OFFSET_BOTTOM + FIELD_HEIGHT)
        column_line.draw()


def draw():
    """
    Method that'll call everything in this file.
    """
    draw_logo()
    draw_score()
    draw_info_bottom()
    draw_game_background()
