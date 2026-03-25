from django.db import models
from django.utils.safestring import mark_safe
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.utils.html import format_html

class User(models.Model):
    name = models.CharField(max_length=100)

@require_GET
def django_raw_query_test(request):
    user_input = request.GET.get('name')

    # Teste 10: SQL Injection (CWE-89)
    unsafe_query = f"SELECT * FROM auth_user WHERE name = '{user_input}'"
    User.objects.raw(unsafe_query)

    # Teste 11: SQL Injection (CWE-89) 
    # SEGURO
    User.objects.raw("SELECT * FROM auth_user WHERE name = %s", [user_input])
    
    return HttpResponse("Teste de SQLi")

@require_GET
def django_xss_test(request):
    user_bio = request.GET.get('bio', '')

    # Teste 12: Cross-site Scripting (CWE-79)
    response_vulnerable = HttpResponse(mark_safe(f"<h1>Bio: {user_bio}</h1>"))
    
    # Teste 13: Cross-site Scripting (CWE-79)
    # Seguro
    response_safe = HttpResponse(format_html("<h1>Bio: {}</h1>", user_bio))
    
    return (response_vulnerable, response_safe)
