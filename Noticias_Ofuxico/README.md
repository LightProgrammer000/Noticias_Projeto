# Relatório - **Extrator de Links - Ofuxico**

## Objetivo

O objetivo deste projeto é criar uma ferramenta em Python para extrair links de uma página web específica, neste caso, o site `https://ofuxico.com.br/`. A ferramenta busca links presentes na página, extraí-los e exibi-los de forma organizada através de uma interface gráfica construída com a biblioteca `Tkinter`. Para a requisição e análise da página, são utilizadas as bibliotecas `requests` e `BeautifulSoup`.

## Funcionalidades

O programa possui as seguintes funcionalidades:

- **Requisição HTTP**: Realiza uma requisição para o site `https://ofuxico.com.br/`.
- **Extração de Links**: Extrai links e seus títulos a partir do conteúdo HTML utilizando `BeautifulSoup`.
- **Exibição de Resultados**: Exibe os links encontrados, com seus respectivos títulos e descrições, em uma interface gráfica.
- **Barra de Rolagem**: Permite rolar o conteúdo caso os links encontrados sejam numerosos ou longos.
- **Interface Gráfica Centralizada**: A janela é centralizada na tela para uma melhor experiência do usuário.

## Tecnologias Utilizadas

Este projeto utiliza as seguintes tecnologias e bibliotecas:

- **Python 3.x**: Linguagem utilizada para o desenvolvimento do programa.
- **Tkinter**: Biblioteca para criação da interface gráfica.
- **Requests**: Biblioteca para realizar as requisições HTTP.
- **BeautifulSoup (bs4)**: Biblioteca para fazer o parsing (análise) do HTML.
- **Colorama**: Biblioteca para adicionar cores ao terminal (não usada diretamente na interface gráfica).

## Instalação

Para rodar o programa, é necessário instalar as dependências. Siga os passos abaixo:

### 1. Clone ou baixe o código

Se você ainda não tem o repositório, pode clonar ou baixar os arquivos do código.

```bash
git clone https://seu-repositorio.git
