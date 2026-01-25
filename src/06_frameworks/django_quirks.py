from django.db import models
from django.utils.safestring import mark_safe
from django.views.decorators.http import require_GET
from django.http import HttpResponse

class User(models.Model):
    name = models.CharField(max_length=100)

# CENÁRIO 1: Django Raw SQL - O jeito CERTO vs O jeito ERRADO
# Desafio: A ferramenta distingue a sintaxe segura de params da insegura?
# O Snyk deve detectar CWE-89 no Caso A (f-string), mas ignorar o Caso B (parametrização).
@require_GET
def django_raw_query_test(request):
    # FONTE (Source): O Snyk reconhece o 'request.GET' como dado não confiável
    user_input = request.GET.get('name')

    # CASO A: VULNERÁVEL (CWE-89)
    unsafe_query = f"SELECT * FROM auth_user WHERE name = '{user_input}'"
    User.objects.raw(unsafe_query)

    # CASO B: SEGURO
    User.objects.raw("SELECT * FROM auth_user WHERE name = %s", [user_input])
    
    return HttpResponse("Teste de SQLi")

# CENÁRIO 2: Django XSS e 'mark_safe'
# Desafio: A ferramenta sabe que o Django escapa HTML por padrão, mas que 'mark_safe' desliga essa proteção?
# O Snyk deve detectar CWE-79 apenas no response_vulnerable.
@require_GET
def django_xss_test(request):
    # FONTE (Source)
    user_bio = request.GET.get('bio', '')

    # CASO A: SEGURO (Django Auto-escape) 
    response_safe = HttpResponse(f"<h1>Bio: {user_bio}</h1>")

    # CASO B: VULNERÁVEL (CWE-79)
    response_vulnerable = HttpResponse(mark_safe(f"<h1>Bio: {user_bio}</h1>"))
    
    return response_vulnerable
