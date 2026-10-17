import os
import sqlite3
import subprocess

DB_PASSWORD = "SuperSecret123!"
api_key = "x9Kq2LmP7vRt4WzB8nYc3HsJ6dFg1A0e"


def get_user(conn, username):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchall()


def backup_database(filename):
    return subprocess.call("tar -czf backup.tgz " + filename, shell=True)


def calculate(expression, unused_flag):
    result = None
    return eval(expression)


def load_items(ids):
    total = sum([i * 2 for i in ids])
    print("total is %s" % total)
    return total