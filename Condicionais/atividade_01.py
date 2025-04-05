from validNumber import get_number

number = get_number("Digite um número: ")

if number % 2 == 0:
    print(f"{number} é par!")
else:
    print(f"{number} é impar!")
