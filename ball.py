from turtle import Screen, Turtle


class Ball(Turtle):
    def __init__(self,positionR):
        super().__init__()
        self.position=positionR
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.color("white")
        self.fillcolor("white")
        self.goto(self.position)
        self.inc_x=10
        self.inc_y=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()
        new_y=self.ycor()
        #if (new_x +self.inc_x >= 390 or new_x +self.inc_x <= -390):
        #    self.bounce_x()
        if (new_y +self.inc_y >= 290 or new_y +self.inc_y <= -290):
            self.bounce_y()
        new_x +=self.inc_x
        new_y +=self.inc_y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.inc_y *= -1

    def bounce_x(self):
        self.inc_x *= -1
        self.move_speed *=0.9
    def reset_position(self):
        self.goto(self.position)
        self.bounce_x()
        self.move_speed =0.1


