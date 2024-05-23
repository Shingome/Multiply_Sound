import gradio as gr
from pydub import AudioSegment
from src.multiply_audio import multiply_audio


def sentence_builder(count: int, offset: float):
    file = "tmp/tmp.mp3"
    multiply_audio(raw_audio, count, offset * 1000.).export(file)
    return file


demo = gr.Interface(
    sentence_builder,
    [
        gr.Slider(1, 1000, step=1, value=1, label="Count", info="Shkibididobsteeeep"),
        gr.Slider(0, 5, step=0.05, value=0, label="Offset", info="Sec between Shkibididobsteeeep")
    ],
    "audio"
)

raw_audio = AudioSegment.from_file("sound.mp3")

if __name__ == "__main__":
    demo.launch()
