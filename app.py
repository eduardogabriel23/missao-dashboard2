import gradio as gr
import requests

API_URL = "https://whisper.gooey.ai/api/v1/transcribe/"
API_KEY = "demo"  # Você pode registrar sua própria chave gratuita em https://whisper.gooey.ai

def transcribe_with_whisper(audio):
    if audio is None:
        return "Nenhum arquivo enviado."
    
    files = {'file': open(audio, 'rb')}
    headers = {'Authorization': f'Bearer {API_KEY}'}
    data = {'diarize': 'false'}

    response = requests.post(API_URL, headers=headers, files=files, data=data)
    if response.ok:
        return response.json()["text"]
    else:
        return f"Erro: {response.text}"

gr.Interface(
    fn=transcribe_with_whisper,
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs="text",
    title="Transcritor Inteligente",
    description="WebApp da equipe Eduardo, Jane e Luana. Envie um vídeo ou áudio em português e receba a transcrição exata."
).launch()
