l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
r=int(input("Enter radius: "))
a=int(input("Enter side: "))
h=int(input("Enter height:"))
bs=int(input("Enter base:"))
choice=input("Enter shape:\n1.Rectangle\n2.Circle\n3.Square\n4.Triangle\n")
if choice == "1":
    calc_choice=input("Give a calculation:\n1.Area\n2.Perimeter\n")
    if calc_choice == "1":
        print("Area is:" , l*b)
    elif calc_choice == "2":
        print("Perimeter is:" , 2*(l+b))
elif choice == "2":
    calc_choice=input("Give a calculation:\n1.Area\n2.Circumference\n")
    if calc_choice == "1":
        print("Area is: " , 3.147*r*r)
    elif calc_choice == "2":
        print("Circumference is: " , 2*3.147*r)
elif choice == "3":
    calc_choice=input("Give a Calculation:\n1.Area\n2.Perimeter\n")
    if calc_choice == "1":
        print("Area is:" , a*a)
    elif calc_choice == "2":
        print("Perimeter is " , 4*a)
elif choice == "4":
    calc_choice=input("Give a calculation:\n1.Area\n")
    if calc_choice == "1":
        print("Area is :" , 0.5*bs*h)
else:
    print("Invalid input")
