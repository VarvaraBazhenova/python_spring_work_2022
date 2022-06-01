#todo: Реализовать классы DB и Profile

import psycopg2


class DB:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

    def get_connect(self):

        connect = psycopg2.connect(host="localhost", port=5432, dbname=self.name, user=self.user, password=self.password)
        return connect

    def get_profile(self, conn, login):
        cur = conn.cursor()
        cur.execute(f"""SELECT * from "Group" where login = '{login}';""")
        obj = cur.fetchall()
        return obj

class Profile:
    def __init__(self, id_group, name, surname, age, group_name, login, password):
        self.id_group = id_group
        self.name = name
        self.surname = surname
        self.age = age
        self.group_name = group_name
        self.login = login
        self.password = password

    def set_profile(self, conn):
        cur = conn.cursor()
        cur.execute(f'''INSERT INTO "Group"("id_user", "login", "password", "name", "surname", "age", "group_name") 
        VALUES ({self.id_group}, '{self.login}', '{self.password}', '{self.name}', '{self.surname}', 
        {self.age}, '{self.group_name}')''')
        conn.commit()


connection = DB("testsystem", "testsystem", "123").get_connect()
conn = DB("testsystem", "testsystem", "123").get_connect()

new_student = Profile(1, 'Ivan', 'Ivanov', 20, 'A', 'Ivivan', '12345').set_profile(conn)
