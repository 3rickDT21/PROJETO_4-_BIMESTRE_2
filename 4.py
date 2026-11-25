'''
4. Dada a massa atômica de átomos, calcular a massa molecular de moléculas
Exemplo:
O algoritmo deve receber dados de massas atômicas (informação contida na Tabela Periódica), por exemplo Hidrogênio = 1; Oxigênio = 16, Carbono = 12, Cálcio = 40, Fósforo = 31.
O algoritmo deve receber uma molécula e retornar sua massa molecular, como 
H20 = 18 (2 * 1 + 16)
H2CO3 = 62 (2 * 1 + 12 + 3 * 16) 
Ca(OH)2 = 74 (40 + (16 + 1) * 2) 
Ca3(PO4)2 = 310 (3 * 40 + (31 + 4 * 16) * 2)
Nota: Não é necessário utilizar o texto subscrito para a entrada das moléculas. Exemplo: H20, H2CO3, Ca3(PO4)2

'''
import tkinter as tk
import pandas as pd
from mendeleev.fetch import fetch_table
import periodictable


df = fetch_table('elements')
series_df = fetch_table('series').set_index('id')['name'].to_dict()
#molecula = input("Informe uma molécula: ex->  H20, H2CO3, Ca3(PO4)2: ")
massa_molecular = 0

CORES = {
    'Nonmetals': '#a1d99b',
    'Noble gases': '#9ecae1',
    'Alkali metals': '#fc9272',
    'Alkaline earth metals': '#fdae6b',
    'Metalloids': '#bcbddc',
    'Halogens': '#7fcdbb',
    'Transition metals': '#fee090',
    'Post-transition metals': '#d9d9d9',
    'Lanthanides': '#fa9fb5',
    'Actinides': '#f768a1'
}

root = tk.Tk()
#nome = input("Digite alguma coisa ai cara")
root.title(f"Tabela Periódica do Erick")
root.configure(bg="#1e1e1e")

painel = tk.Frame(root, bg="#2d2d2d", padx=20, pady=20, width=260)
painel.grid(row=0, column=19, rowspan=10, sticky="ns", padx=10, pady=10)
painel.grid_propagate(False)

lbl_simbolo = tk.Label(painel, text="?", font=("Arial", 44, "bold"), bg="#2d2d2d", fg="white")
lbl_simbolo.pack(pady=(10, 0))

lbl_nome = tk.Label(painel, text="Clique em um elemento", font=("Arial", 14, "bold"), bg="#2d2d2d", fg="#cccccc")
lbl_nome.pack(pady=(0, 15))

lbl_info = tk.Label(painel, text="", font=("Arial", 11), bg="#2d2d2d", fg="white", justify="left")
lbl_info.pack(anchor="w")

#Separador e área de Moléculas no painel lateral
tk.Frame(painel, height=2, bg="#555555").pack(fill="x", pady=15)

tk.Label(painel, text="Analisar Molécula:", font=("Arial", 11, "bold"), bg="#2d2d2d", fg="#cccccc").pack(anchor="w")

entrada_mol = tk.Entry(painel, font=("Arial", 12), bg="#1e1e1e", fg="white", insertbackground="white")
entrada_mol.pack(fill="x", pady=5)
entrada_mol.insert(0, "Ca3(PO4)2")

lbl_mol_res = tk.Label(painel, text="", font=("Arial", 10), bg="#2d2d2d", fg="#a1d99b", justify="left")
lbl_mol_res.pack(anchor="w", pady=5)



def mostrar_detalhes(el):
    lbl_simbolo.config(text=el.get('symbol', '?'))
    lbl_nome.config(text=f"{el.get('atomic_number', '')} - {el.get('name', '')}")
    
    massa = f"{el['atomic_weight']:.3f} u" if pd.notna(el.get('atomic_weight')) else 'N/A'
    grupo = int(el['group_id']) if pd.notna(el.get('group_id')) else 'N/A'
    periodo = el.get('period', 'N/A')
    densidade = f"{el['density']} g/cm³" if pd.notna(el.get('density')) else 'N/A'
    en_pauling = el['en_pauling'] if pd.notna(el.get('en_pauling')) else 'N/A'
    econf = el.get('econf', 'N/A')
    
    texto = (
        f"Massa atômica: {massa}\n\n"
        f"Grupo: {grupo}\n"
        f"Período: {periodo}\n"
        f"Densidade: {densidade}\n"
        f"Eletronegatividade: {en_pauling}\n"
        f"Config. eletrônica:\n{econf}"
    )
    lbl_info.config(text=texto)


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





for _, el in df.iterrows():
    z = int(el['atomic_number'])
    linha = int(el['period'])
    coluna = int(el['group_id']) if pd.notna(el['group_id']) else 0

    if 57 <= z <= 71:
        linha = 8
        coluna = (z - 57) + 3
    elif 89 <= z <= 103:
        linha = 9
        coluna = (z - 89) + 3

    nome_serie = series_df.get(el.get('series_id'), '')
    cor = CORES.get(nome_serie, '#e0e0e0')
    
    btn = tk.Button(
        root,
        text=f"{z}\n{el['symbol']}",
        width=5,
        height=2,
        bg=cor,
        font=("Arial", 9, "bold"),
        command=lambda e=el: mostrar_detalhes(e)
    )
    btn.grid(row=linha, column=coluna, padx=2, pady=2)

root.mainloop()

