#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Database adapter."""

import psycopg2

class PostgreSQLAdapter(object):
    """PostgreSQL database adapter."""

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, database):
        self.connection = psycopg2.connect('dbname=%s' % database)
        self.cursor = self.connection.cursor()
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE,
            self.cursor)

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def execute_and_commit(self, cmd, *args):
        self.cursor.execute(cmd, *args)
        self.connection.commit()

    def execute_and_fetch_one(self, cmd, *args):
        self.cursor.execute(cmd, *args)
        return self.cursor.fetchone()

    def execute_and_fetch_all(self, cmd, *args):
        self.cursor.execute(cmd, *args)
        return self.cursor.fetchall()

    def _convert_format(self, value):
        if type(value) == str:
            return "'{}'".format(value)
        return value

    def create(self, table, data):
        cmd = 'INSERT INTO %s (' % table
        cmd += ', '.join('%s' % column for column in data)
        cmd += ') VALUES ('
        cmd += ', '.join('%s' for value in data.values())
        cmd += ');'

        values = [value for value in data.values()]

        self.execute_and_commit(cmd, values)

    def read(self, table, columns, pk):
        cmd = 'SELECT '
        cmd += ', '.join('{}'.format(column) for column in columns)
        cmd += ' FROM {} WHERE pk = {};'.format(table, pk)
        return self.execute_and_fetch_one(cmd)

    def read_all(self, table, columns):
        cmd = 'SELECT '
        cmd += ', '.join('{}'.format(column) for column in columns)
        cmd += ' FROM {};'.format(table)
        return self.execute_and_fetch_all(cmd)

    def update(self, table, data):
        cmd = 'UPDATE {} SET '.format(table)
        cmd += ', '.join(['%s = ' % column + '%s' for column in data if column != 'pk'])
        cmd += ' WHERE pk = {};'.format(data['pk'])

        values = [value for column, value in data.items() if column != 'pk']

        self.execute_and_commit(cmd, values)

    def delete(self, table, pk):
        cmd = 'DELETE FROM {} WHERE pk = {};'.format(table, pk)
        self.execute_and_commit(cmd)