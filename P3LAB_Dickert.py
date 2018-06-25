# CTI-110
# P3LAB
# Jason Dickert
# 24 June 2018
def main():
    # This program takes a number grade and outputs a letter grade.
    # system uses 10-point grading scale
    # TO DO: define the rest of the scores
    score = float(input('Enter grade:'))
    if score >= 90:
        print('Your grade is: A.')
    if score >= 80 and score < 90:
        print('Your grade is: B.')
    if score >= 70 and score < 80:
        print('Your grade is: C.')
    if score >= 60 and score < 70:
        print('Your grade is: D.')
    if score < 60:
        print('Your grade is: F.')
main()
