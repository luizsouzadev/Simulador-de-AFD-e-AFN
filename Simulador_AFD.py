import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttkb

class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def processa_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        for simbolo in cadeia:
            if simbolo not in self.alfabeto:
                return f"Símbolo inválido: {simbolo}"
            estado_atual = self.transicoes.get((estado_atual, simbolo))
            if estado_atual is None:
                return "Cadeia rejeitada (transição não definida)"
        return "Cadeia aceita" if estado_atual in self.estados_aceitacao else "Cadeia rejeitada"


def criar_afd():
    try:
        estados = set(entrada_estados.get().split(","))
        alfabeto = set(entrada_alfabeto.get().split(","))
        estado_inicial = entrada_estado_inicial.get()
        estados_aceitacao = set(entrada_estados_aceitacao.get().split(","))

        transicoes_raw = entrada_transicoes.get("1.0", tk.END).strip().split("\n")
        transicoes = {}
        for transicao in transicoes_raw:
            origem, simbolo, destino = transicao.split(",")
            transicoes[(origem.strip(), simbolo.strip())] = destino.strip()

        global afd
        afd = AFD(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)
        messagebox.showinfo("Sucesso", "AFD configurado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao configurar o AFD: {e}")


def testar_cadeias():
    if afd is None:
        messagebox.showerror("Erro", "Configure o AFD antes de testar cadeias.")
        return

    resultados = []
    for entrada in entradas_cadeias:
        cadeia = entrada.get()
        resultado = afd.processa_cadeia(cadeia)
        resultados.append(f"Cadeia: {cadeia} - Resultado: {resultado}\n")  

    messagebox.showinfo("Resultados", "".join(resultados))  


def adicionar_cadeia():
    nova_entrada = ttk.Entry(frame_cadeias, width=50)
    nova_entrada.pack(pady=5)
    entradas_cadeias.append(nova_entrada)


def remover_cadeia():
    if entradas_cadeias:
        ultima_entrada = entradas_cadeias.pop()
        ultima_entrada.destroy()
    else:
        messagebox.showinfo("Aviso", "Não há mais cadeias para remover.")


def mostrar_desenvolvedores():
    desenvolvedores_window = ttkb.Window(themename="superhero")
    desenvolvedores_window.title("Desenvolvedores")
    desenvolvedores_window.geometry("400x300")

    label_desenvolvedores = ttk.Label(desenvolvedores_window, text="Colaboradores do Projeto", font=("Arial", 16, "bold"))
    label_desenvolvedores.pack(pady=20)

    colaboradores = ["Nome do Colaborador 1", "Nome do Colaborador 2", "Nome do Colaborador 3"]  # Adicione os nomes dos colaboradores aqui
    for colaborador in colaboradores:
        label = ttk.Label(desenvolvedores_window, text=colaborador, font=("Arial", 14))
        label.pack(pady=5)

    botao_fechar = ttk.Button(desenvolvedores_window, text="Fechar", style="TButton", command=desenvolvedores_window.destroy)
    botao_fechar.pack(pady=20)

    desenvolvedores_window.mainloop()


# Interface Gráfica
root = ttkb.Window(themename="superhero")  # Tema moderno
root.title("Simulador de AFD")
root.geometry("800x600")
root.state('zoomed')  # Abrir em tela cheia

# Criando o Notebook (abas)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Aba 1 - Menu
menu_frame = ttk.Frame(notebook)
notebook.add(menu_frame, text="Menu")

titulo_menu = ttk.Label(menu_frame, text="Bem-vindo ao Simulador de AFD", font=("Arial", 18, "bold"))
titulo_menu.pack(pady=20)

# Aba 2 - Configuração do AFD
config_frame = ttk.Frame(notebook)
notebook.add(config_frame, text="Configurar AFD")

titulo_config = ttk.Label(config_frame, text="Configuração do AFD", font=("Arial", 18, "bold"), anchor="center")
titulo_config.pack(pady=20)

label_estados = ttk.Label(config_frame, text="Estados (separados por vírgulas):")
label_estados.pack()
entrada_estados = ttk.Entry(config_frame, width=50)
entrada_estados.pack(pady=5)

label_alfabeto = ttk.Label(config_frame, text="Alfabeto (separados por vírgulas):")
label_alfabeto.pack()
entrada_alfabeto = ttk.Entry(config_frame, width=50)
entrada_alfabeto.pack(pady=5)

label_estado_inicial = ttk.Label(config_frame, text="Estado Inicial:")
label_estado_inicial.pack()
entrada_estado_inicial = ttk.Entry(config_frame, width=50)
entrada_estado_inicial.pack(pady=5)

label_estados_aceitacao = ttk.Label(config_frame, text="Estados de Aceitação (separados por vírgulas):")
label_estados_aceitacao.pack()
entrada_estados_aceitacao = ttk.Entry(config_frame, width=50)
entrada_estados_aceitacao.pack(pady=5)

label_transicoes = ttk.Label(config_frame, text="Transições (formato: origem,símbolo,destino por linha):")
label_transicoes.pack()
entrada_transicoes = tk.Text(config_frame, width=50, height=8, font=("Arial", 12))
entrada_transicoes.pack(pady=5)

botao_configurar = ttk.Button(config_frame, text="Configurar AFD", style="TButton", command=criar_afd)
botao_configurar.pack(pady=10)



# Aba 4 - Teste de Cadeias
teste_frame = ttk.Frame(notebook)
notebook.add(teste_frame, text="Teste de Cadeias")

titulo_teste = ttk.Label(teste_frame, text="Teste de Cadeias", font=("Arial", 18, "bold"))
titulo_teste.pack(pady=20)

frame_cadeias = ttk.Frame(teste_frame)
frame_cadeias.pack(pady=10)

entradas_cadeias = []

botao_adicionar = ttk.Button(teste_frame, text="Adicionar Cadeia", style="TButton", command=adicionar_cadeia)
botao_adicionar.pack(pady=5)

botao_remover = ttk.Button(teste_frame, text="Remover Cadeia", style="TButton", command=remover_cadeia)
botao_remover.pack(pady=5)

botao_testar = ttk.Button(teste_frame, text="Testar Cadeias", style="TButton", command=testar_cadeias)
botao_testar.pack(pady=20, side=tk.BOTTOM)

# Aba 3 - Desenvolvedores
desenvolvedores_frame = ttk.Frame(notebook)
notebook.add(desenvolvedores_frame, text="Desenvolvedores")

titulo_desenvolvedores = ttk.Label(desenvolvedores_frame, text="Colaboradores do Projeto", font=("Arial", 18, "bold"))
titulo_desenvolvedores.pack(pady=20)

colaboradores = ["LUIZ FELIPE DA COSTA SOUZA", "LUIZ HENRIQUE ALVES FERREIRA", "NEFI ANGELO DIAS DA COSTA", "VINICIUS EDUARDO FREITAS DE SALES", "GABRIEL FILIPE DA SILVA FERNANDES"]
for colaborador in colaboradores:
    label = ttk.Label(desenvolvedores_frame, text=colaborador, font=("Arial", 14))
    label.pack(pady=5)

    
# Inicializar o AFD como None
afd = None

# Rodar a interface
root.mainloop()
