"""SQLite in-memory database for items"""

import sqlite3
from contextlib import contextmanager
from typing import Generator

# SQLite in-memory database connection
connection = sqlite3.connect(":memory:", check_same_thread=False)
connection.row_factory = sqlite3.Row


def init_db() -> None:
	"""Initialize the database schema"""
	cursor = connection.cursor()
	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS items (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT UNIQUE NOT NULL,
			created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		)
		"""
	)
	connection.commit()


@contextmanager
def get_cursor() -> Generator[sqlite3.Cursor, None, None]:
	"""Context manager for database cursor"""
	cursor = connection.cursor()
	try:
		yield cursor
		connection.commit()
	except Exception:
		connection.rollback()
		raise
	finally:
		cursor.close()


# Initialize database on module import
init_db()
