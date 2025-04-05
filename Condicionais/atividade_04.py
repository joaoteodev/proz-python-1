from validNumber import get_number

number = get_number("Digite um número: ")

if number < 0:
    print(f"O número {number} é negativo.")
elif number > 0:
    print(f"O número {number} é positivo.")
else:
    print("O número 0 é neutro.")
