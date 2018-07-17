# CTI-110
# P4HW1 - Distance Traveled
# Tanner Bullock
# 28 June 2018
#

def main ():
    time = int (input ("How many hours has the vehicle traveled? "))
    speed = int (input ("What was the speed of the vehicle? "))

    for i in range (1, time + 1):
        print (i, i * speed)
main ()
