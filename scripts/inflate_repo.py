import os
import shutil

SOURCE_FILE = "../src/02_false_negatives/vulnerable_app.py"
TARGET_DIR = "../src/04_performance_load"

def inflate(copies=500):
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    
    for i in range(copies):
        # Cria 500 ficheiros iguais. O analisador tem de ler e processar cada um.
        # Isto testa a velocidade de I/O e de processamento do motor.
        shutil.copy(SOURCE_FILE, f"{TARGET_DIR}/load_test_{i}.py")


if __name__ == "__main__":
    inflate()
