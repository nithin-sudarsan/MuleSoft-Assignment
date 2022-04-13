import sqlite3

with sqlite3.connect("movies_database.db") as db:
    cursor=db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies(
Movie_name TEXT NOT NULL,
Lead_actor TEXT NOT NULL,
Lead_actress TEXT NOT NULL,
Director_name TEXT NOT NULL,
Year_of_release INTEGER NOT NULL,
);
''')

insert_movie_1='''INSERT INTO movies(question) VALUES(?)'''
cursor.execute(insert_question, [(quest)])
db.commit()
insert_movie_2='''INSERT INTO movies(question) VALUES(?)'''
cursor.execute(insert_question, [(quest)])
db.commit()
insert_movie_3='''INSERT INTO movies(question) VALUES(?)'''
cursor.execute(insert_question, [(quest)])
db.commit()
insert_movie_4='''INSERT INTO movies(question) VALUES(?)'''
cursor.execute(insert_question, [(quest)])
db.commit()
insert_movie_5='''INSERT INTO movies(question) VALUES(?)'''
cursor.execute(insert_question, [(quest)])
db.commit()
insert_movie_6='''INSERT INTO movies(question) VALUES(?)'''
cursor.execute(insert_question, [(quest)])
db.commit()

#or use single insert statement for everything

query='''SELECT Movie_name FROM movies WHERE Lead_actor='actor name' '''
cursor.execute(query) 
quest=cursor.fetchall()
db.commit()

cursor.execute("SELECT * FROM movies")