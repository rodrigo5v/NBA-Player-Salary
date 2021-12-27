import psycopg2

file = 'PlayerWithSalarySeason-210902-184055.tsv'

lines = (row for row in open(file))
raw_csv = (line.rstrip().split('\t') for line in lines)

cols = next(raw_csv)

#raw_dict = list(dict(map(lambda key,value: (key,value), cols, data)) for data in raw_csv)