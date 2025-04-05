from validNumber import get_number

price = get_number("Digite o preço do produto: ")
discount = get_number("Digite a porcentagem do desconto: ")
total = price - (price * (discount / 100))
print(f"O preço do produto com desconto é: R$ {total:.2f}")
