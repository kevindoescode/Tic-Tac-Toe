import pygame
from bot import bot_move
from pygame.locals import VIDEORESIZE, RESIZABLE, MOUSEBUTTONUP
import pygame.gfxdraw
from random import randint


def reset_board():
    board = dict()
    for i in range(3):
        for n in range(3):
            board[str(i) + "_" + str(n)] = None
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
    pygame.draw.line(screen, BLACK, (0, line_c), (screen_x, line_c), 5)
    pygame.draw.line(screen, BLACK, (0, line_d), (screen_x, line_d), 5)
    y0 = int(screen_y * 0.08)
    pygame.draw.line(screen, BLACK, (line_a, y0), (line_a, screen_y), 5)
    pygame.draw.line(screen, BLACK, (line_b, y0), (line_b, screen_y), 5)


def board_draw(board):
    # First Row
    if board["0_0"] == 0:
        o_img_rect_0_0 = o_img.get_rect()
        x_center = int(line_a * 0.5)
        y_center = int(line_c * 0.5 + screen_y * 0.04)
        o_img_rect_0_0.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_0_0)
    if board["0_0"] == 1:
        x_img_rect_0_0 = x_img.get_rect()
        x_center = int(line_a * 0.5)
        y_center = int(line_c * 0.5 + screen_y * 0.04)
        x_img_rect_0_0.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_0_0)
    if board["0_1"] == 0:
        o_img_rect_0_1 = o_img.get_rect()
        x_center = int(line_a * 1.5)
        y_center = int(line_c * 0.5 + screen_y * 0.04)
        o_img_rect_0_1.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_0_1)
    if board["0_1"] == 1:
        x_img_rect_0_1 = x_img.get_rect()
        x_center = int(line_a * 1.5)
        y_center = int(line_c * 0.5 + screen_y * 0.04)
        x_img_rect_0_1.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_0_1)
    if board["0_2"] == 0:
        o_img_rect_0_2 = o_img.get_rect()
        x_center = int(line_a * 2.5)
        y_center = int(line_c * 0.5 + screen_y * 0.04)
        o_img_rect_0_2.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_0_2)
    if board["0_2"] == 1:
        x_img_rect_0_2 = x_img.get_rect()
        x_center = int(line_a * 2.5)
        y_center = int(line_c * 0.5 + screen_y * 0.04)
        x_img_rect_0_2.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_0_2)
    # Second Row
    if board["1_0"] == 0:
        o_img_rect_1_0 = o_img.get_rect()
        x_center = int(line_a * 0.5)
        y_center = int(line_c * 1.5 - screen_y * 0.04)
        o_img_rect_1_0.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_1_0)
    if board["1_0"] == 1:
        x_img_rect_1_0 = x_img.get_rect()
        x_center = int(line_a * 0.5)
        y_center = int(line_c * 1.5 - screen_y * 0.04)
        x_img_rect_1_0.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_1_0)
    if board["1_1"] == 0:
        o_img_rect_1_1 = o_img.get_rect()
        x_center = int(line_a * 1.5)
        y_center = int(line_c * 1.5 - screen_y * 0.04)
        o_img_rect_1_1.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_1_1)
    if board["1_1"] == 1:
        x_img_rect_1_1 = x_img.get_rect()
        x_center = int(line_a * 1.5)
        y_center = int(line_c * 1.5 - screen_y * 0.04)
        x_img_rect_1_1.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_1_1)
    if board["1_2"] == 0:
        o_img_rect_1_2 = o_img.get_rect()
        x_center = int(line_a * 2.5)
        y_center = int(line_c * 1.5 - screen_y * 0.04)
        o_img_rect_1_2.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_1_2)
    if board["1_2"] == 1:
        x_img_rect_1_2 = x_img.get_rect()
        x_center = int(line_a * 2.5)
        y_center = int(line_c * 1.5 - screen_y * 0.04)
        x_img_rect_1_2.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_1_2)
    # Third Row
    if board["2_0"] == 0:
        o_img_rect_2_0 = o_img.get_rect()
        x_center = int(line_a * 0.5)
        y_center = int(line_c * 2.5 - screen_y * 0.12)
        o_img_rect_2_0.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_2_0)
    if board["2_0"] == 1:
        x_img_rect_2_0 = x_img.get_rect()
        x_center = int(line_a * 0.5)
        y_center = int(line_c * 2.5 - screen_y * 0.12)
        x_img_rect_2_0.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_2_0)
    if board["2_1"] == 0:
        o_img_rect_2_1 = o_img.get_rect()
        x_center = int(line_a * 1.5)
        y_center = int(line_c * 2.5 - screen_y * 0.12)
        o_img_rect_2_1.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_2_1)
    if board["2_1"] == 1:
        x_img_rect_2_1 = x_img.get_rect()
        x_center = int(line_a * 1.5)
        y_center = int(line_c * 2.5 - screen_y * 0.12)
        x_img_rect_2_1.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_2_1)
    if board["2_2"] == 0:
        o_img_rect_2_2 = o_img.get_rect()
        x_center = int(line_a * 2.5)
        y_center = int(line_c * 2.5 - screen_y * 0.12)
        o_img_rect_2_2.center = (x_center, y_center)
        screen.blit(o_img, o_img_rect_2_2)
    if board["2_2"] == 1:
        x_img_rect_2_2 = x_img.get_rect()
        x_center = int(line_a * 2.5)
        y_center = int(line_c * 2.5 - screen_y * 0.12)
        x_img_rect_2_2.center = (x_center, y_center)
        screen.blit(x_img, x_img_rect_2_2)


def board_modification(board, mouse_position, lines):
    global turn
    line_a = lines[0]
    line_b = lines[1]
    line_c = lines[2]
    line_d = lines[3]
    if (
        mouse_position[0] < line_a
        and mouse_position[1] < line_c
        and board["0_0"] is None
        and turn == 0
    ):
        board["0_0"] = 0
        turn = turn_move(turn)
    if (
        mouse_position[0] < line_a
        and mouse_position[1] < line_c
        and board["0_0"] is None
        and turn == 1
    ):
        board["0_0"] = 1
        turn = turn_move(turn)
    if (
        (mouse_position[0] < line_b and mouse_position[0] > line_a)
        and mouse_position[1] < line_c
        and board["0_1"] is None
        and turn == 0
    ):
        board["0_1"] = 0
        turn = turn_move(turn)
    if (
        (mouse_position[0] < line_b and mouse_position[0] > line_a)
        and mouse_position[1] < line_c
        and board["0_1"] is None
        and turn == 1
    ):
        board["0_1"] = 1
        turn = turn_move(turn)
    if (
        mouse_position[0] > line_b
        and mouse_position[1] < line_c
        and board["0_2"] is None
        and turn == 0
    ):
        board["0_2"] = 0
        turn = turn_move(turn)
    if (
        mouse_position[0] > line_b
        and mouse_position[1] < line_c
        and board["0_2"] is None
        and turn == 1
    ):
        board["0_2"] = 1
        turn = turn_move(turn)
    # Second Row
    if (
        mouse_position[0] < line_a
        and (mouse_position[1] > line_c and mouse_position[1] < line_d)
        and board["1_0"] is None
        and turn == 0
    ):
        board["1_0"] = 0
        turn = turn_move(turn)
    if (
        mouse_position[0] < line_a
        and (mouse_position[1] > line_c and mouse_position[1] < line_d)
        and board["1_0"] is None
        and turn == 1
    ):
        board["1_0"] = 1
        turn = turn_move(turn)
    if (
        (mouse_position[0] < line_b and mouse_position[0] > line_a)
        and (mouse_position[1] > line_c and mouse_position[1] < line_d)
        and board["1_1"] is None
        and turn == 0
    ):
        board["1_1"] = 0
        turn = turn_move(turn)
    if (
        (mouse_position[0] < line_b and mouse_position[0] > line_a)
        and (mouse_position[1] > line_c and mouse_position[1] < line_d)
        and board["1_1"] is None
        and turn == 1
    ):
        board["1_1"] = 1
        turn = turn_move(turn)
    if (
        mouse_position[0] > line_b
        and (mouse_position[1] > line_c and mouse_position[1] < line_d)
        and board["1_2"] is None
        and turn == 0
    ):
        board["1_2"] = 0
        turn = turn_move(turn)
    if (
        mouse_position[0] > line_b
        and (mouse_position[1] > line_c and mouse_position[1] < line_d)
        and board["1_2"] is None
        and turn == 1
    ):
        board["1_2"] = 1
        turn = turn_move(turn)
    # Third Row
    if (
        mouse_position[0] < line_a
        and mouse_position[1] > line_d
        and board["2_0"] is None
        and turn == 0
    ):
        board["2_0"] = 0
        turn = turn_move(turn)
    if (
        mouse_position[0] < line_a
        and mouse_position[1] > line_d
        and board["2_0"] is None
        and turn == 1
    ):
        board["2_0"] = 1
        turn = turn_move(turn)
    if (
        (mouse_position[0] < line_b and mouse_position[0] > line_a)
        and mouse_position[1] > line_d
        and board["2_1"] is None
        and turn == 0
    ):
        board["2_1"] = 0
        turn = turn_move(turn)
    if (
        (mouse_position[0] < line_b and mouse_position[0] > line_a)
        and mouse_position[1] > line_d
        and board["2_1"] is None
        and turn == 1
    ):
        board["2_1"] = 1
        turn = turn_move(turn)
    if (
        mouse_position[0] > line_b
        and mouse_position[1] > line_d
        and board["2_2"] is None
        and turn == 0
    ):
        board["2_2"] = 0
        turn = turn_move(turn)
    if (
        mouse_position[0] > line_b
        and mouse_position[1] > line_d
        and board["2_2"] is None
        and turn == 1
    ):
        board["2_2"] = 1
        turn = turn_move(turn)
    return board


def info_box():
    pygame.draw.rect(screen, BLACK, (0, 0, screen_x, int(screen_y * 0.08)))
    font = pygame.font.SysFont("Calibri", int(screen_y * 0.06))
    if multi_player is True:
        if turn == 0:
            message = "O's turn"
        if turn == 1:
            message = "X's turn"
        if end_message is not None:
            message = end_message
    if single_player is True:
        message = "Your Turn"
        if end_message is not None:
            message = end_message
    text = font.render(message, True, WHITE, BLACK)
    text_box = text.get_rect()
    text_box.center = (int(screen_x * 0.5), int(screen_y * 0.040))
    screen.blit(text, text_box)


def menu_screen():
    global menu, start, single_player, multi_player, click
    global player_symbol, difficulty, turn
    start = False
    if screen_x < screen_y:
        smallest_screen_value = screen_x
    else:
        smallest_screen_value = screen_y
    font = pygame.font.SysFont("Calibri", int(smallest_screen_value * 0.08))
    text_rectangle_0 = pygame.draw.rect(
        screen,
        BLACK,
        (
            int(screen_x * 0.25),
            int(screen_y * 0.24),
            int(screen_x * 0.50),
            int(screen_y * 0.12),
        ),
    )
    text_0 = font.render("Single Player", True, WHITE, BLACK)
    text_box_0 = text_0.get_rect()
    text_box_0.center = (int(screen_x * 0.5), int(screen_y * 0.3))
    screen.blit(text_0, text_box_0)

    text_rectangle_1 = pygame.draw.rect(
        screen,
        BLACK,
        (
            int(screen_x * 0.25),
            int(screen_y * 0.54),
            int(screen_x * 0.50),
            int(screen_y * 0.12),
        ),
    )
    text_1 = font.render("Multi Player", True, WHITE, BLACK)
    text_box_1 = text_1.get_rect()
    text_box_1.center = (int(screen_x * 0.5), int(screen_y * 0.6))
    screen.blit(text_1, text_box_1)

    if text_rectangle_0.collidepoint(mouse_position) and click is True:
        single_player = True
        click = False
    if text_rectangle_1.collidepoint(mouse_position) and click is True:
        multi_player = True
        click = False
    if single_player is True:
        menu = False
        start = True
        turn = randint(0, 1)
    if multi_player is True:
        menu = False
        start = True
        turn = randint(0, 1)
    font = pygame.font.SysFont("Calibri", int(smallest_screen_value * 0.06))
    text_rectangle_2 = pygame.draw.rect(
        screen,
        BLACK,
        (
            int(screen_x * 0.115),
            int(screen_y * 0.88),
            int(screen_x * 0.27),
            int(screen_y * 0.125),
        ),
    )
    if player_symbol == 0:
        text_2 = font.render("Symbol: O", True, WHITE, BLACK)
    if player_symbol == 1:
        text_2 = font.render("Symbol: X", True, WHITE, BLACK)
    text_box_2 = text_2.get_rect()
    text_box_2.center = (int(screen_x * 0.25), int(screen_y * 0.94))
    screen.blit(text_2, text_box_2)
    if text_rectangle_2.collidepoint(mouse_position) and click is True:
        if player_symbol == 0:
            player_symbol = 1
            click = False
        elif player_symbol == 1:
            player_symbol = 0
            click = False
    font = pygame.font.SysFont("Calibri", int(smallest_screen_value * 0.08))
    text_rectangle_3 = pygame.draw.rect(
        screen,
        BLACK,
        (
            int(screen_x * 0.625),
            int(screen_y * 0.88),
            int(screen_x * 0.25),
            int(screen_y * 0.125),
        ),
    )
    if difficulty == 0:
        text_3 = font.render("Easy", True, WHITE, BLACK)
    if difficulty == 1:
        text_3 = font.render("Normal", True, WHITE, BLACK)
    if difficulty == 2:
        text_3 = font.render("Hard", True, WHITE, BLACK)
    text_box_3 = text_3.get_rect()
    text_box_3.center = (int(screen_x * 0.75), int(screen_y * 0.94))
    screen.blit(text_3, text_box_3)
    if text_rectangle_3.collidepoint(mouse_position) and click is True:
        if difficulty == 0:
            difficulty = 1
            click = False
        elif difficulty == 1:
            difficulty = 2
            click = False
        elif difficulty == 2:
            difficulty = 0
            click = False


def win_lines(board):
    global end_message, player_symbol, game_end
    if board["0_0"] == 0 and board["0_1"] == 0 and board["0_2"] == 0:
        end_message = "O Won!"
        game_end = True
        x0 = int(0 + screen_x * 0.025)
        x1 = int(screen_x - screen_x * 0.025)
        y = int(line_c * 0.5 + screen_y * 0.0375)
        pygame.draw.line(screen, RED, (x0, y), (x1, y), 9)
    if board["1_0"] == 0 and board["1_1"] == 0 and board["1_2"] == 0:
        end_message = "O Won!"
        game_end = True
        x0 = int(0 + screen_x * 0.025)
        x1 = int(screen_x - screen_x * 0.025)
        y = int(line_c + (line_c * 0.5 - screen_y * 0.0425))
        pygame.draw.line(screen, RED, (x0, y), (x1, y), 9)
    if board["2_0"] == 0 and board["2_1"] == 0 and board["2_2"] == 0:
        end_message = "O Won!"
        game_end = True
        x0 = int(0 + screen_x * 0.025)
        x1 = int(screen_x - screen_x * 0.025)
        y = int(line_d + (line_c * 0.5 - screen_y * 0.0425))
        pygame.draw.line(screen, RED, (x0, y), (x1, y), 9)
    if board["0_0"] == 0 and board["1_0"] == 0 and board["2_0"] == 0:
        end_message = "O Won!"
        game_end = True
        x = int(line_a * 0.5 + screen_x * 0.001)
        y0 = int((0 + (screen_y * 0.08) + screen_y * 0.01))
        y1 = int(screen_y - screen_y * 0.01)
        pygame.draw.line(screen, RED, (x, 1), (x, y1), 9)
    if board["0_1"] == 0 and board["1_1"] == 0 and board["2_1"] == 0:
        end_message = "O Won!"
        game_end = True
        x = int(line_a * 0.5 + line_a + screen_x * 0.001)
        y0 = int((0 + (screen_y * 0.08) + screen_y * 0.01))
        y1 = int(screen_y - screen_y * 0.01)
        pygame.draw.line(screen, RED, (x, 1), (x, y1), 9)
    if board["0_2"] == 0 and board["1_2"] == 0 and board["2_2"] == 0:
        end_message = "O Won!"
        game_end = True
        x = int(line_a * 0.5 + line_b + screen_x * 0.001)
        y0 = int((0 + (screen_y * 0.08) + screen_y * 0.01))
        y1 = int(screen_y - screen_y * 0.01)
        pygame.draw.line(screen, RED, (x, 1), (x, y1), 9)
    if board["0_0"] == 0 and board["1_1"] == 0 and board["2_2"] == 0:
        end_message = "O Won!"
        x1 = int((((0 + screen_x * 0.015) + (line_a * 0.5)) / 2) - screen_x * 0.05)
        y1 = int(
            (
                (
                    (line_c * 0.5 + screen_y * 0.04)
                    + (0 + (screen_y * 0.08) + screen_y * 0.015)
                )
                / 2
            )
            - screen_y * 0.0475
        )
        x2 = int(
            (((screen_x - screen_x * 0.015) + (line_a * 0.5 + line_b)) / 2)
            + screen_x * 0.05
        )
        y2 = int(
            (
                (
                    (line_d + (line_c * 0.5 - screen_y * 0.04))
                    + (screen_y - screen_y * 0.015)
                )
                / 2
            )
            + screen_y * 0.045
        )
        for i in range(-4, 5):
            pygame.draw.aaline(screen, RED, (x1 + i, y1), (x2 + i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 + i), (x2, y2 + i))
            pygame.draw.aaline(screen, RED, (x1 - i, y1), (x2 - i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 - i), (x2, y2 - i))
            game_end = True
    if board["0_2"] == 0 and board["1_1"] == 0 and board["2_0"] == 0:
        end_message = "O Won!"
        x1 = int(
            (((screen_x - screen_x * 0.015) + (line_a * 0.5 + line_b)) / 2)
            + screen_x * 0.05
        )
        y1 = int(
            (
                (
                    (line_c * 0.5 + screen_y * 0.04)
                    + (0 + (screen_y * 0.08) + screen_y * 0.03)
                )
                / 2
            )
            - screen_y * 0.0525
        )
        x2 = int((((0 + screen_x * 0.015) + (line_a * 0.5)) / 2) - screen_x * 0.05)
        y2 = int(
            (
                (
                    (line_d + (line_c * 0.5 - screen_y * 0.04))
                    + (screen_y - screen_y * 0.015)
                )
                / 2
            )
            + screen_y * 0.045
        )
        for i in range(-4, 5):
            pygame.draw.aaline(screen, RED, (x1 + i, y1), (x2 + i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 + i), (x2, y2 + i))
            pygame.draw.aaline(screen, RED, (x1 - i, y1), (x2 - i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 - i), (x2, y2 - i))
            game_end = True
    # x win
    if board["0_0"] == 1 and board["0_1"] == 1 and board["0_2"] == 1:
        end_message = "X Won!"
        game_end = True
        x0 = int(0 + screen_x * 0.025)
        x1 = int(screen_x - screen_x * 0.025)
        y = int(line_c * 0.5 + screen_y * 0.0375)
        pygame.draw.line(screen, RED, (x0, y), (x1, y), 9)
    if board["1_0"] == 1 and board["1_1"] == 1 and board["1_2"] == 1:
        end_message = "X Won!"
        game_end = True
        x0 = int(0 + screen_x * 0.025)
        x1 = int(screen_x - screen_x * 0.025)
        y = int(line_c + (line_c * 0.5 - screen_y * 0.0425))
        pygame.draw.line(screen, RED, (x0, y), (x1, y), 9)
    if board["2_0"] == 1 and board["2_1"] == 1 and board["2_2"] == 1:
        end_message = "X Won!"
        game_end = True
        x0 = int(0 + screen_x * 0.025)
        x1 = int(screen_x - screen_x * 0.025)
        y = int(line_d + (line_c * 0.5 - screen_y * 0.0425))
        pygame.draw.line(screen, RED, (x0, y), (x1, y), 9)
    if board["0_0"] == 1 and board["1_0"] == 1 and board["2_0"] == 1:
        end_message = "X Won!"
        game_end = True
        x = int(line_a * 0.5 + screen_x * 0.001)
        y0 = int((0 + (screen_y * 0.08) + screen_y * 0.01))
        y1 = int(screen_y - screen_y * 0.01)
        pygame.draw.line(screen, RED, (x, y0), (x, y1), 9)
    if board["0_1"] == 1 and board["1_1"] == 1 and board["2_1"] == 1:
        end_message = "X Won!"
        game_end = True
        x = int(line_a * 0.5 + line_a + screen_x * 0.001)
        y0 = int((0 + (screen_y * 0.08) + screen_y * 0.01))
        y1 = int(screen_y - screen_y * 0.01)
        pygame.draw.line(screen, RED, (x, y0), (x, y1), 9)
    if board["0_2"] == 1 and board["1_2"] == 1 and board["2_2"] == 1:
        end_message = "X Won!"
        game_end = True
        x = int(line_a * 0.5 + line_b + screen_x * 0.001)
        y0 = int((0 + (screen_y * 0.08) + screen_y * 0.01))
        y1 = int(screen_y - screen_y * 0.01)
        pygame.draw.line(screen, RED, (x, y0), (x, y1), 9)
    if board["0_0"] == 1 and board["1_1"] == 1 and board["2_2"] == 1:
        end_message = "X Won!"
        game_end = True
        x1 = int((((0 + screen_x * 0.015) + (line_a * 0.5)) / 2) - screen_x * 0.05)
        y1 = int(
            (
                (
                    (line_c * 0.5 + screen_y * 0.04)
                    + (0 + (screen_y * 0.08) + screen_y * 0.015)
                )
                / 2
            )
            - screen_y * 0.0475
        )
        x2 = int(
            (((screen_x - screen_x * 0.015) + (line_a * 0.5 + line_b)) / 2)
            + screen_x * 0.05
        )
        y2 = int(
            (
                (
                    (line_d + (line_c * 0.5 - screen_y * 0.04))
                    + (screen_y - screen_y * 0.015)
                )
                / 2
            )
            + screen_y * 0.045
        )
        for i in range(-4, 5):
            pygame.draw.aaline(screen, RED, (x1 + i, y1), (x2 + i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 + i), (x2, y2 + i))
            pygame.draw.aaline(screen, RED, (x1 - i, y1), (x2 - i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 - i), (x2, y2 - i))
            game_end = True
    if board["0_2"] == 1 and board["1_1"] == 1 and board["2_0"] == 1:
        end_message = "X Won!"
        x1 = int(
            (((screen_x - screen_x * 0.015) + (line_a * 0.5 + line_b)) / 2)
            + screen_x * 0.05
        )
        y1 = int(
            (
                (
                    (line_c * 0.5 + screen_y * 0.04)
                    + (0 + (screen_y * 0.08) + screen_y * 0.03)
                )
                / 2
            )
            - screen_y * 0.0525
        )
        x2 = int((((0 + screen_x * 0.015) + (line_a * 0.5)) / 2) - screen_x * 0.05)
        y2 = int(
            (
                (
                    (line_d + (line_c * 0.5 - screen_y * 0.04))
                    + (screen_y - screen_y * 0.015)
                )
                / 2
            )
            + screen_y * 0.045
        )
        for i in range(-4, 5):
            pygame.draw.aaline(screen, RED, (x1 + i, y1), (x2 + i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 + i), (x2, y2 + i))
            pygame.draw.aaline(screen, RED, (x1 - i, y1), (x2 - i, y2))
            pygame.draw.aaline(screen, RED, (x1, y1 - i), (x2, y2 - i))
            game_end = True
    if end_message is not None and single_player is True:
        if player_symbol == 0 and end_message == "O Won!":
            end_message = "You Won!"
        elif player_symbol == 1 and end_message == "X Won!":
            end_message = "You Won!"
        else:
            end_message = "You Lost"
    if game_end is True:
        gameover()


def gameover():
    global board, menu_wait, goal_ticks, game_end, end_message, box_click
    global end_option, draw, menu, start, single_player, multi_player
    info_box()
    if screen_x < screen_y:
        smallest_screen_value = screen_x
    else:
        smallest_screen_value = screen_y
    font = pygame.font.SysFont("Calibri", int(smallest_screen_value * 0.08))
    text_rectangle_0 = pygame.draw.rect(
        screen,
        BLACK,
        (
            int(screen_x * 0.25),
            int(screen_y * 0.34),
            int(screen_x * 0.50),
            int(screen_y * 0.12),
        ),
    )
    text_0 = font.render("Continue", True, WHITE, BLACK)
    text_box_0 = text_0.get_rect()
    text_box_0.center = (int(screen_x * 0.5), int(screen_y * 0.4))
    screen.blit(text_0, text_box_0)

    text_rectangle_1 = pygame.draw.rect(
        screen,
        BLACK,
        (
            int(screen_x * 0.25),
            int(screen_y * 0.64),
            int(screen_x * 0.50),
            int(screen_y * 0.12),
        ),
    )
    text_1 = font.render("Main Menu", True, WHITE, BLACK)
    text_box_1 = text_1.get_rect()
    text_box_1.center = (int(screen_x * 0.5), int(screen_y * 0.7))
    screen.blit(text_1, text_box_1)
    if box_click is True:
        if text_rectangle_0.collidepoint(mouse_position):
            end_option = "continue"
        elif text_rectangle_1.collidepoint(mouse_position):
            end_option = "mainmenu"
    if end_option == "continue":
        end_message = None
        board = reset_board()
        end_option = None
        game_end = False
        box_click = False
        if draw is True:
            draw = False
    elif end_option == "mainmenu":
        single_player = False
        multi_player = False
        start = False
        menu = True
        end_message = None
        end_option = None
        game_end = False
        box_click = False
        if draw is True:
            draw = False
        board = reset_board()


def save_settings(player_symbol, difficulty):
    with open(r"./settings.ini", "w") as settings_file:
        settings = (
            "Player symbol = "
            + str(player_symbol)
            + "\nDifficulty = "
            + str(difficulty)
        )
        settings_file.write(settings)


pygame.init()


screen_size = width, height = 500, 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (105, 105, 105)
screen = pygame.display.set_mode(screen_size, RESIZABLE)

background = WHITE
screen.fill(background)
pygame.display.update()
x_img_int = pygame.image.load("X.png")
o_img_int = pygame.image.load("O.png")


running = True
debug = True
screen_x = screen_size[0]
screen_y = screen_size[1]
line_a = int(screen_x / 3)
line_b = int((screen_x / 3) * 2)
line_c = int(screen_y / 3)
line_d = int((screen_y / 3) * 2)
board = dict()
for i in range(3):
    for n in range(3):
        board[str(i) + "_" + str(n)] = None
turn = randint(0, 1)  # 0 = circle; 1 = X
mouse_position = (0, 0)
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
try:
    with open(r"./settings.ini", "r") as settings_file:
        settings_data = settings_file.read().split("\n")
        settings_data_0 = settings_data[0].split(" = ")
        settings_data_1 = settings_data[1].split(" = ")
        settings = [
            str(settings_data_0[0].replace(" ", "_").lower()),
            str(settings_data_1[0].replace(" ", "_").lower()),
        ]
        i = 0
        for setting in settings:
            globals()[setting] = int(globals()["settings_data_" + str(i)][1])
            i += 1
        del i
except FileNotFoundError:
    with open(r"./settings.ini", "w") as settings_file:
        save_settings(player_symbol, difficulty)
while running:
    ticks = pygame.time.get_ticks()
    screen.fill(background)
    if menu is True:
        menu_screen()
    if start is True:
        line_a = int(screen_x / 3)
        line_b = int((screen_x / 3) * 2)
        line_c = int(((screen_y * 0.92) / 3) + (screen_y * 0.08))
        line_d = int((screen_y * 0.92 / 3) * 2 + (screen_y * 0.08))
        lines = []
        line_letters = ["a", "b", "c", "d"]
        for i in range(len(line_letters)):
            lines.append(globals()["line_" + line_letters[i]])
        info_box()
        board_setup(lines)
        if player_symbol == turn and single_player is True:
            player_turn = True
        elif multi_player is True:
            player_turn = True
        if box_click is True and game_end is False and player_turn is True:
            board = board_modification(board, mouse_position, lines)
            box_click = False
            player_turn = False
        elif (
            single_player is True
            and game_end is False
            and player_turn is False
            and True
        ):
            board = bot_move(board, player_symbol, difficulty)
            turn = turn_move(turn)
        if line_a < line_c:
            line = line_a
        else:
            line = line_c
        o_img = pygame.transform.smoothscale(
            o_img_int, (int(line * 0.65), int(line * 0.65))
        )
        x_img = pygame.transform.smoothscale(
            x_img_int, (int(line * 0.6), int(line * 0.6))
        )
        board_draw(board)  # draws the x and o on the board
        win_lines(board)

        if not (any(n is None for n in board.values())) and game_end is False:
            draw = True
        if draw is True:
            game_end = True
            end_message = "It's a Draw"
            gameover()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            save_settings(player_symbol, difficulty)
        # print(event)
        pygame.display.set_caption("Tic Tac Toe")

        if event.type == VIDEORESIZE:
            screen_size = event.size
            screen = pygame.display.set_mode(screen_size, RESIZABLE)
            screen_x = screen_size[0]
            screen_y = screen_size[1]
        if menu is True:
            if event.type == MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                click = True
        if start is True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and debug is True:
                    board = reset_board()
                    turn = randint(0, 1)
                if event.key == pygame.K_ESCAPE:
                    single_player = False
                    multi_player = False
                    end_message = None
                    end_option = None
                    game_end = False
                    box_click = False
                    player_turn = False
                    if draw is True:
                        draw = False
                    menu = True
                    start = False
                    board = reset_board()
            elif event.type == MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                box_click = True

pygame.quit()
