########################################################
#  Database File
########################################################

import psycopg2
import os

#  Definitions
cred_prod = ''
cred_dev = "dbname='melbourne' user='michael' host='localhost' password=''"
dev = (os.environ['USER'] == 'michael')
cred = cred_dev if dev else cred_prod

########################################################
#  Helper Functions
########################################################

def connect_to_db():
    conn = None
    try:
        conn = psycopg2.connect(cred)
    except:
        print "I am unable to connect to the database"
    return conn

########################################################
#  Database Class
########################################################

class DB:
    # Constructor
    def __init__(self):
        self.db = connect_to_db()

    def get_data(self):
        return
    # Helper methods
