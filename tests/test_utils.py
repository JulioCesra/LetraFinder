import app.utils
import pytest

def test_procurar_letra():
    assert app.utils.procurar_letra(nome_banda='Guns n roses', nome_musica='November Rain')
    assert app.utils.procurar_letra(nome_banda='Legião Urbana', nome_musica='Pais e filhos')

def test_formatar_mensagem():
    assert app.utils.formatar_mensagem('Olá meu nome é Julio')
    assert app.utils.formatar_mensagem('Olá meu nome é Carlos')
    assert app.utils.formatar_mensagem('Olá meu nome é 124')
    assert app.utils.formatar_mensagem('teste')
    
def test_buscar_video_youtube():
    assert app.utils.buscar_video_youtube("Red Hot Chili Peppers", "Californication")
