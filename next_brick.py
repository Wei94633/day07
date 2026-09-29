import random

def random_number():
    numbers = [1, 2, 3, 4, 5, 6]
    number = random.choice(numbers)
    return number
print(random_number())