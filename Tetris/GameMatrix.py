from pyglet import shapes
import MenuAndGameField

MATRIX_ROWS = 20
MATRIX_COLUMNS = 10


class GameMatrix:
    """
    Class representing the state of the game-field via matrices.
    """
    falling_block_matrix = []
    block_stored_matrix = []
    color_of_stored = (0, 0, 255)  # blue
    color_of_falling = (0, 0, 0)

    def __init__(self):
        self.clear_falling_matrix()
        self.clear_stored_matrix()

    def clear_falling_matrix(self):
        """
        Create matrix with zeros representing the field with the moving (falling) block.
        """
        self.falling_block_matrix.clear()
        for i in range(MATRIX_ROWS):
            self.falling_block_matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


    def clear_stored_matrix(self):
        """
        Create two matrix with zeros representing the 'static' game field.
        """
        self.block_stored_matrix.clear()
        for i in range(MATRIX_ROWS):
            self.block_stored_matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


    def check_end(self):
        """
        Checks if game's over by looking at the very top row, if there's just one block (represented as number
        that is not zero), it's end of the game.
        """
        for column in range(MATRIX_COLUMNS):
            if self.block_stored_matrix[0][column] != 0:
                return True
        return False

    def check_complete_row(self, y):
        """
        Line without zeros means a complete row,
        this method is called in check_shift_blocks.
        """
        row = self.block_stored_matrix[y]

        if not (0 in row):
            return True
        return False


    def check_shift_blocks(self):
        """
        Method shifts blocks after there's a complete row and adds 10 to score.
        """
        for line in range(1, MATRIX_ROWS):
            if self.check_complete_row(line):

                # shifting the field down
                for i in range(line, 1, -1):
                    for j in range(MATRIX_COLUMNS):
                        self.block_stored_matrix[i][j] = self.block_stored_matrix[i-1][j]

                # adding 10 to score (+1 for every square)
                MenuAndGameField.score += 10


    def get_block_stored_matrix_element(self, row, column):
        """
        Method used by check_hit_walls, returning -1 or the value of element in matrix in xy coordinates.
        """
        if 0 <= row < MATRIX_ROWS and 0 <= column < MATRIX_COLUMNS:
            return self.block_stored_matrix[row][column]
        return -1


    def check_hit_walls(self, side):
        """
        Method checking if a piece would hit left/right/bottom side of game field or would hit the stored pieces.
        """
        if side == "BOTTOM":
            for row in range(MATRIX_ROWS):
                for column in range(MATRIX_COLUMNS):
                    if self.falling_block_matrix[row][column] != 0:
                        elem = self.get_block_stored_matrix_element(row + 1, column)
                        if elem != 0 or elem == -1:
                            return True

        elif side == "LEFT":
            for row in range(MATRIX_ROWS):
                for column in range(MATRIX_COLUMNS):
                    if self.falling_block_matrix[row][column] != 0:
                        elem = self.get_block_stored_matrix_element(row, column - 1)
                        if elem != 0 or elem == -1:
                            return True

        elif side == "RIGHT":
            for row in range(MATRIX_ROWS):
                for column in range(MATRIX_COLUMNS):
                    if self.falling_block_matrix[row][column] != 0:
                        elem = self.get_block_stored_matrix_element(row, column + 1)
                        if elem != 0 or elem == -1:
                            return True
        return False

    def add_falling_block_to_stored_blocks(self):
        """
        Adds the current falling block to the block_stored_matrix
        """
        for row in range(MATRIX_ROWS):
            for column in range(MATRIX_COLUMNS):
                self.block_stored_matrix[row][column] = \
                    self.block_stored_matrix[row][column] + self.falling_block_matrix[row][column]

    # working with the falling matrix

    def set_falling_block_matrix_elem(self, row, column, value):
        """
        Method setting [row][column] element of falling block matrix to a given value.
        """
        if 0 <= row < MATRIX_ROWS and 0 <= column < MATRIX_COLUMNS:
            self.falling_block_matrix[row][column] = value

    def update(self, block):
        """
        Method updating a matrix based on the Falling block attributes
        """
        column = block.get_x()
        row = block.get_y()
        self.clear_falling_matrix()  # to restart the falling matrix file (so it doesn't overwrite)
        self.color_of_falling = block.get_color()  # get the color for drawing into the game field

        s = block.get_shape()
        for i in range(len(s)):
            for j in range(len(s[0])):
                self.set_falling_block_matrix_elem(row + i, column + j, int(s[i][j]))

    def redraw(self):
        """
        Method that will be called many times, specifically every tik, redrawing the blocks in game field.
        """

        for row in range(MATRIX_ROWS):
            for column in range(MATRIX_COLUMNS):
                square_stored = self.block_stored_matrix[row][column]
                square_fall = self.falling_block_matrix[row][column]

                if square_stored != 0:
                    tmp = shapes.Rectangle(x=30 + column * 30, y=600 - row * 30,
                                           width=30, height=30, color=self.color_of_stored)
                    tmp.draw()

                if square_fall != 0:
                    tmp = shapes.Rectangle(x=30 + column * 30, y=600 - row * 30,
                                           width=30, height=30, color=self.color_of_falling)
                    tmp.draw()
