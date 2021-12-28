number = int(input("Enter number: "))
n1 = 0
n2 = 1
count = 0
if number <= 0:
    print("Please enter a positive number.")
elif number == 1:
    print("Fibonacci sequence upto", number)
    print(n1)
else:
    print("Fibonacci sequence")
    while count <= number:
        print(n1)
        nextnum = n1 + n2
        n1 = n2
        n2 = nextnum
        count = count + 1