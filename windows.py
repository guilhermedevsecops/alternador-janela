import pyautogui
import threading
import subprocess
import sys
import time
import tkinter as tk  # Importe o módulo tkinter como 'tk'

def change_tabs(interval):
    while True:
        pyautogui.hotkey('ctrl', 'tab')  # Muda para a próxima aba
        time.sleep(interval)

def start_changing_tabs():
    interval = int(entry.get())  # Obtém o intervalo definido pelo usuário
    threading.Thread(target=change_tabs, args=(interval,)).start()  # Inicia a função em uma thread

# Cria a interface gráfica
root = tk.Tk()
root.title("Troca de Abas no Navegador")

label = tk.Label(root, text="Tempo para mudar as abas (segundos):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Iniciar", command=start_changing_tabs)
button.pack()

root.mainloop()

import tkinter
print(tkinter.TkVersion)
