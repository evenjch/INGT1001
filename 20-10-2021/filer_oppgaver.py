# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:14:14 2021

@author: evenjc
"""

# Teori - Les en hel fil inn i en variabel

with open("lorem_ipsum.txt") as file:
    text_from_file = file.read()
    
# Oppgave 1 - Del opp teksten slik at hvert paragraf blir et eget element i en liste
# text_from_file = ["Lorem...", "Vestibulem...", osv]



# Teori - Les linje for linje

with open("lorem_ipsum.txt") as file:
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)

# Oppgave 2 - Dette må da kunne gjøres lurere? Bruk boka deres og les de to
# første sidene på kapittel 7.1, og se om du finner noe som kan hjelpe der

