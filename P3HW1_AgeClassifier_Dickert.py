# CTI-110
# P3HW1 - Age Classifier
# Jason Dickert
# 24 June 2018
def main():
    age = float(input("What is the person's age?"))
    if age <= 1:
        print("This person is an infant.")
    if age > 1 and age < 13:
        print("This person is a child.")
    if age >= 13 and age < 20:
        print("This person is a teenager.")
    if age >= 20:
        print("This person is an adult.")
main()

