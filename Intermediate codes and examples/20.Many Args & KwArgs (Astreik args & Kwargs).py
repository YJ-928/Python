def add(*args):
    """Function with many arguments as input"""
    total = 0
    for i in args:
        total += i
    return print(f"The addition of {args} Numbers is: {total}")


add(2, 3, 4, 5, 6, 7, 8, 90, 1)


def calculate(num, **kwargs):
    """Function with many Keyword Arguments"""
    num += kwargs["add"]
    num *= kwargs["multiply"]
    num /= kwargs["divide"]

    return print(f"Total after performing {kwargs} operations on your starting number: {num}")


calculate(9, add=2, multiply=3, divide=1)
