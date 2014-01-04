
class WraparoundGrid:
    def __init__( self, width, height ):
        self._grid = [ WraparoundList( height ) for i in range( 0, width ) ]
        self._width = width
        self._height = height

    def __getitem__( self, k ):
        assert( type( k ) == int )
        index = k + self._width
        index = index % self._width
        
        return self._grid[index]

    def __len__( self ):
        return self._width

class WraparoundList:
    def __init__( self, length ):
        self._list = [ 0 for i in range( 0, length ) ]
        self._length = length

    def __getitem__( self, k ):
        #assert( type( k ) == int )
        index = k + self._length
        index = index % self._length
        
        return self._list[index]

    def __setitem__( self, k, value ):
        #assert( type( k ) == int )
        index = k + self._length
        index = index % self._length
        
        self._list[index] = value

    def __len__( self ):
        return self._length
