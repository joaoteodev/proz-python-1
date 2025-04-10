from validNumber import get_number


print("Números pares no intervalo de número")
print("-" * 30)

number1 = get_number("Digite o primeiro número: ")
number2 = get_number("Digite o segundo número: ")

evens = []

for x in range(number1, number2 + 1):
    if x % 2 == 0:
        evens.append(x)

print("-" * 30)
print(f"{", ".join(map(str, evens[0:-2]))} e {evens[-1]}.")
