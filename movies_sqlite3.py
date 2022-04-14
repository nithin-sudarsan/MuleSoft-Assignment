import sqlite3

with sqlite3.connect("movies_database.db") as db:
    cursor=db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies(
Movie_name TEXT NOT NULL,
Lead_actor TEXT NOT NULL,
Lead_actress TEXT NOT NULL,
Director_name TEXT NOT NULL,
Year_of_release INTEGER NOT NULL);
''')

insert_movies='''INSERT INTO Movies (Movie_name, Lead_actor, Lead_actress, Director_name, Year_of_release) VALUES 
("Inception", "Leonardo DiCaprio", "Elliot Page", "Christopher Nolan", 2010),
("Jurrasic World", "Chris Pratt", "Bryce Dallas", "J.A Bayona", 2018),
("The Nice Guys", "Ryan Gosling", "Margaret Qualley", "Shane Black", 2016),
("Aladdin", "Will Smith", "Naomi Scott", "Guy Ritchie", 2019),
("Spiderman - No way Home", "Tom Holland", "Zendaya", "Jon Watts", 2021),
("The Mask", "Jim Carrey", "Amy Yasbeck", "Chuck Russell", 1994)'''
cursor.execute(insert_movies)
db.commit()

def get_movies():
    query_1='''SELECT * FROM Movies'''
    cursor.execute(query_1)
    rows=cursor.fetchall()
    for row in rows:
        print(row)


get_movies()


def get_movie(actor_name):
    query_2='''SELECT Movie_name FROM Movies WHERE Lead_actor=(?) '''
    cursor.execute(query_2, [(actor_name)]) 
    movie_name=cursor.fetchall()
    for  name in movie_name:
        print("The lead actor of ",name[0], "is", actor_name)

get_movie('Will Smith')