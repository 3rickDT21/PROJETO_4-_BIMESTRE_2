import periodictable
import tkinter as tk
import pandas as pd
from mendeleev.fetch import fetch_table

# ... (seu código atual do painel à direita) ...

# Separador e área de Moléculas no painel lateral
tk.Frame(painel, height=2, bg="#555555").pack(fill="x", pady=15)

tk.Label(painel, text="Analisar Molécula:", font=("Arial", 11, "bold"), bg="#2d2d2d", fg="#cccccc").pack(anchor="w")

entrada_mol = tk.Entry(painel, font=("Arial", 12), bg="#1e1e1e", fg="white", insertbackground="white")
entrada_mol.pack(fill="x", pady=5)
entrada_mol.insert(0, "Ca3(PO4)2")

lbl_mol_res = tk.Label(painel, text="", font=("Arial", 10), bg="#2d2d2d", fg="#a1d99b", justify="left")
lbl_mol_res.pack(anchor="w", pady=5)

def calcular_molecula():
    texto_formula = entrada_mol.get().strip()
    try:
        mol = periodictable.formula(texto_formula)
        composicao = ", ".join([f"{el.symbol}: {qtd}" for el, qtd in mol.atoms.items()])
        lbl_mol_res.config(
            text=f"Massa Molar: {mol.mass:.3f} g/mol\nComposição: {composicao}",
            fg="#a1d99b"
        )
    except Exception:
        lbl_mol_res.config(text="Fórmula inválida! Ex: H2O, H2CO3", fg="#fc9272")

btn_calc = tk.Button(painel, text="Calcular Molécula", command=calcular_molecula, bg="#4a90e2", fg="white", font=("Arial", 10, "bold"))
btn_calc.pack(fill="x", pady=5)
