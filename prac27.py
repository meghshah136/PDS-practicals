marks = {
    'PDS' : 99,
    'CS' : 90,
    'CG' : 87,
    'SE' : 88,
    'PE' : 80,
    'CN' : 90,
    'ADA' : 97
}

print(sorted(marks,key = lambda item:marks[item],reverse = True))