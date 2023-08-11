from bs4 import BeautifulSoup

def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, "html.parser")
        return soup
    except Exception as error:
        print("Erro ao fazer o parsing HTML")
        print(error)