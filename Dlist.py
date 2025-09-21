import os

Dlist = [1, 23, 134, 4, 65, 32, 4, 65, 32, 1, 23, 134]

#for i in range(0, len(Dlist)):
i = 0
j = 0

while i < len(Dlist):
    _TempVar = Dlist[i]
    i += 1
    while j < len(Dlist):
        j += 1
        if(_TempVar == Dlist[j-1] and i == j):
            continue
        elif(_TempVar == Dlist[j-1] and i != j):
            del Dlist[j-1]
    j = 0

print(Dlist)
