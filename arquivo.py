import sqlite3

"""Conexão com a base de dados"""
con = sqlite3.connect("luxtext.db")
"""Criação do cursor"""
cur = con.cursor()
cur.execute("CREATE TABLE (nome_arquivo)")
