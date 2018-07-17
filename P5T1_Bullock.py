# CTI-110
# P5T1: Kilometer Converter
# Tanner Bullock
# 10 July 2018
#

def main():
    distance = int (input ("Enter the distance in Kilometers: "))
    show_miles(distance)

def show_miles(distance):
    miles = distance * 0.6214
    print ("The distance is equal to", format (miles, ',.3f'), "miles")

main()
