#Remove Duplicates from a List: [1, 2, 3, 4, 2, 3, 5, 6, 1]
original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_list = []

for num in original_list:
    if num not in unique_list:
        unique_list.append(num)

print("Original list:", original_list)
print("List without duplicates: ", unique_list)
