from flask import g
from configparser import ConfigParser
from psycopg2 import *


def get_service():
    """ Gets an instance of 'Service' from the 'g' environment. """
    if not hasattr(g, 'service'):
        g.service = Service()
    return g.service


class Service:
    """
        Service / Model for classical SQL queries in PostgreSQL.
        Requires the dependencies "psycopg2" and "ConfigParser" to work.
    """

    def __init__(self):
        """
            Gets the database configuration in the database.ini file.
            The file is supposed to be in the same directory as this one.
        """
        parser = ConfigParser()
        parser.readfp(open('database.ini'))
        host = parser.get('db_config', 'host')
        db = parser.get('db_config', 'database')
        user = parser.get('db_config', 'user')
        pwd = parser.get('db_config', 'password')
        self.connstr = host + " " + db + " " + user + " " + pwd

    def del_content(self, query, query_params):
        """
            Deletes a content from the database.
            Returns the status of the deletion.
        """
        db = connect(self.connstr)
        cur = db.cursor()
        cur.execute(query, query_params)
        if cur.rowcount > 0:
            value = True
        else:
            value = False
        db.commit()
        cur.close()
        db.close()
        return value

    def get_content(self, query, query_params):
        """
            Returns a single entity from the database.
        """
        db = connect(self.connstr)
        cur = db.cursor()
        cur.execute(query, query_params)
        content = cur.fetchone()
        cur.close()
        db.close()
        return content

    def get_custom_contents(self, query, query_params):
        """
            Returns a list of custom entities from the database.
        """
        db = connect(self.connstr)
        cur = db.cursor()
        cur.execute(query, query_params)
        content = cur.fetchall()
        cur.close()
        db.close()
        return content

    def get_contents(self, query):
        """
            Returns a list of entities from the database.
        """
        db = connect(self.connstr)
        cur = db.cursor()
        cur.execute(query)
        content = cur.fetchall()
        cur.close()
        db.close()
        return content

    def post_content(self, query, query_params):
        """
            Insert an entity in the database. Returns its id.
            /!\ : You need to put a RETURNING clause at the end of your query.
        """
        db = connect(self.connstr)
        cur = db.cursor()
        cur.execute(query, query_params)
        if cur.rowcount > 0:
            data = cur.fetchall()
        else:
            data = None
        db.commit()
        cur.close()
        db.close()
        return data[0]

    def put_content(self, query, query_params):
        """
            Edits content in the database. Returns the query's status.
        """
        db = connect(self.connstr)
        cur = db.cursor()
        cur.execute(query, query_params)
        if cur.rowcount > 0:   
            value = True
        else:
            value = False
        db.commit()
        cur.close()
        db.close()
        return value
