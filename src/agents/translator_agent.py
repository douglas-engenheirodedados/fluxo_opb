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
        self.translations_dir = os.path.join("src", "translations")
        os.makedirs(self.translations_dir, exist_ok=True)
        self.max_chunk_size = 4000  # Tamanho seguro para cada chunk

    def split_text(self, text: str) -> list:
        """Divide o texto em chunks menores, tentando manter frases completas"""
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 > self.max_chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
            else:
                current_chunk.append(word)
                current_length += len(word) + 1

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks

    def translate_chunk(self, text: str) -> tuple:
        """Traduz um chunk de texto"""
        try:
            response = self.client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=[
                    {"role": "system", "content": "Você é um tradutor profissional. Traduza o texto para português brasileiro mantendo o contexto e naturalidade."},
                    {"role": "user", "content": f"Traduza o seguinte texto: {text}"}
                ],
                temperature=0.3,
                max_tokens=4000  # Limitando o número de tokens na resposta
            )
            
            return response.choices[0].message.content, None
            
        except Exception as e:
            return None, f"Erro na tradução do chunk: {str(e)}"

    def translate_text(self, text: str) -> tuple:
        """Traduz o texto completo, dividindo em chunks se necessário"""
        try:
            # Divide o texto em chunks menores
            chunks = self.split_text(text)
            translated_chunks = []
            
            # Traduz cada chunk
            for i, chunk in enumerate(chunks):
                translated_chunk, error = self.translate_chunk(chunk)
                if error:
                    return None, error
                translated_chunks.append(translated_chunk)
            
            # Junta todos os chunks traduzidos
            complete_translation = ' '.join(translated_chunks)
            return complete_translation, None
            
        except Exception as e:
            return None, f"Erro na tradução: {str(e)}"

    def save_translation(self, text: str, original_filename: str) -> str:
        """Salva a tradução em um arquivo"""
        base_name = os.path.splitext(os.path.basename(original_filename))[0]
        translated_filename = f"{base_name}_pt_br.txt"
        filepath = os.path.join(self.translations_dir, translated_filename)
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)
        
        return filepath