import random
import shutil
import os
from pathlib import Path

def gerar_numeros(tamanho):

    tamanho_numero = 10  

    num_numeros = tamanho // tamanho_numero

    with open("numeros_grandes.txt", "w") as arquivo:
        for _ in range(num_numeros):

            numero = random.randint(0, 1000000000)
            arquivo.write(f"{numero}\n")

    tamanho_gerado = tamanho / (1024**2)
    print(f"Arquivo gerado com aproximadamente {tamanho_gerado:.2f} MB")
    return tamanho_gerado

def ordenar_numeros():
    print("Lendo números do arquivo...")
    with open("numeros_grandes.txt", "r") as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]
    
    print("Ordenando números...")
    numeros.sort()
    
    print("Salvando números ordenados em arquivo separado...")
    with open("numeros_ordenados.txt", "w") as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")
    
    print("Números ordenados salvos em 'numeros_ordenados.txt' com sucesso!")

def mover_para_area_trabalho():
    print("Movendo arquivos para Área de Trabalho...")
    
    # envio da Área de Trabalho
    desktop = str(Path.home() / "Desktop")
    
    # Move numeros grandes
    if os.path.exists("numeros_grandes.txt"):
        shutil.move("numeros_grandes.txt", os.path.join(desktop, "numeros_grandes.txt"))
        print("✓ numeros_grandes.txt movido para Desktop")
    
    # Move numeros ordenados
    if os.path.exists("numeros_ordenados.txt"):
        shutil.move("numeros_ordenados.txt", os.path.join(desktop, "numeros_ordenados.txt"))
        print("✓ numeros_ordenados.txt movido para Desktop")
    
    print(f"Arquivos movidos com sucesso para: {desktop}")

gerar_numeros(1*1024**3)
ordenar_numeros()
mover_para_area_trabalho()