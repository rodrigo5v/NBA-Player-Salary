import psycopg2

file = open('PlayerWithSalarySeason-210902-184055.tsv','r')
x = next(file)
cols = x.split('\t')

try:
    con = psycopg2.connect(database = 'nba', user = 'postgres', password = '1234', 
                            host = 'localhost', port = '5432')
except:
    print('Failed')

cmd = con.cursor()

cmd.execute(f"""
    CREATE TABLE IF NOT EXISTS raw_data
    (    
        {cols[0]} integer,
        {cols[1]} integer,
        {cols[2]} smallint,
        {cols[3]} character varying(255),
        {cols[4]} character varying(255),
        {cols[5]} integer,
        {cols[6]} integer,
        {cols[7]} character varying(255),
        {cols[8]} integer,
        {cols[9]} character varying(255),
        {cols[10]} character varying(255),
        {cols[11]} character varying(255),
        {cols[12]} integer 
    )
""")
con.commit()

cmd.copy_from(file,'raw_data',sep='\t',null='')
con.commit()