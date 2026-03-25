"""
TESTE DE SUPRESSÃO PÓS ANÁLISE
Objetivo: Marcar no dashboard da ferramenta essa vulnerabilidade abaixo como
"won't fix" ou algum marcador semelhante. Deve ser possível ignorar somente 
um issue e não o arquivo inteiro.
"""
import hashlib

def legacy_hashing(password):
    # Teste 17: Use of Password Hash With Insufficient Computational Effort (CWE-916)
    return hashlib.md5(password.encode()).hexdigest()

