# This is a sample Python script.

import re
import threading

from funcoes_telefone import *
from urls import URL_AUTOMOVEIS

LINKS = []
TELEFONES = []

"""def resposta_busca():
    requisicao(URL_AUTOMOVEIS)
    if resposta_busca:
        soup_busca = parsing(resposta_busca)
        if soup_busca:
            LINKS = encontrar_links(soup_busca)

            THREADS = []
            for i in range(6):
                t = threading.Thread(target=descobrir_telefones)
                THREADS.append(t)

            for t in THREADS:
                t.start()

            for t in THREADS:
                t.join()


if __name__ == "__main__":
    resposta_busca()""""""