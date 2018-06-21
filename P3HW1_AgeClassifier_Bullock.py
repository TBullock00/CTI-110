# CTI-110 
# P3HW1 - Age Classifier 
# Tanner Bullock 
# 20 June 2018
#

def main():
    age = int (input("Please input person's age: "))

    if age < 2:
        print ("The person is an infant.")
    elif age < 13:
        print ("The person is a child.")
    elif age < 20:
        print ("The person is a teenager.")
    elif age > 19:
        print ("Ther person is an adult.")
    else:
        print ("unknown")
main()
