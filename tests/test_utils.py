import app.utils
import pytest
def test_procurar_letra():
    assert app.utils.procurar_letra(nome_banda='Guns n roses', nome_musica='November Rain')
    assert app.utils.procurar_letra(nome_banda=2, nome_musica=3)

def test_formatar_mensagem():
    assert app.utils.formatar_mensagem('Olá meu nome é Julio')
    assert app.utils.formatar_mensagem('Olá meu nome é Carlos')
    assert app.utils.formatar_mensagem('Olá meu nome é 124')
    assert app.utils.formatar_mensagem(134)
    
def test_buscar_video():
    assert app.utils.buscar_video(banda='Guns and roses',musica='November rain')