student1_details = {
    'Name' : 'Megh Shah',
    'Enroll' : 190280107136,
    'Sem' : 5,
    'Div' : 'C',
    'Course' : 'Computer Engineering',
    'SPI' : 9.77
}

student2_details = {
    'Name' : 'Het Shah',
    'Enroll' : 190280107026,
    'Sem' : 5,
    'Div' : 'A',
    'Course' : 'Computer Engineering',
    'SPI' : 9.50
}

student3_details = {
    'Name' : 'Darshan Shah',
    'Enroll' : 190280107106,
    'Sem' : 5,
    'Div' : 'B',
    'Course' : 'Computer Engineering',
    'SPI' : 9.15
}

list_students = []
list_students.append(student1_details)
list_students.append(student2_details)
list_students.append(student3_details)

list_students.sort(key = lambda item:item.get('SPI'))
print(list_students)