# Bibliotecas
from requests import get
from colorama import Fore
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Bibliotecas - Grafico
import tkinter as tk
from tkinter import messagebox


# Função para fazer a requisição HTTP
def requisicao(url):

    try:
        resp_html = get(url)

        if resp_html.status_code == 200:
            return resp_html.text

    except Exception:
        messagebox.showerror("Erro", "Erro na requisição!")

    return None


# Função para fazer o parsing do HTML com BeautifulSoup
def parsing_soup(resp_html):

    try:
        return BeautifulSoup(resp_html, "html.parser")

    except Exception:
        messagebox.showerror("Erro", "Erro ao fazer o parsing da página!")

    return None


# Função para formatar o link
def formatar_link(link):

    try:
        partes = urlparse(link)
        caminho = partes[2].strip("/").split("/")[-1]
        fmt = caminho.replace("-", " ").capitalize()
        return fmt

    except Exception:
        return "Erro ao formatar o link"


# Função para encontrar os links e seus títulos na página
def encontrar_link(soup):

    result = ""

    try:
        div = soup.find_all("div", class_="box-post")

        for i in div:
            links = i.find("a")
            alts = i.find("img")

            if links and alts:
                alt = alts["alt"]
                link = links["href"]
                titulo = formatar_link(link)

                result += f"Tema: {alt}\n"
                result += f"Título: {titulo}\n"
                result += f"Link: {link}\n\n"

        if not result:
            result = "Nenhum link encontrado!"

    except Exception:
        result = "Erro ao encontrar links!"

    return result


# Função para ser chamada ao pressionar o botão
def processar():

    url = "https://ofuxico.com.br/"  # URL fixa
    resp_html = requisicao(url)

    if resp_html:
        soup = parsing_soup(resp_html)

        if soup:
            resultado = encontrar_link(soup)
            text_resultado.delete(1.0, tk.END)  # Limpa o campo de texto antes de exibir o novo resultado
            text_resultado.insert(tk.END, resultado)  # Exibe o resultado no campo de texto


# Criando a janela principal
root = tk.Tk()
root.title("Extrator de Links")

# Definir o tamanho da janela para ocupar uma área maior e ser centralizada
root.geometry("800x600")  # Janela maior
root.resizable(True, True)  # Permite redimensionar

# Centralizando a janela na tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1500
window_height = 600

# Calculando as coordenadas para centralizar
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Label para mostrar o que está acontecendo
label_status = tk.Label(root, text="Buscando links em 'https://ofuxico.com.br/'", font=("Arial", 12))
label_status.pack(pady=10)

# Botão para processar
button_processar = tk.Button(root, text="Buscar Links", command=processar)
button_processar.pack(pady=10)

# Criando um frame para conter o campo de texto e a barra de rolagem
frame_texto = tk.Frame(root)
frame_texto.pack(pady=10)

# Campo de texto para exibir o resultado com mais largura e altura
text_resultado = tk.Text(frame_texto, width=180, height=60)  # Aumentei a largura e altura
text_resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de rolagem associada ao campo de texto
scrollbar = tk.Scrollbar(frame_texto, command=text_resultado.yview)  # Barra de rolagem vertical
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Conectar a barra de rolagem ao campo de texto
text_resultado.config(yscrollcommand=scrollbar.set)

# Iniciar a interface gráfica
root.mainloop()