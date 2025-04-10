from printList import get_text_list
from validNumber import get_number


def is_prime(num1, num2):
    primes = []
    not_primes = []
    for num in range(num1, num2 + 1):
        divisible = 0
        for y in range(1, num + 1):
            if num % y == 0:
                divisible += 1
        if divisible == 2:
            primes.append(num)
        else:
            not_primes.append(num)
    print(f"Os números primos são: {get_text_list(primes)}")
    print(f"Os números não primos são: {get_text_list(not_primes)}")


number1 = get_number("Digite o primeiro número do intervalo: ")
number2 = get_number("Digite o segundo número do intervalo: ")
is_prime(number1, number2)
