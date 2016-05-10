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
