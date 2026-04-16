num=int(input("Enter a no\n"))
n=num
rev=0
d=0
while(n>0):
    d=n%10 
    rev=(rev*10)+d
    n=n//10
if rev==num:
    print("It is a Palindrome")
else:
    print("Not a palindrome")
    