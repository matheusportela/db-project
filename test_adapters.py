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
        self.db.drop_table(self.table)
        self.db.disconnect()

    @check_success_exception
    def testTableWithTextAttributeCreation(self):
        attributes = {
            'attr_boolean': self.db.BOOLEAN,
            'attr_integer': self.db.INTEGER,
            'attr_float': self.db.FLOAT,
            'attr_text': self.db.STRING,
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

if __name__ == '__main__':
    unittest.main()