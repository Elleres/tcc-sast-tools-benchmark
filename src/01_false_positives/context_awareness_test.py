"""
TESTE DE FALSOS POSITIVOS
Objetivo: Verificar se a ferramenta gera alertas em código seguro.
"""
import os
import sqlite3
import sys

# Teste 01: Hardcoded credentials (CWE-798)
class MockConfig:
   def __init__(self):
        self.db_password = "ADMIN_PASSWORD_123" 
        self.aws_secret_key = "AKIA_FAKE_KEY_FOR_TESTING"

# Teste 02: Path traversal (CWE-22)
def safe_path_traversal(filename):
    safe_name = os.path.basename(filename)
    return open(f"/var/log/{safe_name}", "r")

# Teste 03: SQL Injection (CWE-89)
def get_sorted_users(sort_column):
    ALLOWED_COLUMNS = {"id", "username", "created_at"}
    
    if sort_column not in ALLOWED_COLUMNS:
        sort_column = "username"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users ORDER BY {sort_column}"
    
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    user_input = sys.argv[1] if len(sys.argv) > 1 else "default"

    conf = MockConfig()
    print(f"Using DB: {conf.db_password}") 
    try:
        safe_path_traversal(user_input)
        get_sorted_users(user_input)
    except Exception:
        pass
