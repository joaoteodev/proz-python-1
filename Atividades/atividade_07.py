from validNumber import get_number

value = get_number("Digite o valor: ")
tax = get_number("Digite a taxa de juros: ")
years = get_number("Digite o números de anos: ")
result = value + (value * tax * years / 100)

if years < 0:
    print("O ano não pode ser menor que 1.")
else:
    print(
        f"O valor de R$ {value} com uma taxa de juros de {tax}% durante {years} {"ano" if years < 2 else "anos"}, equivale a R$ {result:.2f}")
