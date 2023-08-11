from bs4 import BeautifulSoup
from urls import *

def encontrar_telefone(soup):
    try:
        descricao = soup.find_all("div", class_="sixteen wide column")[2].p.get_text().strip()
    except:
        print("Erro ao encontrar descrição")
        return None

    regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}?(9[ -\.]?\d{4})[ \-\.]?(\d{4})", descricao)
    if regex:
        return regex