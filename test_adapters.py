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
        attributes = [
            ('attr_boolean', self.db.BOOLEAN),
            ('attr_integer', self.db.INTEGER),
            ('attr_float', self.db.FLOAT),
            ('attr_text', self.db.STRING),
            ('attr_pk', self.db.PK),
        ]

        self.db.connect('testdb')
        self.db.create_table(self.table, attributes)

        try:
            columns = self.db.list_columns(self.table)
        except:
            columns = []

        self.db.drop_table(self.table)
        self.db.disconnect()

        for name, type in attributes:
            self.assertTrue(name in columns)
        self.assertFalse('not_attr' in columns)


class DatabaseManipulationTestCase(unittest.TestCase):
    def setUp(self):
        self.db = adapters.PostgreSQLAdapter()
        self.tables = ['test_table_1', 'test_table_2', 'test_table_3']

    def testTableListing(self):
        self.db.connect('testdb')

        for table in self.tables:
            self.db.create_table(table, {})

        try:
            tables = self.db.list_tables()
        except:
            tables = []

        for table in self.tables:
            self.db.drop_table(table)

        for table in self.tables:
            self.assertTrue(table in tables)
        self.assertFalse('not_table' in tables)

        self.db.disconnect()


class TableManipulationTestCase(unittest.TestCase):
    def setUp(self):
        self.db = adapters.PostgreSQLAdapter()
        self.table = 'test_manipulation_table'
        self.columns = [
            ('test_pk', self.db.PK),
            ('test_str', self.db.STRING),
            ('test_int', self.db.INTEGER),
            ('test_float', self.db.FLOAT),
            ('test_bool', self.db.BOOLEAN),
        ]
        self.data_tuple = (123, 'Test name', 42, 3.14159, True)
        self.data_dict = {
            'test_pk': 123,
            'test_str': 'Test name',
            'test_int': 42,
            'test_float': 3.14159,
            'test_bool': True,
        }

    @check_success_exception
    def testInsertDict(self):
        self.db.connect('testdb')

        if self.table not in self.db.list_tables():
            self.db.create_table(self.table, self.columns)

        self.db.insert(self.table, self.data_dict)
        self.db.drop_table(self.table)
        self.db.disconnect()

    def testInsertTuple(self):
        self.db.connect('testdb')

        if self.table not in self.db.list_tables():
            self.db.create_table(self.table, self.columns)

        self.db.insert(self.table, self.data_tuple)
        self.db.drop_table(self.table)
        self.db.disconnect()

    def testSelectAll(self):
        self.db.connect('testdb')
        self.db.create_table(self.table, self.columns)
        self.db.insert(self.table, self.data_tuple)

        all_rows = self.db.select(self.table)

        columns = ['test_pk', 'test_float']
        projected_rows = self.db.select(self.table, columns=columns)
        expected_rows = tuple(self.data_dict[c] for c in columns)

        self.db.drop_table(self.table)
        self.db.disconnect()

        self.assertTrue(self.data_tuple in all_rows)
        self.assertTrue(expected_rows in projected_rows)

    def testSelectWhere(self):
        data = [
            (1, 'Test1', 0, 0.0, False),
            (2, 'Test2', 0, 0.1, False),
            (3, 'Test3', 0, 0.1, True),
        ]

        self.db.connect('testdb')
        self.db.create_table(self.table, self.columns)

        for d in data:
            self.db.insert(self.table, d)

        rows1 = self.db.select(self.table, columns=['test_pk', 'test_str'], where=('=', 'test_pk', 2))
        rows2 = self.db.select(self.table, columns=['test_pk', 'test_str'], where=('=', 'test_str', "'Test3'"))
        rows3 = self.db.select(self.table, where=('=', 'test_int', 0))
        rows4 = self.db.select(self.table, where=('>', 'test_float', 0))
        rows5 = self.db.select(self.table, where=('and', ('>', 'test_float', 0), ('=', 'test_pk', 2)))
        rows6 = self.db.select(self.table, where=('or', ('>', 'test_float', 0), ('=', 'test_bool', False)))

        self.db.drop_table(self.table)
        self.db.disconnect()

        self.assertTrue((2, 'Test2') in rows1)
        self.assertTrue((3, 'Test3') in rows2)
        self.assertEqual(data, rows3)
        self.assertEqual(data[1:], rows4)
        self.assertEqual([data[1]], rows5)
        self.assertEqual(data, rows6)

    def testEq(self):
        where = self.db._convert_where(('=', 'x', 'y'))
        self.assertEqual(where, 'WHERE (x = y)')

        where = self.db._convert_where(('and', 'x', 'y'))
        self.assertEqual(where, 'WHERE (x AND y)')

        where = self.db._convert_where(('or', 'x', 'y'))
        self.assertEqual(where, 'WHERE (x OR y)')


if __name__ == '__main__':
    unittest.main()