user = input("Enter your choice:\n1. Sum of even no's\n2. Sum of odd no's\n")
ES = 0
OS = 0
n = 10

if user == "1":
    for n in range(1, n+1):
        if n % 2 == 0:
            ES += n
    print(f"Even Sum of no's is: {ES}")
elif user == "2":
    for n in range(1, n+1):
        if n % 2 == 1:
            OS += n
    print(f"Odd Sum of no's is: {OS}")
else:
    print("Invalid choice")