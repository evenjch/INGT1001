# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:31:16 2021

@author: evenjc

Et utgangspunkt for Hangman

"""
import random
 
possible_words = [
        "banana",
        "apple",
        ]
 
# Grab a word at random
word = random.choice(possible_words)