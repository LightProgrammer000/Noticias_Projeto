# Bibliotecas
from requests import get
from colorama import Fore
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# Função para fazer a requisição HTTP
def requisicao(url):
    try:
        resp_html = get(url)  # Faz a requisição HTTP
        if resp_html.status_code == 200:  # Verifica se a resposta é bem-sucedida
            return resp_html.text  # Retorna o conteúdo HTML
    except Exception:
        print(f"{Fore.LIGHTYELLOW_EX} Erro na requisicao !{Fore.RESET}")  # Erro na requisição
    return None  # Retorna None caso haja erro


# Função para fazer o parsing do HTML com BeautifulSoup
def parsing_soup(resp_html):
    try:
        return BeautifulSoup(resp_html, "html.parser")  # Retorna o objeto BeautifulSoup
    except Exception:
        print(f"{Fore.LIGHTYELLOW_EX} Erro no Parsing Soup !{Fore.RESET}")  # Erro no parsing


# Função para formatar o link
def formatar_link(link):
    try:
        partes = urlparse(link)  # Divide a URL em partes
        caminho = partes[2].strip("/").split("/")[-1]  # Pega a última parte do caminho da URL
        fmt = caminho.replace("-", " ").capitalize()  # Formata o título do link
        return fmt  # Retorna o título formatado
    except Exception as e:
        print(e)  # Erro ao formatar o link


# Função para encontrar os links e seus títulos na página
def encontrar_link(soup):
    try:
        div = soup.find_all("div", class_="box-post")  # Encontra todas as divs com a classe 'box-post'

        for i in div:
            links = i.find("a")  # Encontra o link
            alts = i.find("img")  # Encontra a imagem

            if links:
                alt = alts["alt"]  # Pega o texto alternativo da imagem
                link = links["href"]  # Pega o link
                titulo = formatar_link(link)  # Formata o título do link

                # Exibe os dados formatados
                print(f"{Fore.LIGHTYELLOW_EX}Tema: {Fore.RESET}{Fore.LIGHTMAGENTA_EX}{alt}{Fore.RESET}")
                print(f"{Fore.LIGHTCYAN_EX}Titulo: {Fore.RESET}{Fore.LIGHTWHITE_EX}{titulo}{Fore.RESET}")
                print(f"{Fore.LIGHTGREEN_EX}Link: {Fore.RESET}{link}\n")

    except Exception:
        print(f"{Fore.LIGHTYELLOW_EX} Erro ao encontrar Links ! {Fore.RESET}")  # Erro ao encontrar links

    return None


# Função principal
def main():
    url = "https://ofuxico.com.br/"  # URL a ser acessada
    try:
        resp_html = requisicao(url)  # Faz a requisição
        if resp_html:
            soup = parsing_soup(resp_html)  # Faz o parsing do HTML
            if soup:
                encontrar_link(soup)  # Encontra e exibe os links e títulos

    except Exception:
        print(f"{Fore.LIGHTYELLOW_EX} Erro de conexao !{Fore.RESET}")  # Erro de conexão


# Execução do script
if __name__ == '__main__':
    main()  # Chama a função principal
