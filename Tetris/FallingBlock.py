from random import randint
import Shapes
from GameMatrix import MATRIX_COLUMNS, MATRIX_ROWS


class FallingBlock:
    """
    Class represents a block with its shape (S, Z, I ,O , J, L or T), also
    implements moving, rotating and checking for collisions of the block.
    """
    x = 4
    y = -3
    rotation = 0

    n = 0  # index of the actual shape
    shape = 0
    color = (0, 0, 0)

    def __init__(self):
        self.set_shape()

    # get methods

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def get_rotation(self):
        return self.rotation

    def get_n(self):
        return self.n

    # other methods:

    def set_shape(self):
        """
        Setting shape to a random shape from list of shapes in file Shapes.py,
        also setting its color.
        """
        self.x = 4
        self.y = -2
        self.rotation = 0
        self.n = randint(0, 6)
        self.shape = Shapes.tetris_shapes[self.n][0]
        self.color = Shapes.shape_colors[self.n]

    def falling_block_side_collision(self, side):
        """
        Method returns true if falling shape collides with sides of the game-field.
        """
        if side == "LEFT":
            if self.x <= 0:
                return True
        if side == "RIGHT":
            if self.x >= MATRIX_COLUMNS:
                return True
        if side == "DOWN":
            if self.y >= MATRIX_ROWS - 1:
                return True
        return False

    def check_if_out_of_field(self):
        """Checking if a block would be out of field after rotation"""
        if self.x < 0:
            self.x = 0
        elif self.x + len(self.shape[0]) > MATRIX_COLUMNS - 1:
            self.x = MATRIX_COLUMNS - len(self.shape[0])



    def do_rotation(self):
        """
        Method that changes the shape based on its rotation number. There are if statements that will make the block
        act more natural around right corner (those changing self.x). Also I won't allow user to rotate a piece near
        bottom of the field (those if statements with self.y).
        """

        self.rotation += 1
        rot = self.rotation
        n = self.n

        if n == 0:  # the 'S' shape
            if rot == 0:
                self.shape = Shapes.tetris_shapes[n][0]
            elif rot == 1:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][1]
                self.rotation = -1

        elif n == 1:  # the 'Z' shape
            if rot == 0:
                self.shape = Shapes.tetris_shapes[n][0]
            elif rot == 1:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][1]
                self.rotation = -1

        elif n == 2:  # the 'I' shape
            if rot == 0:
                if self.y > 16:
                    return
                if self.x == 6:
                    self.x += 3
                    return
                self.shape = Shapes.tetris_shapes[n][0]
            elif rot == 1:
                self.shape = Shapes.tetris_shapes[n][1]
                self.rotation = -1


        elif n == 3:  # the 'O' shape
            pass

        elif n == 4:  # the 'J' shape
            if rot == 0:
                self.shape = Shapes.tetris_shapes[n][0]
            elif rot == 1:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][1]
            elif rot == 2:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x -= 1
                self.shape = Shapes.tetris_shapes[n][2]
            elif rot == 3:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][3]
                self.rotation = -1

        elif n == 5:  # the 'L' shape
            if rot == 0:
                self.shape = Shapes.tetris_shapes[n][0]
            elif rot == 1:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][1]
            elif rot == 2:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x -= 1
                self.shape = Shapes.tetris_shapes[n][2]
            elif rot == 3:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][3]
                self.rotation = -1

        elif n == 6:  # the 'T' shape
            if rot == 0:
                self.shape = Shapes.tetris_shapes[n][0]
            elif rot == 1:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][1]
            elif rot == 2:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x -= 1
                self.shape = Shapes.tetris_shapes[n][2]
            elif rot == 3:
                if self.y > 17:
                    return
                if self.x == 7:
                    self.x += 1
                self.shape = Shapes.tetris_shapes[n][3]
                self.rotation = -1

        self.check_if_out_of_field()

    def move_down(self):
        """Moves block down by one"""
        if not self.falling_block_side_collision("DOWN"):
            self.y += 1

    def move_left(self):
        """Moves block left by one"""
        if not self.falling_block_side_collision("LEFT"):
            self.x -= 1

    def move_right(self):
        """Moves block right by one"""
        if not self.falling_block_side_collision("RIGHT"):
            self.x += 1
