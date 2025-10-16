# Bibliotecas
from requests import get
from colorama import Fore
from threading import Thread
from bs4 import BeautifulSoup

# Usando um set global para armazenar links e evitar duplicação
LINKS_VISITADOS = set()

# Web Request
def requisicao(url):

    try:
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/58.0.3029.110 Safari/537.36'
        }

        resp = get(url, headers=headers)

        if resp.status_code == 200:
            return resp.text

    except Exception:
        print(f"{Fore.RED}Erro ao acessar o site: Status Code {resp.status_code}{Fore.RESET}")

    return None


# Soup
def parsing_soup(html):

    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    except Exception:
        print(f"{Fore.RED}Erro no parsing do HTML {Fore.RESET}")
        return None


# Captura links de uma página
def capturar_links(soup, base_url="https://portalleodias.com"):

    try:
        links = set()
        noticias = soup.find_all("a")

        # Extraímos os links que começam com a URL base fornecida
        for i in noticias:

            link = i.get("href")

            if link and link.startswith(base_url):
                links.add(link)

        return links

    except Exception as e:
        print(e)

    return None

# Função para processar a página, capturar links e seguir links encontrados
def processar_pagina(url):

    try:

        # Evita processar URLs duplicadas
        if url in LINKS_VISITADOS:
            return

        else:

            # Marca o link como visitado
            print(f"{Fore.CYAN}Processando: {url}{Fore.RESET}")
            LINKS_VISITADOS.add(url)

            html = requisicao(url)

            if html:
                soup = parsing_soup(html)

                if soup:
                    links_encontrados = capturar_links(soup)

                    if links_encontrados:

                        # Para cada link encontrado, criamos uma nova thread para processá-lo
                        for i in links_encontrados:

                            # Cria uma nova thread para processar o próximo link
                            t = Thread(target=processar_pagina, args=(i,))
                            t.start()

    except Exception:
        print("Erro")


# Função principal que inicia o processamento
def main():

    try:
        url = 'https://portalleodias.com'

        # Inicia o processamento da página inicial
        processar_pagina(url)


    except Exception:
        pass


# Execução
if __name__ == '__main__':
    main()
