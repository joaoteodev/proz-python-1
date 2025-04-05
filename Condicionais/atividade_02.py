from validNumber import get_number

number1 = get_number("Digite o primeiro número: ")
number2 = get_number("Digite o segundo número: ")

if number1 > number2:
    print(f"{number1} é maior que {number2}!")
elif number1 < number2:
    print(f"{number2} é maior que {number1}!")
else:
    print("Os números são iguais!")
