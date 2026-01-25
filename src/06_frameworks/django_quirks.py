from django.db import models
from django.utils.safestring import mark_safe
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.utils.html import format_html

class User(models.Model):
    name = models.CharField(max_length=100)

# CENÁRIO 1: Django Raw SQL
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

# CENÁRIO 2: format_html e 'mark_safe'
@require_GET
def django_xss_test(request):
    # FONTE (Source)
    user_bio = request.GET.get('bio', '')

    # CASO A: SEGURO Format_html garante a seguranca do dado 
    response_safe = HttpResponse(format_html("<h1>Bio: {}</h1>", user_bio))

    # CASO B: VULNERÁVEL (CWE-79)
    response_vulnerable = HttpResponse(mark_safe(f"<h1>Bio: {user_bio}</h1>"))
    
    return (response_vulnerable, response_safe)
