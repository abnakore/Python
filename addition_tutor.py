import random

# main function
def main():
    quize(0)

def quize(scores):
    # Generating random int
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)

    # Correct answer
    _answer = first_number + second_number
    # getting the user inputs
    answer = int(input(f"what is {first_number} + {second_number}? "))

    if answer == _answer:
        print("Correct answer")
        quize(scores + 1)
    else:
        print("Wrong answer!!!")
        print(f"the correct answer is {_answer}")
        print(f"Your total score(s) is {scores}")


main()