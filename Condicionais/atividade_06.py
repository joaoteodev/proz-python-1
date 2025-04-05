from validNumber import get_number

grade = get_number("Digite a nota do aluno: ")

if grade < 0:
    print("A nota do aluno não pode ser menor que 0.")
elif grade < 7:
    print("O aluno foi reprovado.")
else:
    print("O aluno foi aprovado!")
