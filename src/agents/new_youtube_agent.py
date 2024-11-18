# src/agents/new_youtube_agent.py

import os
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
from datetime import datetime
from typing import Dict, Any, List

# Carrega as variáveis de ambiente
load_dotenv()

class YouTubeTranscriptTool:
    def get_transcript(self, video_url: str) -> Dict[str, Any]:
        """Extrai a transcrição de um vídeo do YouTube"""
        try:
            # Extrai o ID do vídeo da URL
            video_id = self.extract_video_id(video_url)
            
            # Obtém a transcrição
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
        """Processa um vídeo do YouTube e salva a transcrição"""
        result = self.tool.get_transcript(video_url)
        
        if result["status"] == "success":
            self.save_transcript(video_url, result["transcript"])
            return {
                "status": "success",
                "transcript": result["transcript"]
            }
        else:
            return {
                "status": "error",
                "error": result["error"]
            }

    def save_transcript(self, video_url: str, transcript: List[Dict[str, Any]]) -> None:
        """Salva a transcrição em um arquivo"""
        video_id = self.tool.extract_video_id(video_url)
        os.makedirs("transcriptions", exist_ok=True)  # Cria a pasta se não existir
        file_path = f"transcriptions/{video_id}_transcript.txt"
        
        with open(file_path, "w", encoding="utf-8") as f:
            for entry in transcript:
                f.write(f"{entry['text']}\n")  # Salva cada linha da transcrição

# Exemplo de uso
if __name__ == "__main__":
    agent = YouTubeAgent()
    video_url = "https://youtu.be/fafbRw39QVw"  # Substitua pelo URL do vídeo desejado
    result = agent.process_video(video_url)
    print(result)