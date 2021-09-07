enrollments = set()

while True:
    i = 1
    number = int(input(f"Enter marks of subject PDS of student {i}: "))
    enrollments.add(number)
    i += 1
    
    inpt = input("Want to enter more ? (Y/N) :")
    if inpt == 'N':
        break

print(set(sorted(enrollments)))