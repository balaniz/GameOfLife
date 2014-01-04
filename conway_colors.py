#! /user/bin/python3

class ConwayColors:
    def __init__( self ):
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.YELLOW = '\033[33m'
        self.BLUE = '\033[34m'
        self.MAGENTA = '\033[35m'
        self.CYAN = '\033[36m'
        self.LT_RED = '\033[91m'
        self.LT_GREEN = '\033[92m'
        self.LT_YELLOW = '\033[93m'
        self.LT_BLUE = '\033[94m'
        self.LT_MAGENTA = '\033[95m'
        self.LT_CYAN = '\033[96m'
        self.DEFAULT = '\033[0m'
        self.colors = [ self.RED, self.GREEN, self.YELLOW, self.BLUE,
                        self.MAGENTA, self.CYAN, self.LT_RED, self.LT_GREEN,
                        self.LT_YELLOW, self.LT_BLUE, self.LT_MAGENTA,
                        self.LT_CYAN, self.DEFAULT ]

