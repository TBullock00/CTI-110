# CTI-110
# P4LAB1: Shapes
# Tanner Bullock
# 10 July 2018
#

def main():
    import turtle
    bob = turtle.Turtle()

    for i in range (4):
        bob.forward (100)
        bob.left (90)

    bob.penup ()
    bob.forward (150)
    bob.pendown ()

    for i in range (3):
        bob.forward (100)
        bob.left (120)

main()
