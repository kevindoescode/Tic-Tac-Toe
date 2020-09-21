import sys, pygame, random
from pygame.locals import *
from random import randint

def reset_board():
    board = dict()
    for i in range(3):
        for n in range(3):
            board[str(i) + '_' + str(n)] = None
    return board
def turn_move(turn):
    if turn == 0:
        newturn = 1
    elif turn == 1:
        newturn = 0
    return newturn
def board_setup(lines):
    line_a = lines[0]
    line_b = lines[1]
    line_c = lines[2]
    line_d = lines[3]
    pygame.draw.line(screen,black,(0,line_c), (screen_x,line_c), 5) # horizontal 1
    pygame.draw.line(screen,black,(0,line_d), (screen_x,line_d), 5) # horizontal 2
    pygame.draw.line(screen,black,(line_a,(0+(screen_y*0.08))), (line_a,screen_y), 5) # vertical 1
    pygame.draw.line(screen,black,(line_b,(0+(screen_y*0.08))), (line_b,screen_y), 5) # vertical 2
def board_draw(board):
    # First Row
    if(board['0_0'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*0.5),int(line_c*0.5+screen_y*0.04))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['0_0'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*0.5),int(line_c*0.5+screen_y*0.04))
        screen.blit(x_img, x_img_rect_0_0)
    if(board['0_1'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*1.5),int(line_c*0.5+screen_y*0.04))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['0_1'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*1.5),int(line_c*0.5+screen_y*0.04))
        screen.blit(x_img, x_img_rect_0_0)
    if(board['0_2'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*2.5),int(line_c*0.5+screen_y*0.04))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['0_2'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*2.5),int(line_c*0.5+screen_y*0.04))
        screen.blit(x_img, x_img_rect_0_0)
    # Second Row
    if(board['1_0'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*0.5),int(line_c*1.5-screen_y*0.04))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['1_0'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*0.5),int(line_c*1.5-screen_y*0.04))
        screen.blit(x_img, x_img_rect_0_0)
    if(board['1_1'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*1.5),int(line_c*1.5-screen_y*0.04))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['1_1'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*1.5),int(line_c*1.5-screen_y*0.04))
        screen.blit(x_img, x_img_rect_0_0)
    if(board['1_2'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*2.5),int(line_c*1.5-screen_y*0.04))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['1_2'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*2.5),int(line_c*1.5-screen_y*0.04))
        screen.blit(x_img, x_img_rect_0_0)
    # Third Row
    if(board['2_0'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*0.5),int(line_c*2.5-screen_y*0.12))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['2_0'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*0.5),int(line_c*2.5-screen_y*0.12))
        screen.blit(x_img, x_img_rect_0_0)
    if(board['2_1'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*1.5),int(line_c*2.5-screen_y*0.12))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['2_1'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*1.5),int(line_c*2.5-screen_y*0.12))
        screen.blit(x_img, x_img_rect_0_0)
    if(board['2_2'] == 0):
        o_img_rect_0_0 = o_img.get_rect()
        o_img_rect_0_0.center = (int(line_a*2.5),int(line_c*2.5-screen_y*0.12))
        screen.blit(o_img, o_img_rect_0_0)
    if(board['2_2'] == 1):
        x_img_rect_0_0 = x_img.get_rect()
        x_img_rect_0_0.center = (int(line_a*2.5),int(line_c*2.5-screen_y*0.12))
        screen.blit(x_img, x_img_rect_0_0)
def board_modification(board, mouse_position, lines):
    global turn
    line_a = lines[0]
    line_b = lines[1]
    line_c = lines[2]
    line_d = lines[3]
    if mouse_position[0] < line_a and mouse_position[1] < line_c and board['0_0'] == None and turn == 0:
        board['0_0'] = 0
        turn  = turn_move(turn)
    if mouse_position[0] < line_a and mouse_position[1] < line_c and board['0_0'] == None and turn == 1:
        board['0_0'] = 1
        turn  = turn_move(turn)
    if (mouse_position[0] < line_b and mouse_position[0] > line_a) and mouse_position[1] < line_c and board['0_1'] == None and turn == 0:
        board['0_1'] = 0
        turn  = turn_move(turn)
    if (mouse_position[0] < line_b and mouse_position[0] > line_a) and mouse_position[1] < line_c and board['0_1'] == None and turn == 1:
        board['0_1'] = 1
        turn  = turn_move(turn)
    if mouse_position[0] > line_b and mouse_position[1] < line_c and board['0_2'] == None and turn == 0:
        board['0_2'] = 0
        turn  = turn_move(turn)
    if mouse_position[0] > line_b and mouse_position[1] < line_c and board['0_2'] == None and turn == 1:
        board['0_2'] = 1
        turn  = turn_move(turn)
    # Second Row
    if mouse_position[0] < line_a and (mouse_position[1] > line_c and mouse_position[1] < line_d) and board['1_0'] == None and turn == 0:
        board['1_0'] = 0
        turn  = turn_move(turn)
    if mouse_position[0] < line_a and (mouse_position[1] > line_c and mouse_position[1] < line_d) and board['1_0'] == None and turn == 1:
        board['1_0'] = 1
        turn  = turn_move(turn)
    if (mouse_position[0] < line_b and mouse_position[0] > line_a) and (mouse_position[1] > line_c and mouse_position[1] < line_d) and board['1_1'] == None and turn == 0:
        board['1_1'] = 0
        turn  = turn_move(turn)
    if (mouse_position[0] < line_b and mouse_position[0] > line_a) and (mouse_position[1] > line_c and mouse_position[1] < line_d) and board['1_1'] == None and turn == 1:
        board['1_1'] = 1
        turn  = turn_move(turn)
    if mouse_position[0] > line_b and (mouse_position[1] > line_c and mouse_position[1] < line_d) and board['1_2'] == None and turn == 0:
        board['1_2'] = 0
        turn  = turn_move(turn)
    if mouse_position[0] > line_b and (mouse_position[1] > line_c and mouse_position[1] < line_d) and board['1_2'] == None and turn == 1:
        board['1_2'] = 1
        turn  = turn_move(turn)
    # Third Row
    if mouse_position[0] < line_a and mouse_position[1] > line_d and board['2_0'] == None and turn == 0:
        board['2_0'] = 0
        turn  = turn_move(turn)
    if mouse_position[0] < line_a and mouse_position[1] > line_d and board['2_0'] == None and turn == 1:
        board['2_0'] = 1
        turn  = turn_move(turn)
    if (mouse_position[0] < line_b and mouse_position[0] > line_a) and mouse_position[1] > line_d and board['2_1'] == None and turn == 0:
        board['2_1'] = 0
        turn  = turn_move(turn)
    if (mouse_position[0] < line_b and mouse_position[0] > line_a) and mouse_position[1] > line_d and board['2_1'] == None and turn == 1:
        board['2_1'] = 1
        turn  = turn_move(turn)
    if mouse_position[0] > line_b and mouse_position[1] > line_d and board['2_2'] == None and turn == 0:
        board['2_2'] = 0
        turn  = turn_move(turn)
    if mouse_position[0] > line_b and mouse_position[1] > line_d and board['2_2'] == None and turn == 1:
        board['2_2'] = 1
        turn  = turn_move(turn)
    return board
def info_box():
    text_rectangle = pygame.draw.rect(screen, black, (0,0,screen_x,int(screen_y*0.08)))
    font = pygame.font.SysFont('Calibri', int(screen_y*0.06))
    if turn == 0:
        message = 'O\'s turn'
    if turn == 1:
        message = 'X\'s turn'
    if end_message != None:
        message = end_message
    text = font.render(message, True, white, black)
    text_box = text.get_rect()
    text_box.center = (int(screen_x*0.5),int(screen_y*0.040))
    screen.blit(text, text_box)
def menu_screen():
    global menu, start
    start = False

    if event.type == MOUSEBUTTONDOWN:
        mouse_position = pygame.mouse.get_pos()
        single_player = True
        if single_player == True:
            menu = False
            start = True
    if event.type == MOUSEBUTTONUP:
        pygame.time.wait(3000)
            


pygame.init()

screen_size = width, height = 500, 500
speed = [2, 2]
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode(screen_size, RESIZABLE)

background = white
screen.fill(background)
pygame.display.update()
x_img_int = pygame.image.load('X.png')
o_img_int = pygame.image.load('O.png')


running = True
red_box = False
start = (0, 0)
size = (0, 0)
drawing = False
screen_x = screen_size[0]
screen_y = screen_size[1]
line_a = int(screen_x/3)
line_b = int((screen_x/3)*2)
line_c = int(screen_y/3)
line_d = int((screen_y/3)*2)
board = dict()
for i in range(3):
    for n in range(3):
        board[str(i) + '_' + str(n)] = None
turn = randint(0, 1) # 0 = circle; 1 = X

menu = True
gameover = False
end_message = None
ticks = pygame.time.get_ticks()
menu_goal_ticks = 0
menu_wait = False
while running:
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)
        pygame.display.set_caption('Tic Tac Toe')
        screen.fill(background)
        if event.type == VIDEORESIZE:
            screen_size = event.size
            screen  = pygame.display.set_mode(screen_size, RESIZABLE)
            screen_x = screen_size[0]
            screen_y = screen_size[1]
        if menu == True:
            menu_screen()
        if start == True:
            
            line_a = int(screen_x/3)
            line_b = int((screen_x/3)*2)
            line_c = int(((screen_y*0.92)/3)+(screen_y*0.08))
            line_d = int((screen_y*0.92/3)*2+(screen_y*0.08))
            lines = []
            line_letters = ['a','b','c','d']
            for i in range(len(line_letters)):
                lines.append(globals()['line_'+line_letters[i]])
            info_box()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    background = green
                elif event.key == pygame.K_b:
                    background = blue
                elif event.key == pygame.K_r:
                    board = reset_board()
                    turn = randint(0, 1)
                
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                board = board_modification(board, mouse_position, lines)

            board_setup(lines)
            

            if line_a < line_c:
                line  = line_a
            else:
                line = line_c
            o_img = pygame.transform.smoothscale(o_img_int, (int(line*0.65), int(line*0.65)))
            x_img = pygame.transform.smoothscale(x_img_int, (int(line*0.6), int(line*0.6)))
            board_draw(board) # draws the x and o on the board

            if(board['0_0'] == 0 and board['0_1'] == 0 and board['0_2'] == 0):
                gameover = True
    
            if(gameover == True):
                gameover = False
                board = reset_board()

            if not(any(n is None for n in board.values())):
                end_message = 'It\'s a Draw'
                info_box()
                pygame.display.update()
                menu_wait = True
                menu_goal_ticks = ticks + 2000
    

            
        

        
        pygame.display.update()
    if menu_wait == True and (menu_goal_ticks - ticks <= 0):
        menu_wait = False
        menu_goal_ticks = 0
        end_message = None
        board = reset_board()
        #menu = True
        #start = False

pygame.quit()

