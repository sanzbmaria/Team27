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
        id_query = 'SELECT id, password FROM query WHERE id = %s'
        id_query_res = self.execute(id_query, (id,))

        if id_query_res[0][1] == pwd:
            return True
            
        return False


    def register(self, id, pwd, name, major, submajor1, submajor2):
        pass


if __name__=="__main__":
    db = Database()
    db.execute("SELECT * FROM users")