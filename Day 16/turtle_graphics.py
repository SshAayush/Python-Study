from turtle import Turtle, Screen
import turtle 

jimmy = Turtle()
print(jimmy)
jimmy.shape('turtle')
jimmy.color('red')
jimmy.forward(100)

jimmy.pensize(5)

jimmy.pen(1)
jimmy.pencolor("black")
jimmy.speed(2)
u_circle = jimmy.circle(100)
my_screen = Screen()
print(my_screen.canvheight)
jimmy.clear()
print(u_circle)

# jimmy.home()


my_screen.exitonclick()