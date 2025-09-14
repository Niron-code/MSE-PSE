"""
Animal Colour Demo
------------------
This script assigns random CSS color names to various animal classes.
It uses the Colour and TransparentColour classes to represent color information.
If the CSS Colors API is unavailable, it falls back to a static color list.
Each animal is printed with its name, color, and transparency (if applicable).
"""

import random
from colour import Colour, TransparentColour
from animal import *
import requests

class AnimalColour:
    def fetch_css_color_names(self):
        url = "https://www.csscolorsapi.com/api/colors"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return [color['name'] for color in data['colors']]
        except Exception as e:
            print("Error fetching colors:", e)
        return ["Red", "Blue", "Green", "Yellow", "Black", "White"]  # fallback

    def random_colour(self):
        css_colors = self.fetch_css_color_names()
        chosen = random.choice(css_colors)
        if random.choice([True, False]):
            return Colour(chosen)
        else:
            return TransparentColour(chosen, transparency_level=random.randint(1, 10))

if __name__ == "__main__":
    animalColour = AnimalColour()
    animals = [
        Fish("Goldfish", animalColour.random_colour()),
        Amphibia("Frog", animalColour.random_colour()),
        Reptiles("Snake", animalColour.random_colour()),
        Birds("Parrot", animalColour.random_colour()),
        Mammals("Cat", animalColour.random_colour()),
        Arthropoda("Spider", animalColour.random_colour()),
        Insecta("Bee", animalColour.random_colour()),
        Crustacea("Crab", animalColour.random_colour()),
        Archnida("Scorpion", animalColour.random_colour()),
        Diplopoda("Millipede", animalColour.random_colour()),
        Mollusca("Snail", animalColour.random_colour())
    ]
    for animal in animals:
        print(f"{animal.name}: Colour={animal.colour.name}, Type={type(animal.colour).__name__}", end="")
        if isinstance(animal.colour, TransparentColour):
            print(f", Transparency={animal.colour.transparency_level}")
        else:
            print()
        print()