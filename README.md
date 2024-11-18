# YouTube Content Analyzer 🎥

Um aplicativo que extrai, traduz e analisa conteúdo de vídeos do YouTube usando Streamlit e IA.

## 🚀 Funcionalidades Atuais

- ✅ Extração de legendas de vídeos do YouTube
- ✅ Tradução automática para Português (BR) usando Groq AI
- ✅ Interface amigável com Streamlit
- ✅ Download dos textos original e traduzido
- ✅ Visualização lado a lado (original/tradução)

## 🛠️ Tecnologias Utilizadas

- Python 3.8+
- Streamlit
- Groq AI (API)
- youtube-transcript-api
- python-dotenv

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Conta na Groq AI (para chave da API)
- Pip (gerenciador de pacotes Python)

## ⚙️ Configuração do Ambiente

1. Clone o repositório:

```bash
git clone https://github.com/douglas-engenheirodedados/fluxo_opb
cd youtube-content-analyzer
```


2. Crie e ative um ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate
# Linux/Mac
python -m venv venv
source venv/bin/activate
```


3. Instale as dependências:

```bash
pip install -r requirements.txt
```


4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave da API da Groq:

```plaintext
GROQ_API_KEY="sua_chave_da_api_da_groq"
```         


## 📁 Estrutura do Projet   o

```plaintext
youtube-content-analyzer/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── src/
├── init.py
├── main.py
├── transcripts/ # Armazena textos originais
├── translations/ # Armazena traduções
└── agents/
├── init.py
├── youtube_extractor.py
└── translator_agent.py
```


## 🚀 Como Executar

1. Ative o ambiente virtual:

```bash
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

2. Execute o aplicativo:

```bash
streamlit run app.py
```


3. Acesse o aplicativo no navegador (geralmente em `http://localhost:8501`)

## 💡 Como Usar

1. Cole a URL do vídeo do YouTube no campo de entrada
2. Clique em "Processar Vídeo"
3. Aguarde o processamento
4. Visualize os textos original e traduzido
5. Faça o download dos arquivos se desejar

## ⚠️ Limitações Conhecidas

- O vídeo precisa ter legendas disponíveis
- Textos muito longos são processados em partes
- Necessário conexão com internet estável

## 🔜 Próximos Passos

- [ ] Criar resumo automático do conteúdo
- [ ] Gerar roteiro de aula baseado no conteúdo

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato

Douglas - [douglas@engenheirodedados.com.br](mailto:douglas@engenheirodedados.com.br)

Link do Projeto: [https://github.com/douglas-engenheirodedados/fluxo_opb](https://github.com/douglas-engenheirodedados/fluxo_opb)
