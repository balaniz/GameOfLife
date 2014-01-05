#! /user/bin/python3

def pattern_factory():
    return { "blinkers" : make_two_blinkers,
             "blinker" : make_blinker,
             "toad" : make_toad,
             "glider_gun" : make_glider_gun,
             "acorn" : make_acorn,
             "queen_bee_loop" : make_queen_bee_loop,
             "queen_bee_shuttle" : make_queen_bee_shuttle }

def make_queen_bee_shuttle( width, height ):
    pass

def make_queen_bee_loop( width, height ):
    if width < 24 or height < 24:
        return make_blinker( width, height )

    return [ ( 2, 13 ), ( 3, 11 ), ( 3, 13 ), ( 4, 10 ), ( 4, 12 ),
             ( 5, 9 ), ( 5, 12 ), ( 6, 10 ), ( 6, 12 ), ( 7, 11 ),
             ( 7, 13 ), ( 8, 13 ), ( 9, 18 ), ( 10, 17 ), ( 10, 19 ),
             ( 11, 16 ), ( 11, 20 ), ( 12, 17 ), ( 12, 18 ), ( 12, 19 ),
             ( 13, 15 ), ( 13, 16 ), ( 13, 20 ), ( 13, 21 ), ( 14, 2 ),
             ( 14, 3 ), ( 14, 7 ), ( 14, 8 ), ( 15, 4 ), ( 15, 5 ),
             ( 15, 6 ), ( 16, 3 ), ( 16, 7 ), ( 17, 4 ), ( 17, 6 ),
             ( 18, 5 ), ( 19, 14 ), ( 20, 14 ), ( 20, 16 ), ( 21, 15 ),
             ( 21, 17 ), ( 22, 15 ), ( 22, 18 ), ( 23, 15 ), ( 23, 17 ),
             ( 24, 14 ), ( 24, 16 ), ( 25, 14 ) ]

def make_blinker( width, height ):
    return [ (3,3),(3,4),(3,5) ]

def make_two_blinkers( width, height ):
    start_x = int( width / 4 )
    start_y = int( height / 5 )
    vertical_blinker = [ ( start_x, start_y ), ( start_x, start_y + 1 ),
            ( start_x, start_y + 2 ) ]

    start_x = int( width / 2 )
    start_y = int( height / 3 )
    horizontal_blinker = [ ( start_x, start_y ), ( start_x + 1, start_y ),
            ( start_x + 2, start_y ) ]
    return horizontal_blinker + vertical_blinker

def make_toad( width, height ):
    return [ ( 3, 4 ), ( 3, 5 ), ( 3, 6 ), ( 4, 3 ), ( 4, 4 ), ( 4, 5 ) ]

def make_glider_gun( width, height ):
    pass

def make_acorn( width, height ):
    return [ ( 10, 5 ), ( 8, 6 ), ( 10, 6 ), ( 9, 8 ),
            ( 10, 9 ), ( 10, 10 ), ( 10, 11 ) ]
