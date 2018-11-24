# coding:utf-8
import unittest, logging, warnings, time
import mysql.connector

def get_a_connection(option_files='/Users/cjl/.my.cnf'):
    warnings.simplefilter("ignore", ResourceWarning)
    return mysql.connector.connect(option_files=option_files)

def _exec_rsp_cmd(cmd_, conn_):
    try:
        mycursor = conn_.cursor()
        mycursor.execute(cmd_)
        res_batch = []
        for x in mycursor:
            res_batch.append(x)
        mycursor.close()
        return res_batch
    except Exception as e:
        logging.exception(e)
        return []

def _exec_no_rsp_cmd(cmd_, conn_):
    try:
        mycursor = conn_.cursor()
        mycursor.execute(cmd_)
        mycursor.close()
        return True
    except Exception as e:
        logging.exception(e)
        return False

def show_dbs(conn_):
    res = []
    tup_batch = _exec_rsp_cmd('SHOW DATABASES', conn_)
    for tup in tup_batch:
        res.extend(tup)
    return res

def create_db(name_, conn_):
    return _exec_no_rsp_cmd('CREATE DATABASE %s' % name_, conn_)

def create_db_if_not_exist_and_select_it(name_, conn_):
    if name_ not in show_dbs(conn_):
        create_db(name_, conn_)
    _exec_no_rsp_cmd('USE %s' % name_, conn_)

def drop_db(name_, conn_):
    return _exec_no_rsp_cmd('DROP DATABASE %s' % name_, conn_)

def create_table_if_not_exists(name_, fields_, conn_):
    if name_ not in show_tables(conn_):
        create_table(name_, fields_, conn_)

def create_table(name_, fields_, conn_):
    return _exec_no_rsp_cmd('CREATE TABLE IF NOT EXISTS %s %s' % (name_, fields_), conn_)

def drop_table(name_, conn_):
    return _exec_no_rsp_cmd('DROP TABLE %s' % (name_), conn_)

def drop_table_if_exists(name_, conn_):
    if name_ in show_tables(conn_):
        drop_table(name_, conn_)

def desc_table(name_, conn_):
    return _exec_rsp_cmd('DESC %s' % (name_), conn_)

def show_tables(conn_):
    res = []
    for table in _exec_rsp_cmd('SHOW TABLES', conn_):
        res.extend(table)
    return res

class Mysql_Handler(object):
    def __init__(self, option_files='/Users/cjl/.my.cnf', db_name='mission_planning_db', table_name='mission_planning_table'):
        self._db_name, self._table_name = db_name, table_name
        self._conn = get_a_connection(option_files=option_files)
        create_db_if_not_exist_and_select_it(self._db_name, self._conn)
        create_table_if_not_exists(self._table_name, '(name VARCHAR(100), val VARCHAR(20000), UNIQUE KEY unique_name(name))', self._conn)
    
    def erase(self, k):
        cmd = "DELETE FROM %s WHERE name='%s'" % (self._table_name, k)
        return _exec_no_rsp_cmd(cmd, self._conn)

    def push(self, k, v):
        self.erase(k)
        cmd = "INSERT INTO %s VALUES ('%s', '%s')" % (self._table_name, k, v)
        _exec_no_rsp_cmd(cmd, self._conn)
        self._conn.commit()

    def get(self, k):
        cmd = "SELECT val FROM %s WHERE name = '%s'" % (self._table_name, k)
        res = _exec_rsp_cmd(cmd, self._conn)
        if len(res) > 0:
            return res[0][0]
        else:
            return None

    def select_all(self):
        cmd = "SELECT * FROM %s" % (self._table_name)
        res = _exec_rsp_cmd(cmd, self._conn)
        return res

class _UnitTest(unittest.TestCase):
    def sktest_listdb(self):
        conn_ = get_a_connection()
        create_db_if_not_exist_and_select_it('mission_planning_db', conn_)
        drop_table_if_exists('mission_planning_table', conn_)
        create_table('mission_planning_table', '(name VARCHAR(100), val VARCHAR(20000))', conn_)
        print (show_tables(conn_))
        print (desc_table('mission_planning_table', conn_))

    def test_class(self):
        handler = Mysql_Handler()
        handler.push('testkey', 'testval')
        print (handler.select_all())
        handler2 = Mysql_Handler()
        print (handler2.select_all())
        handler2.push('testkey', 'testval')
        print (handler2.select_all())


if __name__ == '__main__':
    unittest.main()