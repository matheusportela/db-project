#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Adapters for various DBMS.

Compatible databases:
- PostgreSQL 9.4.5
"""


class DBAdapter(object):
    """Virtual class for database adapters."""

    def create_table(name, attributes):
        """Create new table in database.

        Parameters:
        name -- Table name.
        attributes -- Dictionary with attributes and repective types.
        """
        raise NotImplemented, 'Database adapter must implement create_table'

    def delete_table(name):
        """Delete existing table from database.

        Parameters:
        name -- Table name.
        """
        raise NotImplemented, 'Database adapter must implement delete_table'