#!/usr/bin/python  
""" Script has CLI arg - filename of targets list. """

import socket  
import sys
import sqlite3
import time

def grab_banner(ip_address,port=80):  
    try:  
        s = socket.socket()  
        socket.setdefaulttimeout(1)

        s.connect((ip_address,port))
        s.send('KEK^)\r\n\r\n')  
        banner = s.recv(1024)
        s.close()

        print ip_address + ':' + banner

        start = banner.find('Server: ')
        fin = start + banner[start:].find('\r\n')
        server = banner[start:fin]
        if not server: server = 'open'

        return ip_address, server, port, time.ctime()
    except:  
        return  


def get_params():
    ''' Handle script arg - filename with targets addresses'''
    tgtsList_filename = sys.argv[1]
    return open(tgtsList_filename).read().split()


conn = sqlite3.connect('test.db')
c = conn.cursor()

targets = get_params()

for target_ip in targets:
    print "Started scan of IP: %s"% (target_ip,)
    result = grab_banner(target_ip, 80)
    if result:
        c.execute("INSERT INTO SCAN_RESULTS VALUES (?,?,?,?)", result)
        conn.commit()

conn.close()
