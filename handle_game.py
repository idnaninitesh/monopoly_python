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


def handle_game(screen,Rects,rect_index,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects,isRunning):
    
    
    # a board card was clicked

    if len(Rects) == 40:
        if rect_index != 40:
            if Rects[0] == None:
                print("Info card : " + str(rect_index))
            else:
                print("Board card : " + str(rect_index))

    # a game action was clicked

    if len(Rects) == 8 and rect_index != 8:
        
        # roll dice

        if rect_index == 0:
            
            cur_player = handle_dice_roll(screen,rect_index,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)

        # build house/hotel

        elif rect_index == 1:

            cur_player = handle_build(screen,Players,Cards,cur_player,Cards_Rects,Option_Rects,Info_Cards_Rects)

            print("1;)")
        elif rect_index == 2:
            print("2;)")
            # trade
        elif rect_index == 3:
            print("3;)")
            # sell
        elif rect_index == 4:
            print("4;)")
            # mortgage
        elif rect_index == 5:
            print("5;)")
            # unmortgage
        elif rect_index == 6:
            print("6;)")
            # rules
        elif rect_index == 7:
            pygame.quit()
            # quit game


        # unlocking the game loop
        isRunning = False

        return cur_player,isRunning

