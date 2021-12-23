import turtle as t

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()  # call the method to create the snake body
        self.head = self.segments[0]

# 1.a to create the snake body
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

# 1.b to create the snake body
    def add_segment(self, position):
        snake = t.Turtle()
        snake.penup()
        snake.shape('square')
        snake.color('white')
        snake.goto(position)
        self.segments.append(snake)

# to add segment to the snake tail
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            move_x = self.segments[seg_num - 1].xcor()
            move_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(move_x, move_y)
        # once the last position is moved, then move the 1st segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        when snake go up it can not go down
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # north

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # south

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)  # west

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)  # east

