"""
TESTE DE WONT FIX
Objetivo: Marcar no dashboard da ferramenta essa vulnerabilidade abaixo como
"won't fix" ou algum marcador semelhante e verificar se ele será ignorado nos próximos
commits.
"""
import hashlib

def legacy_hashing(password):
    return hashlib.md5(password.encode()).hexdigest()
