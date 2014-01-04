#! /user/bin/python3

def pattern_factory( size ):
    return { "blinkers" : make_two_blinkers,
             "toad" : make_toad,
             "glider_gun" : make_glider_gun,
             "acorn" : make_acorn }

def make_two_blinkers( size ):
    return [ ( 3, 3 ), ( 3, 4 ), ( 3, 5 ), ( 6, 4 ), ( 7, 4 ), ( 8, 4 ) ]

def make_toad( size ):
    return [ ( 3, 4 ), ( 3, 5 ), ( 3, 6 ), ( 4, 3 ), ( 4, 4 ), ( 4, 5 ) ]

def make_glider_gun( size ):
    pass

def make_acorn( size ):
    return [ ( 10, 5 ), ( 8, 6 ), ( 10, 6 ), ( 9, 8 ),
            ( 10, 9 ), ( 10, 10 ), ( 10, 11 ) ]
