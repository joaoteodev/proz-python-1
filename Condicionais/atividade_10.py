from validNumber import get_number

age = get_number("Digite a idade: ")

if age <= 0:
    print("A idade não pode ser menor ou igual a 0.")
elif age > 0 and age <= 4:
    print("É um bebê!")
elif age >= 5 and age <= 12:
    print("É uma criança!")
elif age >= 13 and age <= 15:
    print("É um pré-adolescente!")
elif age >= 16 and age <= 17:
    print("É um adolescente!")
elif age >= 18 and age <= 21:
    print("É um jovem-adulto!")
elif age >= 22 and age <= 69:
    print("É um adulto!")
elif age >= 22 and age <= 69:
    print("É um adulto!")
elif age >= 70 and age <= 110:
    print("É um idoso!")
else:
    print("É um ancião!!!")
