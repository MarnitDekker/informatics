def convert_to_decimal(number, base):
    # Функция для преобразования числа из p-ой системы счисления в десятичную систему
    decimal = 0
    power = 0
    number1 = int(number)
    while number1 > 0:
        digit = number1 % 10
        decimal += digit * (base ** power)
        power += 1
        number1 //= 10
    return decimal

def convert_from_decimal(number, base):
    # Функция для преобразования числа из десятичной системы в p-ую систему счисления
    result = ""
    while number > 0:
        digit = number % base
        result = str(digit) + result
        number //= base
    return int(result)

def addition(num1, num2, base):
    # Функция для выполнения операции сложение в p-ой системе счисления
    decimal_num1 = convert_to_decimal(num1, base)
    decimal_num2 = convert_to_decimal(num2, base)
    result = decimal_num1 + decimal_num2
    return convert_from_decimal(result, base)

def subtraction(num1, num2, base):
    # Функция для выполнения операции вычитание в p-ой системе счисления
    decimal_num1 = convert_to_decimal(num1, base)
    decimal_num2 = convert_to_decimal(num2, base)
    result = decimal_num1 - decimal_num2
    return convert_from_decimal(result, base)

# Пример использования программы:
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
base = int(input("Введите систему счисления (2, 8 или 16): "))

result = addition(num1, num2, base)
print(f"Результат сложения: {result}")

result = subtraction(num1, num2, base)
print(f"Результат вычитания: {result}")