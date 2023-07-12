from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
#Serve per mettere off l'animazione
screen.tracer(0)

paddleRight=Paddle((350,0))
paddleLeft=Paddle((-350,0))
ball=Ball((0,0))
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(paddleRight.go_up,"Up")
screen.onkeypress(paddleRight.go_down,"Down")
screen.onkeypress(paddleLeft.go_up,"w")
screen.onkeypress(paddleLeft.go_down,"s")


game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with right paddle
    if ball.distance(paddleRight) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    #Detect collision with left paddle
    elif ball.distance(paddleLeft) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect when the ball is out on the left and right
    elif ball.xcor() < -390 :
        scoreboard.r_point()
        ball.reset_position()
        screen.update()
        time.sleep(0.5)
    elif ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()
        screen.update()
        time.sleep(0.5)

screen.exitonclick()

