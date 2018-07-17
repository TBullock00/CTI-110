# CTI-110
# P4HW3 - Factorial
# Tanner Bullock
# 3 July 2018
#
def main():
    num = int (input ("Enter a number to see it's factorial: "))
    f = 1
    for a in range(1, num + 1):
        f = f * a
        

    print ("The factorial is:", f)

main()

