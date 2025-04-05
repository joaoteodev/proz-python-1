from validNumber import get_number

celsius = get_number("Digite a temperatura em graus Celsius: ")
fahrenheit = (celsius * 9 / 5) + 32
print(f"O valor de {celsius}°C em fahrenheit é: {fahrenheit:.2f}°F")
