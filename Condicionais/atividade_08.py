letter = input("Digite uma letra: ")[0]

vowels = ["A", "E", "I", "O", "U"]

if not letter.isalpha():
    print("Isso não é uma letra do alfabeto!")
elif letter.upper() in vowels:
    print(f"A letra {letter} é uma vogal.")
else:
    print(f"A letra \"{letter}\" é uma consoante.")
