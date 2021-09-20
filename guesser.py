# Finds amino acid based on 1-letter, 3-letter or name
from random import randint
import csv

amino_list = []

with open('AAKT3.csv') as infile:
    reader = csv.reader(infile)
    next(reader, None)  # skip the headers
    for line in infile:
        line = line.strip()
        size = line.split(';')[-1]
        amino = line.split(';')[0:3]
        amino.append(size)
        amino_list.append(amino)

cat = ['name', 'three letter code', 'one letter code', 'size']

i = randint(0,20)
j = randint(0,2)
k = randint(0,3)

while j == k:
    j = randint(0,2)

answer = amino_list[i][k]
hint = amino_list[i][j]

guess = input(f'{hint}\nguess the {cat[k]}: ')
while guess.capitalize() != answer.capitalize():
    print('wrong. try again.')
    guess = input(f'{hint}\nguess the {cat[k]}: ')

print('correct')