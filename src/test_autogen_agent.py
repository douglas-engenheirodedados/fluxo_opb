from agents.autogen_youtube_agent import YouTubeAgent
import json

def test_youtube_agent():
    # Inicializa o agente
    agent = YouTubeAgent()
    
    # URL de teste
    video_url = "https://youtu.be/fafbRw39QVw"
    
    print("🎥 Iniciando processamento do vídeo...")
    
    # Processa o vídeo
    result = agent.process_video(video_url)
    
    # Exibe o resultado
    print("\n📋 Resultado do processamento:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    if result["status"] == "success":
        print(f"\n✅ Legendas salvas em: {result['filepath']}")
        print("\n📝 Primeiros 200 caracteres da transcrição:")
        print(result["text"][:200] + "...")
    else:
        print(f"\n❌ Erro: {result['error']}")

if __name__ == "__main__":
    test_youtube_agent()