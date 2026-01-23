"""
TESTE DE SUPRESSÃO
Objetivo: Tentar desligar a regra de 'Linha muito longa' (E501) e 'Print' (T201)
apenas para este ficheiro, usando ficheiros de configuração, SEM tocar no código.
"""

def function_with_very_long_line():
    # Esta linha tem mais de 120 caracteres propositadamente para disparar o linter de estilo (PEP8)
    print("Este é um texto extremamente longo que serve apenas para violar as regras de comprimento de linha padrão que a maioria dos linters como Flake8, Pylint e SonarQube trazem ativadas por defeito.") 

