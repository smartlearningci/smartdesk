"""Persistência SQLite do MVP."""
import os,sqlite3
def connect(path=None):
 d=sqlite3.connect(path or os.getenv("SMARTDESK_DB","smartdesk.sqlite3"));d.row_factory=sqlite3.Row;d.execute("PRAGMA foreign_keys=ON");return d
def initialize(d):
 d.executescript("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,secret TEXT NOT NULL,role TEXT NOT NULL);
 CREATE TABLE IF NOT EXISTS tickets(id INTEGER PRIMARY KEY,title TEXT NOT NULL,description TEXT NOT NULL,category TEXT NOT NULL,state TEXT NOT NULL DEFAULT 'Aberto',creator_id INTEGER NOT NULL REFERENCES users(id),technician_id INTEGER REFERENCES users(id),resolution TEXT);""");d.commit()
