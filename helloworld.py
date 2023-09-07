#1 hello world
print('Hello world')

#2 
#2.1
a = 1
a = 'Hello World'
a = [1, 2, 3]
a = [1.2,'Hello','W', 2]
#2.3
x = 2
1 < x < 3 # True
10 < x < 20 # False
3 > x <= 2 # True
2 == x < 4 # True
#2.4
for letter in 'Python': # First Example
    print('Current Letter :', letter)
fruits = ['banana','apple','mango']
for fruit in fruits: # Second Example
    print('Current fruit :', fruit)
print("Good bye!")

count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
print("Good bye!")
#2.5
def sum(a, b):
    return (a+b)
sum(1, 2)
#2.6
str1 = "Hello"
str2 = 'world'

str = str1 + " " + str2

str = 'Hello world'
print(str[0:4])
print(str[:4])
print(str[-3:])
print(str[6:-3])

count = len("Hello world")

str = 'Hello world'
newstr = str.replace('Hello','Bye')
print(newstr)

str = 'Hello world'
print(str.find('world'))
print(str.find('Bye'))

str = 'Hello world'
print(str.split(' '))
#2.7
numbers = [1, 2, 3, 4, 5]
names = ['Marry','Peter']

print(numbers[0])
print(numbers[-3])
print(names[1])

mylist = ['a','b','c']
print('a' in mylist)
print('b' not in mylist)

numbers = ['a','b','c','d']
print(numbers[:2])
print(numbers[-2:])

numbers = [1, 2, 3, 4, 5]
del numbers[0]
print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7]
del numbers[2:4]
print(numbers)

a = [1, 2]
b = [1, 3]
print(a + b)

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

numbers = [1, 2, 3]
mynumber = numbers.pop()
print(mynumber)
print(numbers)

