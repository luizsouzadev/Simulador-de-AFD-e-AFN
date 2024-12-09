import tkinter as tk
from tkinter import ttk, messagebox

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
            estado_atual = self.transicoes.get((estado_atual, simbolo))
            if estado_atual is None:
                return "Cadeia rejeitada"
        return "Cadeia aceita" if estado_atual in self.estados_aceitacao else "Cadeia rejeitada"

class AFND:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def processa_cadeia(self, cadeia):
        def epsilon_closure(estados):
            """Calcula o fecho-ε dos estados fornecidos."""
            stack = list(estados)
            closure = set(estados)

            while stack:
                estado = stack.pop()
                for prox_estado in self.transicoes.get((estado, ""), []):
                    if prox_estado not in closure:
                        closure.add(prox_estado)
                        stack.append(prox_estado)

            return closure

        def processar(estados_atuais, cadeia_restante):
            if not cadeia_restante:
                return any(estado in self.estados_aceitacao for estado in estados_atuais)

            simbolo = cadeia_restante[0]
            proximos_estados = set()

            for estado in estados_atuais:
                proximos_estados.update(self.transicoes.get((estado, simbolo), []))

            if not proximos_estados:
                return False

            proximos_estados = epsilon_closure(proximos_estados)
            return processar(proximos_estados, cadeia_restante[1:])

        estados_iniciais = epsilon_closure({self.estado_inicial})
        return "Cadeia aceita" if processar(estados_iniciais, cadeia) else "Cadeia rejeitada"

# Interface gráfica com Tkinter
def criar_automato():
    try:
        estados = entry_estados.get().split(",")
        alfabeto = entry_alfabeto.get().split(",")
        estado_inicial = entry_estado_inicial.get()
        estados_aceitacao = entry_estados_aceitacao.get().split(",")

        transicoes_raw = text_transicoes.get("1.0", tk.END).strip().split("\n")
        transicoes = {}
        tipo = tipo_automato.get()

        for transicao in transicoes_raw:
            origem, simbolo, destinos = transicao.split(",")
            origem = origem.strip()
            simbolo = simbolo.strip()
            destinos = destinos.strip()

            if tipo == "AFD":
                # Certifique-se de que apenas um destino seja atribuído
                if ";" in destinos:
                    raise ValueError("No AFD, cada transição deve ter exatamente um destino.")
                transicoes[(origem, simbolo)] = destinos
            elif tipo == "AFND":
                # Permita múltiplos destinos para AFND
                transicoes.setdefault((origem, simbolo), []).extend(destinos.split(";"))

        global automato
        if tipo == "AFD":
            automato = AFD(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)
        elif tipo == "AFND":
            automato = AFND(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)

        messagebox.showinfo("Sucesso", f"{tipo} configurado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao configurar o automato: {e}")

def processar_cadeia():
    try:
        cadeia = entry_cadeia.get()
        resultado = automato.processa_cadeia(cadeia)
        messagebox.showinfo("Resultado", resultado)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar a cadeia: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Simulador de AFD e AFND")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Entrada de estados
label_estados = ttk.Label(frame, text="Estados (separados por vírgula):")
label_estados.grid(row=0, column=0, sticky=tk.W)
entry_estados = ttk.Entry(frame, width=30)
entry_estados.grid(row=0, column=1, sticky=tk.W)

# Entrada do alfabeto
label_alfabeto = ttk.Label(frame, text="Alfabeto (separado por vírgula):")
label_alfabeto.grid(row=1, column=0, sticky=tk.W)
entry_alfabeto = ttk.Entry(frame, width=30)
entry_alfabeto.grid(row=1, column=1, sticky=tk.W)

# Estado inicial
label_estado_inicial = ttk.Label(frame, text="Estado inicial:")
label_estado_inicial.grid(row=2, column=0, sticky=tk.W)
entry_estado_inicial = ttk.Entry(frame, width=30)
entry_estado_inicial.grid(row=2, column=1, sticky=tk.W)

# Estados de aceitação
label_estados_aceitacao = ttk.Label(frame, text="Estados finais (separados por vírgula):")
label_estados_aceitacao.grid(row=3, column=0, sticky=tk.W)
entry_estados_aceitacao = ttk.Entry(frame, width=30)
entry_estados_aceitacao.grid(row=3, column=1, sticky=tk.W)

# Tipo de automato
label_tipo = ttk.Label(frame, text="Tipo de Autômato:")
label_tipo.grid(row=4, column=0, sticky=tk.W)
tipo_automato = ttk.Combobox(frame, values=["AFD", "AFND"], state="readonly")
tipo_automato.grid(row=4, column=1, sticky=tk.W)
tipo_automato.set("AFD")

# Transições
label_transicoes = ttk.Label(frame, text="Transições (origem,símbolo,destino;destino2):")
label_transicoes.grid(row=5, column=0, sticky=tk.W)
text_transicoes = tk.Text(frame, height=5, width=40)
text_transicoes.grid(row=5, column=1, sticky=tk.W)

# Botão para criar o autômato
button_criar = ttk.Button(frame, text="Criar Autômato", command=criar_automato)
button_criar.grid(row=6, column=0, columnspan=2)

# Entrada de cadeia
label_cadeia = ttk.Label(frame, text="Cadeia a ser processada:")
label_cadeia.grid(row=7, column=0, sticky=tk.W)
entry_cadeia = ttk.Entry(frame, width=30)
entry_cadeia.grid(row=7, column=1, sticky=tk.W)

# Botão para processar a cadeia
button_processar = ttk.Button(frame, text="Processar Cadeia", command=processar_cadeia)
button_processar.grid(row=8, column=0, columnspan=2)

root.mainloop()
