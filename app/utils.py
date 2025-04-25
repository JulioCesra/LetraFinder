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
    
def buscar_video_youtube(banda, musica):
    from googleapiclient.discovery import build

    api_key = 'AIzaSyCld0I_Mmy1JIIg1CeElBzGdmqJby5ILcs'  
    youtube = build("youtube", "v3", developerKey=api_key)
    
    query = f"{banda} {musica} official"
    try:
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=1
        )
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            video_id = response['items'][0]['id']['videoId']
            return f"https://www.youtube.com/watch?v={video_id}"
        else:
            return None
    except Exception as e:
        print(f"Error ao procurar o vídeo, ERRO: {e}")
        return None
