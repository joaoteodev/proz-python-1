from validNumber import get_number

age = get_number("Digite sua idade: ")

if age < 0:
    print("Idade não pode ser menor que 0.")
elif age < 18:
    print("Infelizmente você não pode dirigir!")
else:
    print("Tudo certo. Você pode dirigir!")
