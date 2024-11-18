import streamlit as st
from agents.youtube_extractor import YoutubeExtractorAgent
from agents.translator_agent import TranslatorAgent
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
    
    # Inicializa os agentes
    extractor = YoutubeExtractorAgent()
    translator = TranslatorAgent()
    
    # Área de entrada da URL
    url = st.text_input(
        "Cole a URL do vídeo do YouTube aqui:",
        placeholder="https://www.youtube.com/watch?v=..."
    )
    
    # Botão de processar
    if st.button("Processar Vídeo", type="primary"):
        if url:
            # Extração das legendas
            with st.spinner("Extraindo legendas do vídeo..."):
                transcript, filepath = extractor.get_transcript(url)
                
                if filepath:
                    st.success("Legendas extraídas com sucesso!")
                    
                    # Tradução
                    with st.spinner("Traduzindo para português..."):
                        translated_text, error = translator.translate_text(transcript)
                        
                        if translated_text:
                            # Salva a tradução
                            translated_filepath = translator.save_translation(
                                translated_text, 
                                filepath
                            )
                            
                            st.success("Tradução concluída!")
                            
                            # Exibe os resultados em colunas
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.subheader("Texto Original")
                                with st.expander("Ver texto original", expanded=True):
                                    st.markdown(f"""
                                    <div class="output-container">
                                        <p>{transcript}</p>
                                    </div>
                                    """, unsafe_allow_html=True)
                                    
                                    with open(filepath, 'r', encoding='utf-8') as file:
                                        st.download_button(
                                            label="⬇️ Download Original",
                                            data=file,
                                            file_name=os.path.basename(filepath),
                                            mime="text/plain"
                                        )
                            
                            with col2:
                                st.subheader("Texto Traduzido")
                                with st.expander("Ver tradução", expanded=True):
                                    st.markdown(f"""
                                    <div class="output-container">
                                        <p>{translated_text}</p>
                                    </div>
                                    """, unsafe_allow_html=True)
                                    
                                    with open(translated_filepath, 'r', encoding='utf-8') as file:
                                        st.download_button(
                                            label="⬇️ Download Tradução",
                                            data=file,
                                            file_name=os.path.basename(translated_filepath),
                                            mime="text/plain"
                                        )
                        else:
                            st.error(f"Erro na tradução: {error}")
                else:
                    st.error("Não foi possível extrair as legendas.")
                    st.code(transcript)
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