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
from update_game_unmortgage import *
from display_windows import *

def handle_rules(screen,Players,Cards,cur_player):

    display_rules_window(screen)


    # show the state after update
    
    screen.fill(BACKGROUND_COLOR)

    create_board(screen,Cards)

    create_game_options(screen)

    roll_dice(screen,4,2)
    
    for player in Players:
        player.move_player(screen,player.cur_position)

    create_player_info(screen,Players,Cards,cur_player)

    return cur_player

