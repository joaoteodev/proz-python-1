from validNumber import get_number

weight = get_number("Digite o seu peso em kg: ")
height = get_number("Digite sua altura em metros: ")
print(weight)
print(f"Seu IMC é {weight / (height * height):.2f}")
