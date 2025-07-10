import whisper
import gradio as gr

model = whisper.load_model("small")

def transcribe(audio):
    if audio is None:
        return "Nenhum arquivo enviado."
    result = model.transcribe(audio.name, language="Portuguese")
    return result["text"]

iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs="text",
    title="Transcritor – Eduardo, Jane e Luana",
    description="Suba vídeo ou áudio em português e receba transcrição exata."
)

if __name__ == "__main__":
    iface.launch()
