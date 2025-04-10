from Loops.printList import get_text_list
from validNumber import get_number

print("Números pares no intervalo de número")
print("-" * 30)

number1 = get_number("Digite o primeiro número: ")
number2 = get_number("Digite o segundo número: ")

evens = []

for x in range(number1, number2 + 1):
    if x % 2 == 0:
        evens.append(x)

# evens_size = len(evens)
# evens_text = ""
#
#
# for x in range(evens_size):
#     if x == evens_size - 2:
#         evens_text += f"{evens[x]} e "
#         continue
#
#     if x == evens_size - 1:
#         evens_text += f"{evens[x]}."
#         continue
#
#     evens_text += f"{evens[x]}, "

evens_text = get_text_list(evens)
print("-" * 30)
print(evens_text)
