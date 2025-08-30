from colour import Colour
"""
Animal Class Hierarchy
---------------------
Animal (grand parent class)
	- Vertebrates (parent class)
		- Fish
		- Amphibia
		- Reptiles
		- Birds
		- Mammals
	- Invertebrates (parent class)
		- Arthropoda
		- Insecta
		- Crustacea
		- Archnida
		- Diplopoda
		- Mollusca

Each class accepts a 'colour' variable to represent the animal's colour.
"""

class Animal:
		def __init__(self, name, colour=None):
				self.name = name
				from colour import Colour
				if isinstance(colour, Colour):
					self.colour = colour
				elif isinstance(colour, str):
					self.colour = Colour(colour)
				else:
					self.colour = Colour("Unknown")

class Vertebrates(Animal):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Fish(Vertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Amphibia(Vertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Reptiles(Vertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Birds(Vertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Mammals(Vertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Invertebrates(Animal):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Arthropoda(Invertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Insecta(Invertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Crustacea(Invertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Archnida(Invertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Diplopoda(Invertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)

class Mollusca(Invertebrates):
	def __init__(self, name, colour=None):
		super().__init__(name, colour)