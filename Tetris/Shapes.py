"""
Tetris shapes:
"""

# the 'S' shape and its rotation options (color: (0, 100, 0) = dark green)
S = [['011',
      '110'],
     ['10',
      '11',
      '01']]

# the 'Z' shape and its rotation options (color: (255, 0, 0) = red)
Z = [['110',
      '011'],
     ['01',
      '11',
      '10']]

# the 'I' shape and its rotation options (color: (255, 255, 0) = yellow)
I = [['1',
      '1',
      '1',
      '1'],
     ['1111']]

# the 'O'/box shape (color: (0, 255, 0) = light green)
O = [['11',
      '11']]

# the 'J' shape and its rotation options (color: (170, 0, 255) = violet)
J = [['100',
      '111'],
     ['11',
      '10',
      '10'],
     ['111',
      '001'],
     ['01',
      '01',
      '11']]

# the 'L' shape and its rotation options (color: (255, 150, 0) = orange)
L = [['001',
      '111'],
     ['10',
      '10',
      '11'],
     ['111',
      '100'],
     ['11',
      '01',
      '01']]

# the 'T' shape and its rotation options (color: (237, 50, 231) = pink)
T = [['010',
      '111'],
     ['10',
      '11',
      '10'],
     ['111',
      '010'],
     ['01',
      '11',
      '01']]

tetris_shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 100, 0),
                (255, 0, 0),
                (255, 255, 0),
                (0, 255, 0),
                (170, 0, 255),
                (255, 150, 0),
                (237, 50, 231)]
