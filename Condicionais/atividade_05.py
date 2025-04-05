from validNumber import get_number


def is_triangle(a, b, c):
    if (
            (a + b) > c
            and (a + c) > b
            and (b + c) > a
    ):
        return True
    else:
        return False


def define_triangle():
    a = get_number("Insira o primeiro valor: ")
    b = get_number("Insira o segundo valor: ")
    c = get_number("Insira o terceiro valor: ")

    if is_triangle(a, b, c):
        if a == b and b == c:
            print("Isso é um triângulo equilátero.")
        elif a == b or b == c or a == c:
            print("Isso é um triângulo isósceles.")
        else:
            print("Isso é um triângulo escaleno.")
    else:
        print("Esses valores não podem formar um triângulo.")


define_triangle()
