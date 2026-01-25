import re

def format_search_term(term):
    """
    PROCESSOR: Apenas executa a funcao upper na string, mantendo a string suja.
    """
    if not term:
        return "default"

    # Retorna o termo limpo e encapsulado
    return f"'{term.upper()}'"
