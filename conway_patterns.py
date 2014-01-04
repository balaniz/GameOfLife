#! /user/bin/python3

def pattern_factory():
    return { "blinkers" : make_two_blinkers,
             "blinker" : make_blinker,
             "toad" : make_toad,
             "glider_gun" : make_glider_gun,
             "acorn" : make_acorn }

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
