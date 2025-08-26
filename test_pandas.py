try:
    import pandas as pd
    # Se a importação for bem-sucedida, imprime a versão
    print(f"Pandas instalado com sucesso!")
    print(f"Versão: {pd.__version__}")
except ImportError:
    # Se o pandas não estiver instalado, uma exceção será lançada
    print("Erro: O pacote pandas não está instalado.")
    print("Para instalar, use o comando: pip install pandas")