# ai_core/database_manager.py

import sqlite3

class DatabaseManager:
    def __init__(self, ai):
        self.ai = ai
        self.db_path = "metasploit_ai.db"
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.initialize_database()

    def initialize_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS exploits
                               (id INTEGER PRIMARY KEY, name TEXT, success_rate REAL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS vulnerabilities
                               (id INTEGER PRIMARY KEY, target TEXT, vulnerability TEXT)''')
        self.connection.commit()

    def store_exploit_result(self, name, success_rate):
        self.cursor.execute("INSERT INTO exploits (name, success_rate) VALUES (?, ?)", (name, success_rate))
        self.connection.commit()
        self.ai.logging_manager.log_info(f"Stored exploit result for {name}")

    def store_vulnerability(self, target, vulnerability):
        self.cursor.execute("INSERT INTO vulnerabilities (target, vulnerability) VALUES (?, ?)", (target, vulnerability))
        self.connection.commit()
        self.ai.logging_manager.log_info(f"Stored vulnerability {vulnerability} for target {target}")

    def query_exploits(self):
        self.cursor.execute("SELECT * FROM exploits")
        return self.cursor.fetchall()

    def query_vulnerabilities(self, target=None):
        if target:
            self.cursor.execute("SELECT * FROM vulnerabilities WHERE target=?", (target,))
        else:
            self.cursor.execute("SELECT * FROM vulnerabilities")
        return self.cursor.fetchall()
