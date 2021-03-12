'''Import dependencies''' 
import csv
import itertools


consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'm', 'n', 'p', 'r', 's', 't', 'y']
vovels = ['a', 'e', 'i', 'o', 'u']



con2 = list(itertools.permutations(consonents, 2))
vov3 = list(itertools.permutations(vovels, 2))

# con3 = list(itertools.permutations(consonents, 3))
# vov2 = list(itertools.permutations(vovels, 2))

word23 = []
for i in con2:
    for j in vov3:
        combV = j[0] + i[0] + j[1] + i[1] + '.com'
        combC = i[0] + j[0] + i[1] + j[1] + '.com'
        word23.append(combV)
        word23.append(combC)
print(word23)

with open('word23.csv', 'w', encoding='UTF-8', newline='') as f:
    f1 = csv.writer(f)
    for k in word23:
        f1.writerow([str(k),4])