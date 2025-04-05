from validNumber import get_number

number = get_number("Digite um número: ")

if number % 3 == 0 and number % 5 == 0:
    print(f"O número {number} é divisível por 3 e por 5, sendo respectivamente os resultados:\n"
          f" {number} / 3 = {int(number / 3)}\n"
          f" {number} / 5 = {int(number / 5)}\n")
else:
    print(f"O número {number} não pode ser divido por 3 e por 5")
