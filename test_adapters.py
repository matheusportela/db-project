#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import traceback

import adapters


def check_fail_exception(f):
    """Check whether the test raises an exception."""
    def wrapper(*args, **kwargs):
        self = args[0]

        try:
            v = f(*args, **kwargs)
            print traceback.format_exc()
            self.fail('%s failed' % f.__name__)
            return v
        except:
            pass
    return wrapper

def check_success_exception(f):
    """Test whether the test runs without raising an exception."""
    def wrapper(*args, **kwargs):
        self = args[0]

        try:
            v = f(*args, **kwargs)
        except:
            print traceback.format_exc()
            self.fail('%s failed' % f.__name__)
        return v
    return wrapper


class DatabaseConnectionTestCase(unittest.TestCase):
    def setUp(self):
        self.db = adapters.PostgreSQLAdapter()

    @check_success_exception
    def testSuccessfulConnection(self):
        self.db.connect('testdb')
        self.db.disconnect

    @check_fail_exception
    def testFailedConnection(self):
        self.db.connect('faildb')
        self.db.disconnect


class TableCreationTestCase(unittest.TestCase):
    def setUp(self):
        self.db = adapters.PostgreSQLAdapter()
        self.table = 'test_table'

    @check_success_exception
    def testEmptyTableCreation(self):
        self.db.connect('testdb')
        self.db.create_table(self.table, {})
        tables = self.db.list_tables()
        self.db.drop_table(self.table)
        self.db.disconnect()

        self.assertTrue(self.table in tables)

    @check_success_exception
    def testTableWithTextAttributeCreation(self):
        attributes = {
            'attr_boolean': self.db.BOOLEAN,
            'attr_integer': self.db.INTEGER,
            'attr_float': self.db.FLOAT,
            'attr_text': self.db.STRING,
            'attr_pk': self.db.PK,
        }

        self.db.connect('testdb')
        self.db.create_table(self.table, attributes)

        try:
            columns = self.db.list_columns(self.table)
        except:
            columns = []

        self.db.drop_table(self.table)
        self.db.disconnect()

        for attribute in attributes:
            self.assertTrue(attribute in columns)
        self.assertFalse('not_attr' in columns)


class DatabaseManipulationTestCase(unittest.TestCase):
    def setUp(self):
        self.db = adapters.PostgreSQLAdapter()
        self.tables = ['test_table_1', 'test_table_2', 'test_table_3']

    def testTableListing(self):
        self.db.connect('testdb')

        for table in self.tables:
            self.db.create_table(table, {})

        tables = self.db.list_tables()

        for table in self.tables:
            self.db.drop_table(table)

        for table in self.tables:
            self.assertTrue(table in tables)
        self.assertFalse('not_table' in tables)

        self.db.disconnect()

if __name__ == '__main__':
    unittest.main()