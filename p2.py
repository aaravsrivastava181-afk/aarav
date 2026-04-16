a=int(input("Enter a no:"))
b=int(input("Enter a no: "))
choice=(input("Enter choice:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
if choice == "1":
    print("Addition is",a + b)
elif choice=="2":
     print("Subtraction is" , a - b)
elif choice=="3":
    print("Multiplication is" , a * b)
elif choice=="4":
   print("Division is" , a / b)
elif choice>="5":
    print("Invaid choice")