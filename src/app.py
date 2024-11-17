import streamlit as st
from agents.youtube_extractor import YoutubeExtractorAgent
import os

# Configuração da página
st.set_page_config(
    page_title="YouTube Content Analyzer",
    page_icon="🎥",
    layout="wide"
)

# Estilo CSS atualizado
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
        color: #31333F;
        border: 1px solid #ccc;
    }
    .output-container {
        background-color: #f0f2f6;
        color: #31333F;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stTextInput > div > div > input::placeholder {
        color: #666;
    }
    .stMarkdown {
        color: #31333F;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Título principal
    st.title("🎥 YouTube Content Analyzer")
    st.markdown("---")
    
    # Área de entrada da URL
    url = st.text_input(
        "Cole a URL do vídeo do YouTube aqui:",
        placeholder="https://www.youtube.com/watch?v=..."
    )
    
    # Botão de processar
    if st.button("Extrair Legendas", type="primary"):
        if url:
            with st.spinner("Extraindo legendas do vídeo..."):
                try:
                    # Inicializa o agente
                    extractor = YoutubeExtractorAgent()
                    
                    # Extrai e salva as legendas
                    transcript, filepath = extractor.get_transcript(url)
                    
                    if filepath:
                        # Exibe o sucesso
                        st.success("Legendas extraídas com sucesso!")
                        
                        # Container para a saída
                        with st.expander("Ver Transcrição", expanded=True):
                            st.markdown(f"""
                            <div class="output-container">
                                <p>{transcript}</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                        # Informações do arquivo
                        st.info(f"📁 Arquivo salvo em: {filepath}")
                        
                        # Botão para download
                        with open(filepath, 'r', encoding='utf-8') as file:
                            st.download_button(
                                label="⬇️ Download Transcrição",
                                data=file,
                                file_name=os.path.basename(filepath),
                                mime="text/plain"
                            )
                    else:
                        st.error("Não foi possível extrair as legendas.")
                        st.code(transcript)  # Mostra a mensagem de erro
                        
                except Exception as e:
                    st.error(f"Erro ao processar o vídeo: {str(e)}")
        else:
            st.warning("Por favor, insira uma URL do YouTube.")
    
    # Rodapé
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Desenvolvido com ❤️ usando Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()