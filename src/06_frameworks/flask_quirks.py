from flask import Flask, request, redirect, render_template_string, send_file

app = Flask(__name__)

@app.route('/hello')
def hello_ssti():
    user_name = request.args.get('name', 'Visitante')

    # Teste 14: Cross-site Scripting (CWE-79)
    template_inseguro = f"<h1>Olá, {user_name}!</h1>"
    return render_template_string(template_inseguro)

@app.route('/login')
def login():
    next_url = request.args.get('next')

    login_sucesso = True 

    if login_sucesso and next_url:
        # Teste 15: URL Redirection to Untrusted Site (CWE-601)
        return redirect(next_url)
    
    return "Login Page"

@app.route('/download')
def download_file():
    filename = request.args.get('file')

    # Teste 16: Path Traversal (CWE-22)
    return send_file(f"uploads/{filename}")

