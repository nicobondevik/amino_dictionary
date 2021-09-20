# Finds amino acid based on 1-letter, 3-letter or name




amino_acids = pd.read_csv('AAKT2.csv', sep=';')

letter = input('Enter: ')
letter = letter.capitalize()

while letter != '':
    for index, row in amino_acids.iterrows():
        if row['aminoacid'] == letter or row['1-letter'] == letter or row['3-letter'] == letter:
            print(row)
    letter = (input('Enter: '))
    letter = letter.capitalize()