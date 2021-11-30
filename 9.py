import ephem
from datetime import date

text = input('Введите название планеты')    

list_planet = ([ephem._libastro.builtin_planets()])

def find_planet(text):
    global list_planet
    if text in list_planet:
        print(text)
        a = getattr(list_planet, text)
        print(a)