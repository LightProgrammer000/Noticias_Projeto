# Bibliotecas
from requests import get
from colorama import Fore
from threading import Thread
from bs4 import BeautifulSoup


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

    links = set()
    noticias = soup.find_all("a")

    # Extraímos os links que começam com a URL base fornecida
    for i in noticias:

        link = i.get("href")

        if link and link.startswith(base_url):
            links.add(link)

    return links


# Relatorio
def relatorio(links):

    print(f"\n{Fore.LIGHTYELLOW_EX}{'=-=' * 10} PORTAL LEO DIAS {'=-=' * 10}{Fore.RESET}")
    for i in sorted(links):
        print(f"Links: {i}")


# Função principal que inicia o processamento
def main():

    try:
        relatorio(capturar_links(parsing_soup(requisicao("https://portalleodias.com"))))

    except Exception as e:
        print(e)

# Execução
if __name__ == '__main__':
    main()
