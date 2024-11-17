from youtube_transcript_api import YouTubeTranscriptApi
import os
from datetime import datetime

class YoutubeExtractorAgent:
    def __init__(self):
        self.config = {
            "name": "youtube_extractor",
            "description": "Agente responsável por extrair legendas de vídeos do YouTube"
        }
        # Cria o diretório de transcrições se não existir
        self.transcript_dir = os.path.join("src", "transcripts")
        os.makedirs(self.transcript_dir, exist_ok=True)
    
    def extract_video_id(self, url: str) -> str:
        """Extrai o ID do vídeo da URL do YouTube"""
        if "youtu.be" in url:
            return url.split("/")[-1]
        elif "youtube.com" in url:
            return url.split("v=")[1].split("&")[0]
        return url
    
    def get_video_title(self, video_id: str) -> str:
        """Gera um nome simplificado para o arquivo"""
        # Por enquanto, usaremos o ID do vídeo e timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"transcript_{video_id}_{timestamp}"
    
    def save_transcript(self, text: str, filename: str) -> str:
        """Salva a transcrição em um arquivo"""
        filepath = os.path.join(self.transcript_dir, f"{filename}.txt")
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)
        return filepath
    
    def get_transcript(self, video_url: str) -> tuple:
        """Obtém a transcrição do vídeo e salva em arquivo"""
        try:
            # Adiciona print para debug
            print(f"Tentando extrair legendas do vídeo: {video_url}")
            
            video_id = self.extract_video_id(video_url)
            print(f"ID do vídeo extraído: {video_id}")
            
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            
            # Concatena todo o texto da transcrição
            full_text = " ".join([entry['text'] for entry in transcript])
            
            # Gera nome do arquivo e salva
            filename = self.get_video_title(video_id)
            filepath = self.save_transcript(full_text, filename)
            
            return full_text, filepath
            
        except Exception as e:
            # Melhorando a mensagem de erro
            error_msg = f"Erro ao extrair legendas: {str(e)}\nTipo do erro: {type(e).__name__}"
            print(error_msg)  # Adiciona print do erro
            return error_msg, None