# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:07:37 2021

@author: evenjc
"""

import csv

# Teoribit - Hvordan kan vi lese en CSV-fil?

with open("personer.csv") as file:
    data = csv.reader(file, delimiter=";")
    
    print(data)
    
    for row in data:
        print(row)
        print(type(row))
        
        
# Oppgave - Skriv ut infoen til alle som forskjellige setninger. Det skal se slik ut
# trond er 13 og liker eple
# per er 35 og liker banan


# Teori - Man kan også skrive inn flere linjer i en eksisterende fil
with open("personer.csv", "a", newline='\n') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(['even', 34, 'vannmelon'])
    
# Oppgave - Lag en ny csv-fil og fyll den med arbitrær data (du velger)
# Utvikle over og under with open. Bytt ut din kode med pass.

pass

with open("min_fil.csv", "w"):
    pass