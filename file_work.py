# with open(f'file.txt','r') as file:
#     content = file.read()
#     print(content)
#
# with open (f'file.txt','a') as file:
#     file.write('\n This is a new line.')
#
#
# with open(f'file1.txt', 'x') as file:
#         file.write('This is a new line.')
#
# with open(f'file.txt', 'w') as file:
#     file.write('heloo ')
#
# with open("file.txt",'w+') as file:
#     file.write('Hello,ernis! \n Tb=his is a new line.')
#     file.seek(0)
#     content = file.read()
#     print(content)

with open('numbers.txt','w') as file:
    for i in range(5):
        a = int(input("san jaz: "))
        file.write(f'{a} + \n')
numbers = []
with open ('numbers.txt','r' )as file:
 for line in file:
     numbers.append(int(line.strip()))
     print(sum(numbers))
