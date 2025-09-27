#Balog Monika - GDDNBY
import turtle

def pentagram():
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.hideturtle()
    turtle.color("orange")
    turtle.pensize(10)
    turtle.speed(3)

    turtle.setheading(90)
    for _ in range(5):
        turtle.forward(150)
        turtle.right(144)

    turtle.penup()
    turtle.goto(120, 75)
    turtle.pendown()
    turtle.pensize(5)
    turtle.circle(100)
def exit_program():

    turtle.bye()

ablak = turtle.Screen()
ablak.title("Pentagram START = p")

turtle.listen()
turtle.onkey(pentagram, "p")
turtle.onkey(exit_program, "q")

turtle.mainloop()
