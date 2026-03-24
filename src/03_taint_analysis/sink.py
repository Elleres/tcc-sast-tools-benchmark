"""
TESTE DE CROSS FILE TAINT
Objetivo: Testar se a ferramenta é capaz de fazer taint analysis entre
diferentes arquivos 
"""
import subprocess
from processor import get_dangerous_input
from source import format_data

# Teste 08: Command Injection (CWE-78)
def execute_vulnerability():
    dirty_input = get_dangerous_input()

    payload = format_data(dirty_input)

    print(f"Executando: {payload}")
    
    subprocess.run(payload, shell=True)

if __name__ == "__main__":
    execute_vulnerability()
