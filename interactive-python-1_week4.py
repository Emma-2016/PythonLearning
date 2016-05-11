#--------------------------------------------------Excise 1:

import simplegui

#define a global value
value = 3.14


def convert_unit(val, name):
    result = str(val) + ' ' + name
    if val > 1:
            result = result + 's'
    return result

def convert(val):
    global value
    value = val
    value = float(value)
    dollars = int(value)
    cents = round((value - dollars) * 100)
    
    dollars_string = convert_unit(dollars, 'dollar')
    cents_string = convert_unit(cents, 'cent')

    if cents == 0:
        return dollars_string
    elif dollars == 0:
        return cents_string
    else:
        return dollars_string + ' and ' + cents_string


#define event handlers: input & draw & button

#define a input hanlder
def input_handler(text):
    global value
    value = float(text)
    return value

#define a draw hanlder
def draw_handler(canvas):
    canvas.draw_text(convert(value), (55, 100), 24, 'white')

#define a button handler
def button_handler():
    global value
    value = 0

#create a frame
frame = simplegui.create_frame('Week3', 400, 250)

#register event handlers
frame.add_input('Enter your money number: ', input_handler, 100)
frame.set_draw_handler(draw_handler)
frame.add_button('click me', button_handler, 100)

#start a frame
frame.start()


#-----------------------------------------------------Excise 2:
import simplegui
import random

#create globle variable
position = [100, 100]
interval = 1000
message = 'Hello Emma'

#define handler function
def timer_handler():
    global position
    position[0] = random.randrange(0, 300)
    position[1] = random.randrange(0, 250)
    return position
def input_handler(text):
    global message
    message = text
    return message
def draw_handler(canvas):
    canvas.draw_text(message, position, 24, 'white')
    
#create a frame
frame = simplegui.create_frame('week3_random_position', 300, 250)

#register handlers
timer = simplegui.create_timer(interval, timer_handler)
frame.add_input('Message: ', input_handler, 150)
frame.set_draw_handler(draw_handler)

#start a frame
frame.start()
timer.start()



#-----------------------------------------------------Excise 2:
#use timer to do looping
import simplegui

# global state

result = 0

# helper functions

def init(start):
    """Initializes n."""
    global result
    result = start
    print "Input is", result

def get_next(current):
    if current % 2 == 0:
        return current / 2
    else:
        return current * 3 + 1

# timer callback
result_set = []
def update():
    global result
    if result == 1:
        timer.stop()
        result_set.sort()
        print 'Output is', result_set[-1]
    else:
        result = get_next(result)
        result_set.append(result)
    
# register event handlers

timer = simplegui.create_timer(10, update)

# start program

init(217)
timer.start()
