'''
2. Feladat
Írj egy programot, amely a felhasználótól bekér egy RGB színkód három összetvőjét! 
A program állapítsa meg és írja ki a képernyőre, hogy az adott szín tartalmaz-e zöld komponenst, illetve melyik komponensből van a legtöbb, és melyikből a legkevesebb!
'''

r = int(input('piros: '))
if r > 255:
    r = 255
g = int(input('zold: '))
if g > 255:
    g = 255
b = int(input('kek: '))
if b > 255:
    b = 255
rgb = r,g,b

if rgb[1] > 0:
    print('az adott rgb szín tartalmaz zold komponenst')
else:
    print('az adott rgb szín nem taartalmaz zold komponenst')

r,g,b = rgb
if r > g and r > b:
    print('pirosból van a legtobb')
elif g > r and g > b:
    print('zoldbol van a legtobb')
else:
    print('kekbol van a legtobb')