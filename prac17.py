length = int(input("How many elements you want in list? : "))
lists = []
count = 0
for i in range(length):
    ele = input("Enter elements : ")
    lists.append(ele)
print(lists)
count_element = input("Enter element to find number of occurrence : ")
for i in lists:
    if count_element == i:
        count += 1
print(f"Occurrence of {count_element} is {count}")