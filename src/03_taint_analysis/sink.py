"""
TESTE DE CROSS FILE TAINT
Objetivo: Testar se a ferramenta é capaz de fazer taint analysis entre
diferentes arquivos 
"""
import os
from taint_source import get_dangerous_input
from taint_processor import format_data

def execute_vulnerability(dirty_input):
    dirty_input = get_dangerous_input()

    payload = format_data(dirty_input)

    print(f"Executando: {payload}")
    
    os.system(payload)

if __name__ == "__main__":
    execute_vulnerability()
