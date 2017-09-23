import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
down1 = False
down2 = False
up1 = False
up2 = False
score1 = 0
score2 = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-40.0 / 30.0,  5.0 / 30.0]

paddle1_pos = [    0, HEIGHT/2]
paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT/2]
paddle1_vel = -40.0 / 30.0 * 2
paddle2_vel = -40.0 / 30.0 * 2
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    ball_vel[0] = random.randrange(120, 240)/30
    ball_vel[1] = random.randrange( 60, 180)/30

    if (direction == LEFT):
        ball_vel[0] = -ball_vel[0];
    # these are vectors stored as lists

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    dir = [random.randrange(120, 240)/30, random.randrange(60, 180)/30]
    spawn_ball(dir)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    global ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
      
    if ((ball_pos[0] <= BALL_RADIUS) and
        ((ball_pos[1] > paddle1_pos[1] + PAD_HEIGHT) or
        (ball_pos[1] < paddle1_pos[1]))):
        score2 = score2 + 1
        spawn_ball(RIGHT)    
        
    if ((ball_pos[0] >= WIDTH - BALL_RADIUS) and
        ((ball_pos[1] > paddle2_pos[1] + PAD_HEIGHT) or
        (ball_pos[1] < paddle2_pos[1]))):
        score1 = score1 + 1
        spawn_ball(LEFT)
        
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
        
    if ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    
    if ball_pos[1] <= BALL_RADIUS :
        ball_vel[1] = - ball_vel[1]
         
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    global paddle1_vel
    global paddle2_vel, down1, down2, up1, up2
    if(down1):
        paddle1_pos[1] -= paddle1_vel
    if(down2):
        paddle2_pos[1] -= paddle2_vel
    
    if(up1):
        paddle1_pos[1] += paddle1_vel
    if(up2):
        paddle2_pos[1] += paddle2_vel
   
    if paddle1_pos[1] <= 0:
        # paddle1_vel = - paddle1_vel
        paddle1_pos[1] -= paddle1_vel
        
    if paddle1_pos[1] >= HEIGHT - PAD_HEIGHT:
        # paddle1_vel = - paddle1_vel
        paddle1_pos[1] += paddle1_vel
            
    if paddle2_pos[1] <= 0:
        # paddle2_vel = -paddle2_vel
        paddle2_pos[1] -= paddle2_vel
        
    if paddle2_pos[1] >= HEIGHT - PAD_HEIGHT:
        # paddle2_vel = -paddle2_vel
        paddle2_pos[1] += paddle2_vel
            
    canvas.draw_polygon([[paddle1_pos[0], paddle1_pos[1]],
                         [paddle1_pos[0]+PAD_WIDTH, paddle1_pos[1]],
                         [paddle1_pos[0]+PAD_WIDTH, paddle1_pos[1]+PAD_HEIGHT],
                         [paddle1_pos[0], paddle1_pos[1]+PAD_HEIGHT]], 1, 'White', 'White')
    
    
    
    canvas.draw_polygon([[paddle2_pos[0], paddle2_pos[1]],
                         [paddle2_pos[0]+PAD_WIDTH, paddle2_pos[1]],
                         [paddle2_pos[0]+PAD_WIDTH, paddle2_pos[1]+PAD_HEIGHT],
                         [paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT]], 1, 'White', 'White')

    # determine whether paddle and ball collide    
    
    # draw scores

    
 
    canvas.draw_text(str(score1), (100, 100), 70, 'Pink')
    canvas.draw_text(str(score2), (500, 100), 70, 'Pink')

    #if (score1 > 10):
     #    canvas.draw_text("You win!", (50, 100), 60, 'Cyan')
    #if (score2 > 10):
     #    canvas.draw_text("You win!", (400, 100), 60, 'Cyan')
    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, down1, up1, down2, up2
    if key == simplegui.KEY_MAP["down"]:
        down2 = True
    elif key == simplegui.KEY_MAP["up"]:
        up2 = True
    elif key == simplegui.KEY_MAP["s"]:
        down1 = True
    elif key == simplegui.KEY_MAP["w"]:
        up1= True

def keyup(key):
    global paddle1_vel, paddle2_vel, down1, down2, up1, up2
    if key == simplegui.KEY_MAP["down"]:
        down2 = False
    elif key == simplegui.KEY_MAP["up"]:
        up2 = False
    elif key == simplegui.KEY_MAP["s"]:
        down1 = False
    elif key == simplegui.KEY_MAP["w"]:
        up1 = False
def button_handler():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", button_handler, 100)

# start frame
new_game()
frame.start()
