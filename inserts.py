import psycopg2

try:
    con = psycopg2.connect(database = 'nba', user = 'postgres', password = '1234', 
                            host = 'localhost', port = '5432')
except:
    print('Failed')

cmd = con.cursor()

cmd.execute("""
    CREATE TABLE IF NOT EXISTS teams
    (
        id integer,
        city character varying(255),
        state character varying(255),
        PRIMARY KEY (id)
    );

    CREATE TABLE IF NOT EXISTS players
    (    
        id integer,
        active smallint,
        name character varying(255),
        country character varying(255),
        height integer,
        weight integer,
        position character varying(255),
        team_id integer,
        PRIMARY KEY (id),
        FOREIGN KEY (team_id) REFERENCES teams (id)
    );

    CREATE TABLE IF NOT EXISTS salary
    (
        season character varying(255),
        amount money,
        id_player integer,
        FOREIGN KEY (id_player) REFERENCES players (id)
    )
""")
con.commit()

cmd.execute("""
    INSERT INTO teams(id, city, state)
        SELECT DISTINCT team_id, team_city, team_state FROM raw_data;
""")

con.commit()

cmd.execute("""
    INSERT INTO players(id, active, name, country, height, weight, position, team_id)
        SELECT DISTINCT id, active,name, country, height, weight, position, team_id
            FROM raw_data;
""")

con.commit()


cmd.execute("""
    INSERT INTO salary(season,amount,id_player)
        SELECT player_salary_season, player_salary_amount, id
            FROM raw_data
            WHERE player_salary_season IS NOT NULL
            AND player_salary_amount IS NOT NULL;
""")

con.commit()