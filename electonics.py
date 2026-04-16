import os 
data={
    "Monitor in 10k":r"C:\Users\shrip\OneDrive\Documents\GitHub\aarav",
    "Monitor under 25k":r"C:\Users\shrip\OneDrive\Documents\GitHub\aarav",
    "Keyboard under 1k":r"C:\Users\shrip\OneDrive\Documents\GitHub\aarav",
    "Keyborad in 4k":r"C:\Users\shrip\OneDrive\Documents\GitHub\aarav",
    "GPU under 20k":r"C:\Users\shrip\OneDrive\Documents\GitHub\aarav",
    "GPU under 25k":r"C:\Users\shrip\OneDrive\Documents\GitHub\aarav"
}

device=input("Enter a choice: " 
             "\n1.Monitor in 10k"
             "\n2.Monitor under 25k"
             "\n3.Keyboard under 1k"
             "\n4.Keyboard in 4k"
             "\n5.GPU under 20k"
             "\n6.GPU under 25k\n")

result=data.get(device)

if device == "1":
    os.startfile("Lenevo 10k.png")

elif device == "2":
    os.startfile("LG 22k.png")

elif device == "3":
    os.startfile("Evofox 1k.png")

elif device == "4":
    os.startfile("Kero 4k.png")

elif device == "5":
    os.startfile("RX580 16k.png")

elif device == "6":
    os.startfile("ASUS 37k.png")

else:
    print("File not found")