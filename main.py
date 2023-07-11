from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
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


screen.listen()
screen.onkeypress(paddleRight.go_up,"Up")
screen.onkeypress(paddleRight.go_down,"Down")
screen.onkeypress(paddleLeft.go_up,"w")
screen.onkeypress(paddleLeft.go_down,"s")


game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()



screen.exitonclick()

