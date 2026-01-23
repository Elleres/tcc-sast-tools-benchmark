"""
TESTE DE CROSS FILE TAINT
Objetivo: Testar se a ferramenta é capaz de fazer taint analysis entre
diferentes arquivos 
"""

import sqlite3
from .source import get_user_input
from .processor import format_search_term

# CENÁRIO 1: SQL Injection (CWE-89)
# Dificuldade: Analisar a coleta de dados e processamento de funções
# que vem de diferentes arquivos.
def run_query():
    raw_data = get_user_input()

    formatted_data = format_search_term(raw_data)

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    query = f"SELECT * FROM products WHERE name = {formatted_data}"

    cursor.execute(query)
    print("Query executed")

if __name__ == "__main__":
    run_query()
