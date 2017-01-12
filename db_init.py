#!/usr/bin/python
import sqlite3

try:
    print 'TEST.DB created.'
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    print 'Table SCAN_RESULTS created.'
    c.execute('create table SCAN_RESULTS (ip text, server text, port int, time text)')

    conn.commit()
    conn.close()
except:
    print 'db and table already exist.'