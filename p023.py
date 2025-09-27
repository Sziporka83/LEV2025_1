# Balog Mónika - GDDNBY
"""
    Egyenlő szárú háromszög rajzolása, minden oldal 150 pont hosszú,
    piros színnel, 5 pontos vonalvastagsággal.
    """
import turtle

def haromszog():

    turtle.clear()
    turtle.penup()
    turtle.goto(-75, -75)
    turtle.pendown()
    turtle.showturtle()

    turtle.setheading(0)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(150)
    turtle.left(120)
    turtle.forward(150)
    turtle.left(120)
    turtle.hideturtle()

def exit_program():
    """
    Program kilépése, Turtle ablak bezárása.
    """
    turtle.bye()

""" Ablak és teknős objektum létrehozása, beállítása"""
ablak = turtle.Screen()
ablak.title("Piros egyenlő szárú háromszög billentyűzetvezérléssel")

turtle.hideturtle()
turtle.color("red")
turtle.pensize(5)
turtle.speed(5)

"""Billentyűzetes események beállítása"""
turtle.listen()
turtle.onkey(haromszog, "h")
turtle.onkey(exit_program, "q")

turtle.mainloop()
