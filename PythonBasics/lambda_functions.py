# def add(x, y):
#     return x + y


# print(add(5, 7))

# lambda x, y: x + y

def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [double(x) for x in sequence]
doubled = list(map(double, sequence))
