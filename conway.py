#! /usr/bin/python3

import time
import os
import sys
import random
import conway_patterns
import conway_colors

def init_grid( size ):
    y = [ 0 for num in range( 0, size ) ]
    return [ list( y ) for num in range( 0, size ) ]

def set_starting_cells( grid, cells ):
    for cell in cells:
        grid[cell[1]][cell[0]] = 1
    return grid

def check_rules( x, y, state, living_neighbor_count, dead_cells, new_cells ):
    if state == 1 and living_neighbor_count < 2:
        dead_cells.append( ( x, y ) )
        return dead_cells, new_cells
    if state == 1 and living_neighbor_count < 4:
        return dead_cells, new_cells
    if state == 1 and living_neighbor_count > 3:
        dead_cells.append( ( x, y ) )
        return dead_cells, new_cells
    if state == 0 and living_neighbor_count == 3:
        new_cells.append( ( x, y ) )
        return dead_cells, new_cells

    return dead_cells, new_cells

def apply_changes( grid, dead_cells, new_cells ):
    for cell in dead_cells:
        if cell[0] >= len( grid ) or cell[1] >= len( grid ):
            continue
        grid[cell[1]][cell[0]] = 0
    for cell in new_cells:
        if cell[0] >= len( grid ) or cell[1] >= len( grid ):
            continue
        grid[cell[1]][cell[0]] = 1

    return grid

def play_game( grid, size ):
    """
          ( x-1, y-1 )  ( x-1, y )  ( x-1, y+1 )
          ( x, y-1 )    ( x, y )    ( x, y+1 )
          ( x+1, y-1 )  ( x+1, y )  ( x+1, y+1 )
          
        1. Any live cell with fewer than two live neighbours dies,
                as if caused by under-population.
        2. Any live cell with two or three live neighbours
                lives on to the next generation.
        3. Any live cell with more than three live neighbours dies,
                as if by overcrowding.
        4. Any dead cell with exactly three live neighbours becomes a live cell,
                as if by reproduction.
    """
    new_cells = []
    dead_cells = []

    # check corners
    # top left
    living_neighbor_count = grid[1][0] + grid[1][1] + grid[0][1]
    dead_cells, new_cells = check_rules( 0, 0, grid[0][0],
            living_neighbor_count, dead_cells, new_cells )
    # top right
    living_neighbor_count = grid[size-2][0] + grid[size-2][1] + grid[size-1][1]
    dead_cells, new_cells = check_rules( 0, size-1, grid[size-1][0],
            living_neighbor_count, dead_cells, new_cells )
    # bottom left
    living_neighbor_count = grid[1][size-2] + grid[1][size-1] + grid[0][size-2]
    dead_cells, new_cells = check_rules( size-1, 0, grid[0][size-1],
            living_neighbor_count, dead_cells, new_cells )
    # bottom right
    living_neighbor_count = grid[size-2][size-2] + grid[size-2][size-1] + \
            grid[size-1][size-2]
    dead_cells, new_cells = check_rules( size-1, size-1, grid[size-1][size-1],
            living_neighbor_count, dead_cells, new_cells )

    # check left edge without checking corners
    for x in range( 1, size - 1 ):
        living_neighbor_count = grid[0][x-1] + grid[1][x-1] + \
                grid[1][x] + grid[0][x+1] + grid[1][x+1]
        dead_cells, new_cells = check_rules( x, 0, grid[0][x],
                living_neighbor_count, dead_cells, new_cells )

    # check right edge without checking corners
    for x in range( 1, size - 1 ):
        living_neighbor_count = grid[size-2][x-1] + grid[size-1][x-1] + \
                grid[size-2][x] + grid[size-2][x+1] + grid[size-1][x+1]
        dead_cells, new_cells = check_rules( x, size, grid[size-1][x],
                living_neighbor_count, dead_cells, new_cells )

    # check top edge without checking corners
    for y in range( 1, size - 1 ):
        living_neighbor_count = grid[y-1][0] + grid[y+1][0] + \
                grid[y-1][1] + grid[y][1] + grid[y+1][1]
        dead_cells, new_cells = check_rules( 0, y, grid[y][0],
                living_neighbor_count, dead_cells, new_cells )

    # check bottom edge without checking corners
    for y in range( 1, size - 1 ):
        living_neighbor_count = grid[y-1][size-2] + grid[y][size-2] + \
                grid[y+1][size-2] + grid[y-1][size-1] + grid[y+1][size-1]
        dead_cells, new_cells = check_rules( size-1, y, grid[y][size-1],
                living_neighbor_count, dead_cells, new_cells )
        
    for y in range( 1, size - 1 ):
        for x in range( 1, size - 1 ):
            living_neighbor_count = grid[y-1][x-1] + grid[y][x-1] + \
                    grid[y+1][x-1] + grid[y-1][x] + grid[y+1][x] + \
                    grid[y-1][x+1] + grid[y][x+1] + grid[y+1][x+1]
            dead_cells, new_cells = check_rules( x, y, grid[y][x],
                    living_neighbor_count, dead_cells, new_cells )
    
    return apply_changes( grid, dead_cells, new_cells )

if __name__ == "__main__":
    random.seed( None )
    size = 20
    speed = 0.1
    selection = sys.argv[1] if len( sys.argv ) > 1 else 'acorn'
    grid = init_grid( size )
    grid = set_starting_cells( grid,
            conway_patterns.pattern_factory( size ).get(
            selection, conway_patterns.make_acorn )( size ) )

    while True:
        for col in grid:
            print( ' '.join( [ conway_colors.ConwayColors.DEFAULT + str( ' ' )
                    if num == 0 else
                    random.choice( conway_colors.ConwayColors.colors ) + str( '#' )
                    for num in col ] ) )

        time.sleep( speed )
        grid = play_game( grid, size )
        os.system('cls' if os.name=='nt' else 'clear')

