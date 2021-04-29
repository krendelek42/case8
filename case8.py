'''
Case-study №8 Fractals
Developers:   Dokukina K. (%),
              Nazirova E. (%)
'''

from turtle import *

def square(a):
    '''This fractal draws a square recursively.
        a - line length'''
    if a < 20:
        return
    down()
    for _ in range(4):
        forward(a)
        right(90)
    up()
    right(15)
    forward(a / 8)
    return square(a * 0.9)

def tree(h, an):
    '''This fractal draws a binary tree recursively.
                h - tree height
                an - angle value'''
    if h < 10:
        return
    else:
        dh = h//3
        forward(h)
        left(an)
        tree(h - dh ,an)
        right(2*an)
        tree(h - dh,an)
        left(an)
        backward(h)

def branch(n, size):
    '''This fractal draws a branch recursively.
        order - recursion depth
        size - line length'''
    if n == 0:
        left(180)
        return

    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        right(135)
    forward(x)
    left(180)
    forward(size)

def koch(order, size):
    '''This fractal draws a Koch curve recursively.
        order - recursion depth
        size - line length'''
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

def koch_snow(order, size):
    '''This fractal draws a Koch snowflake recursively.
        order - recursion depth
        size - line length'''
    if order == 0:
        forward(size)
    else:
        koch_snow(order-1, size/3)
        left(60)
        koch_snow(order-1, size/3)
        right(120)
        koch_snow(order-1, size/3)
        left(60)
        koch_snow(order-1, size/3)

def minkov(order, size):
    '''This fractal draws a Minkowski curve recursively.
        order - recursion depth
        size - line length'''
    if order == 0:
        forward(size)
    else:
        minkov(order-1, size/8)
        left(90)
        minkov(order-1, size/8)
        right(90)
        minkov(order - 1, size / 8)
        right(90)
        minkov(order - 1, size / 8)
        minkov(order - 1, size / 8)
        left(90)
        minkov(order - 1, size / 8)
        left(90)
        minkov(order - 1, size / 8)
        right(90)
        minkov(order - 1, size / 8)

def led_1(order, size):
    '''This fractal draws a "Ice" fractals # 1 recursively.
        order - recursion depth
        size - line length'''
    if order == 0:
        forward(size)
    else:
        led_1(order - 1, size/3)
        left(90)
        led_1(order - 1, size/6)
        right(180)
        led_1(order - 1, size/6)
        left(90)
        led_1(order - 1, size/3)

def led(order, size):
    '''This fractal draws a "Ice" fractals # 2 recursively.
        order - recursion depth
        size - line length'''
    if order == 0:
        forward(size)
    else:
        led(order - 1, size/3)
        left(120)
        led(order - 1, size/6)
        right(180)
        led(order - 1, size/6)
        left(120)
        led(order - 1, size / 6)
        right(180)
        led(order - 1, size / 6)
        left(120)
        led(order - 1, size/3)

def levi(order, size):
    '''This fractal draws a Levy curve recursively.
        order - recursion depth
        size - line length'''
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order - 1, size / 2)
        right(90)
        levi(order - 1, size / 2)
        left(45)

'''def drago()'''

def main():
    '''This function is basic.The menu of fractals is displayed here, from which the tester selects one fractal
        (by entering its number), which the program should draw.'''

    print('Меню', '1. Ракушка', '2. Двоичное дерево', '3. Фрактал "Ветка"', '4. Кривая Коха', '5. Снежинка Коха',
          '6. Кривая Минковского', '7. "Ледяные" фракталы №1', '8. "Ледяные" фракталы №2',
          '9. Снежинка из "Ледяного" фрактала',
          '10. Кривая Леви', '11. Фрактал Дракон Хартера-Хейтуэя', sep='\n')
    a = False
    while a != True:
        n = input('Выберите фрактал, который вы хотите нарисовать (укажите цифру):')
        try:
            n = int(n)
            if n == 1:
                a = int(input('Сторона квадрата: '))
                up()
                goto(-100, 0)
                down()
                square(a)
                mainloop()
            if n == 2:
                h = int(input('Введите высоту дерева:'))
                an = int(input('Введите угол отклонения ветвей:'))
                speed(1000)
                up()
                goto(0, -200)
                left(90)
                down()
                tree(h, an)
                mainloop()
            if n == 3:
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                up()
                goto(0, -100)
                left(90)
                down()
                branch(n, a)
                mainloop()
            if n == 4:
                up()
                goto(-100, 0)
                down()
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                koch(n, a)
                mainloop()
            if n == 5:
                speed(1000)
                up()
                goto(-100, 0)
                down()
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                koch_snow(n, a)
                right(120)
                koch_snow(n, a)
                right(120)
                koch_snow(n, a)
                mainloop()
            if n == 6:
                speed(1000)
                up()
                goto(-100, 0)
                down()
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                minkov(n, a)
                mainloop()
            if n == 7:
                speed(1000)
                up()
                goto(-100, 0)
                down()
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                led_1(n, a)
                mainloop()
            if n == 8:
                speed(1000)
                up()
                goto(-100, 0)
                down()
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                led_1(n, a)
                mainloop()
            if n == 9:
                speed(1000)
                up()
                goto(-100, 0)
                down()
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                for _ in range(8):
                    led(n, a)
                    right(180)
                    led(n, a)
                    right(180)
                    goto(-100, 0)
                    right(45)
            if n == 10:
                speed(1000)
                up()
                goto(-100, 0)
                down()
                n = int(input('Глубина рекурсии:'))
                a = int(input('Длина стороны:'))
                levi(n, a)
            '''if n == 11:'''
        except ValueError:
            print(' Введенное "{}" не является числом.'.format(n))
        else:
            a = True

if __name__ == "__main__":
    main()
