from youtube_transcript_api import YouTubeTranscriptApi
import autogen

class YoutubeExtractorAgent:
    def __init__(self):
        self.config = {
            "name": "youtube_extractor",
            "description": "Agente responsável por extrair legendas de vídeos do YouTube"
        }
    
    def extract_video_id(self, url: str) -> str:
        """Extrai o ID do vídeo da URL do YouTube"""
        if "youtu.be" in url:
            return url.split("/")[-1]
        elif "youtube.com" in url:
            return url.split("v=")[1].split("&")[0]
        return url
    
    def get_transcript(self, video_url: str) -> str:
        """Obtém a transcrição do vídeo"""
        try:
            video_id = self.extract_video_id(video_url)
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            
            # Concatena todo o texto da transcrição
            full_text = " ".join([entry['text'] for entry in transcript])
            return full_text
            
        except Exception as e:
            return f"Erro ao extrair legendas: {str(e)}"