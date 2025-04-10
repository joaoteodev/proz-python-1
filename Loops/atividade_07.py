from validNumber import get_number


print("Fatorial de um número")
print("")

number = get_number("Digite um número: ")

factorial = 1
for x in range(number, 0, -1):
    factorial *= x

print(f"{number}! = {factorial}.")
