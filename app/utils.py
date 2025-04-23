from youtubesearchpython import VideosSearch

# Função responsável por buscar o vídeo atráves da biblioteca youtubesearchpython,
# retorna o primeiro elemento da url que contêm o vídeo oficial da banda de acordo com a música passada nos parâmetros. 

def buscar_video(banda, musica):
    query = f"{banda} {musica} official"
    try:
        videosSearch = VideosSearch(query, limit=1)
        return videosSearch.result()['result'][0]['link']  # formato watch?v=
    except Exception as e:
        print("Erro ao buscar vídeo:", e)
        return None



# Formata a mensagem passada (nome da banda/nome da música) para o formato aceito na lyrics api
def formatar_mensagem(string:str):
    string_separada = string.split()
    nova_string = ''
    for i in string_separada:
        nova_string += i.capitalize() + ' '
    
    return nova_string[:-1]

import requests
import re

# Utiliza a biblioteca requests para fazer a requisição na api lyrics, de forma que retorne um arquivo json que posteriormente será tratado.
# A letra da música é retornada formata para a função
def procurar_letra(nome_banda:str, nome_musica:str):
    if ' ' in nome_banda:
        nome_banda = formatar_mensagem(nome_banda)
    if ' ' in nome_musica:
        nome_musica = formatar_mensagem(nome_musica)
    
    response = requests.get(f'https://api.lyrics.ovh/v1/{nome_banda}/{nome_musica}')
    if response.status_code != 200:
        return False
    else:
        letra = response.json()
        letra = letra['lyrics']
        letra = letra.replace('\n', ' ')
        letra_formatada = re.sub(r'(?<!^)\s(?=[A-Z])', '\n', letra)
        return letra_formatada