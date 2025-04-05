from validNumber import *

number1 = get_number("Digite o primeiro número: ")
number2 = get_number("Digite o segundo número: ")
number3 = get_number("Digite o terceiro número: ")
print(f"A média dos números {number1}, {number2}, {number3} é: {((number1 + number2 + number3) / 3):.2f}")
