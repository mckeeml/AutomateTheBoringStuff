import random

def hello(name):
    print('Howdy, ' +name +'!')
    print('Howdy, ' +name +'!!!')
    print('Hello there, ' +name +'!')

hello('Carl')
hello('Joe')
hello('Michael')

#################################

def plus_one(number):
    return number + 1

new_number = plus_one(6)
print(str(new_number))

#################################

def get_answer(answerNumber):
    if answerNumber == 1:
        return 'It is certain.'
    elif answerNumber == 2:
        return 'It is decidedly so.'
    elif answerNumber == 3:
        return 'Yes.'
    elif answerNumber == 4:
        return 'Reply hazy try again.'
    elif answerNumber == 5:
        return 'Ask again later.'
    elif answerNumber == 6:
        return 'Concentrate and ask again.'
    elif answerNumber == 7:
        return 'My reply is no.'
    elif answerNumber == 8:
        return 'Outlook not so good.'
    elif answerNumber == 9:
        return 'Very doubtful.'

print('Think of a yes or no question, and press enter to see the Magic 8-Ball response.')
input()

print(get_answer(random.randint(1,9)))

#################################

print('Hello', end='')
print('World')
print('Cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep='ABC')

#################################

spam = 42 #global variable

def eggs():
    spam = 42 #local variable

print('Some code here.')
print('Some more code.')

#################################

def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)

#################################





