# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:53:12 2021

@author: evenjc
"""

# Teori - Hvordan lese en json fil inn i en dictionary

import json

with open("data.json") as file:
    data = json.load(file)
    
    
# Oppgave - Print ut alle keys, etterfulgt av deres value


# Oppgave - Her leser vi inn en json-fil fra NASA i en variabel. 
with open("near_earth_bodies.json") as file:
    data = json.load(file)
    
    for key in data:
        print(data)
        
# Finn ID-en til alle nære objekter den 2015-09-08 og print de ut.
# Her er det kjekt å bruke variabelutforskeren