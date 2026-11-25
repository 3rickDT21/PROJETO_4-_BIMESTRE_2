'''
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="PRIMEIRA OPÇÃO", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="Erick!").grid(column=2, row=1)
root.mainloop()
'''

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

MOLECULAS = {
    "Água (H2O)": {
        "atomos": [
            ("O", 0.0, 0.0, 0.0, "red", 600),
            ("H", 0.76, 0.59, 0.0, "lightgray", 250),
            ("H", -0.76, 0.59, 0.0, "lightgray", 250),
        ],
        "ligacoes": [(0, 1), (0, 2)]
    },
    "Gás Carbônico (CO2)": {
        "atomos": [
            ("C", 0.0, 0.0, 0.0, "black", 500),
            ("O", -1.16, 0.0, 0.0, "red", 550),
            ("O", 1.16, 0.0, 0.0, "red", 550),
        ],
        "ligacoes": [(0, 1), (0, 2)]
    },
    "Metano (CH4)": {
        "atomos": [
            ("C", 0.0, 0.0, 0.0, "black", 500),
            ("H", 0.63, 0.63, 0.63, "lightgray", 250),
            ("H", -0.63, -0.63, 0.63, "lightgray", 250),
            ("H", -0.63, 0.63, -0.63, "lightgray", 250),
            ("H", 0.63, -0.63, -0.63, "lightgray", 250),
        ],
        "ligacoes": [(0, 1), (0, 2), (0, 3), (0, 4)]
    },
    "Amônia (NH3)": {
        "atomos": [
            ("N", 0.0, 0.0, 0.38, "blue", 550),
            ("H", 0.94, 0.0, 0.0, "lightgray", 250),
            ("H", -0.47, 0.81, 0.0, "lightgray", 250),
            ("H", -0.47, -0.81, 0.0, "lightgray", 250),
        ],
        "ligacoes": [(0, 1), (0, 2), (0, 3)]
    }
}

animando = True
angulo = 0

def desenhar_molecula(event=None):
    nome = combo.get()
    dados = MOLECULAS[nome]
    
    ax.clear()
    atomos = dados["atomos"]
    
    # Desenha as ligações
    for i, j in dados["ligacoes"]:
        x = [atomos[i], atomos[j]]
        y = [atomos[i], atomos[j]]
        z = [atomos[i], atomos[j]]
        ax.plot(x, y, z, color="gray", linewidth=4, zorder=1)
        
    # Desenha os átomos
    for simbolo, x, y, z, cor, tamanho in atomos:
        ax.scatter(x, y, z, color=cor, s=tamanho, edgecolors="black", zorder=2)
        ax.text(x, y, z + 0.18, simbolo, fontsize=11, fontweight="bold", ha="center")
        
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_axis_off()
    ax.set_title(nome, fontsize=14, fontweight="bold")
    canvas.draw()

def animar():
    global angulo
    if animando:
        angulo = (angulo + 2) % 360  # Velocidade da rotação
        ax.view_init(elev=20, azim=angulo)
        canvas.draw_idle()
    janela.after(30, animar)  # Atualiza a cada 30 milissegundos (~33 FPS)

def alternar_animacao():
    global animando
    animando = not animando
    btn_animar.config(text="Pausar Giro" if animando else "Girar 3D")

# Configuração da janela
janela = tk.Tk()
janela.title("Visualizador Molecular 3D Animado")
janela.geometry("620x560")

frame_topo = tk.Frame(janela, pady=10)
frame_topo.pack()

tk.Label(frame_topo, text="Molécula:", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)

combo = ttk.Combobox(frame_topo, values=list(MOLECULAS.keys()), state="readonly", font=("Arial", 11))
combo.current(0)
combo.pack(side=tk.LEFT, padx=5)
combo.bind("<<ComboboxSelected>>", desenhar_molecula)

btn_animar = tk.Button(frame_topo, text="Pausar Giro", command=alternar_animacao, font=("Arial", 10))
btn_animar.pack(side=tk.LEFT, padx=10)

fig = plt.figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111, projection="3d")

canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

desenhar_molecula()
animar()  # Inicia o loop de animação

janela.mainloop()
