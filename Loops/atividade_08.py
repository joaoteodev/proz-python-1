from printList import get_text_list
from validNumber import get_number

print("Seqência de Fibonacci\n")


def get_fibonacci_sequence(n):
    # fibonacci = [0, 1]
    # fibonacci = [1]
    fibonacci = []
    #
    # if n < 1:
    #     return -1
    #
    # if n == 1:
    #     return 0

    while len(fibonacci) < n:
        # fibonacci.append(fibonacci[-1] + fibonacci[-2])
        if len(fibonacci) == 0 or len(fibonacci) == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci


number = get_number("Digite quantos números da sequência deseja exibir: ")

if number < 1:
    print("Nenhum número foi solicitado.")

if number == 1:
    print("O número é: 1.")

if number > 1:
    sequence = get_fibonacci_sequence(number)
    print(f"Os números são: {get_text_list(sequence)}")
