# CTI-110
# P3LAB - Debugging
# Tanner Bullock
# 20 June 2018
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    E_score = 50
    # TO DO: define the rest of the scores - COMPLETE

    
    score = int( input('Enter grade: '))

    if score >= 101:
        print ("Please enter a number between '0' and '100'")
    elif score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print ("Your grade is: C")
    elif score >= D_score:
        print ("Your grade is: D")
    elif score >= E_score:
        print ("Your score is: E")
    else:
        print('Your grade is: F') # TO DO: finish this - COMPLETE







# program start - TESTED
main()
