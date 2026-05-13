import importlib
import teste_import


teste_import.saudacao()

print("\nRecarregando módulo...\n")

importlib.reload(teste_import)

teste_import.saudacao()