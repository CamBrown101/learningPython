def add(x, y):
    result = x + y
    print(result)


add(5, 3)


def say_hello(name, surname):
    print('Hello!')


# say_hello(surname="Bob", name="Smith")


def divide(divided, divisor):
    if divisor != 0:
        print(divided / divisor)
    else:
        print("You fool!")


divide(divided=15, divisor=0)
