# src/agents/autogen_youtube_agent.py

import os
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
from datetime import datetime
from typing import Dict, Any, List
import autogen  # Certifique-se de que a biblioteca AutoGen está instalada

# Carrega as variáveis de ambiente
load_dotenv()

class YouTubeTranscriptTool:
    def get_transcript(self, video_url: str) -> Dict[str, Any]:
        """Extrai a transcrição de um vídeo do YouTube"""
        try:
            video_id = self.extract_video_id(video_url)
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return {
                "status": "success",
                "timestamp": datetime.now().isoformat(),
                "video_id": video_id,
                "transcript": transcript
            }
        except Exception as e:
            return {
                "status": "error",
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            }

    def extract_video_id(self, video_url: str) -> str:
        """Extrai o ID do vídeo da URL"""
        if "v=" in video_url:
            return video_url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in video_url:
            return video_url.split("youtu.be/")[-1].split("?")[0]
        else:
            raise ValueError("URL do vídeo inválida")

class YouTubeAgent:
    def __init__(self):
        self.tool = YouTubeTranscriptTool()

    def process_video(self, video_url: str) -> Dict[str, Any]:
        """Processa um vídeo do YouTube e retorna a transcrição"""
        result = self.tool.get_transcript(video_url)
        return result

class TranslationAgent:
    def __init__(self, llm_model):
        self.llm_model = llm_model

    def translate_text(self, text: str, target_language: str) -> str:
        """Traduza o texto para o idioma alvo usando LLM"""
        # Aqui você deve integrar a chamada para a LLM
        # Exemplo fictício de chamada à LLM
        translated_text = self.llm_model.translate(text, target_language)
        return translated_text

# Exemplo de uso com AutoGen
if __name__ == "__main__":
    video_url = "https://youtu.be/fafbRw39QVw"  # Substitua pelo URL do vídeo desejado

    # Inicializa os agentes
    youtube_agent = YouTubeAgent()
    llm_model = autogen.LLMModel()  # Inicialize seu modelo LLM aqui
    translation_agent = TranslationAgent(llm_model)

    # Extraindo a transcrição
    result = youtube_agent.process_video(video_url)
    if result["status"] == "success":
        transcript = " ".join([entry['text'] for entry in result["transcript"]])
        print("Transcrição extraída com sucesso!")

        # Traduzindo a transcrição
        translated_text = translation_agent.translate_text(transcript, "PT-BR")
        print("Texto traduzido:", translated_text)
    else:
        print(f"Erro: {result['error']}")