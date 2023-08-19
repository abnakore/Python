# main function
def main():
    num = int(input("Enter a number: "))

    print(factorial(num))

# factorial function
def factorial(n):

    factorial = 1
    for i in range(n):
        factorial *= (i + 1)

    return factorial

main()