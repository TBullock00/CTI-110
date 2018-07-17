# CTI-110
# P4LAB2 - Initials
# Tanner Bullock
# 10 July 2018
#

def main():
    import turtle
    bob = turtle.Turtle()
    bob.color ("green2")

    bob.left (90)
    bob.forward (100)
    bob.left (90)
    bob.forward (50)
    bob.right (180)
    bob.forward (100)

    bob.up()
    bob.forward (50)
    bob.down()

    bob.right(90)
    bob.forward (100)
    bob.left (90)
    for i in range(10):
        bob.forward (9)
        bob.left (20)
    bob.right (180)
    for i in range(8):
        bob.forward (9)
        bob.left (20)

    bob.up ()
    bob.right (90)
    bob.forward (100)
main()
