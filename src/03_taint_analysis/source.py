import os

# Dados sujos vindo do usuário
def get_user_input():
    return os.getenv("USER_SEARCH_QUERY", "")
