def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
    
if __name__ == "__main__":
    num = str(input("введите число: "))
    from_base = int(input("Введите начальную сс: "))
    to_base = int(input("Введите конечную сс: "))
    print (convert_base(num, to_base, from_base))