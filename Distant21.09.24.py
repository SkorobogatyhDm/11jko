import math
# Графические задания
#def Number1():
   # a = int(input("Введите число точек по горизонтали: "))
    #b = int(input("Введите число точек по вертикали: "))
    #c = a * b #Умножение точек горизонтали и вертикали
    #return c

#if __name__ == "__main__":
    #result = Number1() 
    #print("Общее количество точек:", result)

#def Number2():
   #a = int(input("Со скольки начаналось: "))
   #b = int(input("До чего дошло: "))
    #c = math.log2(a) # находистся степень числа
    #d = math.log2(b) # находистся степень числа
    #f = d / c 
    #return f
#if __name__ == "__main__":
    #result = Number2() 
    #print("В:", result)

#def Number3():
    #a = int(input("Введите число точек по горизонтали: "))
    #b = int(input("Введите число точек по вертикали: "))
    #d = int(input("сколько КБ: "))
    #c = a * b #Умножение точек горизонтали и вертикали
    #bit = d * 1024 * 8 # Преоброзование в бит
    #z = bit / c # Сколько бит на 1 точку
    #v = 2 ** z # сколко цветов в итоге
    #return v
#if __name__ == "__main__":
    #result = Number3() 
    #print("Цветов:", result)

#def Number4():
    #a = int(input("Сколько цветов в ресунке: "))
    #b = int(input("Сколько байт содержит рисунок: "))
    #f = math.log2(a) # находистся степень числа
    #c = f / 8 # биты в байты
    #v = b / c
    #return v
#if __name__ == "__main__":
    #result = Number4() 
    #print("Точек:", result)

#Звуковые задачи
#def Number1():
    #a = int(input("Сколько минут: "))
    #b = float(input("Сколько кГц: "))
    #c = int(input("Какого разрешение(В битах): "))
    #d = a * 60 # Перевод из минут в секунды
    #f = b * 1000 # Перевод из кГц в Гц
    #v = f * d * c # Нахождение объема памяти
    #return v 
#if __name__ == "__main__":
    #result = Number1() 
    #print("Объем:", result)

#def Number2():
    #a = int(input("Сколько минут: "))
    #c = float(input("Какого разрешение(В Мбайт): "))
    #d = a * 60 # Перевод из минут в секунды
    #f = c * (1024 ** 2) * 8 # Перевод в биты
    #v = f / (d * 8) # Нахождение объема памяти
    #kHz = v / 1000
    #return kHz
#if __name__ == "__main__":
    #result = Number2() 
    #print("кГц:", result)

#def Number3():
    #b = float(input("Сколько кГц: "))
    #c = float(input("Какой объем(В Гб): "))
    #z = b * 1000 # Перевод из кГц в Гц
    #f = c * (1024 ** 3) # Перевод в биты
    #t = f / z / 2 # Считает время в сек
    #t2 = t / 60 # Считает время в мин
    #return t2
#if __name__ == "__main__":
    #result = Number3() 
    #print("Время:", result)

#def Number4():
    #a = int(input("Какой обьём: "))
    #b = float(input("Сколько кГц: "))
    #c = float(input("Какой объем(В Кб): "))
    #z = b * 1000 # Перевод из кГц в Гц
    #f = c * 1024 * 8 # Перевод в биты
    #t = f / z / a # Находим время 
    #return t
#if __name__ == "__main__":
    #result = Number4() 
    #print("Время:", result)

def Number5():
    a = int(input("Какое разрешение: "))
    b = float(input("Сколько кГц: "))
    t = int(input("Время: "))
    t2 = t * 60 # Перевод в секунды
    z = b * 1000 # Перевод из кГц в Гц
    v = t2 * z * a
    return v
if __name__ == "__main__":
    result = Number5() 
    print("Объем:", result)
