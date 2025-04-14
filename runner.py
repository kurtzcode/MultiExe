import os
import subprocess
import sys
import shutil
import tempfile

# Verifica se sys._MEIPASS existe antes de usá-lo
if hasattr(sys, "_MEIPASS"):
    source_path = sys._MEIPASS
else:
    source_path = os.path.dirname(os.path.abspath(__file__))

# Pasta temporária onde os arquivos .exe serão extraídos
temp_path = tempfile.mkdtemp()

# Obtém dinamicamente todos os arquivos .exe dentro do source_path
files = [f for f in os.listdir(source_path) if f.endswith(".exe")]

# Extrai os arquivos para a pasta temporária
for file in files:
    source_file = os.path.join(source_path, file)
    temp_file = os.path.join(temp_path, file)
    
    # Garante que o arquivo existe antes de tentar copiá-lo
    if os.path.exists(source_file):
        with open(source_file, "rb") as src, open(temp_file, "wb") as dst:
            dst.write(src.read())

# Executa os arquivos extraídos
for file in files:
    exe_path = os.path.join(temp_path, file)
    
    if os.path.exists(exe_path):
        subprocess.Popen(exe_path, shell=True)

