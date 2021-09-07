def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num%2,end='')
print("Recursive method : ")
print(f"Decimal 20 to binary : ")
DecimalToBinary(20)
print("\n")

def decimaltobinary(num):
    while num >= 1:
        num //= 2
        print(num%2,end='')
    print(num,end='')
    print("\n")
print("Non-recursive method : ")
print("Decimal 20 to binary : ")
decimaltobinary(20)

def DecimalToOctal(num):
    if num >= 1:
        DecimalToOctal(num // 8)
    print(num%8,end='')
print("Recursive method : ")
print(f"Decimal 20 to octal : ")
DecimalToOctal(20)
print("\n")

def decimaltooctal(num):
    while num >= 1:
        num //= 8
        print(num%8,end='')
    print(num,end='')
    print("\n")
print("Non-recursive method : ")
print(f"Decimal 20 to octal : ")
decimaltooctal(20)

def DecimalToHex(num):
    if num >= 1:
        DecimalToBinary(num // 16)
    if num%16 > 9:
        if num%16==10:
            print('A',end='')
        elif num%16==11:
            print('B',end='')
        elif num%16==12:
            print('C',end='')
        elif num%16==13:
            print('D',end='')
        elif num%16==14:
            print('E',end='')
        else:
            print('F',end='')
    print(num%16,end='')
print("Recursive method : ")
print(f"Decimal 20 to hexadecimal : ")
DecimalToHex(47)
print("\n")

def decimaltohex(num):
    while num >= 1:
        num //= 16
        if num%16 > 9:
            if num%16==10:
                print('A',end='')
            elif num%16==11:
                print('B',end='')
            elif num%16==12:
                print('C',end='')
            elif num%16==13:
                print('D',end='')
            elif num%16==14:
                print('E',end='')
            else:
                print('F',end='')
        else:
            print(num%16,end='')
    print(num,end='')
    print("\n")
print("Non-recursive method : ")
print(f"Decimal 20 to hexadecimal : ")
decimaltohex(160)

def binarytodecimal(num):
    str_num = str(num)
    total = 0
    j = len(str_num) - 1
    for i in str_num:
        if int(i) == 0 or int(i) == 1:
            total += int(i) * (2**j)
            j -= 1
        else:
            print("Enter proper binary value..")
            return
    print(total)
print(f"Binary 1111 to decimal : ")
binarytodecimal(1111)

def octaltodecimal(num):
    str_num = str(num)
    total = 0
    j = len(str_num) - 1
    for i in str_num:
        if 0 <= int(i) <= 7:
            total += int(i) * (8**j)
            j -= 1
        else:
            print("Enter proper octal value..")
            return
    print(total)
print(f"Octal 11 to decimal : ")
octaltodecimal(11)

def hextodecimal(num):
    str_num = str(num)
    total = 0
    j = len(str_num) - 1
    for i in str_num:
        if 0 <= int(i) <= 15:
            total += int(i) * (16**j)
            j -= 1
        else:
            print("Enter proper binary value..")
            return
    print(total)
print(f"Hexadecimal 11 to decimal : ")
hextodecimal(11)

