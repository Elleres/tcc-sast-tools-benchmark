import re

def format_search_term(term):
    """
    PROCESSOR (Sanitizer):
    Agora esta função aplica uma limpeza ativa (Sanitization).
    """
    if not term:
        return "default"
    
    # ESTRATÉGIA: Allowlist (Lista Branca)
    # Remove tudo que NÃO for letra (a-z) ou número (0-9).
    safe_term = re.sub(r'[^a-zA-Z0-9]', '', term)
    
    # Retorna o termo limpo e encapsulado
    return f"'{safe_term.upper()}'"
