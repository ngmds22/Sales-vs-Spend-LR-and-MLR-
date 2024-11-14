from turtle import Turtle
# Creating constant variables for the snake class.
# Constants for starting positions (coordinates).
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Constant for movement distance.
MOVE_DISTANCE = 20

# Constants for directional headings (degrees).
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Defining the snake class.
class Snake:

    # def init self for what variables ot initialize when creating an instance of this class.
    def __init__(self):

        # List for the amount of segments, how long the snake is.
        self.segments = []
        self.create_snake()

        # self.head, the head of the snake is the 0th item in the list.
        self.head = self.segments[0]
    
    # CLass method to create a snake object.
    def create_snake(self):

        # We have three items in the STARTING_COORDINATES list, this loop with loop three times over
        # as there are 3 items, 0, 1 and 2 each pertaining to a coordinate postion.
        # Run 1:
            # For 0th item in SP:
            # create new segment as square,
            # color is white,
            # penup to get rid of trail,
            # go to position (0, 0), Oth item coordinate in SP list,
            # Append this segment to self.segments list, to the object you've created's segment list.
        # Run 1 end.
        
        # This will run 2 more times for 1st and 2nd position.
        # 1st position will be the second body part of the snake and will go to the second
        # coordinate in the SP list (-20, 0).
        # 2nd will be the third body part and will go to the third coordinate in the SP list
        # being (-40, 0).
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
