"""
Colour classes for representing animal colours.
------------------------------------------------
Colour: Basic colour with a name (e.g., 'Red', 'Blue', 'AliceBlue').
TransparentColour: Inherits Colour, adds transparency_level for semi-transparent colours.
Used by animal classes to assign and display colour information.
"""
class Colour(object):
    def __init__(self, name):
        self.name = name

class TransparentColour(Colour):
    def __init__(self, name, transparency_level):
        super().__init__(name)
        self.transparency_level = transparency_level