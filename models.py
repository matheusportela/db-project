#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Data access objects.
"""

import string
import datetime

from db import PostgreSQLAdapter as DBAdapter


class Query(object):
    def __init__(self, objclass, database, table, columns):
        self.objclass = objclass
        self.database = database
        self.table = table
        self.columns = columns
        self.db = DBAdapter()

    def all(self):
        self.db.connect(self.database)
        data = self.db.read_all(self.table, self.columns)
        objects = []
        for d in data:
            obj = self.objclass()
            obj._set_data(d)
            objects.append(obj)
        self.db.disconnect()
        return objects


class BaseModel(object):
    database = 'healthdb'

    def __init__(self, **kwargs):
        self._columns = self._get_columns()

        for c in self._columns:
            if c in kwargs:
                self.__dict__[c] = kwargs[c]
            else:
                self.__dict__[c] = None

        self.table = self._get_table_name(self.__class__.__name__)
        self.db = DBAdapter()

    @classmethod
    def all(cls):
        query = Query(cls, BaseModel.database, cls.get_table(),
            cls._get_columns())
        return query.all()

    @classmethod
    def get_table(cls):
        return BaseModel._get_table_name(cls.__name__)

    @classmethod
    def _get_table_name(self, class_name):
        return string.lower(class_name) + '_table'

    @classmethod
    def _get_columns(cls):
        return [c for c in cls.__dict__ if not c.startswith('__')]

    def _get_data(self):
        return dict((c, self.__dict__[c]) for c in self._columns)

    def _set_data(self, data):
        if type(data) == tuple:
            for c, d in zip(self._get_columns(), data):
                self.__dict__[c] = d
        else:
            raise ValueError, 'Unknown data type'

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, str(self._get_data()))

    def create(self):
        self.db.connect(self.database)
        self.db.create(self.table, self._get_data())
        self.db.disconnect()

    def load(self):
        self.db.connect(self.database)
        data = self.db.read(self.table, self._columns, self.pk)
        self._set_data(data)
        self.db.disconnect()

    def save(self):
        self.db.connect(self.database)
        self.db.update(self.table, self._get_data())
        self.db.disconnect()

    def delete(self):
        self.db.connect(self.database)
        self.db.delete(self.table, self.pk)
        self.db.disconnect()

class SurgeryTypeModel(BaseModel):
    pk = None
    name = None
    specialty = None
    description = None


class SurgeryModel(BaseModel):
    pk = None
    surgery_date = None
    surgery_type_pk = None


class PharmacyModel(BaseModel):
    pk = None
    address = None
    phone = None
    cashier1 = None
    cashier2 = None


if __name__ == '__main__':
    for obj in SurgeryTypeModel.all():
        print str(obj)

    for obj in SurgeryModel.all():
        print str(obj)

    for obj in PharmacyModel.all():
        print str(obj)


    # p = PharmacyModel(pk=1, address='Address 1', phone='Phone', cashier1='Ana',
    #     cashier2='Beto')
    # p.create()

    # s = SurgeryModel(pk=1, surgery_date=datetime.date(2015, 12, 25),
    #     surgery_type_pk=st.pk)
    # s.create()

    # s.delete()
    # p.delete()
    # st.delete()