"""
TESTE DE FALSOS NEGATIVOS AVANÇADO
Objetivo: Vulnerabilidades reais escondidas por ofuscação, má sanitização
ou lógica complexa que desafiam o motor de Taint Analysis.
"""
import os
import pickle
import base64
import re
from flask import request

# CENÁRIO 1: Command Injection via Ofuscação (CWE-78 / CWE-77)
# Dificuldade: A ferramenta precisa descodificar Base64 ou entender 'eval/exec'
def execution_helper(user_input):
    # 'b3Muc3lzdGVt' é 'os.system' em Base64
    cmd_trigger = base64.b64decode(b'b3Muc3lzdGVt').decode('utf-8')
    
    full_cmd = f"echo {user_input}"
    
    # Executamos usando eval() que chama os.system()
    # A ferramenta consegue ligar o 'eval' -> 'base64' -> 'os.system'?
    eval(f"{cmd_trigger}('{full_cmd}')")

# CENÁRIO 2: Path Traversal com Sanitização Falha (CWE-22)
# Dificuldade: A ferramenta vê o '.replace' e assume que o dado foi limpo.
def read_private_file(filename):
    # O usuário envia '....//' -> O replace remove o meio -> sobra '../'
    sanitized = filename.replace("../", "")
    
    with open(f"/var/www/{sanitized}", "r") as f:
        return f.read()

# CENÁRIO 3: Insegurança na Deserialização (CWE-502)
# Dificuldade: O input entra numa classe antes de explodir.
class PayloadHandler:
    def __init__(self, data):
        self.data = data

    def process(self):
        return pickle.loads(self.data)

def load_user_config(serialized_data):
    handler = PayloadHandler(serialized_data)
    return handler.process()

# CENÁRIO 4: ReDoS - Regex Denial of Service (CWE-1333)
# Dificuldade: Não é vulnerabilidade de injeção, é complexidade algorítmica.
def validate_email(email):
    # Regex vulnerável a backtracking
    pattern = re.compile(r"^([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+@example\.com$")
    
    if pattern.match(email):
        return True
    return False
