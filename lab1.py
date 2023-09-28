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

def convert_to_decimal_for_fraction(number, base):
    decimal1 = 0
    decimal2 = 0
    power1 = 0
    number_list = number.split(".")
    number1 = int(number_list[0])
    number2 = int(number_list[1])
    power2 = (len(str(number2))+1) * (-1)
    while power2 != -1:
        digit = number2 % 10
        power2 += 1
        decimal2 = decimal2 + digit * (base ** power2)
        number2 //= 10
    while number1 > 0:
        digit = number1 % 10
        decimal1 += digit * (base ** power1)
        power1 += 1
        number1 //= 10
    return str(decimal1) + '.' + str(decimal2)[2:]

def convert_from_decimal_for_fraction(number, base):
    decimal2 = ''
    result = ''
    number_list = str(number).split(".")
    number1 = int(number_list[0])
    number2 = '0.' + number_list[1]
    power2 = (len(str(number2))+1) * (-1)
    while len(decimal2) < 7:
        number2 = float(number2) * base
        decimal2 = decimal2 + str(number2)[0]
        number2 //= 10
    while number1 > 0:
        digit = number1 % base
        result = str(digit) + result
        number1 //= base
    return str(result) + '.' + str(decimal2)


def convert_to_decimal_for_division(number, base):
    decimal1 = 0
    decimal2 = 0
    power1 = 0
    power2 = 0
    number_list = number.split(".")
    number1 = int(number_list[0])
    number2 = int(number_list[1])
    while number1 > 0:
        digit1 = number1 % 10
        decimal1 += digit1 * (base ** power1)
        power1 += 1
        number1 //= 10
    while number2 > 0:
        digit2 = number2 % 10
        decimal2 += digit2 * (base ** power2)
        power2 += 1
        number2 //= 10
    return str(decimal1) + "." + str(decimal2)

def convert_from_decimal_for_division(number, base):
    number_list = str(number).split(".")
    number1 = int(number_list[0])
    number2 = int(number_list[1])
    result1 = ""
    result2 = ""
    while number1 > 0:
        digit1 = number1 % base
        result1 = str(digit1) + result1
        number1 //= base
    while number2 > 0:
        digit2 = number2 % base
        result2 = str(digit2) + result2
        number2 //= base
    if number1 == 0:
        return "0" + "." + str(result2)
    elif number2 == 0:
        return str(result1) + "." + "0"
    else:
        return str(result1) + "." + str(result2)

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
    if "." in num1:
        decimal_num1 = convert_to_decimal_for_fraction(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    elif "." in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal_for_fraction(num2, base)
    elif "." in num1 and "." in num2:
        decimal_num1 = convert_to_decimal_for_fraction(num1, base)
        decimal_num2 = convert_to_decimal_for_fraction(num2, base)
    elif "." not in num1 and "." not in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    
    if '.' in num1 or '.' in num2:
        result = float(decimal_num1) + float(decimal_num2)
        return convert_from_decimal_for_fraction(result, base)
    else:
        result = decimal_num1 + decimal_num2
        return convert_from_decimal(result, base)

def subtraction(num1, num2, base):
    # Функция для выполнения операции вычитание в p-ой системе счисления
    if "." in num1:
        decimal_num1 = convert_to_decimal_for_fraction(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    elif "." in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal_for_fraction(num2, base)
    elif "." in num1 and "." in num2:
        decimal_num1 = convert_to_decimal_for_fraction(num1, base)
        decimal_num2 = convert_to_decimal_for_fraction(num2, base)
    elif "." not in num1 and "." not in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    
    if '.' in num1 or '.' in num2:
        result = float(decimal_num1) - float(decimal_num2)
        return convert_from_decimal_for_fraction(result, base)
    else:
        result = decimal_num1 - decimal_num2
        if result < 0:
            return convert_from_decimal(abs(result), base)
        else:
            return convert_from_decimal(result, base)

def multiplication(num1, num2, base):
    # Функция для выполнения операции вычитание в p-ой системе счисления
    if "." in num1:
        decimal_num1 = convert_to_decimal_for_fraction(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    elif "." in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal_for_fraction(num2, base)
    elif "." in num1 and "." in num2:
        decimal_num1 = convert_to_decimal_for_fraction(num1, base)
        decimal_num2 = convert_to_decimal_for_fraction(num2, base)
    elif "." not in num1 and "." not in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    
    if '.' in num1 or '.' in num2:
        result = float(decimal_num1) * float(decimal_num2)
        return convert_from_decimal_for_fraction(result, base)
    else:
        result = decimal_num1 * decimal_num2
        if result == 0:
            return 0
        else:
            return convert_from_decimal(result, base)

def division(num1, num2, base):
    # Функция для выполнения операции вычитание в p-ой системе счисления
    if "." in num1:
        decimal_num1 = convert_to_decimal_for_division(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    elif "." in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal_for_division(num2, base)
    elif "." in num1 and "." in num2:
        decimal_num1 = convert_to_decimal_for_division(num1, base)
        decimal_num2 = convert_to_decimal_for_division(num2, base)
    elif "." not in num1 and "." not in num2:
        decimal_num1 = convert_to_decimal(num1, base)
        decimal_num2 = convert_to_decimal(num2, base)
    if '.' in num1 or '.' in num2:
        result = float(decimal_num1) / float(decimal_num2)
        return convert_from_decimal_for_fraction(result, base)
    else:
        result = decimal_num1 / decimal_num2
        if type(result) == int:
            return convert_from_decimal(result, base)
        else:
            return convert_from_decimal_for_fraction(result, base)

num11 = input("Введите первое число: ")
if '-' in num11:
    num1 = num11[1:]
else:
    num1 = num11
num22 = input("Введите второе число: ")
if '-' in num22:
    num2 = num22[1:]
else:
    num2 = num22
base = int(input("Введите систему счисления (2 или 8): "))


if '-' in num11 and '-' in num22:
    result = addition(num1, num2, base)
    print(f"Результат сложения: 1'{result}")

    if abs(float(num1)) > abs(float(num2)):
        result = subtraction(num1, num2, base)
        print(f"Результат вычитания: 1'{result}")
    else:
        result = subtraction(num1, num2, base)
        print(f"Результат вычитания: 0'{result}")
    
    result = multiplication(num1, num2, base)
    print(f"Результат умножения: 0'{result}")

    result = division(num1, num2, base)
    print(f"Результат деления: 0'{result}")

elif '-' in num11 and '-' not in num22:
    if abs(int(num11)) > abs(int(num22)):
        result = subtraction(num1, num2, base)
        print(f"Результат сложения: 1'{result}")

        result = addition(num1, num2, base)
        print(f"Результат вычитания: 1'{result}")
    else:
        result = subtraction(num1, num2, base)
        print(f"Результат сложения: 1'{result}") 

        result = addition(num1, num2, base)
        print(f"Результат вычитания: 0'{result}")

    result = multiplication(num1, num2, base)
    print(f"Результат умножения: 1'{result}")

    result = division(num1, num2, base)
    print(f"Результат деления: 1'{result}")

elif '-' in num22 and '-' not in num11:
    if len(num11) < len(num22):
        result = subtraction(num1, num2, base)
        print(f"Результат сложения: 1'{result}")

        result = addition(num1, num2, base)
        print(f"Результат вычитания: 0'{result}")
    else:
        result = addition(num1, num2, base)
        print(f"Результат сложения: 0'{result}")

        result = subtraction(num1, num2, base)
        print(f"Результат вычитания: 0'{result}")

    result = multiplication(num1, num2, base)
    print(f"Результат умножения: 1'{result}")

    result = division(num1, num2, base)
    print(f"Результат деления: 1'{result}")

else:
    if num11 == '0' and num22 != "0":
        print(f"Результат сложения: 0'{num22}")

        print(f"Результат вычитания: 1'{num22}")

        print(f"Результат умножения: 0")

        print(f"Результат деления: 0")

    elif str(num22) == '0':
        print(f"Результат сложения: 0'{num11}")

        print(f"Результат вычитания: 0'{num11}")

        print(f"Результат умножения: 0")

        print(f"Результата деления нет, так как на ноль делить нельзя")

    elif str(num22) == '0' and str(num11) == '0':
        print(f"Результат сложения: 0")

        print(f"Результат вычитания: 0")

        print(f"Результат умножения: 0")

        print(f"Результата деления нет, так как на ноль делить нельзя")
    else:
        result = addition(num1, num2, base)
        print(f"Результат сложения: 0'{result}")

        result = subtraction(num1, num2, base)
        print(f"Результат вычитания: 0'{result}")

        result = multiplication(num1, num2, base)
        print(f"Результат умножения: 0'{result}")

        result = division(num1, num2, base)
        print(f"Результат деления: 0'{result}")