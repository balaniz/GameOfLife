#! /usr/bin/python3

import time
import os
import sys
import random
import argparse
import threading
import queue
import conway_patterns
import conway_colors
import wraparound_grid

def set_starting_cells( grid, cells ):
    for cell in cells:
        grid[cell[0]][cell[1]] = 1
    return grid

def check_rules( x, y, state, living_neighbor_count, grid ):
    if living_neighbor_count == 3 or \
        ( state == 1 and living_neighbor_count == 2 ):
        grid[x][y] = 1
    else:
        grid[x][y] = 0

    return grid

def play_game( grid ):
    """
          ( x-1, y-1 )  ( x, y-1 )  ( x+1, y-1 )
          ( x-1, y )    ( x, y )    ( x+1, y )
          ( x-1, y+1 )  ( x, y+1 )  ( x+1, y+1 )
          
        1. Any live cell with fewer than two live neighbours dies,
                as if caused by under-population.
        2. Any live cell with two or three live neighbours
                lives on to the next generation.
        3. Any live cell with more than three live neighbours dies,
                as if by overcrowding.
        4. Any dead cell with exactly three live neighbours becomes a live
                cell, as if by reproduction.
    """
    grid_width = len( grid )
    grid_height = len( grid[0] )
    new_grid = wraparound_grid.WraparoundGrid( grid_width, grid_height )

    for y in range( 0, grid_height ):
        for x in range( 0, grid_width ):
            living_neighbor_count = \
                    grid[x-1][y-1] + grid[x][y-1] + grid[x+1][y-1] + \
                    grid[x-1][y] + grid[x+1][y] + \
                    grid[x-1][y+1] + grid[x][y+1] + grid[x+1][y+1]
            new_grid = check_rules( x, y, grid[x][y],
                    living_neighbor_count, new_grid )
    
    return new_grid

def clear_screen():
    #os.system('cls' if os.name=='nt' else 'clear')
    os.system( 'tput reset' )

SLOW, FAST = range( 0, 2 )

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument( '-w', "--width", type = int,
            action = "store", dest = "width", default = 20 )
    parser.add_argument( '-t', "--height", type = int,
            action = "store", dest = "height", default = 20 )
    parser.add_argument( '-p', "--pattern", type = str,
            action = "store", default = "acorn", dest = "pattern" )
    parser.add_argument( '-s', "--slow", dest = "speed",
            const = SLOW, default = FAST, action = "store_const" )
    
    return parser.parse_args()

def make_painter( q ):
    def painter():
        while True:
            grid = q.get()
            clear_screen()
            for col in grid._grid:
                print( ' '.join( [ conway_colors.ConwayColors.DEFAULT + str( ' ' )
                        if num == 0 else
                        random.choice( conway_colors.ConwayColors.colors ) \
                        + str( '#' ) for num in col._list ] ) )
    return painter

def main():
    q = queue.Queue()
    random.seed( None )
    clear_screen()
    args = get_args()

    speed = 0.1 if args.speed == FAST else 0.5
    width = args.width
    height = args.height
    selection = args.pattern

    grid = wraparound_grid.WraparoundGrid( width, height )
    grid = set_starting_cells( grid, conway_patterns.pattern_factory().get(
            selection, conway_patterns.make_acorn )( width, height ) )
    
    painter = make_painter( q )
    thread = threading.Thread( target = painter )
    thread.daemon = True
    thread.start()

    while True:
        grid = play_game( grid )
        q.put( grid )
        time.sleep( speed )
        #clear_screen()

if __name__ == "__main__":
    main()

