#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import psycopg2
from config import DB
from .parser import get_object, main_crawling

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
    

    def get_articles(self, id):
        article_query = "SELECT idx, title, major, date FROM articles WHERE major = main OR major = (SELECT major FROM users WHERE id = %s) ORDER BY idx DESC"
        article_query_result = self.execute(article_query, (id,))
        return article_query_result
    

    def set_favorites(self, id, article_idx):
        favor_chk_query = "SELECT COUNT(*) FROM favorites WHERE user_id = %s AND article_idx=%s"
        favor_chk_result = self.execute(favor_chk_query, (id, article_idx,))[0][0]

        # if already added to list -> delte
        if favor_chk_result:
            favor_del_query = "DELETE FROM favorites WHERE user_id = %s AND article_idx=%s"
            self.execute(favor_del_query, (id, article_idx,))
            return False
        
        # if none -> add
        favor_query = "INSERT INTO favorites(user_id, article_idx) VALUES(%s, %s)"
        self.execute(favor_query, (id, article_idx,))
        return True
    

    def get_favorties(self, id):
        favor_query = "SELECT f.article_idx, a.title, a.major, a.date FROM favorites AS f LEFT JOIN articles AS a ON f.article_idx = a.idx WHERE f.user_id = %s"
        favors_query_result = self.execute(favor_query, (id,))
        return favors_query_result
    

    def upload_crawling(self, articles):
        pass


if __name__=="__main__":
    db = Database()
    # print(db.register("admin", "admin", "admin", "cs"))
