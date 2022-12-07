import random


while True:
    length = int(input("\nEntern the length of password: "))

    if length < 12:
        print("Password Must Be Atleast Of 12 Characters!! \n")
    else:
        Lowercase_Characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                                'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        Uppercase_Characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        Symbols = ['@', '#', '$', '%', '=', ':',
                '?', '.', '/', '|', '~', '*', '(', ')']

        all = Lowercase_Characters + Uppercase_Characters + Digits + Symbols

        temp = random.sample(all, length)
        a=""
        for i in temp:
            a=a+i
        print("Your password is:",a)
        break
