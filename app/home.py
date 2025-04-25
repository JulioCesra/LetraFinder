import streamlit as st
import utils

class LetraFinder:

    st.set_page_config(
    page_title="LetraFinder",       
    page_icon="🎵",
    )

    descricao_site = st.container()
    descricao_site.title(":blue[LetraFinder]")
    descricao_site.write("Encontre, escute e baixe a letra da sua música favorita!")

    entrada_informacaoes = st.container(border=True)
    entrada_informacaoes.write("Digite o nome da música e da banda para encontrar a letra.")
    banda = entrada_informacaoes.text_input('Nome da Banda')
    musica = entrada_informacaoes.text_input('Nome da Música')
    opcoes = entrada_informacaoes.selectbox(label='Selecione uma das opções',options=['Buscar Letra','Buscar vídeo oficial','Baixar Letra'])
    get_informacoes = st.container(border=True)
    if utils.procurar_letra(banda,musica) == False:
        st.warning('Não foi possível encontrar as informações fornecidas!')
    else:
        if opcoes == 'Buscar Letra':
            if banda and musica:
                letra = utils.procurar_letra(banda, musica)
                get_informacoes.text('Letra da Música:')
                get_informacoes.text(letra)    
            else:
                st.warning('Coloque todas as informações necessárias!')
        elif opcoes == 'Buscar vídeo oficial':
            if banda and musica:
                url = utils.buscar_video_youtube(banda,musica)
                get_informacoes.link_button(label='Visualizar vídeo',
                                            url=url)
            else:
                st.warning('Coloque todas as informações necessárias!')
        elif opcoes == 'Baixar Letra':
            if banda and musica:
                get_informacoes.download_button(data=utils.procurar_letra(banda,musica),label='Confirmar Download', file_name=f'{banda}_{musica}.txt', mime='text/plain')
            else:
                st.warning('Coloque todas as informações necessárias!')
        else:   
            st.warning("Escolha uma das opções")
