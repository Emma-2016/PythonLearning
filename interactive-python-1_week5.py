#--------------------------Excise 1
import simplegui

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT /2]

def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'red', 'white')
    
    
def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP['left']:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP['right']:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP['down']:
        ball_pos[1] -= vel
    elif key == simplegui.KEY_MAP['up']:
        ball_pos[1] += vel
        
frame = simplegui.create_frame('Test', 700, 700)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

frame.start()
    



#--------------------------Excise 2
import simplegui

current_key = ''

def keydown(key):
    global current_key
    current_key = chr(key)

def keyup(key):
    global current_key
    current_key = ''

def draw(canvas):
    canvas.draw_text(current_key, [10, 25], 20, 'red')

frame = simplegui.create_frame('Echo', 35, 35)

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

frame.start()


#--------------------------Excise 3
import simplegui

WIDTH = 200
HEIGHT = 150
BALL_RADIUS = 10
init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [4, 3]
time = 0

def tick():
    global time
    time += 1
    
def draw(canvas):
    ball_pos = [0, 0]
    
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[0] + time * vel[1]
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'red', 'white')
    
frame = simplegui.create_frame('Motion', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

frame.start()
timer.start()


#--------------------------Excise 4
import simplegui

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0, 5.0 / 60.0]

def draw(canvas):
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = -vel[0]

    if ball_pos[0] >= WIDTH - BALL_RADIUS:
        vel[0] = -vel[0]

    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'red', 'white')

frame = simplegui.create_frame('Ball physics', WIDTH, HEIGHT)

frame.set_draw_handler(draw)    #this is calling all the time

frame.start()
