# CTI-110
# P4HW2 - Running Total
# Tanner Bullock
# 28 June 2018
#

def main ():
    grade = 0
    total = 0
    print ("Enter a negative number to stop the loop and get your total")

    if grade >= 0:
        while grade >= 0:
            grade = float (input ("Enter a grade: "))
            if grade >= 0:
                total = total + grade
            else:
                print (format (total, ',.2f'))
    else:
        print ("You've found a dead end")
main ()
