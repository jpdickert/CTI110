# CTI-110
# P3T1 - Areas of Rectangle
# Jason Dickert
# 24 June 2018
length1 = float(input("What is the length of the first rectangle?"))
width1 = float(input("What is the width of the first rectangle?"))
length2 = float(input("What is the length of the second rectangle?"))
width2 = float(input("What is the width of the second rectangle?"))
area1 = length1 * width1
area2 = length2 * width2
if area1 > area2:
    print("The first rectangle is larger.")
if area2 > area1:
    print("The second rectangle is larger.")
if area1 == area2:
    print("The rectangles are equal in size.")
