#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Adapters for various DBMS.

Compatible databases:
- PostgreSQL 9.4.5
"""

import psycopg2


def raise_not_implemented(f):
    """Raises not implemented error."""
    def wrapper(*args, **kwargs):
        raise NotImplementedError, ('Database adapter must implement "%s"'
                                    % f.__name__)
    return wrapper


class DBAdapter(object):
    """Virtual class for database adapters."""
    @raise_not_implemented
    def connect(self, database):
        """Connects to existing database.

        Parameters:
        database -- Database name to connect with.
        """
        pass

    @raise_not_implemented
    def disconnect(self):
        """Disconnects from currently connected database."""
        pass

    @raise_not_implemented
    def list_tables(self):
        """Lists the name of all tables in the connected database."""
        pass

    @raise_not_implemented
    def create_table(self, table, attributes):
        """Creates new table in database.

        Parameters:
        table -- Table name.
        attributes -- Dictionary with attributes and repective types.
        """
        pass

    @raise_not_implemented
    def drop_table(self, table):
        """Deletes existing table from database.

        Parameters:
        table -- Table name.
        """
        pass

    @raise_not_implemented
    def list_columns(self, table):
        """Lists the name of all columns in the given table.

        Parameters:
        table -- Table name.

        Return:
        List with columns names.
        """
        pass

    @raise_not_implemented
    def insert(self, table, data):
        """Inserts new data to the given table.

        Parameters:
        table -- Table name.
        data -- Dictionary with column name and value to be inserted.
        """
        pass


class PostgreSQLAdapter(DBAdapter):
    """PostgreSQL database adapter."""

    # PostgreSQL Datatypes
    # http://www.postgresql.org/docs/current/static/datatype.html
    BOOLEAN = 'boolean'
    INTEGER = 'integer'
    FLOAT = 'real'
    STRING = 'text'
    PK = 'serial PRIMARY KEY'

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

    def list_tables(self):
        cmd = ("SELECT table_name FROM information_schema.tables "
              "WHERE table_schema = 'public';")
        self.cursor.execute(cmd)
        return [table[0] for table in self.cursor.fetchall()]

    def create_table(self, name, attributes):
        cmd = 'CREATE TABLE %s (' % name
        cmd += ', '.join('%s %s' % (name, type)
            for name, type in attributes.items())
        cmd += ');'

        self.cursor.execute(cmd)
        self.connection.commit()

    def drop_table(self, name):
        cmd = 'DROP TABLE %s;' % name
        self.cursor.execute(cmd)
        self.connection.commit()

    def list_columns(self, table):
        cmd = 'SELECT * FROM %s;' % table
        self.cursor.execute(cmd)
        return [desc[0] for desc in self.cursor.description]

    def insert(self, table, data):
        cmd = 'INSERT INTO %s (' % table
        cmd += ', '.join('%s' % column for column in data)
        cmd += ') VALUES ('
        cmd += ', '.join('%s' % self._convert_format(value)
            for value in data.values())
        cmd += ');'
        self.cursor.execute(cmd)
        self.connection.commit()

    def _convert_format(self, value):
        """Convert value to PostgreSQL required format. For instance, strings
        must be surrounded by single quotes.

        Parameters:
        value -- Value to be converted.
        """
        if type(value) == str:
            return "'%s'" % value
        return value