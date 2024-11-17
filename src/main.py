from agents.youtube_extractor import YoutubeExtractorAgent

def main():
    # URL de exemplo (você pode trocar por qualquer vídeo do YouTube que tenha legendas)
    video_url = "https://youtu.be/fafbRw39QVw"
    
    # Inicializa o agente
    extractor = YoutubeExtractorAgent()
    
    # Extrai as legendas
    transcript = extractor.get_transcript(video_url)
    
    # Imprime o resultado
    print("Legendas extraídas:")
    print(transcript)

if __name__ == "__main__":
    main()