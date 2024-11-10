# 📺 Baixador de Vídeos do YouTube
![Status do Projeto](https://img.shields.io/badge/Status-Concluido-green)
![Python Version](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Uma aplicação desktop simples desenvolvida em Python que permite baixar vídeos do YouTube e converter para diferentes formatos de áudio/vídeo.

## ✨ Funcionalidades

- 🎥 Download de vídeos do YouTube em formato MP4
- 🎵 Extração e conversão de áudio para formato MP3
- 🎶 Extração e conversão de áudio para formato WAV
- 🖥️ Interface gráfica amigável
- 📊 Atualizações em tempo real do status do download
- ⚠️ Tratamento de erros e feedback ao usuário

## 📋 Requisitos

- ✅ Python 3.6 ou superior
- 📦 Pacotes Python necessários:
  ```
  pytubefix
  ffmpeg-python
  tkinter (geralmente já vem com o Python)
  ```

## 🚀 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/youtube-downloader.git
   cd youtube-downloader
   ```

2. Instale os pacotes necessários:
   ```bash
   pip install pytubefix ffmpeg-python
   ```

3. Certifique-se de ter o FFmpeg instalado no seu sistema:
   - **Windows**: Baixe do [site oficial do FFmpeg](https://ffmpeg.org/download.html) e adicione ao PATH
   - **Linux**: `sudo apt-get install ffmpeg`
   - **macOS**: `brew install ffmpeg`

## 📱 Como Usar

1. Execute a aplicação:
   ```bash
   python main.py
   ```

2. Digite a URL do vídeo do YouTube no campo de texto

3. Selecione o formato de saída desejado:
   - WAV (Áudio)
   - MP3 (Áudio)
   - MP4 (Vídeo)

4. Clique no botão "Baixar"

5. Aguarde o download ser concluído - você verá uma mensagem de sucesso quando terminar

## 📂 Arquivos de Saída

Os arquivos baixados serão salvos no mesmo diretório do script com os seguintes nomes:
- `nome.wav` para formato WAV
- `nome.mp3` para formato MP3
- `nome.mp4` para formato MP4

## ⚠️ Tratamento de Erros

A aplicação inclui tratamento para problemas comuns:
- URLs inválidas
- Problemas de conexão de rede
- Seleção de formato inválida
- Instalação ausente do FFmpeg

## 🤝 Como Contribuir

1. Faça um fork do repositório
2. Crie sua branch de feature: `git checkout -b feature/nova-feature`
3. Faça commit das alterações: `git commit -am 'Adiciona nova feature'`
4. Push para a branch: `git push origin feature/nova-feature`
5. Envie um pull request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- [pytube](https://github.com/pytube/pytube) pela funcionalidade de download do YouTube
- [FFmpeg](https://ffmpeg.org/) pelas capacidades de processamento de mídia

## 💬 Suporte

Se você encontrar algum problema ou tiver sugestões, por favor, abra uma issue no repositório do GitHub.

---
⭐ Feito por Matheus Silvano Pereira
