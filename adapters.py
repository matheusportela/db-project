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
        attributes -- List of tuples containing the attribute name and its type.
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
        data -- Tuple with values or dictionary with column name and value to be
            inserted.
        """
        pass

    @raise_not_implemented
    def select(self, table, columns=None, where=None):
        """Select data from the given table.

        Parameters:
        table -- Table name.
        columns -- List of columns to project onto the table.
        where -- List of filtering conditions in the form [(op, value1, value2)].
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
            for name, type in attributes)
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
        if type(data) == dict:
            cmd = self._generate_insert_query_dict(table, data)
        elif type(data) == tuple:
            cmd = self._generate_insert_query_tuple(table, data)
        else:
            raise ValueError, 'Insert accepts only dict and tuple types'

        self.cursor.execute(cmd)
        self.connection.commit()

    def _generate_insert_query_dict(self, table, data):
        cmd = 'INSERT INTO %s (' % table
        cmd += ', '.join('%s' % column for column in data)
        cmd += ') VALUES ('
        cmd += ', '.join('%s' % self._convert_format(value)
            for value in data.values())
        cmd += ');'
        return cmd

    def _generate_insert_query_tuple(self, table, data):
        cmd = 'INSERT INTO %s (' % table
        cmd += ', '.join('%s' % column for column in self.list_columns(table))
        cmd += ') VALUES ('
        cmd += ', '.join('%s' % self._convert_format(value) for value in data)
        cmd += ');'
        return cmd

    def _convert_format(self, value):
        """Convert value to PostgreSQL required format. For instance, strings
        must be surrounded by single quotes.

        Parameters:
        value -- Value to be converted.
        """
        if type(value) == str:
            return "'%s'" % value
        return value

    def select(self, table, columns=None, where=None):
        cmd = 'SELECT '
        cmd += self._convert_columns(columns)
        cmd += ' FROM %s ' % table
        cmd += self._convert_where(where)
        cmd += ';'
        self.cursor.execute(cmd)
        return self.cursor.fetchall()

    def _convert_columns(self, columns):
        if columns:
            return ', '.join(columns)
        return '*'

    def _convert_where(self, where):
        if where == None:
            return ''

        return 'WHERE ' + self._convert_condition_to_str(where)

    def _convert_condition_to_str(self, condition):
        if type(condition) == tuple:
            op, value1, value2 = condition
            converted_value1 = self._convert_condition_to_str(value1)
            converted_value2 = self._convert_condition_to_str(value2)

            if op == '=':
                return '{} = {}'.format(converted_value1, converted_value2)
            elif op == 'and':
                return '{} AND {}'.format(converted_value1, converted_value2)
            elif op == 'or':
                return '{} OR {}'.format(converted_value1, converted_value2)
            elif op == '>':
                return '{} > {}'.format(converted_value1, converted_value2)
            elif op == '<':
                return '{} < {}'.format(converted_value1, converted_value2)
            elif op == '>=':
                return '{} >= {}'.format(converted_value1, converted_value2)
            elif op == '<=':
                return '{} <= {}'.format(converted_value1, converted_value2)
            else:
                raise ValueError, 'Invalid operation "%s"' % op
        else:
            return condition