# CTI-110
# P3HW2 - Software Sales
# Jason Dickert
# 24 June 2018
def main():
    print("Our software package retails for $99.")
    print("We offer the following discounts for bulk purchases:")
    print("10 to 19 packages:       10% discount")
    print("20 to 49 packages:       20% discount")
    print("50 to 99 packages:       30% discount")
    print("More than 100 packages:  40% discount")
    purchaseqty = float(input("How many packages do you want to buy?"))
    discount10 = ((purchaseqty * 99) * .9)
    discount20 = ((purchaseqty * 99) * .8)
    discount30 = ((purchaseqty * 99) * .7)
    discount40 = ((purchaseqty * 99) * .6)
    if purchaseqty < 10:
        nodiscount = (purchaseqty * 99)
        print("There is no special discount for this amount.")
        print("Your subtotal is $",nodiscount)
    if purchaseqty >= 10 and purchaseqty < 20:
        print("You will recieve a 10% discount for this amount.")
        print("Your subtotal is $",discount10)
    if purchaseqty >=20 and purchaseqty < 50:
        print("You will recieve a 20% discount for this amount.")
        print("Your subtotal is $",discount20)
    if purchaseqty >= 50 and purchaseqty < 100:
        print("You will recieve a 30% discount for this amount.")
        print("Your subtotal is $",discount30)
    if purchaseqty > 100:
        print("You will recieve a 40% discount for this amount.")
        print("Your subtotal is $",discount40)
main()

