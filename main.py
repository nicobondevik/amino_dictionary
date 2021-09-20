import csv

q = input('query (enter when done): ')
while q != '':
    with open('AAKT3.csv') as infile:
        for line in infile:
            line = line.strip()
            data = line.split(';')
            if q.capitalize() in data:
                for i in range(len(data)):
                    print(data[i], ' ' * (15-len(data[i])), end='')
                print()
    q = input('query (enter when done): ').capitalize()
print('bye')