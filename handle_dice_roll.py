import pygame
import sys
from pygame.locals import *

from variables import *
from Player import *
from Card import *
from create_board import *
from create_game_options import *
from create_player_info import *
from handle_mouse_event import *
from update_game_dice import *
from handle_game import *


# roll dice and take action based on the new position of the current player

def handle_dice_roll(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects):
    

    # adding static part
    
    screen.fill(BACKGROUND_COLOR)

    create_board(screen,Cards)

    create_game_options(screen)

    create_player_info(screen,Players,Cards,cur_player)


    # rolling dice
    
    no1,no2,a,b = roll_dice(screen)
    steps = int(no1) + int(no2)

    player = Players[cur_player]

    initial_card = get_rect_pressed_index(player.cur_position,Cards_Rects)
    final_card = (initial_card + steps)%40


    # changing the current players' piece position
   
    final_pos = Cards[final_card].board_pos
    next_position = ()

    if player.color == "BLUE":
        next_position = (final_pos[0] + 19,final_pos[1] + 19)
    elif player.color == "RED":
        next_position = (final_pos[0] + 59,final_pos[1] + 19)
    elif player.color == "GREEN":
        next_position = (final_pos[0] + 19,final_pos[1] + 49)
    elif player.color == "YELLOW":
        next_position = (final_pos[0] + 59,final_pos[1] + 49)
    else:
        next_position = ()

    player.cur_position = next_position
    #player.move_player(screen,next_position)

    # updating the position of all players' piece on the board
    
    for temp in Players:
        temp.move_player(screen,temp.cur_position)


    # add the necessary actions to be taken due to dice roll
    final_card = update_game_dice(screen,initial_card,final_card,no1,no2,Players,Cards,cur_player)

    # changing the position if there is some related instruction in chance or community card 


    final_pos = Cards[final_card].board_pos
    next_position = ()

    if player.color == "BLUE":
        next_position = (final_pos[0] + 19,final_pos[1] + 19)
    elif player.color == "RED":
        next_position = (final_pos[0] + 59,final_pos[1] + 19)
    elif player.color == "GREEN":
        next_position = (final_pos[0] + 19,final_pos[1] + 49)
    elif player.color == "YELLOW":
        next_position = (final_pos[0] + 59,final_pos[1] + 49)
    else:
        next_position = ()

    player.cur_position = next_position

    isBankrupt = False
    quit_player = False

    # check if user is bankrupt or not

    if Players[cur_player].cur_balance < 0:
        Players[cur_player].isBankrupt = True
        isBankrupt = True
    else:
        Players[cur_player].isBankrupt = False
        
    # run loop till player removes bankruptcy or declares himself as bankrupt

    while not quit_player and isBankrupt:

        # show the state after update

        screen.fill(BACKGROUND_COLOR)

        create_board(screen,Cards)

        create_game_options(screen)
        
        for player in Players:
            player.move_player(screen,player.cur_position)

        create_player_info(screen,Players,Cards,cur_player)

        quit_player = display_bankrupt_window(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)

        if Players[cur_player].cur_balance < 0:
            Players[cur_player].isBankrupt = True
            isBankrupt = True
        else:
            Players[cur_player].isBankrupt = False
            isBankrupt = False



    # true implies player declares himself as bankrupt and withdraws from the game
    
    if quit_player == True:
        handle_quit_player(screen,Players,Cards,cur_player)

    # implies player has removed bankruptcy
    
    else:
        

        end_turn = False

        while not end_turn:

            # show the state after update

            screen.fill(BACKGROUND_COLOR)

            create_board(screen,Cards)

            create_game_options(screen)
            
            for player in Players:
                player.move_player(screen,player.cur_position)

            create_player_info(screen,Players,Cards,cur_player)

            end_turn = display_end_turn_window(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)


    # change turn to next player

    screen.fill(BACKGROUND_COLOR)

    create_board(screen,Cards)

    create_game_options(screen)

    roll_dice(screen,4,2)
    
    for player in Players:
        player.move_player(screen,player.cur_position)
    
    cur_player = (cur_player+1)%len(Players)

    create_player_info(screen,Players,Cards,cur_player)

    return cur_player
    

