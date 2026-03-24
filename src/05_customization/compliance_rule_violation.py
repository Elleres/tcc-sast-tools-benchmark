"""
TESTE DE SUPRESSÃO PRÉ-ANÁLISE
Objetivo: Tentar desligar a regra CWE-78 apenas para este arquivo, usando comentário no código.
"""
import os
import sys

# Teste 9: Command Injection (CWE-78)
def testar_conectividade():
    if len(sys.argv) < 2:
        print("Uso: python teste_snyk.py <endereco_ip>")
        return

    ip_alvo = sys.argv[1]

    print(f"Testando conectividade com: {ip_alvo}")

    comando = f"ping -c 4 {ip_alvo}"
    os.system(comando) # nosec # NOSONAR # skipcq

if __name__ == "__main__":
    testar_conectividade()
