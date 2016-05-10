print 'Exercise 1:'
message = 'Hello'
def print_goodbye():
    message = 'Goodbye'
    print message
print_goodbye()
print '-----------'
print message

print'\n================================================'
print 'Exercise 2:'
def set_goodbye():
    global message
    message = 'Goodbye'
    print message
set_goodbye()
print '-------------'
print message

print'\n================================================'
print 'Exercise 3:'
count = 9
def reset():
    global count
    count = 0
def increment():
    global count
    count += 1
def decrement():
    global count
    count -= 1 
def print_count():
    global count
    print count
reset()
increment()
decrement()
decrement()
print_count()

#print'\n================================================'
#print 'Exercise 4:'
#import simplegui
#frame = simplegui.create_frame('My first frame', 100, 200)
#frame.set_canvas_background("#FF0000")
#frame.start()

print'\n================================================'
print 'Exercise 5:'
count1 = 0
def square(x):
    global count1
    count1 += 1
    print count1
    return x**2

print square(square(square(square(3))))

print'\n================================================'
print 'Exercise 6:'
a = 3
b = 6
def f(a):
    c = a + b
    return c
print f(4)
print a

#globle(state)
#helper functions
#classes
#define event handlers
#create a frame
#register event handlers
#start frame & timers

print'\n================================================'
print 'Exercise 7:'

import simplegui

#define global variable(program state)
count = 0

#define helper function
def increment():
    global count
    count += 1

#create event handler function
def tick():
    increment()
    print count

def reset_num():
    global count
    count = 0

#create a frame
frame = simplegui.create_frame('TimerTest', 200, 300)

#register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button('Faster', tick)
frame.add_button('Reset number', reset_num)
frame.add_button('Stop', timer.stop)

#start a frame
#frame.start()
timer.start()

print'\n================================================'
print 'Exercise 8:'
import simplegui

#create a global
store = 0
operand = 0

#define helper function
def output():
    print 'store:', store
    print 'operand:', operand
    print

def swap():
    global store
    global operand
    store, operand = operand, store
    output()

#define event handler 
def add():
    global store
    global operand
    store = store + operand
    output()

def sub():
    global store
    global operand
    store = store - operand   
    output()

def enter(inp):
    global store
    global operand
    store, operand = operand, store
    operand = float(inp)
    output()

#create a frame
frame = simplegui.create_frame('Test', 250, 300)

#register
frame.add_button('Print', output)
frame.add_button('Add', add)
frame.add_button('Sub', sub)
frame.add_input('Enter your number', enter, 150)

#start a frame
frame.start()

print'\n================================================'
print 'Exercise 8:'
import simplegui
import random

#define global
secret_number = 0
tag = 0
count = 0

def range_100():
    global tag
    tag = 7
    new_game()

def range_1000():
    global tag
    tag = 10
    new_game()

def new_game():
    global count
    global tag
    tag = tag
    global secret_number
    print 'A new game start'
    if tag == 7:
        secret_number = random.randrange(0, 100)
    if tag == 10:
        secret_number = random.randrange(0, 1000)
    count = 0
    print

#define handler functions
def input_guess(guess):
    guess = int(guess)
    global count
    count += 1
    print 'Guess is', guess
    if (7 - count >= 0 and tag ==7) or (10 - count >= 0 and tag == 10):
        if guess < secret_number:
            print 'Higher',
            print 'and times to guess is', tag - count, 'left',
            print 'tag is', tag
        elif guess > secret_number:
            print 'Lower',
            print 'and times to guess is', tag - count, 'left',
            print 'tag is', tag
        else:
            print 'Correct'
            print 'A new game start'
            new_game()
    else:
        print 'No more chances to guess'
        print 'the secret number is', secret_number
        new_game()

#create a frame
frame = simplegui.create_frame('Guess Numbers', 300, 240)

#register a handler
frame.add_button('Range [0,100)', range_100, 150)
frame.add_button('Range [0,1000)', range_1000, 150)
frame.add_input('Enter your guess: ', input_guess, 150)
frame.add_button('New game', new_game, 100)

# Start the frame animation
frame.start()
