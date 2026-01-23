"""
TESTE DE NUANCES DE FRAMEWORKS
Objetivo: Verificar se a ferramenta entende os mecanismos de segurança
internos do Django e do Flask.
"""
from django.db import models
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from flask import Flask

app = Flask(__name__)

class User(models.Model):
    name = models.CharField(max_length=100)

# CENÁRIO 1: Django Raw SQL - O jeito CERTO vs O jeito ERRADO
# Desafio: A ferramenta distingue a sintaxe segura de params da insegura?
def django_raw_query_test(user_input):
    # CASO A: VULNERÁVEL (CWE-89)
    unsafe_query = f"SELECT * FROM auth_user WHERE name = '{user_input}'"
    User.objects.raw(unsafe_query)

    # CASO B: SEGURO
    User.objects.raw("SELECT * FROM auth_user WHERE name = %s", [user_input])

# CENÁRIO 2: Django XSS e 'mark_safe'
# Desafio: A ferramenta sabe que o Django escapa HTML por padrão, 
# mas que 'mark_safe' desliga essa proteção?
def django_xss_test(user_bio):
    # CASO A: SEGURO (Django Auto-escape)
    response_safe = HttpResponse(f"<h1>Bio: {user_bio}</h1>")

    # CASO B: VULNERÁVEL (CWE-79)
    response_vulnerable = HttpResponse(mark_safe(f"<h1>Bio: {user_bio}</h1>"))
    
    return response_safe, response_vulnerable

# CENÁRIO 3: Flask Route Types (Validação Implícita)
# Desafio: SQL Injection impossível devido ao tipo da rota.
import sqlite3

@app.route('/user/<int:user_id>')
def get_user_by_id(user_id):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    return "User found"
