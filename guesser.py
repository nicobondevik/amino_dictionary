# Finds amino acid based on 1-letter, 3-letter or name
import random

# groups
oneLetter = ['A', 'R', 'D', 'N', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S',
             'T', 'W', 'Y', ' V']
threeLetter = ['Ala', 'Arg', 'Asp', 'Asn', 'Cys', 'Glu', 'Gln', 'Gly', 'His', 'Ile', 'Leu',
               'Lys', 'Met', 'Phe', 'Pro', 'Ser', 'Thr', 'Trp', 'Tyr', 'Val']
name = ['Alanine', 'Arginine', 'Aspartic Acid', 'Asparagine', 'Cystine', 'Glutamic acid',
        'Glutamine', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methyonine',
        'Phenylalanine', 'Proline', 'Serine', 'Threonine', 'Tryptophan', 'Tyrosin', 'Valine']

# group in list
group = [oneLetter, threeLetter, name]
groupName = ['1-letter code', '3-letter code', 'name']

# picking group and the group element
while True:
    i = random.randint(0, 2)
    j = random.randint(0, 19)
    k = random.randint(0, 2)
    if i != k:
        break

answer = group[i][j]
hint = group[k][j]

print(hint)

while True:
    guess = input(f'Guess the {groupName[i]}: ')

    if guess.upper() == answer.upper():
        print('correct.')
        break

    else:
        print('wrong. try again.')