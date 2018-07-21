# Test Grading Program
# 03 July 2018
# CTI-110 P5HW1 - Test Average and Grade
# Jason Dickert
#

def determine_grade(grade):
    if (grade >= 90):
        return "A"
    elif (grade >= 80):
        return "B"
    elif (grade >= 70):
        return "C"
    elif (grade >= 60):
        return "D"
    elif (grade < 60):
        return "F"
    
def calc_average(grade1, grade2, grade3, grade4, grade5):
    average = (grade1 + grade2 + grade3 + grade4 + grade5)/5
    return average

def main():
    grade1 = float(input("Enter the grade of Test 1: "))
    grade2 = float(input("Enter the grade of Test 2: "))
    grade3 = float(input("Enter the grade of Test 3: "))
    grade4 = float(input("Enter the grade of Test 4: "))
    grade5 = float(input("Enter the grade of Test 5: "))
    print("Test 1 numeric grade:",grade1)
    print("Test 1 letter grade:",determine_grade(grade1))
    print("Test 2 numeric grade:",grade2)
    print("Test 2 letter grade:",determine_grade(grade2))
    print("Test 3 numeric grade:",grade3)
    print("Test 3 letter grade:",determine_grade(grade3))
    print("Test 4 numeric grade:",grade4)
    print("Test 4 letter grade:",determine_grade(grade4))
    print("Test 5 numeric grade:",grade5)
    print("Test 5 letter grade:",determine_grade(grade5))
    print("Average test grade:",calc_average(grade1, grade2, grade3, grade4, grade5))
main()


