# Biblioteca
import os
from time import sleep
from requests import get
from colorama import Fore
from threading import Thread
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Modo Grafico
from tkinter import Tk, Text, Button, Scrollbar
from tkinter import messagebox


"""
# METODOS WEB
"""


def requisicao(url):

    try:

        resposta = get(url)
        if resposta.status_code == 200:
            return resposta.text

    except Exception:
        return None


def parsing_soup(file_html):

    try:
        return BeautifulSoup(file_html, "html.parser")

    except Exception:
        return None


"""
# METODOS PRINCIPAIS
"""

def titulo_mais_populares(url):

    try:
        separando_url = urlparse(url)
        caminho_url = separando_url.path.split("/")[-1]  # Captura a última parte do link

        return caminho_url.replace("-", " ").capitalize()

    except IndexError:
        return "Erro na montagem do título !"


def mais_populares(url, text_widget):

    try:

        resp_html = requisicao(url)

        if resp_html:
            soup = parsing_soup(resp_html)

            if soup:
                div = soup.find_all(name="div", class_="ld-image")
                text_widget.insert('end', f"\n{'=-=' * 5} NOTÍCIAS MAIS POPULARES {'=-=' * 5}\n")

                for i in div:
                    tag = i.find("a")
                    link = tag["href"]

                    titulo = titulo_mais_populares(link)
                    text_widget.insert('end', f"Titulo: {titulo}\nLink: {link}\n\n")

                text_widget.insert('end', f"{'=-=' * 10}\n")

    except Exception:
        text_widget.insert('end', "Erro ao pegar as notícias mais populares.\n")


def noticias_famosos(url, text_widget):

    try:
        resp_html = requisicao(url)

        if resp_html:
            soup = parsing_soup(resp_html)
            div = soup.find_all(name="div", class_="ld-info")
            text_widget.insert('end',f"\n{'=-=' * 5} NOTÍCIAS DOS FAMOSOS {'=-=' * 5}\n")

            for i in div:
                tag = i.find("a")
                links = tag["href"]
                titulo = tag.get_text()

                text_widget.insert('end', f"Titulo: {titulo}\nLinks: {links}\n\n")

            text_widget.insert('end', f"{'=-=' * 50}\n")

    except Exception:
        text_widget.insert('end', "Erro ao pegar as notícias dos famosos.\n")


def atualizar_noticias_famosos(url, text_widget):

    # Executa as notícias dos famosos em uma thread para não travar a interface
    def task():
        noticias_famosos(url, text_widget)

    Thread(target=task).start()


def atualizar_mais_populares(url, text_widget):

    # Executa as notícias mais populares em uma thread para não travar a interface
    def task():
        mais_populares(url, text_widget)

    Thread(target=task).start()


def main_gui():

    # Configuração da interface gráfica
    root = Tk()
    root.title("Notícias de Famosos e Populares")

    # Configuração da área de texto
    text_widget = Text(root, height=25, width=180)
    text_widget.pack(padx=10, pady=10)

    # Barra de rolagem
    scroll = Scrollbar(root, command=text_widget.yview)
    scroll.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scroll.set)

    # Funções para atualizar as notícias
    def on_click_famosos():

        url = "https://portalleodias.com/famosos"
        text_widget.delete(1.0, "end")  # Limpa a área de texto
        text_widget.insert('end', f"Atualizando notícias dos famosos...\n")

        atualizar_noticias_famosos(url, text_widget)

    def on_click_populares():

        url = "https://portalleodias.com/famosos"
        text_widget.delete(1.0, "end")  # Limpa a área de texto
        text_widget.insert('end', f"Atualizando notícias mais populares... \n")

        atualizar_mais_populares(url, text_widget)

    # Botões para as funções
    button_famosos = Button(root, text="Notícias dos Famosos", command=on_click_famosos)
    button_famosos.pack(pady=5)

    button_populares = Button(root, text="Mais Populares", command=on_click_populares)
    button_populares.pack(pady=5)

    # Inicia a interface gráfica
    root.mainloop()


if __name__ == '__main__':

    try:
        main_gui()

    except KeyboardInterrupt:
        print("Programa finalizado!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
