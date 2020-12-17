import pyglet
from pyglet import shapes
from pyglet.window import key
import os

from NextShape import draw_next_shape
from GameMatrix import GameMatrix
import MenuAndGameField
from FallingBlock import FallingBlock
from MenuAndGameField import HEIGHT, WIDTH, path

"""
All put together:
"""

# window settings
window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption="Tetris")
window_background = shapes.Rectangle(x=0, y=0, width=WIDTH, height=HEIGHT, color=(12, 150, 166))

# global variables
game_matrix = GameMatrix()
blocks = [FallingBlock(), FallingBlock()]

defeat = False
paused = False

s_tik = 0.6
ms_tik = 0.001


def show_game_field():
    """
    Draws empty game field.
    """
    window.clear()
    window_background.draw()
    MenuAndGameField.draw()


def key_pressed(symbol, modifiers):
    """
    Event handler reacting to input with arrows/WSAD, space and enter after defeat.
    """
    global blocks
    global paused
    global s_tik

    block = blocks[0]
    if symbol == key.UP or symbol == key.W:
        block.do_rotation()

    elif symbol == key.DOWN or symbol == key.S:
        if not game_matrix.check_hit_walls("BOTTOM"):
            block.move_down()


    elif symbol == key.LEFT or symbol == key.A:
        if not game_matrix.check_hit_walls("LEFT"):
            block.move_left()

    elif symbol == key.RIGHT or symbol == key.D:
        if not game_matrix.check_hit_walls("RIGHT"):
            block.move_right()

    elif symbol == key.ENTER and defeat:
        pyglet.app.exit()

    elif symbol == key.SPACE:
        if paused:
            paused = False
            pyglet.clock.schedule_interval(millisecond_tik, ms_tik)
            pyglet.clock.schedule_interval(second_tik, s_tik)
        else:
            paused = True
            pyglet.clock.unschedule(second_tik)
            pyglet.clock.unschedule(millisecond_tik)
    return


def draw():
    """
    Draws the Game Over logo.
    """
    if defeat:
        game_over_label = pyglet.sprite.Sprite(pyglet.image.load(os.path.join(path, "GameOver.png")), x=45, y=290)
        game_over_label.scale = 0.3
        game_over_label.draw()
        pyglet.text.Label("Press ENTER to quit the game", font_name='bauhaus', font_size=14, bold=True,
                          color=(0, 0, 0, 255),
                          x=WIDTH//2-40, y=280).draw()



window.push_handlers(on_draw=draw, on_key_press=key_pressed)


def millisecond_tik(t):
    """
    Function called every millisecond, redrawing everything. Also it checks for end or block to be stored down.
    """
    global defeat

    show_game_field()
    game_matrix.check_shift_blocks()
    game_matrix.update(blocks[0])
    game_matrix.redraw()
    draw_next_shape(blocks[1].get_n())

    if game_matrix.check_hit_walls("BOTTOM"):
        if game_matrix.check_end():
            pyglet.clock.unschedule(second_tik)
            defeat = True
        else:
            game_matrix.add_falling_block_to_stored_blocks()
            blocks[0] = blocks[1]
            blocks[1] = FallingBlock()


def second_tik(t):
    """
    Function that moves block down automatically.
    """
    blocks[0].move_down()


pyglet.clock.schedule_interval(millisecond_tik, ms_tik)
pyglet.clock.schedule_interval(second_tik, s_tik)

# runs the app
pyglet.app.run()
