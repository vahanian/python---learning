a = 1
b = 2
c = 3

if a == 1 and b == 3:
    print('a=1, b=3')
elif a == 1 and c == 2:
    print ('a=1 i c=3')
else:
    print('nie wiem ile jest a i b i c')

print('------------------------------')

a = 2
b = 1
c = 1

if (a == 1 or b == 1) and c == 1:
    print('ktoras ze zmiennych jest rowna 1')
else:
    print('zadna z liczb nie jest rowna 1')