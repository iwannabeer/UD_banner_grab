#!/usr/bin/python
import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('select * from SCAN_RESULTS')
results = c.fetchall()

for scan in results: print scan

conn.close()