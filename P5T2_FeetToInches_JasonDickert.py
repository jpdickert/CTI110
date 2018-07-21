# Feet to Inches
# 27 June 2018
# CTI-110 P5T2_FeetToInches
# Jason Dickert
#
inches_per_foot = 12
def main():
    feet = int(input("Enter feet: "))
    print(feet,"feet equals",feet_to_inches(feet),"inches.")
def feet_to_inches(feet):
    return feet * inches_per_foot
main()
