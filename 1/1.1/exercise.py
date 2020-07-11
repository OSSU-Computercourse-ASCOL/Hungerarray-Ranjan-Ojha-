#--------------------------------------------------------------------
# Exercise: First Class
#--------------------------------------------------------------------

class Coordinate(object):
    # method to initialize the class
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # self defined method
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** .5
    
    # method to add objects of class
    def __add__ (self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    