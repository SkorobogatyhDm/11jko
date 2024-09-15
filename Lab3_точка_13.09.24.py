def convert_to_base():
    try:
        num_bytes = int(input("Введите количество байт: "))
        number = input("Введите число (может быть отрицательным, с десятичной точкой): ")
        input_base = int(input("Введите систему счисления исходного числа (от 2 до 16): "))
        output_base = int(input("Введите систему счисления результата (от 2 до 16): "))
    except ValueError:
        return "Введите корректные значения!"

    if input_base < 2 or input_base > 16 or output_base < 2 or output_base > 16:
        return "Основание системы счисления должно быть между 2 и 16!"

    num_to_char = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    char_to_num = {v: k for k, v in num_to_char.items()}

    def is_valid_digit(char, base):
        return char in char_to_num and char_to_num[char] < base

    def validate_number(number, base):
        if number[0] == '-':
            number = number[1:]
        integer_part = ""
        fractional_part = ""
        found_dot = False
        for char in number:
            if char == '.':
                if found_dot:
                    return False
                found_dot = True
                continue
            if found_dot:
                fractional_part += char
            else:
                integer_part += char
        return all(is_valid_digit(char, base) for char in integer_part) and \
               all(is_valid_digit(char, base) for char in fractional_part)

    if not validate_number(number, input_base):
        return "Число содержит недопустимые символы для указанной системы счисления!"

    is_negative = number[0] == '-'
    if is_negative:
        number = number[1:]

    integer_part = ""
    fractional_part = ""
    found_dot = False
    for char in number:
        if char == '.':
            found_dot = True
            continue
        if found_dot:
            fractional_part += char
        else:
            integer_part += char

    def to_binary(integer_part, base):
        if integer_part == "":
            return "0"
        dec_value = 0
        for i in range(len(integer_part)):
            char = integer_part[-(i + 1)]
            dec_value += char_to_num[char] * (base ** i)
        binary_value = ""
        while dec_value > 0:
            binary_value = str(dec_value % 2) + binary_value
            dec_value //= 2
        return binary_value

    def fractional_to_binary(fractional_part, base):
        if fractional_part == "":
            return ""
        dec_value = 0
        for i in range(len(fractional_part)):
            char = fractional_part[i]
            dec_value += char_to_num[char] * (base ** -(i + 1))
        binary_value = ""
        count = 0
        while dec_value > 0 and count < 50:  
            dec_value *= 2
            bit = int(dec_value)
            binary_value += str(bit)
            dec_value -= bit
            count += 1
        return binary_value

    integer_bin = to_binary(integer_part, input_base)
    fractional_bin = fractional_to_binary(fractional_part, input_base)
    full_binary = integer_bin + fractional_bin
    if full_binary == "":
        full_binary = "0"
    dot_position = len(integer_bin)
    shifted_binary = "1" + full_binary[dot_position:]
    order = dot_position
    order_bin = ""
    if order < 0:
        order = -order
        order_bin = "1"
    else:
        order_bin = "0" 
    while order > 0:
        order_bin = str(order % 2) + order_bin
        order //= 2
    while len(order_bin) < 8:
        order_bin = '0' + order_bin
    mantissa = shifted_binary[1:] 
    while len(mantissa) < 8:
        mantissa += "0"
    sign = "1" if is_negative else "0"
    internal_representation = sign + order_bin + mantissa
    total_length = num_bytes * 8
    if len(internal_representation) > total_length:
        internal_representation = internal_representation[:total_length]
    elif len(internal_representation) < total_length:
        internal_representation = internal_representation + '0' * (total_length - len(internal_representation))

    def binary_to_base(binary_value, base):
        dec_value = 0
        for i in range(len(binary_value)):
            bit = binary_value[-(i + 1)]
            dec_value += int(bit) * (2 ** i)

        base_value = ""
        if dec_value == 0:
            base_value = "0"
        while dec_value > 0:
            base_value = num_to_char[dec_value % base] + base_value
            dec_value //= base

        return base_value

    base_value = binary_to_base(internal_representation, output_base)
    required_length = num_bytes * 2
    if len(base_value) < required_length:
        base_value = '0' * (required_length - len(base_value)) + base_value

    return (f"Внутреннее представление (двоичное): {internal_representation}\n"
            f"Результат в системе счисления {output_base}: {base_value}")

if __name__ == "__main__":
    print(convert_to_base())