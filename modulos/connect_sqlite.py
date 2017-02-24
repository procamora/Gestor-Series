#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3


def conectionSQLite(db, query, dict=False):
    conn = sqlite3.connect(db)
    if dict:
        conn.row_factory = __dictFactory
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    cursor.close()
    conn.close()

    return data


def __dictFactory(cursor, row):
    d = dict()
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def ejecutaScriptSqlite(db, script):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    cursor.close()
    conn.close()
