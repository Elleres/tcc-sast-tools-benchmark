"""
TESTE DE SUPRESSÃO
Objetivo: Tentar desligar a regra CWE-78 apenas para este arquivo, utilizando a interface gráfica.
"""
import os
import sys

def testar_conectividade():
    """
    Testa a conectividade de rede com um IP fornecido pelo usuário.
    Vulnerabilidade: O IP de entrada não é validado antes de ser concatenado no comando do sistema.
    """
    if len(sys.argv) < 2:
        print("Uso: python teste_snyk.py <endereco_ip>")
        return

    ip_alvo = sys.argv[1]

    print(f"Testando conectividade com: {ip_alvo}")

    comando = f"ping -c 4 {ip_alvo}"
    
    os.system(comando)

if __name__ == "__main__":
    testar_conectividade()
