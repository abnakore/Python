# main function
def main():
    # getting the user inputs
    card_number = input("Card Number: ")

    #print(check_sum(card_number))

    if check_sum(card_number):
        length = len(card_number)
        match first_two(card_number):
            case 34 | 37:
                if length == 15:
                    print("AMEX")
            case 51 | 52 | 53 | 54 | 55:
                if length == 16:
                    print("MasterCard")
            case 40 | 41 | 42 | 43 | 44| 45 | 46 | 47 | 48 | 49:
                if length == 13 or length == 16:
                    print("VISA")
            case _:
                print("INVALID")
            
        exit()

    print("INVALID")


def check_sum(num):
    num = int(num)
    sum = 0
    tmp = 0
    
    while num != 0:
        sum += num % 10
        num //= 10
        tmp = (num % 10) * 2
        if len(str(tmp)) > 1:
            for i in str(tmp):
                sum += int(i)
        else:
            sum += tmp
        num //= 10

    return sum % 10 == 0

def first_two(card_number):
    n = 0
    for i in range(2):
        n = (n * 10) + int(card_number[i])
    return n


main()