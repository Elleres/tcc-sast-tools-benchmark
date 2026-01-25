from flask import Flask, request, redirect, render_template_string, send_file

app = Flask(__name__)

# CENÁRIO 1: Flask SSTI (Server-Side Template Injection - CWE-74)
@app.route('/hello')
def hello_ssti():
    user_name = request.args.get('name', 'Visitante')

    # VULNERÁVEL - RCE/SSTI.
    template_inseguro = f"<h1>Olá, {user_name}!</h1>"
    return render_template_string(template_inseguro)

# CENÁRIO 2: Flask Open Redirect (CWE-601)
@app.route('/login')
def login():
    # FONTE (Source): O parâmetro 'next' vindo da URL
    next_url = request.args.get('next')

    login_sucesso = True 

    if login_sucesso and next_url:
        return redirect(next_url)
    
    return "Login Page"


# CENÁRIO 3: Path Traversal (LFI) via Flask Send File (CWE-22)
@app.route('/download')
def download_file():
    filename = request.args.get('file')

    # VULNERÁVEL - '?file=../../../etc/passwd'
    return send_file(f"uploads/{filename}")

