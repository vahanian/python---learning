grades = [5, 4, 3, 3.5, 2]

# print(grades[0])
# print(grades[5])  causes error !!!
sum = 0
lengthGrades = len(grades)

for grade in grades:
    sum = sum + grade
    print('ocena ', grade)

average = sum / lengthGrades

print('suma: ', sum)
print('srednia: ', average)

