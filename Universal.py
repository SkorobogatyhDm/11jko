def Base(input_base, dec_num, output_base):
    if input_base < 2 or input_base > 16 or output_base < 2 or output_base > 16:
        return "Основание СС должно быть от 2 до 16."
    
    try:
        number = int(dec_num, input_base)  
    except ValueError:
        return "Некорректное число в данной системе счисления."

    if output_base == 2:
        return int_dva(number)  # Перевод в двоичную СС
    elif output_base == 8:
        return int_vosem(number)  # Перевод в восьмеричную СС
    elif output_base == 10:
        return str(number)  # Десятичная СС
    elif output_base == 16:
        return int_shestnadtsat(number)  # Перевод в шестнадцатеричную СС
    else:
        return "Некорректное основание СС."
    
def int_conv(number):  # Десятичная СС
    return str(int(number, 10))

def int_dva(number):  # Двоичная СС
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    return result

def int_vosem(number):  # Восьмеричная СС
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = str(number % 8) + result
        number //= 8
    return result

def int_shestnadtsat(number):  # Шестнадцатеричная СС
    alf = {
        0: "0", 
        1: "1", 
        2: "2", 
        3: "3", 
        4: "4", 
        5: "5", 
        6: "6", 
        7: "7", 
        8: "8", 
        9: "9", 
        10: "A", 
        11: "B", 
        12: "C", 
        13: "D", 
        14: "E", 
        15: "F",
    }
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = alf[number % 16] + result
        number //= 16
    return result

if __name__ == "__main__":
    dec_num = input("Введите число: ")
    input_base = int(input("Введите начальную СС (2, 8, 10, 16): "))
    output_base = int(input("Введите СС, в которую хотите преобразовать (2, 8, 10, 16): "))
    print(Base(input_base, dec_num, output_base))