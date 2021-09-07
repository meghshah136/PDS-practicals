enrollments = {190280107136,190280107128,190280107146,190280107140,190280107135,190280107138}
print(enrollments)

print("Adding one enrollment number into the set...")
enrollments.add(190280107001)
print(enrollments)

print("Deleting one enrollment number from the set...")
enrollments.remove(190280107136)
print(enrollments)

print("Sorted set...")
sorted_list = sorted(list(enrollments))
print(sorted_list)