def int_fract(dec_num):
    int_part = ""
    fract_part = ""
    flag = False
    for i in dec_num:
        if i == ",":
            flag = True
            continue
        if flag == False:
            int_part = int_part + i
        else:
            fract_part = fract_part + i
    if flag == False:
        return str(int_conv(int_part))
    else:
        return str(int_conv(int_part)) + "," + str(fract_conv(fract_part))[2:]

def int_conv(dec_num):
    index = len(dec_num) - 1
    result = 0
    for i in dec_num:
        result += int(i) * (2 ** index)
        index -= 1
    return result

def fract_conv(dec_num):
    index = 1
    result = 0
    for i in dec_num:
        if index <= len(dec_num):
            result += int(i) * (2 ** -index)
            index += 1
    return result

if __name__ == "__main__":
    dec_num = str(input("Введите двоичное число: "))
    print(int_fract(dec_num))