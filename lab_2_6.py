mass = []
list1 = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']
list2 = ['1010', '1011', '1100', '1101', '1110', '1111', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '0000']
print('Пример ввода  -7A , F , -7 ')
ch = str(input('Введите 16-ричное число  '))
if ch == '-0':
    print('Error')
    exit()
count = 0
spi = ''
for i in ch:
    if i in list1:
        mass.append(i)
        count += 1
if ('-' not in mass) and (count > 2) or count > 3:
            print('Too much')
else:
    if '-' in mass:
        if count == 3:
            per1 = mass[1]
            per2 = mass[2]
            x = list1.index(per1)
            y = list1.index(per2)
            stroka = list2[x] + list2[y]
            print(stroka)
            des = int(stroka, 2)
            if des > 128:
                print('Too much man')
            else:
                print('в десятичной ', -des)
                k = ''
                list1 = []
                a = 128 - int(des)
                a_b = bin(a)[2:].zfill(8)
                x = a_b[0].replace('0', '1')
                print('Дополнительный код',x+a_b[1:])
        else:
            per1 = mass[1]
            x = list1.index(per1)
            stroka = list2[x]
            des = int(stroka, 2)
            if des > 127:
                print('Too much man')
            else:
                print('в десятичной ', -des)
                k = ''
                list1 = []
                a = 128 - int(des)
                a_b = bin(a)[2:].zfill(8)
                x = a_b[0].replace('0', '1')
                print('Дополнительный код', x + a_b[1:])
    else:
        if count == 2:
            per1 = mass[0]
            per2 = mass[1]
            x = list1.index(per1)
            y = list1.index(per2)
            stroka = list2[x] + list2[y]
            des = int(stroka, 2)
            if des > 127:
                print('Too much man')
            else:
                print('в десятичной ', des)
                a_b = bin(des)[2:].zfill(8)
                print('Дополнительный код', a_b)
        else:
            per1 = mass[0]
            x = list1.index(per1)
            stroka = list2[x]
            des = int(stroka, 2)
            if des > 127:
                print('Too much man')
            else:
                print('в десятичной ', des)
                a_b = bin(des)[2:].zfill(8)
                print('Дополнительный код', a_b)
input()