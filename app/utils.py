from googleapiclient.discovery import build

acesso_api_youtube = 'AIzaSyCld0I_Mmy1JIIg1CeElBzGdmqJby5ILcs'

# Função responsável por buscar o vídeo no youtube
def buscar_video_youtube(banda, musica):
    youtube = build('youtube', 'v3', developerKey=acesso_api_youtube)
    
    query = f"{banda} {musica} official"
    try:
        request = youtube.search().list(part="snippet",q=query,type="video",maxResults=1)
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            return f"https://www.youtube.com/watch?v={response['items'][0]['id']['videoId']}"
        else:
            print("Nenhum vídeo encontrado.")
            return None
    except Exception as e:
        print(f"Erro ao buscar vídeo: {e}")
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