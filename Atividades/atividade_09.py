from validNumber import get_number

value1 = get_number("Digite o primeiro valor: ")
value2 = get_number("Digite o segundo valor: ")

value3 = value2
value2 = value1
value1 = value3

print(f"Valor 1: {value1}")
print(f"Valor 2: {value2}")
