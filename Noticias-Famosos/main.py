# Bibliotecas
import os
from time import sleep
from requests import get
from colorama import Fore
from threading import Thread
from bs4 import BeautifulSoup
from urllib.parse import urlparse

"""
# METODOS WEB
"""

def requisicao(url):

    try:
        resposta = get(url)

        if resposta.status_code == 200:
            file_html = resposta.text

            return file_html

    except Exception:
        print(f"Erro na requisicao !")


def parsing_soup(file_html):

    try:
        soup = BeautifulSoup(file_html, "html.parser")
        return soup

    except Exception:
        print(f"Erro no parsing !")

"""
# METODOS PRINCIPAIS
"""

def titulo_mais_populares(url):

    try:
        # Decompor URL: Dominio, Caminho, Parametros, etc.
        separando_url = urlparse(url)
        caminho_url = separando_url.path.split("/")[-1] # Capturar a ultima parte do link
        formatar = caminho_url.replace("-", " ")
        titulo = formatar.capitalize()

        return titulo

    except IndexError:
        print("Erro na montagem do titulo !")

    return None


def mais_populares(url):

    try:
        resp_html = requisicao(url)

        if resp_html:
            soup = parsing_soup(resp_html)

            if soup:
                div = soup.find_all(name="div", class_="ld-image")

                print(f"\n{'=-=' * 10}{Fore.LIGHTGREEN_EX} NOTICIAS MAIS POPULARES {Fore.RESET}{'=-=' * 10} \n")

                for i in div:
                    tag = i.find("a")

                    # Montagem das informacoes
                    link = tag["href"]
                    titulo = titulo_mais_populares(link)

                    print(f"Titulo: {titulo}")
                    print(f"Link: {link}\n")

                print(f"{'=-=' * 50}\n")

    except Exception:
        pass


def noticias_famosos(url):

    try:

        resp_html = requisicao(url)

        if resp_html:
            soup = parsing_soup(resp_html)

            div = soup.find_all(name="div", class_="ld-info")

            print(f"\n{'=-=' * 10}{Fore.LIGHTRED_EX} NOTICIAS DOS FAMOSOS {Fore.RESET}{'=-=' * 10} \n")

            for i in div:
                tag = i.find("a")

                links = tag["href"]
                titulo = tag.get_text()

                print(f"Titulo: {titulo}")
                print(f"Links: {links}\n")

            print(f"{'=-=' * 50}\n")

    except Exception:
        pass


def main():

    try:
        url = "https://portalleodias.com/famosos"

        while True:

            t1 = Thread(target=mais_populares(url))
            t1.start()

            t2 = Thread(target=noticias_famosos(url))
            t2.start()

            print(f"{Fore.LIGHTYELLOW_EX} Proxima atualizacao em 10 minutos {Fore.RESET}")
            sleep(60 * 10)

    except KeyboardInterrupt:
        print("Programa Finalizao !")

    except Exception:
        pass


if __name__ == '__main__':
    main()