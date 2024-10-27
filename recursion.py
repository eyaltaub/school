def factorial_calc(num):
    num = int(num)
    if num == 0:
        return 1
    return num * factorial_calc(num - 1)

number = input()
print(factorial_calc(number))


def add_by_one(x, y):
   if y == 0:
       return x
   return add_by_one(x + 1, y - 1)


def multiply_by_add(x, y):
    if y == 0:
        return 0
    return add_by_one(x, multiply_by_add(x, y - 1))


def factorial_by_multiply(num):
    if num == 0:
        return 1
    return multiply_by_add(num, factorial_by_multiply(num - 1))

print(factorial_by_multiply(6))