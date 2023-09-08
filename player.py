from turtle import Turtle
player = Turtle()

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.color("black")
        self.setheading(90)

    def player_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def player_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def player_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


    def player_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
