# CTI-110
# P4HW1 - Distance Traveled
# Jason Dickert
# 25 June 2018
def main():
    speed = float(input("What is the speed of the vehicle in mph?"))
    hours = int(input("How many hours has the vehicle traveled?"))
    hourcount = 1
    print("Hour",'\t',"Distance Traveled")
    print("--------------------------")
    while hourcount <= hours:
        print(hourcount,'\t',(speed * hourcount))
        hourcount = hourcount + 1
main()
