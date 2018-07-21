# CTI-110
# P4T2 - Bug Collector
# Jason Dickert
# 25 June 2018
def main():
    total = 0
    for day in range(1, 8):
        print("Enter bugs collected on day", day)
        bugs = int(input())
        total = total + bugs
    print("You collected a total of", total, "bugs.")
main()
