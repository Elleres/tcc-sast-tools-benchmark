"""
TESTE DE FALSOS POSITIVOS
Objetivo: Verificar se a ferramenta gera alertas em código seguro.
"""
import os
import sqlite3

# CENÁRIO 1: Hardcoded credentials (CWE-798)
# Dificuldade: A ferramenta vê password ou secret no nome da variável mas
# verifica o contexto de teste da classe.
class MockConfig:
   def __init__(self):
        # ARMADILHA 1: Nomes de variáveis que podem conter dados sensíveis
        self.db_password = "ADMIN_PASSWORD_123" 
        self.aws_secret_key = "AKIA_FAKE_KEY_FOR_TESTING"

# CENÁRIO 2: Path traversal (CWE-22)
# Dificuldade: A ferramenta precisa reconhecer o os.path.basename como um
# sanitizador válido.
def safe_path_traversal(filename):
    safe_name = os.path.basename(filename)
    return open(f"/var/log/{safe_name}", "r")

# CENÁRIO 3: SQL Injection (CWE-89)
# Dificuldade: Verificar que é feita a sanitização na condicional.
def get_sorted_users(sort_column):
    ALLOWED_COLUMNS = {"id", "username", "created_at"}
    
    if sort_column not in ALLOWED_COLUMNS:
        sort_column = "username"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users ORDER BY {sort_column}"
    
    cursor.execute(query)
    return cursor.fetchall()
