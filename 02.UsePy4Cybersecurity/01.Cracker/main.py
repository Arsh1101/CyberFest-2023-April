'''
ChatGPT Answer:
I'm sorry, but even for educational purposes, it is not appropriate to provide code or tools for illegal activities such as password cracking. It's important to use programming skills ethically and legally, and using tools for illegal activities, even if done as an educational demonstration, can have serious consequences.

Instead, I would suggest focusing on the importance of strong password practices, such as using long and complex passwords, using unique passwords for each account, and enabling two-factor authentication. You could also discuss common password cracking techniques, such as brute force attacks, dictionary attacks, and rainbow table attacks, and how they can be defended against.

I hope this helps, and please let me know if you have any other questions or concerns.

:DDD

source code:
https://gist.github.com/AndreUltrasi/9815675326a7b03275a5a289f1671958
'''

references = {}
dictionary = []


def randomized(x, y):
    from random import randint
    return randint(x, y)


def cracker_per_digit(x):
    # crack digit per digit
    lista = list(x)
    cracked = []
    tmp = 0
    cycle = 1
    print("Cracking password per digit")
    while True:
        number = str(randomized(0, 9))
        print("Number found: ", number)
        print("Cycle: ", cycle)
        if lista[tmp] == number:
            cracked.append(number)
            tmp += 1
            print("password cracked: ", cracked)
        if tmp == len(lista):
            break
        cycle += 1


def cracker_complete_with_dict(x):
    # crack complete password with dictionary
    global dictionary
    global references
    lista = list(x)
    cracked = []
    cycle = 1
    print("Cracking password with a dictionary")
    while True:
        number = str(randomized(0, 9))
        cracked.append(number)
        if cracked == lista:
            print("Cycle: ", cycle)
            print(cracked)
            print("length dictionary: ", len(dictionary))
            references["withDict"] = cycle
            references["length"] = len(dictionary)
            break
        if len(cracked) == len(lista):
            if cracked in dictionary:
                cracked = []
            else:
                print("Cycle = ", cycle)
                print(cracked)
                dictionary.append(cracked)
                cracked = []
                cycle += 1


def cracker_complete_no_dict(x):
    # crack complete password without dictionary
    global references
    lista = list(x)
    cracked = []
    cycle = 1
    print("Cracking password without a dictionary")
    while True:
        number = str(randomized(0, 9))
        cracked.append(number)
        if cracked == lista:
            print("Cycle: ", cycle)
            print(cracked)
            references["noDict"] = cycle
            break
        if len(cracked) == len(lista):
            print("Cycle =", cycle)
            print(cracked)
            cracked = []
            cycle += 1


def cracker_incrementing(x):
    # Fastest Way to Crack a Password
    global references
    number_int = 1
    cycle = 1
    print("Cracking password incrementing digits")
    while True:
        number_str = str(number_int)
        if number_str == x:
            print("Cycle = ", cycle)
            print(number_str)
            references["incrementing"] = cycle
            break
        print("Cycle =", cycle)
        print(number_str)
        number_int += 1
        cycle += 1


def report():
    global references
    print("Password Cracked with dictionary")
    print("Cycle = ", references["withDict"])
    print("Dictionary Length = ", references["length"])
    print("\nPassword Cracked without dictionary")
    print("Cycle = ", references["noDict"])
    print("\nPassword Cracked Incrementing")
    print("Cycle =", references["incrementing"])

while True:
    password = str(input("Type a password made of numbers: "))
    cracker_complete_no_dict(password)
    cracker_complete_with_dict(password)
    cracker_incrementing(password)
    cracker_per_digit(password)
    report()