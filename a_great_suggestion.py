#!/usr/bin/python

import random
from heapq import nsmallest

# Create our dataset - Part 1: Homo Sapiens #
hs0 = ['mahanth', 'rohan', 'dan', 'ven', 'arun', 'eric', 'alan', 'brock', 'yuvamathi', 'john', 'lisa', 'lakshman', 'hariprasath', 'abe', 'kate']
hs1 = ['david', 'chris', 'jake', 'john', 'george', 'bala', 'lakshmi', 'louis', 'payam', 'tina', 'alexis', 'mary', 'adam', 'mark', 'john', 'vinjith']
hs2 = []
hs = hs0 + hs1 + hs2

# Create our dataset - Part 2:
babyformula  = 'babyformula'
diaper       = 'diaper'
battery      = 'battery'
rccar        = 'rccar'

# Initialize our Dictionary #
hsd = {}
for people in hs:
    hsd[people] = random.choice([babyformula, diaper, battery, rccar])

#def binary(num, length=4):
    #return format(num, '0{}b'.format(length))

### Create our dataset - Part 3: Add 'binary' features to items ##
baby           = 8  #binary(8)  #1000
newmom         = 4  #binary(4)  #0100
fun            = 2  #binary(2)  #0010
toys           = 1  #binary(1)  #0001
## Manually Add Features for Product Categories #
babyformula    = 12 #binary(12) #1100
diaper         = 12 #binary(12) #1100
battery        = 3  #binary(3)  #0011
rccar          = 3  #binary(3)  #0011

# Initialize our features with our products #
items      = {'babyformula': babyformula, 'diaper': diaper, 'battery': battery, 'rccar': rccar }
categories = {'baby': baby, 'newmom': newmom, 'fun': fun, 'toys': toys}

def a_great_suggestion():
    for k0, v0 in hsd.items():
        print '%s purchased: %s' % (k0.title(), v0.title())
        purchase = [v0]
        for k1, v1 in items.items():
            itemlist = []
            if v0 in (k1, v1):
                itemlist.append(v1)
            nummatch = []
            for number in itemlist:
                thing = nsmallest(1, categories.values(), key=lambda x: abs(x-number))
                nummatch.append(thing[0])
            matchitem = []
            for number in nummatch:
                thing = nsmallest(1, items.values(), key=lambda x: abs(x-number))
                matchitem.append(thing[0])
            for number in matchitem:
                for k2, v2 in items.items():
                    if number in (k2, v2):
                        purchase.append(k2)
        while v0 in purchase: purchase.remove(v0)
        greatrec = ' '.join(purchase)
        print 'We recommend a: %s' % greatrec.title()
        print

if __name__ == '__main__':
    a_great_suggestion()
