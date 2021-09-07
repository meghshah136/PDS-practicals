student_details = {
    'Name' : 'Megh Shah',
    'Enroll' : 190280107136,
    'Sem' : 5,
    'Div' : 'C',
    'Course' : 'Computer Engineering'
}

print(student_details['Name'])

print("Adding into dictionary...")
student_details['College'] = 'L.D.'
print(student_details)

print("Removing some info from dictionary...")
student_details.pop('Div')
print(student_details)

print("Updating Sem 5 to 6...")
student_details['Sem'] = 6
print(student_details)