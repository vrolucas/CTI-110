Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # A program written to give simple math quizzes to a user.
... 
...    # 4/12/23
... 
...    # CTI-110 P5HW - Math Quiz
... 
...    # Lucas Garcia
... 
...    #
... 
... 
... 
... import random
... 
... def addProblem():
...     a = random.randint(10,99)
...     b = random.randint(10,99)
...     print(f' {a}')
...     print(f'+{b}')
...     print('Enter answer.')
...     ans = int(input())
...     while ans!=(a+b):
...         if ans<(a+b):print('Sorry, guess is too low.')
...         else: print('Sorry, guess is too high.')
...         ans = int(input('try again:'))
...     print('Congratulations!!!! your answer is correct...\n')
... 
... def subProblem():
...     a = random.randint(10, 99)
...     b = random.randint(10, 99)
...     if a<b:a,b=b,a
...     print(f' {a}')
...     print(f'-{b}')
...     print('Enter answer.')
...     ans = int(input())
...     while ans != (a - b):
...         if ans < (a - b):
...             print('Sorry, guess is too low.')
...         else:
...             print('Sorry, guess is too high.')
...         ans = int(input('try again:'))
...     print('Congratulations!!!! your answer is correct...\n')
... 
... def main():
...     print('Welcome to Math Quiz\n')
...     while True:
...         print('MAIN MENU')
...         print('-------------------')
...         print('1. Adding Random Numbers')
...         print('2. Subtracting Random Numbers')
...         print('3. Exit\n')
...         choice = input('Please choose one of the menu options: ')
...         if choice == '1':
...             addProblem()
...         elif choice == '2':
...             subProblem()
...         elif choice == '3':
...             print('Thank you for playing...\nBye!!')
...             break


