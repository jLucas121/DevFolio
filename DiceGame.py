# Program Name: Dice Program
# My Name: James Lucas Smith
# Program Number: P22
# Version: Python 3.1.6
# Date Started- Date Finished: 9/21/22-9/21/22
# Description: Dice against computer

'''
Write a Dice Game program that generates two random dice values between
1 and 6 for you, and 2 for the computer.

You get to roll as many times as you like (if you don't like your 2 dice),
while the computer only rolls once, after you have decided that you like your two dice. 

Determine who wins, you or the computer.
'''

from random import randint

while True:
    d1 = randint(1,6)
    d2 = randint(1,6)

    keep = input('you rolled %i amd %i for a total of %i, keep y/n:' %(d1,d2,d1+d2))
    if keep == 'y':
        break
Hal1 = randint(1,6)
Hal2 = randint(1,6)

if Hal1 + Hal2 > d1 + d2:
    print('Im sorry, Dave, Ive won.')
elif Hal1 + Hal2 < d1 + d2:
    print('You killed Hal-9000')
else:
    print('Tie,Dave')

'''
Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: /Users/lucas/Desktop/Intro to Python/P22.py =============
you rolled 5 amd 6 for a total of 11, keep y/n:y
You killed Hal-9000

============= RESTART: /Users/lucas/Desktop/Intro to Python/P22.py =============
you rolled 6 amd 1 for a total of 7, keep y/n:n
you rolled 5 amd 2 for a total of 7, keep y/n:n
you rolled 6 amd 1 for a total of 7, keep y/n:n
you rolled 4 amd 4 for a total of 8, keep y/n:n
you rolled 2 amd 1 for a total of 3, keep y/n:y
Im sorry, Dave, Ive won.

============= RESTART: /Users/lucas/Desktop/Intro to Python/P22.py =============
you rolled 3 amd 3 for a total of 6, keep y/n:y
Tie,Dave
'''
