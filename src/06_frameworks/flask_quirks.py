from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# VULNERABILIDADE 1: OS Command Injection (CWE-78)
# O motor do Snyk deve rastrear o request.args como Fonte e os.system como Destino.
# Uma vulnerabilidade Crítica deve ser reportada nesta função.
@app.route('/ping')
def ping_server():
    # FONTE (Source): O Snyk rastreia especificamente o request.args do Flask
    ip_address = request.args.get('ip')
    
    # DESTINO (Sink): A entrada vai direto para o shell
    comando = f"ping -c 1 {ip_address}"
    os.system(comando)
    
    return f"Testando conectividade com: {ip_address}"

# VULNERABILIDADE 2: SQL Injection (CWE-89)
# Desafio: O motor do Snyk deve detectar a concatenação direta da query vinda do request.
@app.route('/user')
def get_user():
    # FONTE (Source)
    user_id = request.args.get('id')
    
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # DESTINO (Sink): Concatenação de string direto na execução do SQL
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    return "Busca realizada"

# CENÁRIO 3: Flask Route Types (Validação Implícita)
# Desafio: O motor semântico do Snyk deve entender que <int:user_id> sanitiza o input implicitamente.
# Nenhuma vulnerabilidade CWE-89 deve ser reportada nesta função.
@app.route('/user/<int:user_id>')
def get_user_by_id(user_id):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    return "User found"

if __name__ == '__main__':
    app.run(debug=True)
