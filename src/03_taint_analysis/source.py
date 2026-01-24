import sys

def get_dangerous_input():
    """
    SOURCE: Retorna o primeiro argumento da linha de comando.
    Para o Snyk, isso é explicitamente 'Tainted'.
    """
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "default_value"
