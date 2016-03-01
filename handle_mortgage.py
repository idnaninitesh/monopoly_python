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
from update_game_build import *
from update_game_sell import *
from update_game_mortgage import *


# allow user to mortgage property to the bank

def handle_mortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects):

    # adding static part

    screen.fill(BACKGROUND_COLOR)

    create_board(screen)

    create_game_options(screen)

    create_player_info(screen,Players,Cards,cur_player)

    for player in Players:
        player.move_player(screen,player.cur_position)

    # create cards available for mortgage

    Mark = []

    player = Players[cur_player]

    for prop in player.property_owned:
        Mark.append(prop)

    if Mark != []:
        update_game_mortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,Mark)

    # show the state after update


    screen.fill(BACKGROUND_COLOR)

    create_board(screen)

    create_game_options(screen)

    roll_dice(screen,4,2)
    
    for player in Players:
        player.move_player(screen,player.cur_position)

    create_player_info(screen,Players,Cards,cur_player)

    return cur_player


