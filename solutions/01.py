def f1():
    for num1 in numbers:
        num2 = 2020 - num1

        if num2 in numbers:
            print(num1, num2, num1*num2)

            return

def f2():
    for num1 in numbers:
        for num2 in numbers:
            num3 = 2020-(num1+num2)

            if num3 in numbers:
                print(num1, num2, num3, num1*num2*num3)

                return

from input_loader import load_input

numbers = sorted([int(num) for num in load_input().split()])

f1()
f2()