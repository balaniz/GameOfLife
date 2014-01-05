import sys
import time
import random
import conway_patterns
import conway_colors
import wraparound_grid

def set_starting_cells( grid, cells ):
    for cell in cells:
        grid[cell[0]][cell[1]] = 1
    return grid

if __name__ == "__main__":
    random.seed( None )
    selection = sys.argv[1]
    width = int( sys.argv[2] )
    height = int( sys.argv[3] )

    grid = wraparound_grid.WraparoundGrid( width, height )
    grid = set_starting_cells( grid, conway_patterns.pattern_factory().get(
            selection, conway_patterns.make_acorn )( width, height ) )

    for col in grid._grid:
        print( ' '.join( [ conway_colors.ConwayColors.DEFAULT + str( ' ' )
                if num == 0 else
                random.choice( conway_colors.ConwayColors.colors ) \
                + str( '#' ) for num in col._list ] ) )
    time.sleep( 3 )
