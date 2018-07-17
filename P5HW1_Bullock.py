# CTI-110
# P5HW1: Test Average and Grade
# Tanner Bullock
# 10 July 2018
#
average = 0
total = 0
def main():
    for i in range (5):
        grade = int (input ("Enter grade: "))
        calc_average(average, total, grade)
        determine_grade(grade)
    print (calc_average(average, total)
    

def calc_average(average, total):
    total = total + grade
    average = total / 5
    
    return average

def determine_grade(grade):

    if grade >= 101:
        print ("Please enter a number between '0' and '100'")
    elif grade >= 90 and grade <= 100:
        print('Your grade is an A')
    elif grade >= 80 and grade <=89:
        print('Your grade is a B')
    elif grade >= 70 and grade <=79:
        print ("Your grade is a C")
    elif grade >= 60 and grade <= 69:
        print ("Your grade is a D")
    elif grade >= 50 and grade <=59:
        print ("Your score is a E")
    else:
        print('Your grade is a F')
    print (" ")

calc_average(average, total)
main()
