"""
TESTE DE FALSOS NEGATIVOS AVANÇADO
Objetivo: Vulnerabilidades reais escondidas por ofuscação, má sanitização
ou lógica complexa.
""" 
import pickle
import sys
import base64
import re

# Teste 04: Code Injection via Ofuscação (CWE-77)
def execution_helper(user_input):
    cmd_trigger = base64.b64decode(b'b3Muc3lzdGVt').decode('utf-8')
    
    full_cmd = f"echo {user_input}"
    
    eval(f"{cmd_trigger}('{full_cmd}')")

# Teste 05: Path Traversal com Sanitização Falha (CWE-22)
def read_private_file(filename):
    sanitized = filename.replace("../", "")
    
    with open(f"/var/www/{sanitized}", "r") as f:
        return f.read()

# Teste 06: Insegurança na Deserialização (CWE-502)
class PayloadHandler:
    def __init__(self, data):
        self.data = data

    def process(self):
        return pickle.loads(self.data)

def load_user_config(serialized_data):
    handler = PayloadHandler(serialized_data)
    return handler.process()

# Teste 07: ReDoS - Regex Denial of Service (CWE-1333)
def validate_email(email):
    pattern = re.compile(r"^([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+@example\.com$")
    
    if pattern.match(email):
        return True
    return False

if __name__ == "__main__":
    user_input = sys.argv[1] 
    load_user_config(user_input)
    read_private_file(user_input)
    execution_helper(user_input)
    validate_email(user_input)
