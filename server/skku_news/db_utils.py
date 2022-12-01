#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import psycopg2
from config import DB
from parser import get_object, main_crawling

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
        article_query = "SELECT a.idx, a.title, n.major, a.date, n.link, a.link FROM articles AS a LEFT JOIN notice_boards AS n ON a.major = n.code WHERE a.major = 'SKKU' OR a.major = (SELECT major FROM users WHERE id = %s) ORDER BY date DESC"
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
    

    def get_favorites(self, id):
        favor_query = "SELECT f.article_idx, a.title, n.major, a.date, n.link, a.link FROM favorites AS f LEFT JOIN articles AS a ON f.article_idx = a.idx LEFT JOIN notice_boards as n ON a.major = n.code WHERE f.user_id = %s"
        favors_query_result = self.execute(favor_query, (id,))
        return favors_query_result
    

    def upload_crawling(self, major, articles):
        articles_query = 'SELECT major, num FROM articles'
        article_list = set(self.execute(articles_query))

        articles_insert_query = "INSERT INTO articles (major, num, title, date, link) VALUES "

        for i in range(len(articles)):
            if (major, articles[i]['num']) in article_list:
                continue

            articles_insert_query += f"('{major}', '{articles[i]['num']}', '{articles[i]['title']}', '{articles[i]['date']}', '{articles[i]['link']}')"
            
            if i != len(articles) - 1:
                articles_insert_query += ", "
        # print(articles_insert_query)
        self.execute(articles_insert_query)
        
        return True
    

    def get_boards(self):
        board_query = 'SELECT code, link FROM notice_boards'

        boards = self.execute(board_query)
        
        for board in boards:
            major, link = board
            print(major, link)
            page = get_object(link)
            crawled_articles = main_crawling(page)

            self.upload_crawling(major, crawled_articles)
        




if __name__=="__main__":
    db = Database()
    db.get_boards()
