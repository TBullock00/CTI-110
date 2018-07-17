# CTI-110
# P4T2: Bug Collector
# Tanner Bullock
# 10 July 2018
#

def main():
    bugInput = 0
    current = 0
    total = 0
    for i in range (7):
        current = current + 1
        print ("How many bugs did you collect on day", current)
        bugPerDay = int (input ())
        total = bugPerDay + total

    print ("Your total is:",total)

main()
