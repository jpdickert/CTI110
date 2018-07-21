# CTI-110
# P4HW2 - Running Total
# Jason Dickert
# 25 June 2018
def main():
    total = 0
    while total >= 0:
        number = float(input("Enter a number: "))
        total = total + number
        if number < 0:
            total = total - number
            print("You have entered a negative number. Your total is", total)
main()
