# Getting user input
number = int(input("Number: "))

prev = 0
cur = 1
next = 1

if number > 0:
    print(prev)
    if number > 1:
        print(cur)
        for _ in range(2, number):
            print(next)
            prev = cur
            cur = next
            next = prev + cur
        
else:
    print("Invalid input")
