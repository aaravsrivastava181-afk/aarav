#NESTED DICTIONARY
data = {
    "maths" : "83",
     "physics" : "73",
      " chemistry" : " 70"

}

subject=input("Enter a subject:\n")
result=data.get(subject)

if result is not None:
    print("Marks:" , result)
else:
    print("Subject not found") 