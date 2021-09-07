marks = []
user_input = 'Y'
while user_input != 'N':
    i = 1
    mark = int(input(f"Enter marks of subject PDS of student {i}: "))
    marks.append(mark)
    i += 1
    
    user_input = input("Want to enter more ? (Y/N) :")
    
tuple_marks = tuple(marks)
print(f"Tuple of Marks of all students : {tuple_marks}")
