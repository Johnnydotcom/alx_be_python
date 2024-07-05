number = int(input("Enter the size of the pattern: "))
count = 1
while count <= number :
    for i in range(0, number) :
        print("*", end="")
    count+=1
    print("\n")

