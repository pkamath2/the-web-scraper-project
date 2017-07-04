from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_lotr_characters(characters_soup, lotr_file):
    all_divs_for_charList = characters_soup.findAll("div", class_="listchar")
    lotr_file.write("Character")
    lotr_file.write(",")
    lotr_file.write("Race")
    lotr_file.write("\n")
    for character in all_divs_for_charList:
        character_name = character.text
        character_type = ''
        if "hobbit" in character["class"]:
            character_type = "hobbit"
        if "man" in character["class"]:
            character_type = "man"
        if "elf" in character["class"]:
            character_type = "elf"
        if "istari" in character["class"]:
            character_type = "Istari"
        if "dwarf" in character["class"]:
            character_type = "dwarf"
        if len(character_name) > 0:
            lotr_file.write(character_name.strip().replace('"',"'"))
            lotr_file.write(",")
            lotr_file.write(character_type)
            lotr_file.write("\n")


lotr_file = open('lotr_characters.csv','w')
html = urlopen('http://lotrproject.com/char/List')
html_soup = BeautifulSoup(html, 'html.parser')
get_lotr_characters(html_soup,lotr_file)
lotr_file.close()