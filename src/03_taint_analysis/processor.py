# Processamento, porém sem sanitização dos dados
def format_search_term(term):
    if not term:
        return "default"
    
    return f"'{term.upper()}'"
