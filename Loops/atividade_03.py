from validNumber import get_number

numbers = []

while len(numbers) < 5:
    if len(numbers) == 0:
        num = get_number("Digite um número: ")
        numbers.append(num)
    else:
        num = get_number("Digite outro número: ")
        numbers.append(num)

numbers_sum = 0

for x in range(0, len(numbers) - 1):
    numbers_sum += numbers[x]


print(f"{" + ".join(map(str, numbers))} = {numbers_sum}")
