# CTI-110 
# P3HW2 - Software Sales
# Tanner Bullock 
# 20 June 2018
#

def main():
    print ("The sale price is $99.")
    price = 99
    quantity = int (input ("Please enter the quantity ordered: "))

    if quantity > 9 and quantity < 20:
        discount = .10
        print ("Your discount is 10% off of your purchase")
    elif quantity > 19 and quantity < 50:
        discount = .20
        print ("Your discount is 20% off of your purchase")
    elif quantity > 49 and quantity < 100:
        discount = .30
        print ("Your discount is 30% off of your purchase")
    elif quantity > 99:
        discount = .40
        print ("Your discount is 40% off of your purchase")
    else:
        print ("Your purchase does not qualify for a discount.")

    if quantity > 9:
        totalDiscount = price * discount
        unitCost = price - totalDiscount
        total = unitCost * quantity
        print ("Your per unit savings is $", totalDiscount)
        print ("Your per-unit cost is $", unitCost)
        original = price * quantity
        savings = original - total
        print ("Your total amount of savings is $", savings)
    else:
        total = quantity * price
        print ("Order 10 or more to qualify for a discount")
    
    print ("Your total is $", total)

main()
