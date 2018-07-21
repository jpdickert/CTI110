# CTI-110
# P5T1 Kilometer Converter
# Jason Dickert
# 27 June 2018
def main():
    km = float(input("Enter kilometers: "))
    def show_miles():   
        miles = km * .6214
        print(km,"kilometers equal",miles,"miles.")
    show_miles()
main()
