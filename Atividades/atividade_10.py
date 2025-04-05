from validNumber import get_number

grade1 = get_number("Digite a primeira nota: ")
grade1_weight = get_number("Digite o peso dessa nota: ")

grade2 = get_number("Digite a segunda nota: ")
grade2_weight = get_number("Digite o peso dessa nota: ")

grade3 = get_number("Digite a terceira nota: ")
grade3_weight = get_number("Digite o peso dessa nota: ")

average = ((grade1 * grade1_weight) + (grade2 * grade2_weight) + (grade3 * grade3_weight)) / (
        grade1_weight + grade2_weight + grade3_weight)

print(f"A media ponderada entre as notas {grade1}, {grade2} e {grade3} é: {average:.2f}")
