import sys, pygame, random
from bot import bot_move
from pygame.locals import *
import pygame.gfxdraw
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
    pygame.draw.line(screen,black,(line_a,(0+(int(screen_y*0.08)))), (line_a,screen_y), 5) # vertical 1
    pygame.draw.line(screen,black,(line_b,(0+(int(screen_y*0.08)))), (line_b,screen_y), 5) # vertical 2
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
    if multi_player == True:
        if turn == 0:
            message = 'O\'s turn'
        if turn == 1:
            message = 'X\'s turn'
        if end_message != None:
            message = end_message
    if single_player == True:
        message = 'Your Turn'
        if end_message != None:
            message = end_message
    text = font.render(message, True, white, black)
    text_box = text.get_rect()
    text_box.center = (int(screen_x*0.5),int(screen_y*0.040))
    screen.blit(text, text_box)
def menu_screen():
    global menu, start, single_player, multi_player, click
    start = False
    if screen_x < screen_y: 
        smallest_screen_value = screen_x
    else:
        smallest_screen_value = screen_y
    font = pygame.font.SysFont('Calibri', int(smallest_screen_value*0.08))
    text_rectangle_0 = pygame.draw.rect(screen, black, (int(screen_x*0.25),int(screen_y*0.24),int(screen_x*0.50),int(screen_y*0.12)))
    text_0 = font.render('Single Player', True, white, black)
    text_box_0 = text_0.get_rect()
    text_box_0.center = (int(screen_x*0.5),int(screen_y*0.3))
    screen.blit(text_0, text_box_0)

    text_rectangle_1 = pygame.draw.rect(screen, black, (int(screen_x*0.25),int(screen_y*0.54),int(screen_x*0.50),int(screen_y*0.12)))
    text_1 = font.render('Multi Player', True, white, black)
    text_box_1 = text_1.get_rect()
    text_box_1.center = (int(screen_x*0.5),int(screen_y*0.6))
    screen.blit(text_1, text_box_1)

    if text_rectangle_0.collidepoint(mouse_position) and click == True:
        single_player = True
        click = False
    if text_rectangle_1.collidepoint(mouse_position) and click == True:
        multi_player = True
        click = False
    if single_player == True:
        menu = False
        start = True
    if multi_player == True:
        menu = False
        start = True
def win_lines(board):
    global end_message, player_symbol, game_end
    if(board['0_0'] == 0 and board['0_1'] == 0 and board['0_2'] == 0):
        end_message = 'O Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(0+screen_x*0.025),int(line_c*0.5+screen_y*0.0375)), (int(screen_x-screen_x*0.025),int(line_c*0.5+screen_y*0.0375)), 9)
    if(board['1_0'] == 0 and board['1_1'] == 0 and board['1_2'] == 0):
        end_message = 'O Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(0+screen_x*0.025),int(line_c+(line_c*0.5-screen_y*0.0425))), (int(screen_x-screen_x*0.025),int(line_c+(line_c*0.5-screen_y*0.0425))), 9)
    if(board['2_0'] == 0 and board['2_1'] == 0 and board['2_2'] == 0):
        end_message = 'O Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(0+screen_x*0.025),int(line_d+(line_c*0.5-screen_y*0.0425))), (int(screen_x-screen_x*0.025),int(line_d+(line_c*0.5-screen_y*0.0425))), 9)
    if(board['0_0'] == 0 and board['1_0'] == 0 and board['2_0'] == 0):
        end_message = 'O Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(line_a*0.5+screen_x*0.001),int((0+(screen_y*0.08)+screen_y*0.01))), (int(line_a*0.5+screen_x*0.001),int(screen_y-screen_y*0.01)), 9)
    if(board['0_1'] == 0 and board['1_1'] == 0 and board['2_1'] == 0):
        end_message = 'O Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(line_a*0.5+line_a+screen_x*0.001),int((0+(screen_y*0.08)+screen_y*0.01))), (int(line_a*0.5+line_a+screen_x*0.001),int(screen_y-screen_y*0.01)), 9)
    if(board['0_2'] == 0 and board['1_2'] == 0 and board['2_2'] == 0):
        end_message = 'O Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(line_a*0.5+line_b+screen_x*0.001),int((0+(screen_y*0.08)+screen_y*0.01))), (int(line_a*0.5+line_b+screen_x*0.001),int(screen_y-screen_y*0.01)), 9)#start
        game_end = True
    if(board['0_0'] == 0 and board['1_1'] == 0 and board['2_2'] == 0):
        end_message = 'O Won!'
        x1 = int((((0+screen_x*0.015)+(line_a*0.5))/2)-screen_x*0.05)
        y1 = int((((line_c*0.5+screen_y*0.04)+(0+(screen_y*0.08)+screen_y*0.015))/2)-screen_y*0.0475)
        x2 = int((((screen_x-screen_x*0.015)+(line_a*0.5+line_b))/2)+screen_x*0.05)
        y2 = int((((line_d+(line_c*0.5-screen_y*0.04))+(screen_y-screen_y*0.015))/2)+screen_y*0.045)
        for i in range(-4,5):
            pygame.draw.aaline(screen, red, (x1+i,y1),(x2+i,y2))
            pygame.draw.aaline(screen, red, (x1,y1+i),(x2,y2+i))
            pygame.draw.aaline(screen, red, (x1-i,y1),(x2-i,y2))
            pygame.draw.aaline(screen, red, (x1,y1-i),(x2,y2-i))
            game_end = True
    if(board['0_2'] == 0 and board['1_1'] == 0 and board['2_0'] == 0):
        end_message = 'O Won!'
        x1 = int((((screen_x-screen_x*0.015)+(line_a*0.5+line_b))/2)+screen_x*0.05)
        y1 = int((((line_c*0.5+screen_y*0.04)+(0+(screen_y*0.08)+screen_y*0.03))/2)-screen_y*0.0525)
        x2 = int((((0+screen_x*0.015)+(line_a*0.5))/2)-screen_x*0.05)
        y2 = int((((line_d+(line_c*0.5-screen_y*0.04))+(screen_y-screen_y*0.015))/2)+screen_y*0.045)
        for i in range(-4,5):
            pygame.draw.aaline(screen, red, (x1+i,y1),(x2+i,y2))
            pygame.draw.aaline(screen, red, (x1,y1+i),(x2,y2+i))
            pygame.draw.aaline(screen, red, (x1-i,y1),(x2-i,y2))
            pygame.draw.aaline(screen, red, (x1,y1-i),(x2,y2-i))
            game_end = True
    #x win
    if(board['0_0'] == 1 and board['0_1'] == 1 and board['0_2'] == 1):
        end_message = 'X Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(0+screen_x*0.025),int(line_c*0.5+screen_y*0.0375)), (int(screen_x-screen_x*0.025),int(line_c*0.5+screen_y*0.0375)), 9)
    if(board['1_0'] == 1 and board['1_1'] == 1 and board['1_2'] == 1):
        end_message = 'X Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(0+screen_x*0.025),int(line_c+(line_c*0.5-screen_y*0.0425))), (int(screen_x-screen_x*0.025),int(line_c+(line_c*0.5-screen_y*0.0425))), 9)
    if(board['2_0'] == 1 and board['2_1'] == 1 and board['2_2'] == 1):
        end_message = 'X Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(0+screen_x*0.025),int(line_d+(line_c*0.5-screen_y*0.0425))), (int(screen_x-screen_x*0.025),int(line_d+(line_c*0.5-screen_y*0.0425))), 9)
    if(board['0_0'] == 1 and board['1_0'] == 1 and board['2_0'] == 1):
        end_message = 'X Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(line_a*0.5+screen_x*0.001),int((0+(screen_y*0.08)+screen_y*0.01))), (int(line_a*0.5+screen_x*0.001),int(screen_y-screen_y*0.01)), 9)
    if(board['0_1'] == 1 and board['1_1'] == 1 and board['2_1'] == 1):
        end_message = 'X Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(line_a*0.5+line_a+screen_x*0.001),int((0+(screen_y*0.08)+screen_y*0.01))), (int(line_a*0.5+line_a+screen_x*0.001),int(screen_y-screen_y*0.01)), 9)
    if(board['0_2'] == 1 and board['1_2'] == 1 and board['2_2'] == 1):
        end_message = 'X Won!'
        game_end = True
        pygame.draw.line(screen,red,(int(line_a*0.5+line_b+screen_x*0.001),int((0+(screen_y*0.08)+screen_y*0.01))), (int(line_a*0.5+line_b+screen_x*0.001),int(screen_y-screen_y*0.01)), 9)#start
    if(board['0_0'] == 1 and board['1_1'] == 1 and board['2_2'] == 1):
        end_message = 'X Won!'
        game_end = True
        x1 = int((((0+screen_x*0.015)+(line_a*0.5))/2)-screen_x*0.05)
        y1 = int((((line_c*0.5+screen_y*0.04)+(0+(screen_y*0.08)+screen_y*0.015))/2)-screen_y*0.0475)
        x2 = int((((screen_x-screen_x*0.015)+(line_a*0.5+line_b))/2)+screen_x*0.05)
        y2 = int((((line_d+(line_c*0.5-screen_y*0.04))+(screen_y-screen_y*0.015))/2)+screen_y*0.045)
        for i in range(-4,5):
            pygame.draw.aaline(screen, red, (x1+i,y1),(x2+i,y2))
            pygame.draw.aaline(screen, red, (x1,y1+i),(x2,y2+i))
            pygame.draw.aaline(screen, red, (x1-i,y1),(x2-i,y2))
            pygame.draw.aaline(screen, red, (x1,y1-i),(x2,y2-i))
            game_end = True
    if(board['0_2'] == 1 and board['1_1'] == 1 and board['2_0'] == 1):
        end_message = 'X Won!'
        x1 = int((((screen_x-screen_x*0.015)+(line_a*0.5+line_b))/2)+screen_x*0.05)
        y1 = int((((line_c*0.5+screen_y*0.04)+(0+(screen_y*0.08)+screen_y*0.03))/2)-screen_y*0.0525)
        x2 = int((((0+screen_x*0.015)+(line_a*0.5))/2)-screen_x*0.05)
        y2 = int((((line_d+(line_c*0.5-screen_y*0.04))+(screen_y-screen_y*0.015))/2)+screen_y*0.045)
        for i in range(-4,5):
            pygame.draw.aaline(screen, red, (x1+i,y1),(x2+i,y2))
            pygame.draw.aaline(screen, red, (x1,y1+i),(x2,y2+i))
            pygame.draw.aaline(screen, red, (x1-i,y1),(x2-i,y2))
            pygame.draw.aaline(screen, red, (x1,y1-i),(x2,y2-i))
            game_end = True
    if end_message != None and single_player == True:
        if player_symbol == 0 and end_message == 'O Won!':
            end_message = 'You Won!'
        elif player_symbol == 1 and end_message == 'X Won!':
            end_message = 'You Won!'
        else:
            end_message = 'You Lost'
    if game_end == True:
        gameover()
def gameover():
    global board, menu_wait, goal_ticks, game_end, end_message, box_click, end_option, draw, menu, start, single_player, multi_player
    info_box()
    if screen_x < screen_y: 
        smallest_screen_value = screen_x
    else:
        smallest_screen_value = screen_y
    font = pygame.font.SysFont('Calibri', int(smallest_screen_value*0.08))
    text_rectangle_0 = pygame.draw.rect(screen, black, (int(screen_x*0.25),int(screen_y*0.34),int(screen_x*0.50),int(screen_y*0.12)))
    text_0 = font.render('Continue', True, white, black)
    text_box_0 = text_0.get_rect()
    text_box_0.center = (int(screen_x*0.5),int(screen_y*0.4))
    screen.blit(text_0, text_box_0)

    text_rectangle_1 = pygame.draw.rect(screen, black, (int(screen_x*0.25),int(screen_y*0.64),int(screen_x*0.50),int(screen_y*0.12)))
    text_1 = font.render('Main Menu', True, white, black)
    text_box_1 = text_1.get_rect()
    text_box_1.center = (int(screen_x*0.5),int(screen_y*0.7))
    screen.blit(text_1, text_box_1)

    if text_rectangle_0.collidepoint(mouse_position):
        end_option = 'continue'
    elif text_rectangle_1.collidepoint(mouse_position):
        end_option = 'mainmenu'
    if end_option == 'continue':
        end_message = None
        board = reset_board()
        end_option = None
        game_end = False
        box_click = False
        if draw == True:
            draw = False
    elif end_option == 'mainmenu':
        single_player = False
        multi_player = False
        start = False
        menu = True
        end_message = None
        end_option = None
        game_end = False
        box_click = False
        if draw == True:
            draw = False
        board = reset_board()

pygame.init()


screen_size = width, height = 500, 500
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (105,105,105)

screen = pygame.display.set_mode(screen_size, RESIZABLE)

background = white
screen.fill(background)
pygame.display.update()
x_img_int = pygame.image.load('X.png')
o_img_int = pygame.image.load('O.png')


running = True
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
mouse_position = (0,0)
menu = True
end_message = None
click = None
game_end = False
box_click = False
single_player = False
multi_player = False
end_option = None
game_end = False
draw = False
player_turn = False
player_symbol = 0
difficulty = 0
while running:
    ticks = pygame.time.get_ticks()
    screen.fill(background)
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
        board_setup(lines)
        if player_symbol == turn and single_player == True:
            player_turn = True
        elif multi_player == True:
            player_turn = True
        if box_click == True and game_end == False and player_turn == True:
            board = board_modification(board, mouse_position, lines)
            box_click = False
            player_turn = False
        elif single_player == True and game_end == False and player_turn == False:
            board = bot_move(board, player_symbol, difficulty)
            turn = turn_move(turn)
        if line_a < line_c:
            line  = line_a
        else:
            line = line_c
        o_img = pygame.transform.smoothscale(o_img_int, (int(line*0.65), int(line*0.65)))
        x_img = pygame.transform.smoothscale(x_img_int, (int(line*0.6), int(line*0.6)))
        board_draw(board) # draws the x and o on the board
        win_lines(board)
          
        
        if not(any(n is None for n in board.values())) and game_end == False:
            draw = True
        if draw == True:
            end_message = 'It\'s a Draw'
            gameover()



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)
        pygame.display.set_caption('Tic Tac Toe')
        
        if event.type == VIDEORESIZE:
            screen_size = event.size
            screen  = pygame.display.set_mode(screen_size, RESIZABLE)
            screen_x = screen_size[0]
            screen_y = screen_size[1]
        if menu == True:
            if event.type == MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                click = True
        if start == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    background = green
                elif event.key == pygame.K_b:
                    background = blue
                elif event.key == pygame.K_r:
                    board = reset_board()
                    turn = randint(0, 1)
                elif event.key == pygame.K_ESCAPE:
                    single_player = False
                    multi_player = False
                    end_message = None
                    end_option = None
                    game_end = False
                    box_click = False
                    player_turn = False
                    if draw == True:
                        draw = False
                    menu = True
                    start = False
                    board = reset_board()
            elif event.type == MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                box_click = True
                
pygame.quit()

