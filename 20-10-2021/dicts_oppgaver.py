# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:33:38 2021

@author: evenjc
"""

# Teori - Hvordan en dict ser ut

my_dictionary = {
    'name': 'Kevin',
    'age': 29,
    'work': 'engineer',
    }

# 

for key in my_dictionary:
    print(key)
    print(my_dictionary[key])
    
# Oppgave - Endre printingen slik at det skrives ut litt mer meningsfult.
# Eks: name: Kevin osv

# Teori - Nøstede dictionaries

workers = {
    'Bob': {
        'salary':'3 bananas',
        'bonuses':'None',
        },
    'Sarah': {
        'salary': '5 bananas',
        'bonuses':'1 apple',
        }
    }

for key in workers:
    print(key)
    
# Oppgave - Skriv ut til monitor hvor mange bananer hver ansatt får i lønn




# Teori - Hvordan legge til nye elementer
workers['Thomas'] = {
    'salary': '4 bananas',
    'bonuses': '1 orange',
    }

for key in workers:
    print(key)


# For å slette en oppføring bruker man Pop
workers.pop("Thomas")
