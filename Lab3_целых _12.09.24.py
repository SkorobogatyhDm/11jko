import math

def Main(operation, dec_num, input_base, output_base):
    if operation == '+':
        bit = int(input("Введите количество байт: ")) 
        return vnutri(int(dec_num, input_base), bit)
    elif operation == '-':
        return Base(input_base, int(dec_num, input_base), output_base)
    else:
        return "Некорректная операция. Пожалуйста, выберите '+' или '-'."

def Bit(bit):
    return "0" * (bit * 8)

def Base(input_base, dec_num, output_base):
    if output_base == 2:
        return int_dva(dec_num) # Перевод в двоичную СС
    elif output_base == 8:
        return int_vosem(dec_num) # Перевод в восьмеричную СС
    elif output_base == 10:
        return int_conv(dec_num) # Перевод в десятичную СС
    elif output_base == 16:
        return int_shestnadtsat(dec_num) # Перевод в шестнадцатеричную СС
    else:
        return "Некорректное СС."
    
def Start(input_base, output_base):
    if input_base < 2 or input_base > 16 or output_base < 2 or output_base > 16:
        return "Основание системы счисления должно быть от 2 до 16!"
def int_conv(dec_num): # Десятичная СС
    return str(dec_num)

def int_dva(dec_num): # Двоичная СС
    quotient = int(dec_num)
    result = ""
    while quotient > 1:
        result = str(quotient % 2) + result
        quotient = quotient // 2
    result = str(quotient) + result
    return result

def int_vosem(dec_num): # Восьмеричная СС
    quotient = int(dec_num)
    result = ""
    while quotient > 0:
        result = str(quotient % 8) + result
        quotient //= 8
    return result if result else "0"

def int_shestnadtsat(dec_num):  # Шестнадцатеричная СС
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
    quotient = int(dec_num)
    result = ""
    while quotient > 0:
        result = alf[quotient % 16] + result
        quotient //= 16
    return result if result else "0"

def vnutri(dec_num, bit):
    line = len(Bit(bit))
    binary_num = int_dva(dec_num)
    return binary_num.zfill(line)

def invert(dec_num, bit):
    line = len(Bit(bit))
    inverted = int_dva(dec_num)
    inverted = ''.join('1' if char == '0' else '0' for char in inverted)
    return inverted.zfill(line)

if __name__ == "__main__":
    dec_num = input("Введите число: ")
    input_base = int(input("Введите начальную СС (2, 8, 10, 16): "))
    operation = input("Нужно ли производить перевод целых, ДА то '+' если НЕТ то '-': ")

    if operation == '+':
        bit = int(input("Введите количество байт: ")) 
        minus = input("Число является отрицательным, если ДА то '-' если НЕТ то '+': ")
        if minus == '-':
            print(invert(int(dec_num, input_base), bit))
        else:
            print(vnutri(int(dec_num, input_base), bit))
    elif operation == '-':
        output_base = int(input("Введите СС, в которую хотите преобразовать (2, 8, 10, 16): "))
        print(Main(operation, dec_num, input_base, output_base))
    else:
        print("Некорректная операция. Пожалуйста, выберите '+' или '-'.")