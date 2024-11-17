from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class TranslatorAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        self.config = {
            "name": "translator",
            "description": "Agente responsável por traduzir textos para PT-BR"
        }
        # Cria o diretório de traduções se não existir
        self.translations_dir = os.path.join("src", "translations")
        os.makedirs(self.translations_dir, exist_ok=True)

    def translate_text(self, text: str) -> tuple:
        """Traduz o texto para PT-BR usando a API da Groq"""
        try:
            response = self.client.chat.completions.create(
                model="mixtral-8x7b-32768",  # Modelo Mixtral da Groq
                messages=[
                    {"role": "system", "content": "Você é um tradutor profissional. Traduza o texto para português brasileiro mantendo o contexto e naturalidade."},
                    {"role": "user", "content": f"Traduza o seguinte texto: {text}"}
                ],
                temperature=0.3,
                max_tokens=32768
            )
            
            translated_text = response.choices[0].message.content
            return translated_text, None
            
        except Exception as e:
            error_msg = f"Erro na tradução: {str(e)}"
            return None, error_msg

    def save_translation(self, text: str, original_filename: str) -> str:
        """Salva a tradução em um arquivo"""
        base_name = os.path.splitext(os.path.basename(original_filename))[0]
        translated_filename = f"{base_name}_pt_br.txt"
        filepath = os.path.join(self.translations_dir, translated_filename)
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)
        
        return filepath