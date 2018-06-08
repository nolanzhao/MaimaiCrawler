# -*- coding: UTF-8 -*-

import MySQLdb

DB_PARAM = {
    'host': 'IP地址',
    'user': '用户名',
    'password': '密码',
    'database': '数据库名',
}

db = MySQLdb.connect(DB_PARAM['host'], DB_PARAM['user'], DB_PARAM['password'], DB_PARAM['database'])
cursor = db.cursor()


def create_table():
    cursor.execute("DROP TABLE IF EXISTS gossip")
    sql = """CREATE TABLE gossip (
                id    int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                m_id  int(11) NOT NULL,
                text  longtext DEFAULT NULL,
                created_at  datetime(6) DEFAULT NULL)
        """

    cursor.execute(sql)
    db.close()


def save_db(g):
    cursor.execute('select * from gossip where m_id = %d' % g['id'])
    results = cursor.fetchall()
    if len(results) != 0:
        return 'EXIST'

    sql = "INSERT INTO GOSSIP(m_id, text) VALUES ('%d', '%s')" % \
          (g['id'], g['text'])
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(str(e))
        db.rollback()

    return True


if __name__ == '__main__':
    create_table()
