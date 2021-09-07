stri = input("Enter String : ")
num = int(input("Enter index number from which new string is added..: "))
newstr = input("Enter new string : ")
result = stri[:num] + newstr + stri[num:]
print(result)