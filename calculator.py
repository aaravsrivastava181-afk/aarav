while True:
    a = int(input("Number 1\n"))
    b = int(input("Number 2\n"))
    choice = input("What to do?" 
    "\n 1. Addition" 
    "\n 2. Subtraction" 
    "\n 3. Division" 
    "\n 4. Multiplication"
    "\n 5. Exponentation"
    "\n 6. Modulus\n")
    if choice == "1":
        print("Answer:", a + b)
    elif choice == "2":
        print("Answer:", a - b)
    elif choice == "3":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Answer:", a / b)
    elif choice == "4":
        print("Answer:", a * b)
    elif choice == "5":
        print("Answer:" , a**b) 
    elif choice == "6":
        print("Answer:" ,a%b)
    else:
        print("Invalid")
    again = input("Do you want to continue? (y/n)")
    if again.lower() != "y":
        break