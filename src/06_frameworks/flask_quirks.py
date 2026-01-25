from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# VULNERABILIDADE 1: OS Command Injection (CWE-78)
@app.route('/ping')
def ping_server():
    # FONTE (Source): O Snyk rastreia especificamente o request.args do Flask
    ip_address = request.args.get('ip')
    
    # DESTINO (Sink): A entrada vai direto para o shell
    comando = f"ping -c 1 {ip_address}"
    os.system(comando)
    
    return f"Testando conectividade com: {ip_address}"

# VULNERABILIDADE 2: SQL Injection (CWE-89)
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
@app.route('/user/<int:user_id>')
def get_user_by_id(user_id):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    return "User found"

if __name__ == '__main__':
    app.run(debug=True)
