from Loops.printList import get_text_list
from Loops.validNumber import get_number, clear

print("Calculo de média de notas")
print("-"*25)

grades = []

while True:
    grade = get_number("Digite a nota que deseja calcular: ")

    if grade == -1:
        break
    if grade < 0:
        continue

    clear()
    grades.append(grade)
    print("Nota adicionada com sucesso. Digite -1 quando quiser sair.")

# grades_sum = sum(grades)
grades_sum = 0

for x in grades:
    grades_sum += x

average = grades_sum / len(grades)

print(f"A média das notas {get_text_list(grades)} é {average}")