import os
from time import sleep


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_number(text):
    while True:
        input_number = input(text).replace(",", ".")
        try:
            if "." in input_number:
                return float(input_number)
            else:
                return int(input_number)

        except ValueError:
            print("O valor digitado não é um número válido. Tente novamente.")
            sleep(0.5)
            clear()
