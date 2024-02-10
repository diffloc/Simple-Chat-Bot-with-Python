class Bot:
    def __init__(self, name, year):
        self.bot_name = name
        self.birth_year = year


def greet(bot_name, birth_year):
    print(f"Hello! my name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print('Please, remind me your name.')
    user_name = input()
    print(f"What a great name you have, {user_name}!")


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    remainder = []

    for i in range(3):
        remainder.append(int(input()))

    your_age = (remainder[0] * 70 + remainder[1] * 21 + remainder[2] * 15) % 105

    print(f"Your age is {your_age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("""Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")
    while True:
        answer = int(input())
        if answer == 2:
            break  # Correct answer, exit loop
        else:
            print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')


beep_boop = Bot("David", 2024)

greet(beep_boop.bot_name, beep_boop.birth_year)
remind_name()
guess_age()
count()
test()
end()
