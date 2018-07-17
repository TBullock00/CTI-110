# CTI-110
# P4LAB - Nested Loops
# Tanner Bullock
# 3 July 2018
#

def main ():
    import turtle
    bob = turtle.Turtle ()
    bob.left (110)
    bob.speed ('fast')

    for i in range (5):
        for i in range (3):
            bob.forward (100)
            bob.right (120)
        bob.left (360)
        bob.forward (100)
        bob.left (72)
main ()

