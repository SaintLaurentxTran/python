# weightLbs = input('May bao nhieu pao? ')
# print(type(weightLbs))
# weightKgs = int(weightLbs) * 0.45
# print(type(weightKgs))
# print(weightKgs)


# course = '''
# Dear, Nvi

# Here is my exercise done.

# See you soon

# Cheer,

# '''
# print(course)


# Strings = 'Thanh mòi đẹp trai vl'
# print( Strings[0:5])


###  Formatted Strings  ###

# first = 'Tran'
# last = 'Thanh'
# age = 16
# message1 = last + ' ['+first+']' +  ' is '
# message2 = f'{last} [{first}] is {age} a student'
# print(message1)
# # print(message2)


# String Methods
# Fact = 'Liverpool is absolutely a strong team'
# print(Fact.upper())
# print(Fact.lower())
# print(Fact.find('in'))
# print(Fact.replace('absolutely', 'definitely'))
# print('is' in Fact)
# print(Fact.title())
# more and more and more


# Operator Precedence
# print(12 // 5)
# x = 6
# x -= 4
# print(x)
# y = 12
# y //= 2
# print(y)
# x = (4 + 5) ** 3
# print(x)


# Math Functions
# x = 9.9
# print(round(x))
# print(abs(-x))
# import math
# print(math.floor(x))
# print(math.frexp(x))
# print(math.pi)
# print(math.degrees(0.15))


# If Statements
# isGood = True
# isBad = False
# if isGood:
#     print("It's a good day")
#     print("Go out and play football")
# elif isBad:
#     print("It's a bad day")
#     print("Stay home and relax")
# else:
#     print("What a awesome day")
# print("Enjoy your day")

# price = 1000000
# hasGoodCredit = True
# if hasGoodCredit:
#     downPayment = 0.1 * price
# else:
#     downPayment = 0.2 * price
# print(f'Down payment: ${downPayment}')


# Logical Operator
# hasGoodCredit = True
# hasCriminalRecord = True
# if hasGoodCredit or hasCriminalRecord:
#     print('Eligible for loan')


# temperature = int(input('Type the temperature today(celcius) '))
# if temperature >= 30 and temperature <= 100:
#     print("It's a hot day")
# elif temperature >= -100 and temperature <= 10:
#     print("It's a cold day")
# else:
#     print("It's a normal day")


# name = input('Type your full name ')
# if len(name) <3:
#     print('Name must be at least 3 characters')
# elif len(name) >50:
#     print('Name can be maximum of 50 characters')
# else:
#     print('Name looks good')


# Weight converter proggram
# height = float(input('Type your height: '))
# unit = input('(ft)s or (m)s: ')
# if unit.upper() == "FT":
#     converted = height * 0.3048
#     print(f'You are tall {converted} meters')
# else:
#     converted = height / 0.3048
#     print(f'You are tall {converted} feets ')


# temp = float(input("Type the temperature you want to convert: "))
# unit = input("(celcius) or (fahrenheit): ")
# if unit.upper() == "CELCIUS":
#     converted = temp * 1.8 + 32
#     print(f"It's {converted} Fahrenheit")
# else:
#     converted = (temp - 32) / 1.8
#     print(f"It's {converted} Celcius")


# heightFeets = float(input('Type your height?(ft)'))
# convertedToMeters = heightFeets * 0.3048
# print(f"You are tall {convertedToMeters}")


# While loops
# x = 100
# while x > 10:
#     print(f'x = {x}')
#     x -= 10
# print('Done')


# Print first 10 natural numbers using while . loop
# i = 0
# while i <=10:
#     print(i)
#     i +=1


# Building a guessing game

# birthDay = 18
# birthMonth = 2
# birthYear = 2005
# guessCount = 0
# guessLimit = 3
# while guessCount < guessLimit:
#     guess = int(input("Birthday: "))
#     guessCount += 1
#     if guess == birthDay:
#         print(f'My birth day is {birthDay}')
#         continue
#     elif guess == birthMonth:
#         print(f'My birth month is {birthMonth}')
#         continue
#     elif guess == birthYear:
#         print(f'My birth year is {birthYear}')
#         break
# else:
#     print('18/02/2005')


# Building a plane game
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Plane is already started!")
#         else:
#             started = True
#             print("Plane started...")
#     elif command == "stop":
#         if not started:
#             print("Plane is already stopped!")
#         else:
#             started = False
#             print("Plane stopped.")
#     elif command == "help":
#         print("""
# start - to start the plane.
# stop - to stop the plane.
# quit - to quit.
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I don't understand that.")


# For loops
# for x in range(0,100, 5):
#     print(x)


# prices = [3123, 5345, 8941]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# n = 2
# for i in range(1, 11):
#     product = n*i
#     print(product)


# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# for item in list1:
#     if item > 150:
#         break
#     if item % 5 ==0:
#         print(item)


# chuoi = ['dad', 'mom', 'you']
# for tu in range(len(chuoi)):
#     print('I love', chuoi[tu])


# Nested Loops

# for x in range(10):
#     print(x)


# numbers = [1, 8, 2, 2, 5]
# for xNumber in numbers:
#     print('x' * xNumber)


# List

# names = ['Tran', 'Quoc', 'Thanh']
# print(names)

# numbers = [9, 172, 13, 3, 45, 18, 99]
# max = numbers[1]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)


# List Method


# numbers = [7, 2, 1, 8, 4, 5, 9]
# clear(): Xoá hết phần tử khỏi danh sách
# print(numbers.clear())
# # append(): Thêm một phần tử vào cuối danh sách
# print(numbers.append(18))
# remove(): Xoá một phần tử được chọn
# print(numbers.remove(4))
# # index(): Trả về vị trí của phần tử được chọn
# print(numbers.index(8))
# # copy(): Trả về một bản sao của danh sách
# print(numbers.copy())
# # count(): Trả về số phần tử có giá trị được chỉ định
# print(numbers.count(7))


# numbers = [2, 3, 1, 9, 4, 6, 9, 3]
# unit = []
# for number in numbers:
#     if number not in unit:
#         unit.append(number)
# print(unit)


# array4 = [1, 2, 3, 4, 3, 5, 1, 4]


# phoneNumber = input("Type your phone number: ")
# spell = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eigth",
#     "9": "Nine",
#     "0": "Oh"
# }
# output = ""
# for characters in phoneNumber:
#     output += spell.get(characters, "!") + " "
# print(output)


# mess = input("How are you today? ")
# words = mess.split(' ')
# emojis = {
#     ":)": "😀",
#     ":(": "😢"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


# def merge(d1,d2):
#     d1.update(d2)
#     return d1

# dictionaries = merge({'a': 100, 'b': 200}, {'x': 300, 'y': 200})
# print(dictionaries)


# import random


# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second

# dice = Dice()
# print(dice.roll())
