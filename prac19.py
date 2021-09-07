numbers = [2,6,1,5,8,4,9,5,3,7]
smallest = numbers[0]
largest = numbers[0]
for i in numbers:
    if smallest > i:
        smallest = i
    if largest < i:
        largest = i
print(f"Smallest element = {smallest}")
print(f"Largest element = {largest}")