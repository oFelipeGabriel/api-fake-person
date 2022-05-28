import requests
import json 
from bs4 import BeautifulSoup

#url = 'https://www.fakenamegenerator.com/gen-random-ninja-br.php'
url = 'https://www.fakenamegenerator.com/gen-random-tlh-br.php'
#url = 'https://www.fakenamegenerator.com/gen-random-br-br.php'

headers_dict = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36'}


def busca_pessoa():
    res = requests.get(url, headers=headers_dict)
    html_page = res.text

    soup = BeautifulSoup(html_page, 'html.parser')
    #soup.prettify()
    dados = {}

    nome = soup.find('h3').text
    dados['nome'] = nome

    endereco = soup.find('div', class_='adr').get_text(separator="<>").split("<>")

    for i, e in enumerate(endereco):
        endereco[i] = e.strip()

    dados_endereco = {}
    dados_endereco['rua'] = endereco[0]
    dados_endereco['cidade'] = endereco[1]
    dados_endereco['cep'] = endereco[2]

    dados['endereco'] = dados_endereco

    dls = soup.find_all('dl')
    for d in dls:
        texto = d.find('dt').text
        if (texto == 'Phone'):
            dados['telefone'] = d.find('dd').text
        elif (texto == 'Cadastro de Pessoas Físicas'):
            dados['cpf'] = d.find('dd').text
        elif (texto == 'Birthday'):
            dados['nascimento'] = d.find('dd').text
        elif (texto == 'Email Address'):
            email = d.find('dd').text
            dados['email'] = email.split(' ')[0]
        elif (texto == 'Tropical zodiac'):
            dados['signo'] = d.find('dd').text
        
        
    json_object = json.dumps(dados, indent=4, ensure_ascii=False) 
    return dados
