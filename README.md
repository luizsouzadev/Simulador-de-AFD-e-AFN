# Simulador de AFD (Autômato Finito Determinístico)

Este projeto é um simulador de Autômatos Finitos Determinísticos (AFD) desenvolvido em Python utilizando a biblioteca `Tkinter` e o framework `ttkbootstrap`. O aplicativo permite ao usuário configurar um AFD, testar cadeias de entrada e visualizar os resultados de forma interativa. O sistema é dividido em várias páginas, permitindo uma navegação fácil entre as diferentes funcionalidades.

## Funcionalidades

### 1. **Configuração do AFD**
   - O usuário pode definir os **estados**, **alfabeto**, **estado inicial**, **estados de aceitação** e as **transições** do AFD.
   - O AFD é configurado dinamicamente com base nas entradas fornecidas pelo usuário.

### 2. **Testar Cadeias**
   - O usuário pode adicionar várias cadeias de caracteres para testar o AFD.
   - O sistema processa cada cadeia e retorna se a cadeia é **aceita** ou **rejeitada** pelo autômato.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para o desenvolvimento do simulador.
- **Tkinter**: Biblioteca gráfica utilizada para a interface do usuário.
- **ttkbootstrap**: Biblioteca para dar uma aparência moderna à interface, com temas e estilos aprimorados.

## Pré-requisitos

Antes de executar o projeto, você precisa ter o **Python** instalado em sua máquina.

### Instalar dependências

Após instalar o Python, você pode instalar as dependências do projeto. No terminal, navegue até o diretório do projeto e execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install ttkbootstrap
```
### Execução do Arquivo

```bash
python main.py
```

