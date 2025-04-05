from validNumber import get_number


def discount():
    price = get_number("Digite o preço do produto: ")

    if price <= 100:
        print("O valor do produto precisa ser maior que R$ 100")
        return

    discount = get_number("Digite a porcentagem do desconto: ")
    final = price - (price * (discount / 100))

    print(f"O valor do produto com desconto é: R$ {final:.2f}")


discount()
