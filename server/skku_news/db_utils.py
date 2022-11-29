#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import psycopg2
from config import DB

class Database:
    def __init__(self):
        self.db = psycopg2.connect(host=DB['host'],
                                dbname=DB['dbname'],
                                user=DB['user'],
                                password = DB['password'],
                                port=DB['port'])
        self.cursor = self.db.cursor()


    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

        if query.startswith('S') or query.startswith('s'):
            row = self.cursor.fetchall()
            return row

        else:
            self.db.commit()
    
    def login(self, id, pwd):
        id_query = 'SELECT u.id, u.password, u.name, b.major FROM users AS u LEFT JOIN notice_boards as b ON u.major = b.code WHERE u.id = %s'
        id_query_result = self.execute(id_query, (id,))

        if len(id_query_result) == 0:
            return False

        usr_id, usr_pwd, usr_name, usr_major = id_query_result[0]
        if usr_pwd == pwd:
            return usr_id, usr_name, usr_major
            
        return False


    def register(self, id, pwd, name, major):
        id_chk_query = "SELECT COUNT(*) FROM users WHERE id = %s"
        id_chk_query_result = self.execute(id_chk_query, (id,))[0][0]

        if id_chk_query_result:
            return False
        
        reg_query = "INSERT INTO users(id, password, name, major) VALUES (%s, %s, %s, %s)"
        self.execute(reg_query, (id, pwd, name, major))

        return True


if __name__=="__main__":
    db = Database()
    # print(db.register("admin", "admin", "admin", "cs"))
