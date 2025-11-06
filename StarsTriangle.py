stars_rows = int(input('Enter no. of starts rows:'))
star = '*'

for i in range(0, stars_rows):
    count_per_row = i + 1
    print(star * count_per_row)