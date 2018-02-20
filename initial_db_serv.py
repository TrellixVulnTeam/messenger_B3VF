import sqlite3
import random
from models_repository_serv import Repository, Users, UserContacts
from sqlalchemy.exc import IntegrityError

conn = sqlite3.connect("server_db.db")
cursor = conn.cursor()

cursor.execute("drop table if exists users")
cursor.execute("drop table if exists history_users")
cursor.execute("drop table if exists user_contacts")
cursor.execute("create table users (id integer primary key autoincrement, username text UNIQUE, socket, "
               "flag integer NOT NULL )")
cursor.execute("create table history_users (id integer primary key autoincrement, time text, "
               "id_user integer REFERENCES users (id))")
cursor.execute("create table user_contacts (id integer primary key autoincrement, "
               "id_user integer references users (id)  , id_contact integer REFERENCES users (id), UNIQUE (id_user, id_contact))")

conn.commit()

rep = Repository()
for i in range(50):
    rep.add(Users('pilik{}'.format(i)))

for i in range(random.randint(5, 100)):
    try:
        rep.add(UserContacts(random.randint(0,50),random.randint(0,50)))
    except IntegrityError as err:
        pass
