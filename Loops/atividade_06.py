import random

from validNumber import *


random_number = random.randint(1, 51)

while True:
    number = get_number("Digite um número entre 1 e 50: ")

    if number == random_number:
        clear()
        print(f"Você acertou! O número era {random_number}.")
        break
    elif number > random_number:
        clear()
        print("O número é menor.")
    else:
        clear()
        print("O número é maior.")
