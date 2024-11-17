from agents.youtube_extractor import YoutubeExtractorAgent

def main():
    # Substitua esta URL por uma URL válida do YouTube
    video_url = "https://youtu.be/fafbRw39QVw"
    
    print(f"Iniciando extração do vídeo: {video_url}")
    
    # Inicializa o agente
    extractor = YoutubeExtractorAgent()
    
    # Extrai e salva as legendas
    transcript, filepath = extractor.get_transcript(video_url)
    
    if filepath:
        print(f"\nLegendas extraídas e salvas em: {filepath}")
        print("\nPrimeiros 200 caracteres da transcrição:")
        print(transcript[:200] + "...")
    else:
        print("\nErro ao processar o vídeo:")
        print(transcript)  # Agora vai mostrar a mensagem de erro detalhada

if __name__ == "__main__":
    main()