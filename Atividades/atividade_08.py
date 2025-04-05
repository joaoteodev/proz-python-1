from validNumber import get_number

age_years = get_number("Digite sua idade em anos: ")

age_months = age_years * 12
age_days = age_years * 365

print(f"Sua idade em meses é: {age_months} meses.")
print(f"Sua idade em dias é: {age_days} dias.")
