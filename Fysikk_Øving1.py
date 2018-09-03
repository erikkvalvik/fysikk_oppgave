# -*- coding: utf-8 -*-
"""
Fysikkøving1: Pythonprogrameringog bevegelsesfysikk.
For en tid tilbake var jeg på sandstranda i Alcudia og nøt latmannslivet i fulle drag. 
Stranda var rett og lang og det var plassert ut små Pizza-steder med jevne mellomrom til å innta lunsj.  
Parallelt med stranda gikk det en strandpromenade og hver dag rundt lunsjtider vurderte jeg hva som lønte seg. 
Skulle jeg gå direkte på den tunge stranda eller lønte det seg å gå opp til promenaden og deretterned igjen til Pizzaen?
Itilfelle det siste, hvilken vinkel skulle jeg velge fra solstolen til promenaden? 

Noen fakta: Min fart i sand 0.8m/s, promenadefart 3.0m/s, 
avstanden mellom min solstol og Pizza var 200m og både jeg og Pizza lå 15 meter frapromenaden. 
"""
import math

sandfart = 0.8
promenadefart = 3.0
strandtilpizza = 200
frapromenaden = 15
vinkel = "?"
ssand = list(range(1,200))


tider = []


for i in ssand:
    hypotenus = math.sqrt(15**2 + i**2)
    tidsand = hypotenus / 0.8
    spromenade = 200 - 2*i
    tidprom = spromenade / 3.0
    tidtotal = tidprom + tidsand * 2
    tider.append(tidtotal)
    mintid = min(tider)
    if tidtotal == mintid:
        print(i, "meter katet",  tidtotal, "sekunder", hypotenus, "hypotenus", hypotenus * 2, "meter i sanden", spromenade, "meter på promenade\n")
print("minste tid brukt er", min(tider))


#minkat =
#print(minkat)
#minhyp = (min(tider) - tidprom / 2)  
#minms = 
#minmp = 

















