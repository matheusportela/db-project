#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Adapters for various DBMS.

Compatible databases:
- PostgreSQL 9.4.5
"""

import psycopg2


class DBAdapter(object):
    """Virtual class for database adapters."""
    def connect(self, database):
        """Connects to existing database.

        Parameters:
        database -- Database name to connect with.
        """
        raise NotImplemented, 'Database adapter must implement connect'

    def disconnect(self):
        """Disconnects from currently connected database."""
        raise NotImplemented, 'Database adapter must implement disconnect'

    def create_table(self, name, attributes):
        """Creates new table in database.

        Parameters:
        name -- Table name.
        attributes -- Dictionary with attributes and repective types.
        """
        raise NotImplemented, 'Database adapter must implement create_table'

    def drop_table(self, name):
        """Deletes existing table from database.

        Parameters:
        name -- Table name.
        """
        raise NotImplemented, 'Database adapter must implement drop_table'


class PostgreSQLAdapter(DBAdapter):
    """PostgreSQL database adapter."""
    def __init__(self):
        super(PostgreSQLAdapter, self).__init__()
        self.connection = None
        self.cursor = None

    def connect(self, database):
        self.connection = psycopg2.connect('dbname=%s' % database)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def create_table(self, name, attributes):
        cmd = 'CREATE TABLE %s ();' % name
        self.cursor.execute(cmd)
        self.connection.commit()

    def drop_table(self, name):
        cmd = 'DROP TABLE %s;' % name
        self.cursor.execute(cmd)
        self.connection.commit()