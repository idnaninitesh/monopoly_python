# implement other game options

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
from handle_dice_roll import *
from handle_build import *
from handle_trade import *
from handle_sell import *
from handle_mortgage import *
from handle_unmortgage import *
from handle_decide_winner import *
from handle_rules import *
from handle_quit import *


def handle_game(screen,Rects,rect_index,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,isRunning):
    
    
    # a board card was clicked

    if len(Rects) == 40:
        if rect_index != 40:
            if Rects[0] == None:
                print("Info card : " + str(rect_index))
            else:
                print("Board card : " + str(rect_index))

    # a game action was clicked

    if len(Rects) == 9 and rect_index != 9:
        

        if rect_index == 0:
            
            cur_player = handle_dice_roll(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)


        elif rect_index == 1:

            cur_player = handle_build(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)

        elif rect_index == 2:

            cur_player = handle_trade(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)
            
        elif rect_index == 3:

            cur_player = handle_sell(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)

        elif rect_index == 4:

            cur_player = handle_mortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)

        elif rect_index == 5:

            cur_player = handle_unmortgage(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)

        elif rect_index == 6:

            cur_player = handle_decide_winner(screen,Players,Cards,cur_player)

        elif rect_index == 7:

            cur_player = handle_rules(screen,Players,Cards,cur_player)

        elif rect_index == 8:

            cur_player = handle_quit(screen,Players,Cards,cur_player)



        # unlocking the game loop
        isRunning = False

        return cur_player,isRunning

