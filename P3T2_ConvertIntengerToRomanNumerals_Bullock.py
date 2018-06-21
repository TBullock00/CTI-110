# Convert integers 1 to 5 to Roman Numerals
# CTI-110
# Tanner Bullock
# 19 June 2018

choice = "y"
while choice == "y" :

    int1 = int(input("Enter an Integer (1 thru 5): "))

    if int1 == 1:
        print("I")
    elif int1 == 2:
        print("II")
    elif int1 == 3:
        print("III")
    elif int1 == 4:
        print("IV")
    elif int1 == 5:
        print("V")
    else :
        print("Invalid number")
    choice = input("Do you want to run this program again? y for yes, n for no: ")
print("Goodbye")
