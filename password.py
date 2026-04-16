while True:
    import random

    letter="abcdefghigkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789" 
    symbols="!@#$%^&*"

    length=int(input("Enter the length of the password\n"))

    password=[]

    password.append(random.choice(letter))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))

    for i in range(length - 3):
        password.append(random.choice(letter + numbers + symbols))

        random.shuffle(password)
        print("Your password is:", "".join(password))