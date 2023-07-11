from turtle import Screen, Turtle


class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.color("white")
        self.fillcolor("white")
        self.goto(position)
        self.inc_x=10
        self.inc_y=10

    def move(self):
        new_x=self.xcor()
        new_y=self.ycor()
        if (new_x +self.inc_x >= 390 or new_x +self.inc_x <= -390):
            self.inc_x *=-1
        if (new_y +self.inc_y >= 290 or new_y +self.inc_y <= -290):
            self.inc_y *=-1
        new_x +=self.inc_x
        new_y +=self.inc_y
        self.goto(new_x,new_y)
