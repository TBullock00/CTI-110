# CTI-110
# P5T2: Feet to Inches
# Tanner Bullock
# 10 July 2018
# This program asks for the user to input a feet length then converts the given
#   length to inches.

def main():
    length = int (input ("Enter the length in feet: "))
    show_length(length)

def show_length(length):
    inches = length * 12
    print ("The length is equal to", inches, "inches")

main()
