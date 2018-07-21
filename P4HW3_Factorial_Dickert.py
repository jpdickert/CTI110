# CTI-110
# P4HW3 - Factorial
# Jason Dickert
# 25 June 2018
def main():
    number = int(input("Enter a positive integer: "))
    factorial = 1
    if number < 0:
        print("Your number is negative.")
    elif number == 0:
        print("The factorial of 0 is 1.")
    else:
        for factor in range(1,number + 1):
            factorial = factorial * factor
        print("The factorial of",number,"is",factorial)
main()
