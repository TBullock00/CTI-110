# CTI-110
# P3T1 - Area of Rectangles
# Tanner Bullock
# 19 June 2018

choice = "y"
while choice == "y" :

    length1 = int(input("Enter first rectangle's length: "))
    width1 = int(input("Enter first rectangle's width: "))

    length2 = int(input("Enter second rectangle's length: "))
    width2 = int(input("Enter second retangle's width: "))

    area1 = length1 * width1
    area2 = length2 * width2

    print("The area of the first rectangle is:", area1)
    print("The area of the second rectangle is:", area2)

    if area1 > area2 :
        print("The first rectangle has the larger area")
    elif area1 < area2 :
        print("The second rectangle has the larger area")
    else :
        print("Both rectangles have the same area")
    choice = input("Do you want to run this program again? y for yes, n for no: ")
