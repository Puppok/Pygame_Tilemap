# name = 'Tom'
# age = -4
# print(f'Hello, {name}, you are {age} years old')

# print('Im using Python with Git')

a = int(input())
b = int(input())
if a > b:
    print(f'{a} больше {b}')
elif a == b:
    print(f'{a} равно {b}')
else:
    print(f'{a} меньше {b}')
s = 0
arr = list(input())
for el in arr:
    s += int(el)
print(s)
print('Im using Python with Git')

def table_multi():
    print('\nTable Multi:')
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end = '\t')
        print()

table_multi()
