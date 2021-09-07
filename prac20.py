list_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
list_b = ['Megh','Meet','Neel','Supan','Tanmay','Umesh','Megh','megh','megh','megh','Megh']
def partition(numbers):
    
    unique = []
    duplicate = []
    temp = []
    
    for i in numbers:
        if i not in unique:
            unique.append(i)
        else:
            duplicate.append(i)
    
    for i in duplicate:
        if i not in temp:
            count = 0
            for j in duplicate:
                if i == j:
                    count += 1
                else:
                    pass
            print(f"Duplicates of {i} : {count}")
            temp.append(i)

partition(list_a)
partition(list_b)